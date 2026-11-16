
class Node:
    def __init__(self, time):
        self.time = time
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert appointment at the end
    def book_appointment(self, time):

        if time < 9 or time > 17:
            print("Invalid time! Working hours are 9 AM to 5 PM.")
            return

        if self.search(time):
            print("This appointment slot is already booked!")
            return

        new_node = Node(time)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Appointment booked successfully!")

    # Search for an appointment
    def search(self, time):
        temp = self.head

        while temp is not None:
            if temp.time == time:
                return True
            temp = temp.next

        return False

    # Display all booked appointments
    def display(self):
        if self.head is None:
            print("No appointments booked.")
            return

        temp = self.head
        print("\nBooked Appointments:")

        while temp is not None:
            print(temp.time, "to", temp.time + 1, "PM/AM (hour slot)")
            temp = temp.next

    # Display free appointment slots
    def display_free_slots(self):
        print("\nAvailable Appointment Slots:")

        found = False

        for time in range(9, 17):
            if not self.search(time):
                print(time, ":00 -", time + 1, ":00")
                found = True

        if not found:
            print("No free slots available.")

    # Cancel appointment
    def cancel_appointment(self, time):

        if time < 9 or time >= 17:
            print("Invalid cancellation time!")
            return

        if not self.search(time):
            print("No appointment found at this time!")
            return

        temp = self.head

        while temp is not None:
            if temp.time == time:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                print("Appointment cancelled successfully!")
                return

            temp = temp.next

    # Sort appointments using data swapping
    def sort_by_data(self):

        if self.head is None:
            print("No appointments to sort.")
            return

        current = self.head

        while current is not None:
            index = current.next

            while index is not None:
                if current.time > index.time:
                    current.time, index.time = index.time, current.time

                index = index.next

            current = current.next

        print("Appointments sorted using data swapping.")

    # Sort appointments using pointer manipulation
    def sort_by_pointer(self):

        if self.head is None or self.head.next is None:
            print("List is already sorted.")
            return

        current = self.head.next

        while current is not None:

            next_node = current.next
            temp = current.prev

            # Find correct position
            while temp is not None and temp.time > current.time:
                temp = temp.prev

            # Remove current node from its position
            if current.prev is not None:
                current.prev.next = current.next

            if current.next is not None:
                current.next.prev = current.prev

            # Insert at beginning
            if temp is None:
                current.prev = None
                current.next = self.head
                self.head.prev = current
                self.head = current

            # Insert after temp
            else:
                current.prev = temp
                current.next = temp.next

                if temp.next is not None:
                    temp.next.prev = current

                temp.next = current

            current = next_node

        print("Appointments sorted using pointer manipulation.")


# Main Program
dll = DoublyLinkedList()

while True:

    print("\n========== APPOINTMENT SCHEDULING ==========")
    print("1. Display Free Slots")
    print("2. Book Appointment")
    print("3. Display Booked Appointments")
    print("4. Sort by Time (Data Swapping)")
    print("5. Cancel Appointment")
    print("6. Sort by Time (Pointer Manipulation)")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.display_free_slots()

    elif choice == 2:
        time = int(input("Enter appointment time (9 to 16): "))
        dll.book_appointment(time)

    elif choice == 3:
        dll.display()

    elif choice == 4:
        dll.sort_by_data()
        dll.display()

    elif choice == 5:
        time = int(input("Enter appointment time to cancel: "))
        dll.cancel_appointment(time)

    elif choice == 6:
        dll.sort_by_pointer()
        dll.display()

    elif choice == 7:
        print("Thank you for using Appointment Scheduling System!")
        break

    else:
        print("Invalid choice! Please try again.")
