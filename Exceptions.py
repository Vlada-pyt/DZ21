class BaseError(Exception):
    message = 'Произошла ошибка'

class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'

class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'

class TooManyProductError(BaseError):
    message = 'Слишком много товара'


class BadRequestError(BaseError):
    message = 'Неправильный запрос'

class UnknownStorage(BaseError):
    message = 'Неизвестный склад'

