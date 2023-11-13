import requests
import time

def get_air_data():
    server_url = "https://"
    response = requests.get(server_url)
    return response.json()
    # dummy
    # response = {
    #     '2_5': 51,
    #     '10': 15,
    #     'voc': 5
    # }
    # return response


def get_average(list: list):
    sum = 0
    if len(list) == 0:
        return 0

    for val in list:
        sum = sum + val

    return sum / len(list)

def display_warning():
    print('Air quality is currently poor.')

def init_process():
    cnt = 0
    pm_2_5_queue = []
    pm_10_queue = []
    voc_queue = []
    return cnt, pm_2_5_queue, pm_10_queue, voc_queue

def process():
    cnt, pm_2_5_queue, pm_10_queue, voc_queue = init_process()

    while True:
        cnt = cnt + 1
        if cnt < 25:
            response = get_air_data()
            pm_2_5_queue.append(response['2_5'])
            pm_10_queue.append(response['10'])
            voc_queue.append(response['voc'])

            if cnt == 24:
                if get_average(pm_2_5_queue) > 50 or get_average(pm_10_queue) > 15 or get_average(voc_queue) > 5:
                    display_warning()
                cnt, pm_2_5_queue, pm_10_queue, voc_queue = init_process()
        time.sleep(0.2)


if __name__ == '__main__':
    process()