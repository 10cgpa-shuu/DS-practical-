
class Graph:

    def __init__(self):
        self.graph = {}

    # Add a city (vertex)
    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = []
            print("City added successfully!")
        else:
            print("City already exists!")

    # Add flight path (edge)
    def add_flight(self, city1, city2, weight):

        if city1 not in self.graph or city2 not in self.graph:
            print("Please add both cities first!")
            return

        self.graph[city1].append((city2, weight))
        self.graph[city2].append((city1, weight))

        print("Flight path added successfully!")

    # Display adjacency list
    def display(self):

        if not self.graph:
            print("Graph is empty!")
            return

        print("\nFlight Paths (Adjacency List):")

        for city in self.graph:
            print(city, "->", end=" ")

            for neighbour, weight in self.graph[city]:
                print(neighbour, "(", weight, ")", end=" ")

            print()

    # DFS traversal
    def dfs(self, city, visited):

        visited.add(city)

        for neighbour, weight in self.graph[city]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    # Check graph connectivity
    def is_connected(self):

        if not self.graph:
            return False

        visited = set()

        start_city = next(iter(self.graph))

        self.dfs(start_city, visited)

        if len(visited) == len(self.graph):
            return True
        else:
            return False


# Main Program
g = Graph()

while True:

    print("\n====== FLIGHT PATH GRAPH ======")
    print("1. Add City")
    print("2. Add Flight Path")
    print("3. Display Graph")
    print("4. Check Connectivity")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        city = input("Enter city name: ")
        g.add_city(city)

    elif choice == 2:

        city1 = input("Enter starting city: ")
        city2 = input("Enter destination city: ")
        weight = int(input("Enter flight time/fuel cost: "))

        g.add_flight(city1, city2, weight)

    elif choice == 3:

        g.display()

    elif choice == 4:

        if g.is_connected():
            print("The graph is CONNECTED.")
        else:
            print("The graph is DISCONNECTED.")

    elif choice == 5:

        print("Program terminated successfully!")
        break

    else:
        print("Invalid choice! Please try again.")
