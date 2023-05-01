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
def get_split_date_time(datetime_):
    """
    Получает на вход строку с датой и временем по типу:
        "ГГГГ-ММ-ДДT00:00:00.000000"
    Вохвращает список из двух элементов,
    первый элемент дата,
    второй элемент время.
    """
    return datetime_.split("T")


# 3
def format_operations(operation_dict):
    """
    Функция принимает на вход список из 5 операций и возвращает их в виде строк в заданном формате:

    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    date = operation_dict['date']
    description = operation_dict['description']
    if 'from' in operation_dict:
        from_card = operation_dict['from']
        # Маскируем номер карты или счета
        if 'Счет' in from_card:
            from_card_masked = f"{from_card[:-20]}**{from_card[-4:]}"
        else:
            from_card_masked = f"{from_card[:-12]} {from_card[-12:-10]}** **** {from_card[-4:]}"
    else:
        from_card_masked = "Unknown"
    to = operation_dict['to']
    amount = operation_dict['operationAmount']['amount']
    currency = operation_dict['operationAmount']['currency']['name']

    # Маскируем
    to_masked = to[:-20] + '**' + to[-4:]

    # Форматируем информацию
    formatted = f"\n{date} {description}\n{from_card_masked} -> {to_masked}\n{amount} {currency}"
    return formatted


# 4
def get_last_5_operations(operations_lict):
    """
    Функция принимает на вход словарь с вложенными списками операций и возвращает
    5 последних операций по дате.
    """
    from datetime import datetime

    all_operations = []
    for operation in operations_lict:
        if "date" in operation:
            date, time = get_split_date_time(operation['date'])
            operation['date'] = date
            operation['time'] = time
            all_operations.append(operation)

    sorted_operations = sorted(all_operations, key=lambda op: datetime.strptime(op['date'], '%Y-%m-%d'), reverse=True)

    return sorted_operations[:5]

print(get_last_5_operations(load_operations()))

# 5
def print_last_five_operations(operations_list):
    """
    Функция принимает на вход словарь с вложенными списками операций,
    использует функцию get_last_five_operations() для получения 5 последних операций,
    использует функцию format_operations_by_type() для форматирования операций по типу,
    и выводит отформатированные операции в консоль.
    """
    last_five_operations = get_last_5_operations(operations_list)
    for operation in last_five_operations:
        print(format_operations(operation))
