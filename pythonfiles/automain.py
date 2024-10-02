import pandas as pd
from pandasgui import show

csvfile = pd.read_csv("champtext.csv", index_col= 0)

names = csvfile.index.values


with open("pruebamain.html", mode="w") as filehtml:
    page = []
    page.append('<html>\n\n<head>\n\t<title>Practica </title>\n\t<link rel="stylesheet" href="css/Style.css">\n</head>\n')
    page.append('<body>\n\t<h1 id="title">League of Legends</h1>\n\t<h2>Champions</h2>\n\t<div id="div1">')
    for name in names:
        chhtml = f'\t\t<div class="champ">\n\t\t\t<a href="Champions/{name.upper()}.html#HechoPorJunfeng">\n\t\t\t\t<img src="Imagenes/{name}.jpg">\n\t\t\t\t<span>{name.upper()}</span>\n\t\t\t</a>\n\t\t</div>\n'
        page.append(chhtml)
    page.append("\t</div>\n</body>\n\n</html>")
    filehtml.write("\n".join(page))


