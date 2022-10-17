from typing import Dict

from abstract import AbstractStorage
from request import Request


class Delivery:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.departure: AbstractStorage = storages[self.__request.depature]
        self.destination: AbstractStorage = storages[self.__request.destination]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.depature}')

        print(f'Курьер везёт {self.__request.amount} {self.__request.product} со {self.__request.depature}'
              f'в {self.__request.destination}')
        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(f'курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')