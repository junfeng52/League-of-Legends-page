import os


fileNameWithExt = os.listdir("Imagenes")


for filename in fileNameWithExt:
    os.rename(f"Imagenes/{filename}", f"Imagenes/{filename}")

