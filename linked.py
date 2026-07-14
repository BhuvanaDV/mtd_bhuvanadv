class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, value, position):
        if position < 1:
            raise ValueError("Position must be 1 or greater")

        new_node = Node(value)
        if position == 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 1
        while current.next and index < position - 1:
            current = current.next
            index += 1

        new_node.next = current.next
        current.next = new_node

    def insert_front(self, value):
        self.insert_at_position(value, 1)

    def insert_rear(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        if position == 1:
            removed = self.head
            self.head = self.head.next
            return removed.value

        current = self.head
        index = 1
        while current.next and index < position - 1:
            current = current.next
            index += 1

        if current.next is None:
            raise IndexError("Position out of range")

        removed = current.next
        current.next = removed.next
        return removed.value

    def delete_front(self):
        return self.delete_at_position(1)

    def delete_rear(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def update_at_position(self, position, value):
        if self.head is None:
            raise IndexError("List is empty")
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        current = self.head
        index = 1
        while current and index < position:
            current = current.next
            index += 1
        if current is None:
            raise IndexError("Position out of range")
        current.value = value

    def search(self, value):
        positions = []
        current = self.head
        index = 1
        while current:
            if current.value == value:
                positions.append(index)
            current = current.next
            index += 1
        return positions

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, value, position):
        if position < 1:
            raise ValueError("Position must be 1 or greater")

        new_node = DoublyNode(value)
        if position == 1 or self.head is None:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        index = 1
        while current.next and index < position - 1:
            current = current.next
            index += 1

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def insert_front(self, value):
        self.insert_at_position(value, 1)

    def insert_rear(self, value):
        if self.head is None:
            self.head = DoublyNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = DoublyNode(value)
        current.next.prev = current

    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        if position == 1:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return removed.value

        current = self.head
        index = 1
        while current and index < position:
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Position out of range")

        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        return current.value

    def delete_front(self):
        return self.delete_at_position(1)

    def delete_rear(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        current = self.head
        while current.next:
            current = current.next
        value = current.value
        current.prev.next = None
        return value

    def update_at_position(self, position, value):
        if self.head is None:
            raise IndexError("List is empty")
        if position < 1:
            raise ValueError("Position must be 1 or greater")
        current = self.head
        index = 1
        while current and index < position:
            current = current.next
            index += 1
        if current is None:
            raise IndexError("Position out of range")
        current.value = value

    def search(self, value):
        positions = []
        current = self.head
        index = 1
        while current:
            if current.value == value:
                positions.append(index)
            current = current.next
            index += 1
        return positions

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


class Stack:
    def __init__(self):
        self._list = SinglyLinkedList()

    def push(self, value):
        self._list.insert_front(value)

    def pop(self):
        return self._list.delete_front()

    def update(self, position, value):
        self._list.update_at_position(position, value)

    def search(self, value):
        return self._list.search(value)

    def display(self):
        return self._list.display()


class Queue:
    def __init__(self):
        self._list = SinglyLinkedList()

    def enqueue(self, value):
        self._list.insert_rear(value)

    def dequeue(self):
        return self._list.delete_front()

    def update(self, position, value):
        self._list.update_at_position(position, value)

    def search(self, value):
        return self._list.search(value)

    def display(self):
        return self._list.display()


def read_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue
        return value


def run_singly_linked_list():
    lst = SinglyLinkedList()
    while True:
        print("""
Singly Linked List Menu:
1. Insert at position
2. Delete at position
3. Update at position
4. Search value
5. Display list
6. Back to main menu
""")
        choice = read_int("Enter choice (1-6): ", 1, 6)
        if choice == 1:
            value = input("Enter value: ")
            position = read_int("Enter position: ", 1)
            try:
                lst.insert_at_position(value, position)
                print("Value inserted.")
            except Exception as error:
                print(error)
        elif choice == 2:
            if lst.head is None:
                print("List is empty.")
                continue
            position = read_int("Enter position to delete: ", 1)
            try:
                removed = lst.delete_at_position(position)
                print(f"Removed: {removed}")
            except Exception as error:
                print(error)
        elif choice == 3:
            if lst.head is None:
                print("List is empty.")
                continue
            position = read_int("Enter position to update: ", 1)
            value = input("Enter new value: ")
            try:
                lst.update_at_position(position, value)
                print("Node updated.")
            except Exception as error:
                print(error)
        elif choice == 4:
            value = input("Enter value to search: ")
            positions = lst.search(value)
            if positions:
                print(f"Value found at positions: {positions}")
            else:
                print("Value not found.")
        elif choice == 5:
            print("List:", lst.display())
        else:
            return


def run_doubly_linked_list():
    lst = DoublyLinkedList()
    while True:
        print("""
Doubly Linked List Menu:
1. Insert at position
2. Delete at position
3. Update at position
4. Search value
5. Display list
6. Back to main menu
""")
        choice = read_int("Enter choice (1-6): ", 1, 6)
        if choice == 1:
            value = input("Enter value: ")
            position = read_int("Enter position: ", 1)
            try:
                lst.insert_at_position(value, position)
                print("Value inserted.")
            except Exception as error:
                print(error)
        elif choice == 2:
            if lst.head is None:
                print("List is empty.")
                continue
            position = read_int("Enter position to delete: ", 1)
            try:
                removed = lst.delete_at_position(position)
                print(f"Removed: {removed}")
            except Exception as error:
                print(error)
        elif choice == 3:
            if lst.head is None:
                print("List is empty.")
                continue
            position = read_int("Enter position to update: ", 1)
            value = input("Enter new value: ")
            try:
                lst.update_at_position(position, value)
                print("Node updated.")
            except Exception as error:
                print(error)
        elif choice == 4:
            value = input("Enter value to search: ")
            positions = lst.search(value)
            if positions:
                print(f"Value found at positions: {positions}")
            else:
                print("Value not found.")
        elif choice == 5:
            print("List:", lst.display())
        else:
            return


def run_stack():
    stack = Stack()
    while True:
        print("""
Stack Menu:
1. Push (insert at front)
2. Pop (delete from front)
3. Update at position
4. Search value
5. Display stack
6. Back to main menu
""")
        choice = read_int("Enter choice (1-6): ", 1, 6)
        if choice == 1:
            value = input("Enter value to push: ")
            stack.push(value)
            print("Pushed.")
        elif choice == 2:
            try:
                value = stack.pop()
                print(f"Popped: {value}")
            except Exception as error:
                print(error)
        elif choice == 3:
            if not stack.display():
                print("Stack is empty.")
                continue
            position = read_int("Enter position to update: ", 1)
            value = input("Enter new value: ")
            try:
                stack.update(position, value)
                print("Stack updated.")
            except Exception as error:
                print(error)
        elif choice == 4:
            value = input("Enter value to search: ")
            positions = stack.search(value)
            if positions:
                print(f"Value found at positions: {positions}")
            else:
                print("Value not found.")
        elif choice == 5:
            print("Stack:", stack.display())
        else:
            return


def run_queue():
    queue = Queue()
    while True:
        print("""
Queue Menu:
1. Enqueue (insert at rear)
2. Dequeue (delete from front)
3. Update at position
4. Search value
5. Display queue
6. Back to main menu
""")
        choice = read_int("Enter choice (1-6): ", 1, 6)
        if choice == 1:
            value = input("Enter value to enqueue: ")
            queue.enqueue(value)
            print("Enqueued.")
        elif choice == 2:
            try:
                value = queue.dequeue()
                print(f"Dequeued: {value}")
            except Exception as error:
                print(error)
        elif choice == 3:
            if not queue.display():
                print("Queue is empty.")
                continue
            position = read_int("Enter position to update: ", 1)
            value = input("Enter new value: ")
            try:
                queue.update(position, value)
                print("Queue updated.")
            except Exception as error:
                print(error)
        elif choice == 4:
            value = input("Enter value to search: ")
            positions = queue.search(value)
            if positions:
                print(f"Value found at positions: {positions}")
            else:
                print("Value not found.")
        elif choice == 5:
            print("Queue:", queue.display())
        else:
            return


def run_app():
    while True:
        print("""
Main Menu:
1. Singly Linked List CRUD
2. Doubly Linked List CRUD
3. Stack (Singly Linked List)
4. Queue (Singly Linked List)
5. Exit
""")
        choice = read_int("Enter choice (1-5): ", 1, 5)
        match choice:
            case 1:
                run_singly_linked_list()
            case 2:
                run_doubly_linked_list()
            case 3:
                run_stack()
            case 4:
                run_queue()
            case 5:
                print("End of App")
                break


if __name__ == '__main__':
    run_app()
