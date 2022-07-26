import shutil
import requests
import os
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

def StartSearch():
    search = input("Hey! What are you looking for today? Type 'exit' to exit. ")

    try:
        search_lower = search.lower()
        # print(search_lower)
        if search_lower == 'exit':
            return
    except:
        pass

    # print('Continued.')
    dir_name = input('Name of Folder: ')
    if not os.path.exists('./{}'.format(dir_name)):
        os.mkdir('./{}'.format(dir_name))

    else:
        shutil.rmtree('./{}'.format(dir_name))
        os.mkdir('./{}'.format(dir_name))

    params = {'q' : search}

    r = requests.get("https://www.unsplash.com/search", params=params)

    soup = BeautifulSoup(r.text, 'html.parser')

    # with open('imagesoup.txt', 'w+', encoding='utf-8') as iss:
    #     iss.write(soup.prettify())

    links = soup.findAll('img', {'class' : "YVj9w"})
    # print(links)

    i = 1

    for link in links:
        if i <= 30:
            img = requests.get(link.attrs['src'])
            print('------------------')
            
            # print("https://www.unsplash.com{}".format(link.attrs['href']))
            # img_url = requests.get(link.attrs['src'])
            # print(img_url.url)


            img_alt = '{} {}'.format(dir_name,i)
            i += 1

            print(img_alt)

            img = Image.open(BytesIO(img.content))
            # print(img.format)
            # print('Yes')
            # img = Image.open(BytesIO(img_url))
            img = img.save('./{}/'.format(dir_name) + (img_alt) + '.png')
            print('Saved a picture!')

            # # if img_url and img_alt:
            # #     print(img_alt)
            # #     print()
            # #     print("-------------------")

            # # else:
            # #     print('No Results Found.')
            # #     exit()
    
    StartSearch()

StartSearch()