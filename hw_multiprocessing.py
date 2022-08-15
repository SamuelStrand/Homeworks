import asyncio
import time
import requests
import threading
import multiprocessing
import aiohttp
import json

url = 'https://jsonplaceholder.typicode.com/todos/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def measure(func):
    def wrap(*args, **kwargs):
        print('start measure')

        time1 = time.perf_counter()
        res = func(*args, **kwargs)  # ядро декорируемой функции

        print('end measure')
        print(f'функция потратила времени: {time.perf_counter() - time1}')
        return res

    return wrap


def get_data(index=0):
    urls = 'https://jsonplaceholder.typicode.com/todos/'
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url=urls, headers=headers)

    print(response.content)
    print(type(response.content))

    json_data = json.loads(response.content)[0:10]

    print(json_data)
    print(type(json_data))

    index = 0
    for i in json_data:
        index = index + 1
        with open(f'Temp_hw/new_{index}.json', 'w') as file:
            json_string = json.dumps(i)
            file.write(json_string)


# multithreading
@measure
def func_thread():
    thread_list = [threading.Thread(target=get_data, args=(f"thread_{x}",), kwargs={}) for x in range(1, 10)]

    for i in thread_list:
        i.start()

    for i in thread_list:
        i.join()


# multiprocessing
@measure
def func_processing():
    process_list = [multiprocessing.Process(target=get_data, args=(f"process_{x}",), kwargs={}) for x in
                    range(1, 10)]

    for i in process_list:
        i.start()

    for i in process_list:
        i.join()


# async
async def async_get_data(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as await_response:
            data = await await_response.json()

    index = 0
    for i in data[0:10]:
        index = index + 1
        with open(f'Temp_hw/async_json{index}.json', 'w') as file:
            json_string = json.dumps(i)
            file.write(json_string)


@measure
def func_async():
    async def tasks_generator():
        await asyncio.gather(
            *[async_get_data(f"async_{x}") for x in range(1, 11)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


if __name__ == '__main__':
    # get_data()
    # func_thread()
    # func_processing()
    func_async()
