import json
import requests
from bs4 import BeautifulSoup




def  extract_link(url):
    # Custom headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    card_contents = soup.find_all(class_='card-content pt-20 pb-20 pr-20')

    result = []

    for card in card_contents:
        # Extract text or HTML of intervals
        intervals = [interval.get_text(strip=True) for interval in card.find_all(class_='interval')]

        # Extract href and text for each link inside card-content
        links = []
        for link in card.find_all('a'):
            links.append({
                "href": link.get('href', ''),
                "text": link.get_text(strip=True)
            })
        
        result.append({
            "intervals": intervals,
            "links": links
        })

    data = []


    for item in result:
        if "1h ago" in item.get("intervals", []):
            data.append(item)



    # Convert to JSON string (pretty formatted)
    json_output = json.dumps(data, indent=2, ensure_ascii=False)

    with open("data/output.json", "w", encoding="utf-8") as f:
        f.write(json_output)




