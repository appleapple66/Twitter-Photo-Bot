#photo scraping for twitter photo bot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with photo images
url = 'https://pixabay.com/en/photos/travel/'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for theme photo images
if not os.path.exists('twitterImage'):
    os.makedirs('twitterImage')

# move to new directory
os.chdir('twitterImage')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('tweet-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
