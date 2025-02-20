import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, output_folder):
    response = requests.get(url)
    if response.status_code != 200:
        print("Fehler beim Abrufen der Webseite")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []
    titles = {}
    
    for container in soup.find_all('div', class_='text-white text-md p-2'):
        title_tag = container.find('span', class_='font-bold')
        img_tag = container.find('img')
        
        if title_tag and img_tag:
            title = title_tag.text.strip()
            img_url = img_tag['src']
            full_img_url = urljoin(url, img_url)
            
            if title in titles:
                titles[title] += 1
                filename = f"{title} {titles[title]}.jpg"
            else:
                titles[title] = 1
                filename = f"{title}.jpg"
            
            images.append((full_img_url, filename))
    
    os.makedirs(output_folder, exist_ok=True)
    
    for img_url, filename in images:
        img_response = requests.get(img_url, stream=True)
        if img_response.status_code == 200:
            with open(os.path.join(output_folder, filename), 'wb') as file:
                for chunk in img_response.iter_content(1024):
                    file.write(chunk)
            print(f"Bild gespeichert: {filename}")
        else:
            print(f"Fehler beim Herunterladen: {img_url}")

# URLs der Seiten und Ausgabe-Ordner
pages = {
    "utilityPoles": "https://geohints.com/meta/utilityPoles"
}

output_directories = {
    "bollards": "bollard_images",
    "utilityPoles": "pole_images"
}

for key, url in pages.items():
    download_images(url, output_directories[key])
