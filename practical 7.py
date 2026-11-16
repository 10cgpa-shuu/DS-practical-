class PizzaQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def add_order(self, order):
        if self.count == self.capacity:
            print("Queue is full! Cannot accept more orders.")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order
        self.count += 1
        print("Order added successfully:", order)

    def serve_order(self):
        if self.count == 0:
            print("No orders to serve.")
            return

        order = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print("Order served:", order)

    def display(self):
        if self.count == 0:
            print("No pending orders.")
            return

        print("Pending orders:")
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            print(self.queue[index])

    def total_orders(self):
        return self.count


m = int(input("Enter maximum number of orders: "))
if m <= 0:
    print("Capacity must be greater than zero.")
else:
    pizza = PizzaQueue(m)

    while True:
        print("\n--- PIZZA PARLOUR ---")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. Display Pending Orders")
        print("4. Count Pending Orders")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            order = input("Enter order name or number: ").strip()
            if order:
                pizza.add_order(order)
            else:
                print("Order cannot be empty.")

        elif choice == "2":
            pizza.serve_order()

        elif choice == "3":
            pizza.display()

        elif choice == "4":
            print("Pending orders:", pizza.total_orders())

        elif choice == "5":
            print("Exiting Pizza Parlour system.")
            break

        else:
            print("Invalid choice.")
