import threading
import time

"""
# Funkce, kterou budeme volat v každém vlákně
def print_numbers():
    for i in range(5):
        time.sleep(2)  # Simulace časově náročné operace
        print(f"Vlákno {threading.current_thread().name}: {i}")


# Vytvoření dvou vláken
thread1 = threading.Thread(target=print_numbers, name="Vlákno 1")
thread2 = threading.Thread(target=print_numbers, name="Vlákno 2")

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení obou vláken
thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")

"""



def main_menu():
    print("Please enter three numbers.")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))

    choice = input("Choose 'max' for maximum, 'min' for minimum").lower()

    analysis = NumberAnalysis(number1, number2, number3)

    if choice == 'max':
        print("The maximum of the three numbers is:", analysis.find_max())
        print(f"Vlákno {threading.current_thread().name}: {i}")
    elif choice == 'min':
        print("The minimum of the three numbers is:", analysis.find_min())
        print(f"Vlákno {threading.current_thread().name}: {i}")
    else:
        print("Invalid choice. Please select 'max', 'min'.")

thread1 = threading.Thread(target=main_menu, name="Vlákno 1")
thread2 = threading.Thread(target=main_menu, name="Vlákno 2")

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení obou vláken
thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")

if __name__ == "__main__":
    main_menu()
