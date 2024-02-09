import requests
from bs4 import BeautifulSoup
import csv
import time
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re


file = open('loic_amazon.csv','r')
refrence_data = csv.reader(file)
# ['9781785585005','9781785580598','9781846090417','9781849381772','9789043166485','5020679508626','9790046172045']:
proxies = None

for refrence in refrence_data:
    try:
        refrence = refrence[0]
        url = f"https://www.amazon.fr/s/ref=nb_sb_noss?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords={refrence}&crid=3PXGWWXB6KWYS&sprefix={refrence}%2Caps%2C122"
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.amazon.fr/',
        #   'Cookie': 'session-id=259-3187579-6379441; session-id-time=2082787201l; i18n-prefs=EUR; csm-hit=tb:TFPF6M0PZPKKHPMXMY9S+s-TFPF6M0PZPKKHPMXMY9S|1707312542418&t:1707312542418&adb:adblk_no; ubid-acbfr=260-7793125-4792531; session-token=V7/TG+57YsPDvHhHZ3xq6emxm9yngQBfbuw/aj2TlprJkUFtFVlMGldD+qGY7SQ8Svsk93l7VQFxW8LOvUu1yk/+lGT0PNgkUiM8FKuvMWtvet4B4txTa5vIqKz68d58bfW8HBp4xPkzIxKcAO2A6A3Fg/lj0kvEKTaRv9mniZn8XoqzEwVLj0gBXhW1eoxcBJjNTobhTl7QZ/zbC0W3AH4RHVPDPhOxnlMg3PVhlAfaWMrEf1l7dH7+ufLvDmtDLlnL490stg/wCmNRm5gfxdghPwwGw5lXehpr3EB5hJuI/ubmNfC7hz/58UacigL011Rks13UbLJQjcWMeEOUqFeUyldqtzqm; at-acbfr=Atza|IwEBIN3xKuTPrD3OMFNj_IaFd9-EoA3VqmuMaA-SdnspROdXaBbbDkDWqfqoRo2K3XwU3Y14mbtO6zaJEejrAPyOqObIZ4niRGGt2recbFX7UzUqWcr8pwZmlyt1lov9EchYn0shxNBexqaf8W06todS8f7sY9EzxFNiFgB-17UtZPl3l-6ylKVs2Gw_FzQpyjJ4y6l_RFqNXiT3jYaxoEETV_YSlLlM83QN9hPfccSzaEFypQ; i18n-prefs=EUR; lc-acbfr=fr_FR; sess-at-acbfr="J/ym6ch/+4jIp125n6JlquqGjTq7+0Q84Ui4+KIeFHY="; session-id=257-0631528-9652625; session-id-time=2082787201l; session-token=maIjcgG6aGY0zf5Bn5MsvF82M2BnyWm8eYFhGgRWGrWDCbHcOD/11ybOlHctU4Ph9YuVoWWCd2kcoDwGJevZBYiQMVrPXi733v4fr0OPdWOoDPvsAkTT2s0OqNnPLapOTilykqV5oXX0zOk3dausZSn5SuOHt6aQkQo1mmghRLQFYuZ7cb8HWcBnFmhKfrBwZmVCRFyz2pwTK7tMn3zV/mkAhTjuGwwvhD3EatunoBp7Q2syqBeZrhXUxI/Bq0k5wmAjleBz3Vi+afcxtf70IdKcuNRuobLG2fDsVTvSPGFV4FAUqCJQWRA94cHz7P/SvE/FCgGlIxpSWbRKYLyPZiz+SzxCL8LhjpMXMwlnwOlQ5g8h+6pL+ljFrzQHq38c; sst-acbfr=Sst1|PQHpswFXKfrxqjF8KC0nBJyKCeONrrE7h26EpWMH9lmUqU668O4DkurZXVGpIiOGYBkE9-FItepfGNmHoLZFqHCg-npP0H9bRw1b5Gx00kXFpAMTwVakbM5tsUf5Mh2Iq5x-Ld1l16-3nldnWBHwcYUG3J54H0BsVPCzeLEDkBKMa0PbKMNRGnUe4tkqjhZ9svdm226nlw8j2XW-kR9PTWpWJMqnWh4B0_nGB1DHltGlTTBjEH-jAS-y1GkeI5B9gCAQ5M-mPqGR1zzzFNOCRhYCGaAqyD2Yw3T0KOR-EJL_8IY; ubid-acbfr=260-4636801-9753029; x-acbfr=jxbOkJ96aVWKJtErugx8pM9vLx3nUdL4dWNcI54eMEe6Eww4j052kb6HTrikOK2O',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
        }

        # response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        response = requests.get(url, headers=headers, verify=False, proxies=proxies)

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Status code: {response.status_code} for {refrence}")
        results = soup.select('div.s-search-results > div.s-result-item.s-asin')
        if (response.status_code == 200) and (len(results) > 0):
            for res in results:
                item = {}
                item['référence'] = refrence
                href = res.select_one('span[data-component-type="s-product-image"]>a').attrs.get("href")
                response = requests.get(f"https://www.amazon.fr{href}",headers=headers, verify=False, proxies=proxies)
                soup = BeautifulSoup(response.text, 'html.parser')
                item['titre'] = soup.select_one('span[id="productTitle"]').get_text().strip()
                if 'Actuellement indisponible' in response.text:
                    item['disponibility'] = 'indisponible'
                    item['prix'] = None
                    item['Expédié_par'] = None
                    item['Vendu_par'] = None
                    item['Livraison'] = None
                else:
                    item['disponibility'] = 'disponible'
                    try:
                        whole = soup.select_one('div[id="rightCol"] span.a-price-whole').get_text().strip()
                        fraction = soup.select_one('div[id="rightCol"] span.a-price-fraction').get_text().strip()
                        symbol = soup.select_one('div[id="rightCol"] span.a-price-symbol').get_text().strip()
                        item['prix'] = f"{whole}{fraction}{symbol}"
                    except:
                        try:
                            item['prix'] = soup.select_one('div[id="rightCol"] span.slot-price').get_text().strip()
                            if '€' not in item['prix']:
                                item['prix'] = item['prix'] + '€'
                        except:
                            item['prix'] = None        
                    
                    try:
                        item['Expédié_par'] = soup.select_one('div[id="fulfillerInfoFeature_feature_div"]>div.offer-display-feature-text').get_text().strip()
                    except:
                        item['Expédié_par'] = None
                    try:
                        item['Vendu_par'] = soup.select_one('div[id="merchantInfoFeature_feature_div"]>div.offer-display-feature-text').get_text().strip()
                    except:
                        item['Vendu_par'] = None
                    try:
                        item['Livraison']  = soup.select_one('div[id="mir-layout-DELIVERY_BLOCK"] span.a-text-bold').get_text().strip()
                    except: 
                        item['Livraison']  = None
                    if item['Expédié_par'] == 'Amazon':
                        item['Frais_livraison']  = "O€"
                    elif item['Expédié_par'] == None:
                        item['Frais_livraison']  = None
                    else:    
                        item['Frais_livraison']  = re.findall(r'Livraison à (.+?) ', soup.select_one('div[id="mir-layout-DELIVERY_BLOCK"]').get_text().strip())[0]

                    if item['prix'] == None:
                        item['disponibility'] = 'indisponible'
                    
                    if item['prix'] != None:
                        if '€' not in item['prix']:
                            item['prix'] = item['prix'] + '€'

                with open('amazon.csv','a', encoding='utf-8', newline='') as op_file:
                    fields = ['référence', 'titre','disponibility','prix', 'Expédié_par', 'Vendu_par', 'Livraison','Frais_livraison']
                    writer = csv.DictWriter(op_file, fieldnames=fields)
                    writer.writerow(item)
        else:
            item ={}
            item['référence'] = refrence
            item['titre'] = None
            item['disponibility'] = None
            item['prix'] = None
            item['Expédié_par'] = None
            item['Vendu_par'] = None
            item['Livraison'] = None
            item['Expédié_par'] = None
            item['Vendu_par'] = None
            item['Livraison']  = None
            item['Frais_livraison']  = None
            with open('amazon.csv','a', encoding='utf-8', newline='') as op_file:
                    fields = ['référence', 'titre','disponibility','prix', 'Expédié_par', 'Vendu_par', 'Livraison','Frais_livraison']
                    writer = csv.DictWriter(op_file, fieldnames=fields, extrasaction='ignore')
                    writer.writerow(item)

    except Exception as e:
        print(e)
        continue

