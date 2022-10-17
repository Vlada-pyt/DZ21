from typing import Dict

from Exceptions import BadRequestError, UnknownStorage
from abstract import AbstractStorage


class Request:
    def __init__(self, request, storages: Dict[str, AbstractStorage]):
        split_req = request.strip().lower().split(' ')
        if len(split_req) != 7:
            raise BadRequestError
        self.amount = int(split_req[1])
        self.product = split_req[2]
        self.depature = split_req[4]
        self.destination = split_req[6]

        if self.depature not in storages or self.destination not in storages:
            raise UnknownStorage