
 
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

class Point:
    row = 0
    col = 0


                #maze, stack,   row,  col
def maze_pather(maze, maze_path, row, col, depth, came_from):
    print("depth " + str(depth))

    spot = maze_path.peek()
    print (spot)
    next_spot = spot
    prev_spot = spot
    draw_path(spot, maze)
    advance = False

##    i = 0
##    while i < 5:
    

#left                     
    if (maze[spot[0]][spot[1]-1] == " " and came_from != "left"):
        next_spot[1] = spot[1] -1
        maze_path.push(next_spot)
        
        input('go left?')
        print("went left")
        draw_path(spot, maze)
        
        came_from = "right"
        advance = True
        depth = depth + 1
        #maze_pather(maze, maze_path, row, col, depth, came_from)
        
        if advance == True:
            input('next?')
            maze_pather(maze, maze_path, row, col, depth, came_from)
            input('returned')

        input('go back?')
        print("backup")
        print(maze_path.peek())
        prev_spot[1] = spot[1] +1
        draw_erase(prev_spot, maze)
        maze_path.pop()
        return 
#down        
    elif (maze[spot[0] + 1][spot[1]] == " " and came_from != "down"):
        next_spot[0] = spot[0] + 1
        maze_path.push(next_spot)
        
        person = input('go down?')
        print("went down")
        draw_path(spot, maze)

        came_frome = "up"
        advance = True
        depth = depth + 1
        #maze_pather(maze, maze_path, row, col, depth, came_from)
        
        if advance == True:
            input('next?')
            maze_pather(maze, maze_path, row, col, depth, came_from)
            input('returned')

        input('go back?')
        print("backup")
        print(maze_path.peek())
       # prev_spot[0] = spot[0] - 1
        prev_spot[0] = maze_path.peek()
        draw_erase(prev_spot , maze)
        maze_path.pop()
        return 

#right
    elif (maze[spot[0]][spot[1]+1] == " " and came_from != "right"):
        next_spot[1] = spot[1] + 1
        maze_path.push(next_spot)
        
        input('go right?')
        print ("went right")
        draw_path(spot, maze)
        
        came_from = "left"
        advance = True
        depth = depth + 1
        #maze_pather(maze, maze_path, row, col, depth, came_from)
        
        if advance == True:
            input('next?')
            maze_pather(maze, maze_path, row, col, depth, came_from)
            input('returned')

        input('go back?')
        print("backup")
        print(maze_path.peek())
        prev_spot[1] = spot[1] - 1
        draw_erase(prev_spot, maze)
        maze_path.pop()
        return 

#up
    elif (maze[spot[0] - 1][spot[1]] == " " and came_from != "up"):
        next_spot[0] = spot[0] - 1
        maze_path.push(next_spot)
        
        input('go up?')
        print("went up")
        draw_path(spot, maze)
        
        came_from = "down"
        advance = True
        depth = depth + 1
        
        if advance == True:
            input('next?')
            maze_pather(maze, maze_path, row, col, depth, came_from)
            input('returned')

        input('go back?')
        print("backup")
        print(maze_path.peek())
        prev_spot[0] = spot[0] + 1
        draw_erase(prev_spot, maze)
        maze_path.pop()
        return 

#finish
    elif maze[spot[0]][spot[1]-1] == "!" or maze[spot[0]+1][spot[1]] == "!" or maze[spot[0]][spot[1]+1] == "!" :
        return True
            
##        else:
##            input('go back?')
##            print("backup")
##            print(maze_path.peek())
##            maze_path.pop()
##            draw_erase(spot, maze)
##            return 5

    
##    if advance == True:
##        input('next?')
##        maze_pather(maze, maze_path, row, col, depth, came_from)
##        input('returned')
##
##    input('go back?')
##    print("backup")
##    print(maze_path.peek())
##    maze_path.pop()
##    draw_erase(spot, maze)
##    return 5


    #depth = depth + 1
    #maze_pather(maze, maze_path, row, col, depth)
        
    
    #spot[row, (col - 1)]
def draw_erase(point, maze):
    #

    #list = maze
    mazed = list(maze)
    print(maze[point[0]][point[1]])
    maze[point[0]][point[1]] = ' '

    i = 0
    for e in maze:
        print(maze[i])
        i= i+1
    
def draw_path(point, maze):
    #

    #list = maze
    mazed = list(maze)
    maze[point[0]][point[1]] = 'x'

    i = 0
    for e in maze:
        print(maze[i])
        i= i+1
    '''print(maze[0])
    print(maze[1])
    print(maze[2])
    print(maze[3])'''

def main():
    # maze = open("mazes/maze.txt", "r")
    # print (maze.read())
    
    # we want an array for the whole maze with each element being another array
    # those smaller arrays hold four booleans for each cardinal direction
    # that are true if the path is a viable or potential option

    maze_section = [False, False, False, False]
    maze_path = Stack()
    horz_pos = 1
    horz, vert = 6, 3
    maze_matrix = [[0 for x in range(horz)] for y in range(vert)]
    
    coordinate = [0, 1] # [row, col] 
    
    # pos 1 entry point
    # starting at pos 1, we look at the neighbors then below it and repeat

    with open("mazes/maze.txt") as f:
        maze0 = f.readlines()

    i = 0
    maze = [None] * 8
    for  e in maze0:
        print(i)
        maze[i] = list(maze0[i])
        i = i + 1
                       

    #maze = tuple(open("mazes/maze.txt", 'r'))
    #maze = open("mazes/maze.txt").read().splitlines()
    print (maze)
    i = 0
    ii = 0
    
    maze_path.push(coordinate)

    print ("here we are")
    maze[2][2]
    maze_pather(maze, maze_path, 0, 1, 0, "start")

    
    for e in maze:
        temp = maze[0]

        for e in maze[ii]:
            #sdf
            
            his = 5



       
        print( [pos for pos, char in enumerate(temp) if char == " "])
        #if  temp[e] == " ":
        #    print (temp[e])
            #maze_path.push(maze_section)

        i = i + 1
        
    

    
    maze_path.push(maze_section)
    # print (maze_path.peak())


if __name__ == "__main__":
    main()
