import requests
import bs4
import re
import wget
import os

def searchchap(chname, url):
    chpage = requests.get(url).text
    page = bs4.BeautifulSoup(chpage)

    os.makedirs(f"img/{chname}", exist_ok=True)
    chname = f"img/{chname}/{chname}"
    ppage = page.find_all("div", {"class":"innerWrapper"})
    for k ,result in enumerate(re.findall(r"(https?:\/\/[\w\-\.]+(\/[\w\-\.\/]*)*\.(jpg|png))", str(ppage))):
        churl = result[0]
        if k > 5: break
        if k == 0 : wget.download(churl, out=f"{chname}_P.png")
        elif k == 1 : wget.download(churl, out=f"{chname}_Q.png")
        elif k == 2 : wget.download(churl, out=f"{chname}_W.png")
        elif k == 3 : wget.download(churl, out=f"{chname}_E.png")
        elif k == 4 : wget.download(churl, out=f"{chname}_R.png")
        elif k == 5 : wget.download(churl, out=f"{chname}_0.jpg")
        else: break

chpages = requests.get("https://www.leagueoflegends.com/es-es/champions/").text
urls= sorted(list(set(re.findall(r"/es-es/champions/[A-Za-z_-]+", chpages))))
chnames = [i.split("/")[-1] for i in urls]
print(urls)

for chn, link in zip(chnames, urls):
    searchchap(chn ,f"https://www.leagueoflegends.com{link}")