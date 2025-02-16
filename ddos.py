import requests  

target = input("Введіть URL сайту: ")  
  
if not target.startswith("http://") and not target.startswith("https://"):  
    target = "https://" + target  

while True:  
    try:  
        r = requests.get(target)  
        print(f"Відповідь сервера: {r.status_code}")  
    except requests.exceptions.RequestException as e:  
        print(f"Помилка: {e}")  
        break  
