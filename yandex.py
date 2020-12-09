import requests
import json
import yadisk
#g = requests.get('https://cloud-api.yandex.net/v1/disk/resources?' ,
#params={'path': '/'},
#headers={"Authorization": "OAuth AgAAAABKfUYlAAbBdsmIa8C0tkb1r_Y6ls8NPfI"})

#g.raise_for_status()
#data = g.json()
#for file in data['_embedded']['items']:
    #print(file['name'])


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        y = yadisk.YaDisk(token=self.token)
        y.upload(f'{file_path}', f'/{file_path}')

    def delete(self, file_path: str):
        y = yadisk.YaDisk(token=self.token)
        y.remove(f'{file_path}', permanently=True)


uploader = YaUploader('токен')
result = uploader.upload('Ваш файл')
result2 = uploader.delete('Ваш файл')
