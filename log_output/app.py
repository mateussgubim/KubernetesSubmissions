import uuid
import time
from datetime import datetime

def generate_uuid():
    random_string = uuid.uuid4()

    print(random_string)

generate_uuid()

def date():
    date_string = datetime.now(tz=None)
    
    print(date_string)

date()
