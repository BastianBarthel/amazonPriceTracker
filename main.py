from bs4 import BeautifulSoup
import os
import requests
import smtplib

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
SMTP = "smtp.gmail.com"
URL = "https://www.amazon.de/Canon-EOS-800D-SLR-Digitalkamera-Schwarz/dp/B06X6LMVFW/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Canon+EOS+800D+SLR&qid=1621452876&sr=8-1"
BUY_AT = 600

headers = {
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
price = float(soup.find(name="span", id="priceblock_ourprice").text.replace(",", ".").split()[0])
name = soup.find(name="span", id="productTitle").text.strip()

if price < BUY_AT:
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert\n\n{name} for {'{:.2f}'.format(price)}€ on\n{URL}".encode("utf-8")
        )
