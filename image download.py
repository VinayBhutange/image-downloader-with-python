import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,1000)
    full_name= str(name) + ".jpg"
    urllib.request.urlretrieve(url,  full_name)

download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKZhcknIqR_ecPIxsViKnkFqYeJocB6YjZKUP4ylQfC1-Lzq8q")
