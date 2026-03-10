import os
import requests

BASE_URL = "https://comune.grosotto.so.it"
PAGE_NAME = "domande-frequenti"
PAGE_URL = f"{BASE_URL}/{PAGE_NAME}/"

OUTPUT_FOLDER = "pages"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

response = requests.get(PAGE_URL)

with open(os.path.join(OUTPUT_FOLDER, f"{PAGE_NAME}.html"), "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML downloaded successfully!")