class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = new_node

        print("Node Inserted Successfully")

    def delete(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        value = int(input("Enter value to delete: "))

        if self.head.data == value:
            self.head = self.head.link
            print("Node Deleted")
            return

        prev = None
        temp = self.head

        while temp is not None:
            if temp.data == value:
                prev.link = temp.link
                print("Node Deleted")
                return
            prev = temp
            temp = temp.link

        print("Value Not Found")

    def update(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        old = int(input("Enter old value: "))
        new = int(input("Enter new value: "))

        temp = self.head

        while temp is not None:
            if temp.data == old:
                temp.data = new
                print("Node Updated")
                return
            temp = temp.link

        print("Value Not Found")

    def search(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        value = int(input("Enter value to search: "))

        position = 1
        temp = self.head

        while temp is not None:
            if temp.data == value:
                print("Value Found at Position", position)
                return
            temp = temp.link
            position += 1

        print("Value Not Found")

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        temp = self.head

        print("Linked List:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.link
        print("None")

ll = LinkedList()

def insert():
    ll.insert()

def delete():
    ll.delete()

def update():
    ll.update()

def search():
    ll.search()

def display():
    ll.display()

def menu(choice):
    match choice:
        case 1:
            insert()
        case 2:
            delete()
        case 3:
            update()
        case 4:
            search()
        case 5:
            display()
        case _:
            print("Invalid Choice")

def run_app():
    while True:
        print("\n------ Linked List Menu ------")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Search")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 6:
            break

        menu(choice)

    print("End of Program")

run_app()
