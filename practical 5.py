
class Node:
    def __init__(self, time):
        self.time = time
        self.prev = None
        self.next = None


class Appointment:
    def __init__(self):
        self.head = None

    # Book Appointment
    def book(self, time):
        if time < 9 or time > 17:
            print("Invalid time! Enter between 9 and 17.")
            return

        temp = self.head
        while temp:
            if temp.time == time:
                print("Slot already booked!")
                return
            temp = temp.next

        new = Node(time)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

        print("Appointment booked successfully!")

    # Display Free Slots
    def free_slots(self):
        print("Available Slots:")

        for t in range(9, 18):
            temp = self.head
            found = False

            while temp:
                if temp.time == t:
                    found = True
                    break
                temp = temp.next

            if not found:
                print(t, "to", t + 1)

    # Display Appointments
    def display(self):
        temp = self.head

        if temp is None:
            print("No appointments booked.")
            return

        print("Booked Appointments:")
        while temp:
            print(temp.time, "to", temp.time + 1)
            temp = temp.next

    # Cancel Appointment
    def cancel(self, time):
        temp = self.head

        if time < 9 or time > 17:
            print("Invalid time!")
            return

        while temp:
            if temp.time == time:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print("Appointment cancelled successfully!")
                return

            temp = temp.next

        print("Appointment not found!")

    # Sort using Data Swapping
    def sort_data(self):
        temp = self.head

        while temp:
            current = temp.next

            while current:
                if temp.time > current.time:
                    temp.time, current.time = current.time, temp.time

                current = current.next

            temp = temp.next

        print("Sorted using data swapping.")

    # Sort using Pointer Manipulation
    def sort_pointer(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            current.prev = None
            current.next = None

            if sorted_head is None:
                sorted_head = current

            elif current.time < sorted_head.time:
                current.next = sorted_head
                sorted_head.prev = current
                sorted_head = current

            else:
                temp = sorted_head

                while temp.next and temp.next.time < current.time:
                    temp = temp.next

                current.next = temp.next
                current.prev = temp

                if temp.next:
                    temp.next.prev = current

                temp.next = current

            current = next_node

        self.head = sorted_head
        print("Sorted using pointer manipulation.")


# Main Program
a = Appointment()

while True:
    print("\n--- APPOINTMENT SCHEDULING ---")
    print("1. Display Free Slots")
    print("2. Book Appointment")
    print("3. Display Appointments")
    print("4. Cancel Appointment")
    print("5. Sort using Data Swapping")
    print("6. Sort using Pointer Manipulation")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a.free_slots()

    elif choice == 2:
        t = int(input("Enter appointment time (9-17): "))
        a.book(t)

    elif choice == 3:
        a.display()

    elif choice == 4:
        t = int(input("Enter time to cancel: "))
        a.cancel(t)

    elif choice == 5:
        a.sort_data()

    elif choice == 6:
        a.sort_pointer()

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
