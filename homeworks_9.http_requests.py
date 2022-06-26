from pprint import pprint
import json
import requests
import sys
import os
import time
import datetime as dt

# TOKEN = "2619421814940190"

# class superhero_api:
    
#     def __init__(self, token):
#         self.token = token


def test_request(adress):
    url = adress
    response = requests.get(url)
    return response


def Hero_intelligence(Hero_name,lst):
    for dic in lst:
            if dic['name'] == Hero_name :
                result = dic['powerstats']['intelligence']
    return result


def Hero_int_sort(intel:dict) -> str:
    count = 0
    for key in intel:
         if intel[key] > count:
            result = key
            count = intel[key]
    return result

class YandexDisk:

    def __init__(self, token):
        self.token = token
    
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    
    
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


def stackoverflow_quest(todayt,dayt,tag:str) -> dict:
    params = {
        'site': 'Stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': f'{dayt}',
        'todate': f'{todayt}',
        'tagged': tag

    }
    response = requests.get(url, params=params)
    resp = response.json()
    result = {}
    for items in resp['items']:
        unixdates = items['last_activity_date']
        date =dt.datetime.utcfromtimestamp(unixdates).strftime('%Y-%m-%d')
        result.setdefault(items['question_id'], {date: items['link']})
    return result

    


if __name__ == '__main__':

    # Задача 1


    adres = "https://akabab.github.io/superhero-api/api//all.json"
    js = test_request(adres)
    intel = {}
    lst =js.json()
    intel['Hulk'] = Hero_intelligence('Hulk',lst)
    intel['Captain America'] = Hero_intelligence('Captain America',lst)
    intel['Thanos'] = Hero_intelligence('Thanos',lst)
    hero = Hero_int_sort(intel)
    print(f'Самый умный герой {hero}')

    # Задача 2

    TOKEN = ""
    print(os.getcwd())
    path = '/test.txt'
    ya = YandexDisk(token=TOKEN)
    print("Текущая деректория:", os.getcwd())
    path_to_file = os.path.join(os.getcwd(),'test.txt')
    

    ya.upload_file_to_disk(path_to_file,'test.txt')


    # Задача 3

today = dt.date.today()
day = today - dt.timedelta(2)
print(day)
url = 'https://api.stackexchange.com/2.3/questions'
pprint(stackoverflow_quest(today, day, 'python'))








    
    


