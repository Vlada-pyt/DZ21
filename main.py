from typing import Dict

from Delivery import Delivery
from Exceptions import BaseError
from Shop import Shop
from abstract import AbstractStorage
from request import Request
from store import Store

store = Store(
    items={'яблоко': 10,
           'груша': 10}, capacity=100)

shop = Shop(
    items={'груша': 5}, capacity=20, max_unique_items=5
)

storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print('Добрый день')

    while True:

        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится\n{storage.get_items()}')

        req = input('Введите запрос\n'
                    'Введите "стоп" или "stop" чтобы закончить.').lower()
        if req in ('stop', 'стоп'):
            break

        try:
            request = Request(request=req, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        delivery = Delivery(request=request, storages=storages)
        try:
            delivery.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
