from ctypes.wintypes import tagMSG
import requests as req
import json
from bs4 import BeautifulSoup
import tqdm

data = {
    "data":[]
}

for page in range(0,40) :
    resp = req.get(f"https://ulan-ude.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&clusters=true&ored_clusters=true&enable_snippets=true&page={page}&hhtmFrom=vacancy_search_list", headers={'user-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    for iter in tqdm.tqdm(tags):
    # print(iter.text, iter.attrs["href"])

        url_object = iter.attrs["href"]
        # print( url_object)
        resp_object = req.get(url_object, headers={'user-agent': 'Mozilla/5.0'})

        soup_object = BeautifulSoup(resp_object.text, "lxml")
    
        tags_price = soup_object.find(attrs={"data-qa":"vacancy-salary"}).find(attrs={"class":"bloko-header-section-2 bloko-header-section-2_lite"}).text
        # print(iter.text, tags_price)
        tags_regions = soup_object.find(attrs={"data-qa":"vacancy-view-raw-address"})
        tags_experience = soup_object.find(attrs={"class":"vacancy-description-list-item"}).find(attrs={"data-qa":"vacancy-experience"}).text
        if (tags_regions) :
            tags_region = soup_object.find(attrs={"data-qa":"vacancy-view-raw-address"}).text
        else :
            tags_region = ''
        #print(tags_region)  
        data["data"].append({"Title":iter.text, "Work_experience": tags_experience,"Salary":tags_price, "Region": tags_region})  

        with open("data.json","w") as file:
            json.dump(data, file, ensure_ascii=False) 