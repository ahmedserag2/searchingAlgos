from queue import PriorityQueue


# Node of the graph
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = {}
        self.visited = False

    # add a neighbour name to a vertex
    def add_neighbor(self, vertexName, cost):
        if vertexName not in self.neighbors:
            # print(self.name + ' and ' + vertexName + 'are now neigbors')
            self.neighbors[vertexName] = cost


class Graph:
    # Dictionary "Python" or Hashmap "Java" of Vertices in the graph =>key = vertex name, value = object of vertex
    vertices = {}
    verticesObj = []

    def reset_vertices(self):
        for i in self.verticesObj:
            i.visited = False

    def add_vertex(self, vertex):
        self.verticesObj.append(vertex)
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # Create edge between two vertices that already exists in the graph
    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # key = vertex name, value = object of vertex
            for key, value in self.vertices.items():
                # Adding each vertex name neighbour to the other vertex with cost
                if key == vertex1:
                    # print(vertex1 + 'and ' + vertex2 + 'are now neigbors')
                    value.add_neighbor(vertex2, cost)
                if key == vertex2:
                    # print(vertex1 + 'and ' + vertex2 + 'are now neigbors')
                    value.add_neighbor(vertex1, cost)
            return True
        else:
            return False

    # BFS Algorithm that user specify starting vertex and goal vertex
    def BFS(self, start, goal):
        queue = list()
        searchList = [start.name]
        start.visited = True
        queue.append((0, start.name))
        actual_cost = 0
        while (len(queue)):

            cost, s = queue.pop(0)
            # print(cost)
            if s == goal:
                print(s)
                print('cost is ' + str(cost))
                break
            # print(s)
            node_u = self.vertices[s]
            print(node_u.name, end=' ')
            node_u.visited = True
            # neigbor loop
            for i in node_u.neighbors:
                node_v = self.vertices[i]

                if node_v.visited == False and i not in searchList:
                    new_cost = cost + node_u.neighbors[node_v.name]
                    queue.append((new_cost, i))
                    searchList.append(i)
            # print("frontier",searchList)
        self.reset_vertices()
        return searchList

    def DFS(self, start, goal):
        stack = list()
        searchList = [start.name]
        start.visited = True
        stack.append((0, start.name))
        actual_cost = 0
        while (len(stack)):

            cost, s = stack.pop()
            # print(cost)
            if s == goal:
                print(s)
                print('cost is ' + str(cost))
                break
            # print(s)
            node_u = self.vertices[s]
            print(node_u.name, end=' ')
            node_u.visited = True
            # self.neighbors[vertexName] = cost
            # if (not s.visited):
            # print(s.name,end=' ')
            # s.visited = True
            # neigbor loop
            for i in node_u.neighbors:
                node_v = self.vertices[i]

                if node_v.visited == False and i not in searchList:
                    new_cost = cost + node_u.neighbors[node_v.name]
                    stack.append((new_cost, i))
                    searchList.append(i)
            # print("frontier",searchList)
        self.reset_vertices()
        return searchList

    # ASTAR Algorithm
    def ASTAR(self, h, start, goal):
        count = 0
        frontier = PriorityQueue()
        frontier.put((0, [start]))
        cost_so_far = {}
        cost_so_far[start] = 0
        while frontier:
            count += 1
            cost, node = frontier.get()
            current = self.vertices[node[len(node) - 1]]
            if current.visited == False:
                current.visited = True
                if current.name == goal:
                    print("Path found by Astar: " + str(node) + ", Cost = " + str(cost) + ", Count= " + str(count))
                    break
                for vertexName, edgeCost in current.neighbors.items():
                    if self.vertices[vertexName].visited == False:
                        temp = node[:]
                        temp.append(vertexName)
                        new_cost = cost_so_far[current.name] + edgeCost
                        heuristicValue = h[vertexName]
                        frontier.put((new_cost + heuristicValue, temp))
                        cost_so_far[vertexName] = new_cost
                # print("Path till now", node)
        self.reset_vertices()

    # UCS
    def UCS(self, start, goal):
        count = 0
        frontier = PriorityQueue()
        frontier.put((0, [start]))
        while frontier:
            count += 1
            cost, node = frontier.get()
            current = self.vertices[node[len(node) - 1]]
            if current.visited == False:
                current.visited = True
                if current.name == goal:
                    print("Path found by UCS: " + str(node) + ", Cost = " + str(cost) + ", Count= " + str(count))
                    break
                for vertexName, edgeCost in current.neighbors.items():
                    if self.vertices[vertexName].visited == False:
                        temp = node[:]
                        temp.append(vertexName)
                        new_cost = cost + edgeCost
                        frontier.put((new_cost, temp))
                # print("Path till now", node)
        self.reset_vertices()

    # GBFS
    def GBFS(self, h, start, goal):
        count = 0
        frontier = PriorityQueue()
        frontier.put((0, [start]))

        while frontier:
            count += 1
            cost, node = frontier.get()
            # print(cost)
            current = self.vertices[node[len(node) - 1]]
            if current.visited == False:
                current.visited = True
                if current.name == goal:
                    print("Path found by GBFS: " + str(node) + ", And the cost is= " + str(cost) + ", Count= " + str(
                        count))
                    break
                for vertexName, edgeCost in current.neighbors.items():
                    if self.vertices[vertexName].visited == False:
                        temp = node[:]
                        temp.append(vertexName)
                        heuristicValue = h[vertexName]
                        new_cost = cost + edgeCost
                        frontier.put((heuristicValue, temp))
                # print("Path till now", node)
        self.reset_vertices()

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


# Create Graph
g = Graph()

vertices = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea',
            'Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu'
            ,'Urziceni','Hirsova','Vaslui','Iasi','Neamt','Efori']

vertexArr = []
c = 0
for i in vertices:
    vertexArr.append(Vertex(i))
    g.add_vertex(vertexArr[c])
    c += 1

# g.print_graph()
edges = {
    'Arad': {'Zerind': 75, 'Sibiu': 140},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138},
    'Fagaras': {'Bucharest': 211},
    'Dobreta': {'Craiova': 120},
    'Bucharest': {'Pitesti': 101, 'Giurgiu': 90,'Urziceni':85},
    'Urziceni': {'Hirsova': 98,'Vaslui':142},
    'Hirsova': {'Efori': 86},
    'Vaslui': {'Iasi':92},
    'Iasi': {'Neamt':87}
    

}

for vertex1, value in edges.items():
    for vertex2, cost in edges[vertex1].items():
        g.add_edge(vertex1, vertex2, cost)

heuristicValue = {'Arad': 366, 'Zerind': 374,
                  'Timisoara': 200,
                  'Sibiu': 253,
                  'Oradea': 380,
                  'Lugoj': 244, 'RimnicuVilcea': 193,
                  'Mehadia': 241, 'Craiova': 160,
                  'Pitesti': 10, 'Fagaras': 176,
                  'Dobreta': 242, 'Bucharest': 0,
                  'Giurgiu': 77,
                  'Urziceni':80, 'Hirsova':151, 'Efori':161,'Vaslui':199,'Iasi':226,'Neamt':234}



def MainCode():
    ans=True
    while ans:
        g.print_graph()
        print("""\n**Choose From The Graph your start and goal**\n""")
        start = input("Your Start : ")
        goal = input("Your goal : ")
        print("""
        1.UCS
        2.DFS
        3.BFS
        4.GBFS
        5.A Star
        6.Exit/Quit
        """)
        ans=input("What would you like to do? \n")
        if ans=="1":
            g.UCS(start,goal)
            break
        elif ans=="2":
            g.DFS(Vertex(start),goal)
            break
        elif ans=="3":
            g.BFS(Vertex(start), goal)
            break
        elif ans=="4":
            g.GBFS(heuristicValue, start, goal)
            break
        elif ans=="5":
            g.ASTAR(heuristicValue,start,goal)
            break
        elif ans=="6":
            print("\n Goodbye")
            ans = None
        else:
            print("\n Not Valid Choice Try again")


MainCode()
while True:
    a = input("Enter yes/no to continue\n")
    if a=="yes":
        MainCode()
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no")
