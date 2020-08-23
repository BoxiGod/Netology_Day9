import requests
import os


class YaUploader:

    access_token = ""
    headers = {"Authorization": "OAuth " + access_token}

    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        download_url = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload?path='
                                    + os.path.basename(self.file_path), headers=self.headers).json()
        download = requests.put(download_url['href'], open(self.file_path, 'rb'))
        if download.status_code == 201:
            return 'Успешно загружено'
        else:
            return 'Ошибка', download


if __name__ == '__main__':
    uploader = YaUploader(r'c:\my_folder\file2.txt')
    result = uploader.upload()
    print(result)
