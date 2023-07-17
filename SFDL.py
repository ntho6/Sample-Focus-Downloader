# samplefocus.com Downloader

import requests
from bs4 import BeautifulSoup
import os

def download_mp3(url):
    response = requests.get(url)
    filename = url.split("/")[-1].split("?")[0]
    filename = os.path.splitext(filename)[0] + ".mp3"
    
    with open(filename, "wb") as file:
        file.write(response.content)
    
    print(f"Download completed: {filename}")

def extract_mp3_url(html):
    soup = BeautifulSoup(html, "html.parser")
    meta_tags = soup.find_all("meta", itemprop="contentUrl")
    
    if meta_tags:
        mp3_url = meta_tags[0]["content"]
        return mp3_url
    else:
        return None

def main():
    url = input("Enter the website URL: ")
    response = requests.get(url)
    
    if response.status_code == 200:
        mp3_url = extract_mp3_url(response.text)
        
        if mp3_url:
            download_mp3(mp3_url)
        else:
            print("No MP3 URL found in the HTML.")
    else:
        print("Error during HTTP request.")

if __name__ == "__main__":
    main()
