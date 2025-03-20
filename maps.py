import random

class Map:
    
    def __init__(self, obstacles,line_size, lines):
        self.obstacles = obstacles
        self.line_size = line_size
        self.lines = lines
        self.map = self.generateMap(self.obstacles, self.line_size, self.lines)

    
    def generateMap(self, obstacles, line_size, lines):

        map = []
        for i in range(lines):
            line = []
            for i in range(line_size):
                line.append("O")
            map.append(line)


        obstacle_count = 0

        while obstacle_count < obstacles:
            for line in map:
                
                loc = random.randint(0, line_size*2)
                

                
                while(loc < line_size and line[loc] == "+"):
                    loc=random.randint(0, line_size*2)
                
                if(loc >= line_size):
                    continue
                
                line[loc] = "+"
                obstacle_count += 1

                if obstacle_count >= obstacles:
                    break
        
        return map

    def print_map(self):
        for line in self.map:
            # line_as_string = ""
            # for char in line:
            #     line_as_string += char + " "

            print(line)
            


       
    
    def count_obstacles(self):
        count = 0
        for line in self.map:
            for char in line:
                if char == "+":
                    count += 1

        return count
    
    def update_coord(self,x, y, val):
        self.map[y][x] = val

    def __explore__(self, queue, start_pos):
        
        max_h = len(self.map)
        max_w = len(self.map[0])
        
        x = start_pos[0]
        y = start_pos[1]
        

        
            

        if x + 1 >= 0 and x+1< max_w and y >= 0 and y < max_h and self.map[y][x + 1] == "O":
            queue.append((x + 1, y + 0))
            self.map[y][x + 1] = f"{start_pos[0]},{start_pos[1]}"
        if x >= 0 and x < max_w and y + 1 >= 0 and y + 1 < max_h and self.map[y + 1][x] == "O":
            queue.append((x , y + 1))
            self.map[y + 1][x] = f"{start_pos[0]},{start_pos[1]}"
        if x + 1 >= 0 and x + 1 < max_w and y + 1 >= 0 and y + 1 < max_h and self.map[y + 1][x + 1] == "O":
            queue.append((x + 1 , y + 1))
            self.map[y + 1][x + 1] = f"{start_pos[0]},{start_pos[1]}"
        if x - 1 >= 0 and x - 1 < max_w and y + 1 >= 0 and y + 1 < max_h and self.map[y + 1][x - 1] == "O":
            queue.append((x - 1 , y + 1))
            self.map[y + 1][x - 1] = f"{start_pos[0]},{start_pos[1]}"

        if x - 1 >= 0 and x - 1< max_w and y >= 0 and y < max_h and self.map[y][ x-1] == "O":
            queue.append((x - 1, y + 0))
            self.map[y][x - 1] = f"{start_pos[0]},{start_pos[1]}"
        if x  >= 0 and x < max_w and y - 1 >= 0 and y - 1 < max_h and self.map[y - 1][x] == "O":
            queue.append((x, y - 1))
            self.map[y - 1][x] = f"{start_pos[0]},{start_pos[1]}"
        if x - 1 >= 0 and x - 1 < max_w and y - 1 >= 0 and y - 1 < max_h and self.map[y - 1][x - 1 ] == "O":
            queue.append((x - 1 , y - 1))
            self.map[y - 1][x - 1] = f"{start_pos[0]},{start_pos[1]}"
        if x + 1 >= 0 and x + 1 < max_w and y - 1 >= 0 and y - 1 < max_h and self.map[y - 1][x + 1] == "O":
            queue.append((x + 1 , y - 1))
            self.map[y - 1][x + 1] = f"{start_pos[0]},{start_pos[1]}"




    def find_shortest_path(self, start = (0,0), end = (1,1)):
        self.__reset__()
        queue = [start]
        current_pos = start
        self.map[start[1]] [start[0]] = "#"
        
        
        #find the ending
        while len(queue) != 0 and (current_pos[0] != end[0] or current_pos[1] != end[1]):
            #exploring
            current_pos = queue.pop(0)
           
            self.__explore__(queue, current_pos)
            
        if(current_pos != end):
            shortest_path = self.__backtrack__(current_pos)
            self.__reset__()
            self.__update__path(shortest_path)
            
            
            print("TRAPPED!")
            return True
        

        #Backtracking
       
        shortest_path = self.__backtrack__(end)

        self.__reset__()

        self.__update__path(shortest_path)

        

        return False
    
    def __reset__(self):
        for line in self.map:
            for i in range(0, len(line)):
                if line[i] != "+":
                    line[i] = "O"
    
    def __update__path(self,short_list):
        for (x,y) in short_list:
            self.map[y][x] = "S"
    
    def __backtrack__(self, end_pos):
        a = end_pos
        
        shortest_path = [a]
        while(self.map[a[1]][a[0]] != "#"):
            text = self.map[a[1]][a[0]]
            sp = text.split(",")
            x = int(sp[0])
            y = int(sp[1])
            a = (x, y)
            shortest_path.append(a)
        return shortest_path
        




        

    
        

def run_map_test(obstacles, width, height, reps=10000):

    map = Map(obstacles, width, height)
    i = 0
    while(map.count_obstacles() == obstacles and i < reps):
        map = Map(obstacles,width,height)
        i += 1

    if map.count_obstacles() != obstacles:
        print("there is a problem with your code")
        map.print_map()
    else:
        print("code is successful")
        map.print_map()


def generate_new_random_map(genhw, obstacles):
    if genhw * genhw <= obstacles:
        #return a blank map
        return generate_new_random_map(genhw, 0)
    new_map = Map(obstacles, genhw, genhw)
    return new_map
