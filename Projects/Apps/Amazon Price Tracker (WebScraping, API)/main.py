from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP = os.environ["SMTP"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}


#response = requests.get(practice_url, headers=header)
response = requests.get(live_url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText()
price_without_currency = price.split("$")[1]
price_total = price_without_currency.split(" ")[0]

price_as_float = float(price_total)
print(price_as_float)

# ====================== Send an Email ===========================

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 80

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    print(message)

    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8")
        )