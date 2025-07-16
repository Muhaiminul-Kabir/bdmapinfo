import requests
from bs4 import BeautifulSoup


def extract_para(url):
    # Custom headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')



    filtered_p = []
    for p in paragraphs:
        if not p.find("a"):  # skip <p> that contains <a>
            filtered_p.append(p)



    # Save to text file
    with open("data/output.txt", "w", encoding="utf-8") as file:
        for p in filtered_p:
            text = p.get_text(strip=True)
            file.write(text + "\n")    
