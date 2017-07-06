import pandas
import requests
from bs4 import BeautifulSoup

base_url = "http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
listall = []
rtemp = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
ctemp = rtemp.content
souptemp = BeautifulSoup(ctemp, "html.parser")
page_number = souptemp.find_all("a", {"class":"Page"})[-1].text
for page in range(0, int(page_number)*10, 10):
    req = requests.get(base_url + str(page) + ".html")
    c = req.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class":"propertyRow"})

    for prop in all:
        dict = {}
        dict["Address"] = prop.find_all("span", {"class":"propAddressCollapse"})[0].text.replace("\n","")
        dict["Address State"] = prop.find_all("span", {"class":"propAddressCollapse"})[1].text.replace("\n","")
        dict["Price"] = prop.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")
        try:
            dict["Beds"] = prop.find("span",{"class":"infoBed"}).find("b").text
        except:
            dict["Beds"] = None

        try:
            dict["Sq Ft"] = prop.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            dict["Sq Ft"] = None

        try:
            dict["Baths"] = prop.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            dict["Baths"] = None

        try:
            dict["Half Baths"] = prop.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            dict["Half Baths"] = None

        for col_grp in prop.find_all("div",{"class":"columnGroup"}):
            #print(col_grp)
            for feat_grp, feat_name in zip(col_grp.find_all("span",{"class":"featureGroup"}), col_grp.find_all("span",{"class":"featureName"})):
                if 'Lot Size' in feat_grp.text:
                    dict["Lot size"] = feat_name.text.replace(",","")

        listall.append(dict)

dataframe = pandas.DataFrame(listall)
dataframe.to_csv("Scraped_info.csv")
