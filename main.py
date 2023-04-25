from functions import *
from datetime import *

for operation in load_operations():
    print(operation["state"])
    datetime_ = operation["date"]
    print(datetime_)
    print(datetime(datetime_))
