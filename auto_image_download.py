#coding: utf-8
#Download images automatically from google
# Author: Baimam Boukar Jean Jacques (baimamboukar@gmail.com), twiter: @Baimamjj



#Importing Modules that we will need for this script

import os
import json
import requests
from bs4 import BeautifulSoup


GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


def prepare_folder(data):
    folder = data.replace(" ", "_")
    os.mkdir(folder)
    return folder


def download_images():
    data = input("What specific images are you looking for ? : ")
    
    number_of_images = int(input("How many images do you want? : "))
   
    DESTINATION_FOLDER = prepare_folder(data)
    search_url = GOOGLE_IMAGE + "q=" + data
    response = requests.get(search_url, headers=usr_agent)
    html_data = response.text

    parsed_response = BeautifulSoup(html_data, 'html.parser')
    results = parsed_response.find_all('img', limit = number_of_images)
    images_links = []
    for image_tag in results:
        name = image_tag['alt']
        if name != "Google":
            link = image_tag['src']
            images_links.append(link)


    for i, imagelink in enumerate(images_links):
        # open image link and save as file
        img_response = requests.get(imagelink)
        base_name_of_images = data.replace(" ", "_")
        imagename = DESTINATION_FOLDER + '/' + base_name_of_images + str(i+1) + '.jpg'
        print(imagename)
        with open(imagename, 'wb') as file:
            file.write(img_response.content)



if __name__ == "__main__":
    download_images()

   
