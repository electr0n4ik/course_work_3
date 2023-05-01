from functions import *


def test_load_operations():
    operations = load_operations()
    assert isinstance(operations, list)
    assert len(operations) > 0


def test_get_split_date_time():
    datetime_str = "2023-05-01T12:30:00.000000"
    date, time = get_split_date_time(datetime_str)
    assert date == "2023-05-01"
    assert time == "12:30:00.000000"


def test_format_operations():
    operation_dict = {

        "id": 414894334,
        "state": "EXECUTED",
        "date": "2019-06-30",
        "operationAmount": {
            "amount": "95860.47",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 59956820797131895975",
        "to": "Счет 43475624104328495820"
    }
    expected_result = (
        "\n2019-06-30 Перевод со счета на счет\nСчет **5975 -> Счет **5820\n95860.47 руб."
    )
    assert format_operations(operation_dict) == expected_result


def test_get_last_5_operations():
    operations_list = load_operations()

    expected_result = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08',
                        'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                        'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907',
                        'time': '22:46:21.935582'},
                       {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07',
                        'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                         'to': 'Счет 35158586384610753655', 'time': '06:17:14.634890'},
                       {'id': 560813069, 'state': 'CANCELED', 'date': '2019-12-03',
                        'operationAmount': {'amount': '17628.50', 'currency': {'name': 'USD', 'code': 'USD'}},
                        'description': 'Перевод с карты на карту', 'from': 'MasterCard 1796816785869527',
                        'to': 'Visa Classic 7699855375169288', 'time': '04:27:03.427014'},
                       {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19',
                        'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                        'to': 'Счет 43241152692663622869', 'time': '09:22:25.899614'},
                       {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13',
                        'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
                        'to': 'Счет 46765464282437878125', 'time': '17:38:04.800051'}]

    assert get_last_5_operations(operations_list) == expected_result
