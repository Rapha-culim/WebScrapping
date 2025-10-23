import requests
from bs4 import BeautifulSoup

def scrape_dfg_tibia_gold():
    url = "https://www.dfg.com.br/pt-PT/tibia/gold/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                      "AppleWebKit/537.36 (KHTML, like Gecko) " +
                      "Chrome/115.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")

    anuncios = []
    for h4 in soup.select("h4"):
        title = h4.get_text(strip=True)
    
        parent = h4.parent

        
        price_tag = parent.select_one("h4 + *")  
        price = price_tag.get_text(strip=True) if price_tag else None

        sales_tag = parent.select_one("p")
        sales = sales_tag.get_text(strip=True) if sales_tag else None

        vendor_tag = parent.select_one("a")
        vendor = vendor_tag.get_text(strip=True) if vendor_tag else None

        anuncios.append({
            "title": title,
            "price": price,
            "sales": sales,
            "vendor": vendor
        })

    return anuncios

if __name__ == "__main__":
    data = scrape_dfg_tibia_gold()
    for ad in data:
        print(ad)
