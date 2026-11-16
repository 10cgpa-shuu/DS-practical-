class Node:
    def __init__(self, prn, name):
        self.prn = prn
        self.name = name
        self.next = None


class Club:
    def __init__(self):
        self.head = None

    def add_president(self, prn, name):
        node = Node(prn, name)
        node.next = self.head
        self.head = node

    def add_secretary(self, prn, name):
        node = Node(prn, name)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def add_member(self, prn, name):
        node = Node(prn, name)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        node.next = current.next
        current.next = node

    def delete(self, prn):
        if self.head is None:
            print("Club is empty.")
            return

        if self.head.prn == prn:
            self.head = self.head.next
            print("Member deleted.")
            return

        current = self.head
        while current.next and current.next.prn != prn:
            current = current.next

        if current.next:
            current.next = current.next.next
            print("Member deleted.")
        else:
            print("PRN not found.")

    def count(self):
        total = 0
        current = self.head
        while current:
            total += 1
            current = current.next
        return total

    def display(self):
        current = self.head
        if current is None:
            print("Club is empty.")
            return

        position = 0
        while current:
            if position == 0:
                role = "President"
            elif current.next is None:
                role = "Secretary"
            else:
                role = "Member"

            print(role, "-> PRN:", current.prn,
                  "Name:", current.name)
            current = current.next
            position += 1

    def concatenate(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head
        other.head = None


division_a = Club()
division_b = Club()

while True:
    print("\n--- PINNACLE CLUB ---")
    print("1. Add President")
    print("2. Add Member")
    print("3. Add Secretary")
    print("4. Delete Member by PRN")
    print("5. Display Members")
    print("6. Count Members")
    print("7. Add Member to Division B")
    print("8. Concatenate Division B into Division A")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice in ("1", "2", "3", "7"):
        prn = input("Enter student PRN: ").strip()
        name = input("Enter student name: ").strip()

        if not prn or not name:
            print("PRN and name cannot be empty.")
            continue

        if choice == "1":
            division_a.add_president(prn, name)
        elif choice == "2":
            division_a.add_member(prn, name)
        elif choice == "3":
            division_a.add_secretary(prn, name)
        else:
            division_b.add_member(prn, name)

        print("Record added.")

    elif choice == "4":
        prn = input("Enter PRN to delete: ").strip()
        division_a.delete(prn)

    elif choice == "5":
        print("\nDivision A:")
        division_a.display()
        print("\nDivision B:")
        division_b.display()

    elif choice == "6":
        print("Division A members:", division_a.count())
        print("Division B members:", division_b.count())

    elif choice == "8":
        division_a.concatenate(division_b)
        print("Division B concatenated into Division A.")

    elif choice == "9":
        break

    else:
        print("Invalid choice.")
