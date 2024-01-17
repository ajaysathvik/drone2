import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://px4-travis.s3.amazonaws.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "xml")

links = soup.find_all("Key")

drone = "px4fmu-v2"

for link in links:
    if "_default.px4" in link.text:
        if drone in link.text:
            file_url = "https://px4-travis.s3.amazonaws.com/" + link.text
            response = requests.get(file_url) 
            f = open("dronefirmware.px4", 'wb')
            f.write(response.content)
            print("Downloaded")
            f.close()