#Start by importing the necessary libraries


from PIL import Image
import requests
from io import BytesIO


#Define a function called open_image with a url parameter for the image address
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


#Call your function with an image URL
open_image("https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg")
open_image("https://s3.us-west-1.amazonaws.com/wakegov.com.if-us-west-1/s3fs-public/styles/card_grid/public/images/2024-04/adobestock_666178740.jpeg?h=487950bf&itok=4Fsxwen6")

#DO NOT FORGET TO CITE YOUR SOURCE
#The adorable face of a dog. Image source: The Dog API. 2009. Accessed via https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg CC BY-NC 2.0.
