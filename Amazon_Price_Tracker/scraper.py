import requests
from bs4 import BeautifulSoup
import smtplib


def CheckPrice():
    url = 'https://www.amazon.in/ACOOSTA-TRUBUDS-Wireless-Bluetooth-Assistant/dp/B0839H1C58/ref=sr_1_1_sspa?m=A14CZOWI0VEHLG&pf_rd_i=1388921031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=a1737d75-1ed4-4031-8218-f873431bfebc&pf_rd_r=W7Y1BHKS4VJP12C76G11&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1579443493&refinements=p_6%3AA14CZOWI0VEHLG%2Cp_89%3AACOOSTA%7CAnt+Audio%7CBEATS%7CBLAUPUNKT%7CBeats%7CBlaupunkt%7CBoat%7CBose%7CHiFiMAN%7CMOTOROLA%7CMotorola%7CNU+REPUBLIC%7CNoise%7CNu+Republic%7CPORTRONICS%7CPortronics%7CSENNHEISER%7CSennheiser%7CSkullcandy%7CThomson&rnid=3837712031&s=electronics&smid=A14CZOWI0VEHLG&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTNU5SRktYWlRPU1gmZW5jcnlwdGVkSWQ9QTA5NDMyODkxTlpPMlhYVExXTUJKJmVuY3J5cHRlZEFkSWQ9QTA1NDkzNjJTRzNKVExYMDEwOVMmd2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3NlJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[4:8])
    print(price.strip())

    if(converted_price > 900):
        SendMail()


def SendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('redtimex02@gmail.com', 'password')
    subject = 'Price fell down'
    body = 'Check you product'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'redtimex02@gmail.com',
        'raunak31j@gmail.com',
        msg
    )

    print('Hey Email has been sent')

    server.quit()


CheckPrice()
