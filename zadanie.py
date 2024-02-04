import requests
import random
from xml.etree import ElementTree as ET

def pobierz_informacje_o_kraju(zapytanie):
    soap_country_info_url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'
    headers = {'Content-Type': 'text/xml'}
    body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.oorsprong.org/websamples.countryinfo">
        <soapenv:Header/>
        <soapenv:Body>
            <web:FullCountryInfo>
                <web:sCountryISOCode>{zapytanie}</web:sCountryISOCode>
            </web:FullCountryInfo>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    response = requests.post(soap_country_info_url, headers=headers, data=body)
    informacje_o_kraju = {}

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for element in root.findall('.//{http://www.oorsprong.org/websamples.countryinfo}FullCountryInfoResult'):
            for child in element:
                key = child.tag.split('}')[1].replace('s', '') 
                if 'language' not in key.lower() and 'flag' not in key.lower() and 'phonecode' not in key.lower():
                    informacje_o_kraju[key] = child.text

    return informacje_o_kraju
    
def pobierz_ciekawostki_o_liczbie(liczba):
    soap_numbers_url = 'http://numbersapi.com/'
    response = requests.get(f'{soap_numbers_url}{liczba}')

    if response.status_code == 200:
        return f"Ciekawostki o liczbie {liczba}:\n{response.text}"
    else:
        return f"Nie udało się pobrać ciekawostek o liczbie. Kod statusu: {response.status_code}"

def celsius_na_fahrenheit(celsius):
    url = "https://www.w3schools.com/xml/tempconvert.asmx"
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
            <Celsius>{celsius}</Celsius>
        </CelsiusToFahrenheit>
    </soap12:Body>
</soap12:Envelope>"""
    headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}
    response = requests.post(url, headers=headers, data=payload)
    
    root = ET.fromstring(response.content)
    fahrenheit = root.find('.//{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult').text
    return fahrenheit


def tv_info():
    rest_tvmaze_url = 'http://api.tvmaze.com/shows'
    response = requests.get(rest_tvmaze_url)

    if response.status_code == 200:
        shows = response.json()
        if shows:
            show_info = random.choice(shows)
            return f"Informacje o serialach:\nTytuł: {show_info.get('name', 'Unknown')}\nJęzyk: {show_info.get('language', 'Unknown')}\nGatunki: {', '.join(show_info.get('genres', []))}"
        else:
            return "Nie znaleziono serialu."
    else:
        return f"Nie udało się pobrać informacji o serialu. Kod statusu: {response.status_code}"


if __name__ == "__main__":
    zapytanie_o_kraj = input("Wprowadź nazwę kraju lub kod ISO: ")
    informacje_o_kraju = pobierz_informacje_o_kraju(zapytanie_o_kraj)
    print("\nInformacje o kraju:")
    for key, value in informacje_o_kraju.items():
        if key != 'Languages':
            print(f"{key}: {value}")

    liczba = int(input("\nWprowadź liczbę: "))
    ciekawostki_o_liczbie = pobierz_ciekawostki_o_liczbie(liczba)
    print("\n", ciekawostki_o_liczbie)

    celsius = float(input("\nWprowadź temperaturę w stopniach Celsjusza: "))
    fahrenheit = celsius_na_fahrenheit(celsius)
    print("\n", fahrenheit)

    tv_show_info = tv_info()
    print("\n", tv_show_info)