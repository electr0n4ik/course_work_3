from functions import *

list_5_last_date = []
for operation in load_operations():
    if operation["date"] > list_5_last_date[-1]:
        list_5_last_date.append(operation["date"])
