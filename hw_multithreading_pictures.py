import threading
import requests

url = 'https://picsum.photos/200'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def download_image():
    for i in range(1, 20):
        response = requests.get(url=url, headers=headers)
        with open(f'Temp_hw/image_{i}.jpg', 'wb') as file:
            file.write(response.content)


new_thread_1 = threading.Thread(target=download_image)
new_thread_1.start()
new_thread_2 = threading.Thread(target=download_image)
new_thread_2.start()
new_thread_3 = threading.Thread(target=download_image)
new_thread_3.start()


