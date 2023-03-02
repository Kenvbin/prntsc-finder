import webbrowser
import random
import time
import string

characters = string.ascii_lowercase + string.digits

for i in range(5):
    exti = ''.join(random.choice(characters) for i in range(6))
    webbrowser.open(f'https://prnt.sc/{exti}')
    time.sleep(1)