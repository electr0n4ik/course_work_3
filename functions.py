# 1
def load_operations():
    """
    Зaгрузка списка операций из файла
    :return: возвращаем полученный список операций
    """
    import json

    with open("candidates.json", encoding="utf-8") as file:
        operations = json.load(file)
    return operations
