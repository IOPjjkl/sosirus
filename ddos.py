import requests
import json
import time
import os

API_URL = "https://server.leakosint.com/"
TIMEOUT_FILE = "last_request_time.txt"
TIME_LIMIT = 0 * 60 

def save_last_request_time():
    with open(TIMEOUT_FILE, "w") as f:
        f.write(str(time.time()))

def get_last_request_time():
    if os.path.exists(TIMEOUT_FILE):
        with open(TIMEOUT_FILE, "r") as f:
            return float(f.read().strip())
    return 0

def can_make_request():
    last_request_time = get_last_request_time()
    current_time = time.time()
    if current_time - last_request_time >= TIME_LIMIT:
        return True
    else:
        remaining_time = TIME_LIMIT - (current_time - last_request_time)
        print(f"Подождите еще {remaining_time // 60:.0f} минут {remaining_time % 60:.0f} секунд перед следующим запросом.")
        return False

def search_leaks(request, token, limit=1000):
    data = {
        "token": token,
        "request": request,
        "limit": limit
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        save_last_request_time()
        return handle_response(response)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")
        return {"error": "Запрос не удался"}

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def print_leak_info(leak_info):
    if 'NumOfResults' in leak_info and leak_info['NumOfResults'] > 0:
        for source, details in leak_info['List'].items():
            print(f"Источник: {source}")
            for record in details['Data']:
                if isinstance(record, dict):
                    for key, value in record.items():
                        if key != 'InfoLeak':
                            print(f"  - {key}: {value}")
    else:
        print("Результаты не найдены либо LeakOsint сдох")

if __name__ == "__main__":
    token = "5206469931:yYk4Sa21"  
    if can_make_request():
        request = input("Введите запрос для поиска: ")
        result = search_leaks(request, token)
        print_leak_info(result)

