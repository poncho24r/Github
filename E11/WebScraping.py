#!/usr/bin/env python3

import argparse
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

# Parte de argsparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "URL", help="Inserte la URL donde desee realizar Web Scraping")
args = parser.parse_args()

#Ubicacion y creacion de directorios
Ubicacion = str(os.path.dirname(os.path.abspath(__file__)))
Carpeta = input("Ingrese el nombre de la carpeta a crear: ")
os.makedirs(Carpeta + "/Imagenes/")
os.makedirs(Carpeta + "/Outputs/")
#RutaParaImagenes = os.path.join(Ubicacion, Carpeta, "/Imagenes/")
#RutaParaOutputs = os.path.join(Ubicacion, Carpeta, "/Outputs/")

# Parte de Web Scraping
print("\nHaciendo el Web Scraping, espere un segundo...")
r = requests.get(args.URL)
soup = BeautifulSoup(r.text, "html.parser")
for item in soup.find_all("img"):
    link = item["src"]
    split = link.split("/")
    with open(Ubicacion + "/" + Carpeta + "/Imagenes/" + split[-1], "wb") as f:
        imagen = requests.get(link)
        f.write(imagen.content)

# Parte de sacar Metadata y el output a un .txt
print("\nExtrayendo el metadata de las imagenes, espere un segundo...\n")
for item in os.listdir(Ubicacion + "/" + Carpeta + "/Imagenes/" ):
    image = Image.open(Ubicacion + "/" + Carpeta + "/Imagenes/" + item)
    exifdata = image.getexif()
    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        with open(Ubicacion + "/" + Carpeta + "/Outputs/" + item + ".txt", "a") as myfile:
            myfile.write(f"{tagname:25}: {value}\n")
