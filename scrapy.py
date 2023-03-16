import requests
from bs4 import BeautifulSoup
import datetime
import re
information = []
class Scrapy:
    def __init__(self,url):
        self.response = requests.get(url)

    def search_info(self):
        soup = BeautifulSoup(self.response.content, "html.parser")
        
        # Buscar elementos con clase 'producto' que contienen información de las mochilas

        productos = soup.find_all("div",class_="b-product_tile")
        for producto in productos:
            
            #promo = producto.find(class_="b-product_tile-badge_promo m-bold")
            #pro = promo.find('span').get_text()
            #imgen = producto.find('picture',{'class' :'b-product_image m-main-img h-blend_mode_bg' })
            #img = imgen.find('img',{'class':'h-blend_mode_img lazy entered loaded'}).get('src')
            #print(img)
            #imgDowload = requests.get(img)
            #name = img.split("/")[-1]
            #SendImg = open(name+'.png','wb').write(imgDowload.content)
            nombre = producto.find( class_="b-product_tile-brand").text.strip()
            precio1 = producto.find(class_="b-product_price-value").text.strip()
            for i in range(len(precio1)):
                #print(i)
                if precio1[i] == '$':    
                    new_precio = precio1[i+1:len(precio1)]
            new_precio_clean = new_precio.replace(',','')
            precio = [float (precio) for precio in re.findall(r'-?\d+\.?\d*', new_precio_clean)]
            #precio = float(new_precio_clean)
            descripcion = producto.find(class_="b-product_tile-name").text.strip()
            tiempo_actual = datetime.datetime.now()
            information.append((nombre,precio[0],descripcion,tiempo_actual))
        return information
  