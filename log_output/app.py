import uuid
import time
from datetime import datetime

def generate_output():
    string = f"{datetime.now(tz=None)}: {uuid.uuid4()}"

    print(string)

while True:
   generate_output()
   time.sleep(5)
