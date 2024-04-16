from fronta import CharQueue


def main():
    queue_size = int(input("Enter the size of the queue: "))
    char_queue = CharQueue(queue_size)

    while True:
        print("\nMenu:")
        print("1. Check if the queue is empty")
        print("2. Check if the queue is full")
        print("3. Add an element to the queue (Enqueue)")
        print("4. Delete an element from the queue (Dequeue)")
        print("5. Display all queue elements")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Queue is empty." if char_queue.is_empty() else "Queue is not empty.")

        elif choice == '2':
            print("Queue is full." if char_queue.is_full() else "Queue is not full.")

        elif choice == '3':
            if char_queue.is_full():
                print("Queue is full. Cannot add new element.")
            else:
                element = input("Enter the character to enqueue: ")
                char_queue.enqueue(element)
                print("Element enqueued.")

        elif choice == '4':
            item = char_queue.dequeue()
            if item is not None:
                print(f"Dequeued element: {item}")
            else:
                print("Queue is empty. Cannot dequeue.")

        elif choice == '5':
            char_queue.show()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()