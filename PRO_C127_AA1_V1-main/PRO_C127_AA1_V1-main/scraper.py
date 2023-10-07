from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager

import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Definir el método de extracción de datos para Exoplanet
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ##objeto de beautifulSoup##
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags =ul_tag.find_all("li")        
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
                planets_data.append(temp_list)
            browser.find_element(by= By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



        
# Llamada del método
scrape()

# Definir los encabezados
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Definir el dataframe de Pandas
planets_df_1 = pd.DataFrame (planets_data, columns=headers)

# Convertir a CSV
planets_df_1.to_csv("scrped_data.cvs", index=True, index_label="id")
    


