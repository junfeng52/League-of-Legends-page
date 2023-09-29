import requests
import re
import wget
import os



def searchchap(chname,url):
    chpage = requests.get(url).text
    imgchamp = re.findall(r'https:\/\/ddragon\.leagueoflegends\.com\/cdn\/img\/champion\/splash\/[A-Za-z_0-9]+\.jpg',chpage)[0]
    links = re.findall(r'(https:\/\/ddragon\.leagueoflegends\.com\/cdn\/([0-9]+(\.[0-9]+)+)\/img\/[spell | passive]+\/[A-Za-z_]+\.png)',chpage)
    links = [link[0] for i,link in enumerate(links) if i%2 == 0]
    links.append(imgchamp)
    os.makedirs(chname, exist_ok=True)
    for link in links: 
        wget.download(link,out=chname)

chpages = requests.get("https://www.leagueoflegends.com/es-es/champions/").text
urls= re.findall(r"/es-es/champions/[A-Za-z_-]+", chpages)
chlinks = re.findall(r"https:\/\/images\.contentstack\.io\/v3\/assets\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+\/RiotX_ChampionList_[a-zA-Z_\-0-9]+\.jpg", chpages)

for link in set(chlinks):
        wget.download(link, out="Imgenes")