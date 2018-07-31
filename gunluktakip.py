import requests
import bs4


def havadurumu():
    base_url = "https://www.havadurumu15gunluk.net/havadurumu/ankara-hava-durumu-15-gunluk.html"
    ana_response = requests.get(base_url)
    ana_soup = bs4.BeautifulSoup(ana_response.text, "html.parser")
    listem = ana_soup.find_all("strong")
    derece = listem[4].text
    durum = listem[5].text
    hava="Günlük durum raporu: \n\n"+ "Ankara için hava durumu: "+ derece + " " + durum + "\n\n"
    return hava


def dolarkuru():
    base_url = "http://www.bloomberght.com/doviz/dolar"
    ana_response = requests.get(base_url)
    ana_soup = bs4.BeautifulSoup(ana_response.text, "html.parser")
    classname = "col-lg-8 col-sm-12 col-xs-12 col-md-6 marB10 piyasaDetayTitle"
    kur = ana_soup.find("div", class_=classname)
    return kur.text


def kurtakip():
    base_url = "https://coinmarketcap.com/"
    ana_response = requests.get(base_url)
    ana_soup = bs4.BeautifulSoup(ana_response.text, "html.parser")
    classname: str = "no-wrap percent-change  text-right negative_change"
    ana_soup.find("td", class_=classname)
    btc_kur = ana_soup.find_all("td", {"class": "no-wrap"})

    degisim, deger, yuzde, oran = dolarkuru().split(" ")
    btckur = float(btc_kur[2].text.replace("$", ""))
    dolarkur = float(deger.replace(",", "."))
    hava=havadurumu()
    with open("takip.txt","w") as f:
        f.write(hava+
              "Anlık dolar kuru: " + deger +
              "\n" +
              "Dolar değişim oranı: " + yuzde + oran+ "\n\n"+
              "Anlık bitcoin değeri(USD): " + btc_kur[2].text + "\n" +
              "Anlık bitcoin değeri (TL): " + str(btckur * dolarkur) + "\n" +
              "Bitcoin değişim oranı : " + btc_kur[5].text + "\n")


havadurumu()
kurtakip()
