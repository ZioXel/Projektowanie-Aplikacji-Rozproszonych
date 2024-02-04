# Integracja z Serwisami SOAP i RESTful

Kod wykożystujący serwisy typu SOAP i REST api.

## Wykorzystane Usługi

1. **Usługa Informacyjna o Kraju**
   - Adres Usługi: [http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso](http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso)
   - Metoda: POST
   - Treść Zapytania: Zapytanie SOAP o pełne informacje o kraju na podstawie kodu ISO.

2. **API Liczbowe**
   - Adres Usługi: [http://numbersapi.com/](http://numbersapi.com/)
   - Metoda: GET
   - Zapytanie: Pobranie ciekawostek dotyczących danej liczby.

3. **Usługa Konwersji Temperatury**
   - Adres Usługi: [https://www.w3schools.com/xml/tempconvert.asmx](https://www.w3schools.com/xml/tempconvert.asmx)
   - Metoda: POST
   - Treść Zapytania: Zapytanie SOAP o konwersję stopni Celsjusza na Fahrenheita.

4. **Usługa Informacyjna o Programach Telewizyjnych**
   - Adres Usługi: [http://api.tvmaze.com/shows](http://api.tvmaze.com/shows)
   - Metoda: GET
   - Zapytanie: Pobranie informacji o programach telewizyjnych.

## Metody w Pythonie i Ich Wyniki

### 1. `pobierz_informacje_o_kraju(zapytanie)`
   - Metoda do pobierania informacji o kraju na podstawie kodu ISO.
   - Zwraca słownik z informacjami o kraju.

### 2. `pobierz_ciekawostki_o_liczbie(liczba)`
   - Metoda do pobierania ciekawostek na temat danej liczby.
   - Zwraca tekst z ciekawostkami.

### 3. `celsius_na_fahrenheit(celsius)`
   - Metoda do konwersji stopni Celsjusza na Fahrenheita za pomocą usługi SOAP.
   - Zwraca temperaturę w stopniach Fahrenheita.

### 4. `tv_info()`
   - Metoda do pobierania losowych informacji o programach telewizyjnych za pomocą usługi RESTful.
   - Zwraca sformatowany tekst z detalami dotyczącymi programu.

### Uruchamianie Skryptu
   - Uruchom skrypt i postępuj zgodnie z instrukcjami, aby podać nazwę kraju, liczbę i temperaturę w stopniach Celsjusza.


