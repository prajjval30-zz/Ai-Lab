author:@prajjval

graph={}

class waterjug:
    max_capacity=[0,0]
    initial_state_as = (0,0)
    x_jug=initial_state_as[0]
    y_jug=initial_state_as[1]
    goal=[]
    visited=[(0,0)]
    parent={}
    j=(0,0)
    bfs=[]

    def initializing_initial_state_as(self):
        print("Setting the initial_state_as capacityt.....")
        x_jug_cap=0
        y_jug_cap=0
        
        x_jug_cap = int(input("Enter Jug 1 capacity : "))
        
        while x_jug_cap<0:
            print("Invalid entries ! Enter again")
            x_jug_cap = int(input("Enter Jug 1 capacity again : "))

        y_jug_cap = int(input("Enter Jug 2 capacity : "))
        
        while y_jug_cap<0:
            print("Invalid entries ! Enter again")
            y_jug_cap = int(input("Enter Jug 2 capacity again : "))
        
        self.max_capacity=[x_jug_cap,y_jug_cap]
        print("Volume of each jug inserted")
        self.goal_state()

    def goal_state(self):
        print("Setting the goal state")
        goal_1=int(input("Enter the goal capacity : "))
    
        while goal_1>max(self.max_capacity[0],self.max_capacity[1]):
            print("Invalid goal amount!")
            goal_1 = int(input("Enter the goal amount : "))
    
        for goal_cap in range(max(self.max_capacity[0],self.max_capacity[1])+1):
        
            self.goal.append((goal_1,goal_cap))
            self.goal.append((goal_cap,goal_1))

        
        print("Goal Amount entered")

        self.search_methods()
    

    def search_methods(self):
        choice=3
        while choice>2 or choice<0:
            print("Enter the type of search method to use :")
            print("1.BFS")
            print("2.DFS")
            print("3.Exit")

            choice=int(input(choice))
            if choice>2 or choice<0:
                print("invalid choice! please try again")

            if choice == 1:
                self.bfs(self.initial_state_as)
            if choice == 2:
                self.dfs(self.initial_state_as)
            if choice == 3:
                exit(0)

    def print_result(self):
        print("Graph: ",graph)
        exit(0)
    
    def dfs(self,initial_state_as):
            
        if initial_state_as in self.goal:
            
            print("Depth First Search solution: ")
            self.print_result()
        
        else:
            #fill A
            if not self.visited.__contains__((self.max_capacity[0],initial_state_as[1])):
                graph[initial_state_as]=[[self.max_capacity[0],initial_state_as[1]]]

                graph[self.max_capacity[0],initial_state_as[1]]=[]
                self.visited.append((self.max_capacity[0],initial_state_as[1]))
                j=(self.max_capacity[0],initial_state_as[1])
                #print(j)
                self.dfs(j)

            #fill B    
            if not self.visited.__contains__((initial_state_as[0],self.max_capacity[1])):
                graph[initial_state_as]=[initial_state_as[0],self.max_capacity[1]]

                graph[initial_state_as[0],self.max_capacity[1]]=[]
                self.visited.append((initial_state_as[0],self.max_capacity[1]))
                j=(initial_state_as[0],self.max_capacity[1])
                # print(j)
                self.dfs(j)

            #empty A
            if not self.visited.__contains__((0,initial_state_as[1])):
                graph[initial_state_as]=[0,initial_state_as[1]]
                graph[0,initial_state_as[1]]=[]
                self.visited.append((0,initial_state_as[1]))
                j=(0,initial_state_as[1])
                self.dfs(j)

            #transfer from jug B to jug A    
            leftover_y_capacity=self.max_capacity[0]-initial_state_as[0]

            if leftover_y_capacity >= initial_state_as[1]:
                if not self.visited.__contains__((initial_state_as[0]+initial_state_as[1],0)):
                    graph[initial_state_as]=[initial_state_as[0]+initial_state_as[1],0]
                    graph[initial_state_as[0]+initial_state_as[1],0]= [ ]
                    self.visited.append((initial_state_as[0]+initial_state_as[1],0))
                    j = (initial_state_as[0]+initial_state_as[1],0)
                    self.dfs(j)

            else:
                if not self.visited.__contains__((initial_state_as[0]+leftover_y_capacity,initial_state_as[1]-leftover_y_capacity)):
                    graph[initial_state_as]= [initial_state_as[0]+leftover_y_capacity,initial_state_as[1]-leftover_y_capacity]
                    graph[initial_state_as[0]+leftover_y_capacity,initial_state_as[1]-leftover_y_capacity] = [ ]
                    self.visited.append((initial_state_as[0]+leftover_y_capacity,initial_state_as[1]-leftover_y_capacity))
                    j = (initial_state_as[0]+leftover_y_capacity,initial_state_as[1]-leftover_y_capacity)
                    self.dfs(j)



            #empty jug 2
            if not self.visited.__contains__((initial_state_as[0],0)):
                graph[initial_state_as]=[initial_state_as[0],0]
                graph[initial_state_as[0],0] = [ ]
                self.visited.append((initial_state_as[0],0))
                j = (initial_state_as[0],0)
                self.dfs(j)
            #transfer from jug1 to jug 2

            jug2left = self.max_capacity[1]-initial_state_as[1]
            if jug2left >= initial_state_as[0]:
                #that means that jug1 does not have the water enough to fill the jug1 fully hence we will pour
                # the entire water of jug 1 to jug 2 therefore jug 1 = 0 and jug 2 = jug2(initial)+ whatever thier was in jug1 (initial(0))
                if not self.visited.__contains__((0,initial_state_as[1]+initial_state_as[0])):
                    graph[initial_state_as] = [0,initial_state_as[1]+initial_state_as[0]]
                    graph[0,initial_state_as[1]+initial_state_as[0]] = [ ]
                    self.visited.append((0,initial_state_as[1]+initial_state_as[0]))
                    j = (0,initial_state_as[1]+initial_state_as[0])
                    self.dfs(j)

            else:
                #that means that jug1 has more water than it is required to fill jug 2
                #hence jug 1 = initial[0] - water needed by jug2 [jug2left],
                #jug2 = initial[1]+water required to fill [jug2left]
                if not self.visited.__contains__((initial_state_as[0]-jug2left,initial_state_as[1]+jug2left)):
                    graph[initial_state_as]=[initial_state_as[0]-jug2left,initial_state_as[1]+jug2left]
                    graph[initial_state_as[0]-jug2left,initial_state_as[1]+jug2left] = [ ]
                    self.visited.append((initial_state_as[0]-jug2left,initial_state_as[1]+jug2left))
                    j = (initial_state_as[0]-jug2left,initial_state_as[1]+jug2left)
                    self.dfs(j)                             
    def bfs(self,initial_state_as):
        if not self.visited.__contains__((self.max_capacity[0],initial_state_as[1])):
            graph[initial_state_as]=[self.max_capacity[0],initial_state_as[1]]
            graph[self.max_capacity[0],initial_state_as[1]]=[]
            self.visited.append((self.max_capacity[0],initial_state_as[1]))
            self.j = (self.max_capacity[0], initial_state_as[1])
            self.parent[self.j] = initial_state_as
            self.check_bfs_goal(self.j)
            
        if not self.visited.__contains__((initial_state_as[0], self.max_capacity[1])):
            graph[initial_state_as].append([initial_state_as[0], self.max_capacity[1]])
            graph[initial_state_as[0], self.max_capacity[1]] = []
            self.visited.append((initial_state_as[0], self.max_capacity[1]))
            self.parent[initial_state_as[0], self.max_capacity[1]] = initial_state_as
            self.j = (initial_state_as[0], self.max_capacity[1])
            self.parent[self.j] = initial_state_as
            self.check_bfs_goal(self.j)

        # transfer jug 1 to jug 2
        jug2left = self.max_capacity[1] - initial_state_as[1]
        if initial_state_as[0] <= jug2left:
            if not self.visited.__contains__((0, initial_state_as[1] + initial_state_as[0])):
                graph[initial_state_as].append([0, initial_state_as[1] + initial_state_as[0]])
                self.visited.append((0, initial_state_as[1] + initial_state_as[0]))
                graph[0, initial_state_as[1] + initial_state_as[0]] = []
                flag = 1
                self.j = (0, initial_state_as[1] + initial_state_as[0])
                self.parent[self.j] = initial_state_as
                self.check_bfs_goal(self.j)
            else:
                if not self.visited.__contains__((initial_state_as[0] - jug2left, initial_state_as[1] + jug2left)):
                    graph[initial_state_as].append([initial_state_as[0] - jug2left, initial_state_as[1] + jug2left])
                    graph[initial_state_as[0] - jug2left, initial_state_as[1] + jug2left] = []
                    self.visited.append((initial_state_as[0] - jug2left, initial_state_as[1] + jug2left))
                    self.j = (initial_state_as[0] - jug2left, initial_state_as[1] + jug2left)
                    self.parent[self.j] = initial_state_as
                    self.check_bfs_goal(self.j)


        # empty jug 1
        if not self.visited.__contains__((0, initial_state_as[1])):
            graph[initial_state_as].append([0, initial_state_as[1]])
            graph[0, initial_state_as[1]] = []
            self.visited.append((0, initial_state_as[1]))
            self.j = (0, initial_state_as[1])
            self.parent[self.j] = initial_state_as
            self.check_bfs_goal(self.j)
        # empty jug 2
        if not self.visited.__contains__((initial_state_as[0], 0)):
            graph[initial_state_as].append([initial_state_as[0], 0])
            graph[initial_state_as[0], 0] = []
            self.visited.append((initial_state_as[0], 0))
            self.j = (initial_state_as[0], 0)
            self.parent[self.j] = initial_state_as
            self.check_bfs_goal(self.j)
        # transfer jug 2 to jug 1
        jug1left = self.max_capacity[0] - initial_state_as[0]
        if jug1left >= initial_state_as[1]:
            if not self.visited.__contains__((initial_state_as[1] + initial_state_as[0], 0)):
                graph[initial_state_as].append([initial_state_as[1] + initial_state_as[0], 0])
                graph[initial_state_as[1] + initial_state_as[0], 0] = []
                self.visited.append((initial_state_as[1] + initial_state_as[0], 0))
                self.j = (initial_state_as[1] + initial_state_as[0], 0)
                self.parent[self.j] = initial_state_as
                self.check_bfs_goal(self.j)
            else:
                if not self.visited.__contains__((initial_state_as[0] + jug1left, initial_state_as[1] - jug1left)):
                    graph[initial_state_as].append([initial_state_as[0] + jug1left, initial_state_as[1] - jug1left])
                    graph[initial_state_as[0] + jug1left, initial_state_as[1] - jug1left] = []
                    self.visited.append((initial_state_as[0] + jug1left, initial_state_as[1] - jug1left))
                    self.j = (initial_state_as[0] + jug1left, initial_state_as[1] - jug1left)
                    self.parent[self.j] = initial_state_as
                    self.check_bfs_goal(self.j)

            i=self.visited.index(initial_state_as)
            k=self.visited[i+1]
            self.bfs(k)
                                
    def check_bfs_goal(self,initial_state_as):
        if initial_state_as in self.goal:
            print("Breadth First Search solution: ")
            print("steps: ")
            flag = 0
            self.parents(self.j)



    def parents(self,j):
        while j!=self.initial_state_as:
            self.bfslist.append(j)
            self.parents(self.parent[j])
        self.bfslist.append(self.initial_state_as)
        for n in range(len(self.bfslist)-1,0,-1):
            print(self.bfslist[n])
        print(self.bfslist[0])
        print("Graph :", graph)
        exit(0)

j=waterjug()
graph={}
max_capacity=j.initializing_initial_state_as()
