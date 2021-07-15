from bs4 import BeautifulSoup
import time
import csv
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)

headers = [
    "VMAG",
    "NAME",
    "DESIGNATION",
    "DISTANCE",
    "SPECTRAL_CLASS",
    "MASS",
    "RADIUS",
    "LUMINOSITY"
]

star_data = []

def scrape():
    soup = BeautifulSoup(page.content, "html.parser")

    
    for tbody_tag in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):

        t_body_tag = tbody_tag.find_all("tbody")
        temp_list = []
        print(t_body_tag)
        
        for tr_tag in t_body_tag:
            tr_tags = tr_tag.find_all("tr")
            for tr_tag in tr_tags.find_all("tr"):
                td_tags = tr_tag.find_all("td")

            for index,td_tag in enumerate(td_tags):
                try:
                    temp_list.append(td_tag)
                except:
                    temp_list.append("")
        star_data.append(temp_list)

    #print(star_data)    

scrape()

with open("planetData.csv", "w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)



