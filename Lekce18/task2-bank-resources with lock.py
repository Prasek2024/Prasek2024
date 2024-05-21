import threading
import time

balance = 1000
lock = threading.Lock()

def make_transaction(amount):
    global balance

    with lock:
        current_balance = balance

        time.sleep(0.1)
        balance = current_balance - amount


thread1 = threading.Thread(target=make_transaction, args=(200,))
thread2 = threading.Thread(target=make_transaction, args=(300,))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

# Očekávaný výsledek je 500, ale může být odlišný kvůli race condition
print("Zůstatek na účtu po transakcích:", balance)