class HashTable:
    def __init__(self, size, method):
        self.size = size
        self.method = method
        self.table = [None] * size

    def hash1(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def hash2(self, key):
        return 1 + (
            sum(ord(ch) for ch in key) % (self.size - 1)
        )

    def insert(self, name, phone):
        index = self.hash1(name)
        step = self.hash2(name)

        for i in range(self.size):
            if self.method == "linear":
                pos = (index + i) % self.size
            elif self.method == "quadratic":
                pos = (index + i * i) % self.size
            else:
                pos = (index + i * step) % self.size

            if self.table[pos] is None:
                self.table[pos] = (name, phone)
                print("Contact added successfully.")
                return

            if self.table[pos][0] == name:
                self.table[pos] = (name, phone)
                print("Contact updated successfully.")
                return

        print("Hash table is full or no free slot was found.")

    def search(self, name):
        index = self.hash1(name)
        step = self.hash2(name)

        for i in range(self.size):
            if self.method == "linear":
                pos = (index + i) % self.size
            elif self.method == "quadratic":
                pos = (index + i * i) % self.size
            else:
                pos = (index + i * step) % self.size

            entry = self.table[pos]

            if entry is None:
                return None

            if entry[0] == name:
                return entry[1]

        return None

    def display(self):
        print("\nIndex | Name | Telephone Number")
        for i, entry in enumerate(self.table):
            if entry is None:
                print(i, "| Empty")
            else:
                print(i, "|", entry[0], "|", entry[1])


size = int(input("Enter hash table size (minimum 2): "))
if size < 2:
    print("Table size must be atleast 2.")
else:
    print("1. Linear Probing")
    print("2. Quadratic Probing")
    print("3. Double Hashing")
    choice = input("Choose collision method (1/2/3): ")

    methods = {
        "1": "linear",
        "2": "quadratic",
        "3": "double"
    }

    if choice not in methods:
        print("Invalid choice.")
    else:
        ht = HashTable(size, methods[choice])

        while True:
            print("\n1. Add Contact")
            print("2. Search Contact")
            print("3. Display Directory")
            print("4. Exit")

            option = input("Enter choice: ")

            if option == "1":
                name = input("Enter client name: ").strip()
                phone = input("Enter telephone number: ").strip()
                if name and phone:
                    ht.insert(name, phone)
                else:
                    print("Name and phone cannot be empty.")

            elif option == "2":
                name = input("Enter client name to search: ").strip()
                phone = ht.search(name)
                if phone is not None:
                    print("Telephone number:", phone)
                else:
                    print("Contact not found.")

            elif option == "3":
                ht.display()

            elif option == "4":
                print("Exiting telephone directory.")
                break

            else:
                print("Invalid choice.")