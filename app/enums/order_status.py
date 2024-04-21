from enum import Enum


class OrderStatus(str, Enum):
    new = "Новый заказ"
    recruitment = "Подбор сотрудников"
    canceled = "Отменен"
    problems = "Неполадки"
    rejection = "Исполнитель отказался"
    execution = "В исполнении"
