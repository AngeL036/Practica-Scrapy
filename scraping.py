from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapy import Scrapy
from connection_mysql import DB
import pandas as pd


names = []
prices = []
descriptions = []
times = []
class Scraping():
        def __init__(self) -> None:
                pass
        def principal(self):
                # Abrir el navegador y cargar la página
                driver = webdriver.Chrome()
                driver.get("https://www.elpalaciodehierro.com")

                driver.implicitly_wait(3)
                        
                # busca los componentes por medio de clases y por nombre
                search_product = driver.find_element(by=By.NAME,value="q")
                search_button = driver.find_element(by=By.CLASS_NAME,value="b-quick_search-submit")
                #escribe en el buscador
                search_product.send_keys("mochilas")
                #presiona el boton para realizar la busqueda 
                search_button.click()
                #se crea un objeto tipo Scrapy insertando una url 
                scrapy = Scrapy(driver.current_url)
                informations =  scrapy.search_info()
                db = DB('localhost',3306,'root','Mariadb','mochilas')
                db.StartConnection()
                db.insert(informations)
                db.EndConection()
                iterable = driver.find_element(by=By.XPATH,value="/html/body/div[2]/div[3]/section/section/div[57]/div/ul/li[7]/a/span")
                number = int(iterable.text)

                for i in range(number-1):
                
                        informations.clear()
                        next_page = driver.find_element(by=By.CSS_SELECTOR, value="#maincontent > section > section > div.l-plp-container_pagination > div > ul > li.b-pagination-elements_list.b-next-btn > a")
                        page_url = next_page.get_attribute("href")
                        driver.get(next_page.get_attribute("href"))
                        driver.implicitly_wait(3)
                        next_scrapy = Scrapy(page_url)
                        informations = next_scrapy.search_info()
                        db.StartConnection()
                        db.insert(informations)
                        db.EndConection()


                


                '''
                for info,price,description in informations:
                names.append(info)
                prices.append(price)
                descriptions.append(description)
                #times.append(time)

                datos = {'nombre':names ,'precio':prices,'descripcion':descriptions,'hora y fecha':times}
                df = pd.DataFrame(datos)
                df.to_excel('prueba.xlsx',index=False)


                print(df)
                '''


                # Cerrar el navegador
                driver.implicitly_wait(5)
                driver.quit()