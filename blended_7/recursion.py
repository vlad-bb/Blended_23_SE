import requests
import time


def save_ststus(order_id):
    pass


def send_order(order_id: int):
    response = requests.post(url=f'https://nova-post.com/api/create_order/{order_id}')
    if response.status_code == 200:  # base case
        save_ststus(order_id)
    elif response.status_code == 429:  # recursion case
        time.sleep(12)
        send_order(order_id)


