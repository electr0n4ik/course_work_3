# 1
def load_operations():
    """
    Зaгрузка списка операций из файла
    :return: возвращаем полученный список операций
    """
    import json

    with open("operations.json", encoding="utf-8") as file:
        operations = json.load(file)
    return operations


# 2
def get_5_last_operations(list_operations):
    """
    Получает список операций и возвращает 5 последних выполненных операций
    :param list_operations: список операций
    :return: 5 последних выполненных операций
    """
    list_executed = []
    for operation in list_operations:
        if operation["state"] == "EXECUTED":
            list_executed.append(operation)

