from tkinter import *
import math
def angle_of_vision(point, watcher):
    vec = (point[0]-watcher[0], point[1]-watcher[1], point[2]-watcher[2])
    k = watcher[1]/vec[1] * -1
    ret = [0,0,0]
    for i in range(3):
        ret[i] = watcher[i]+vec[i] * k;
    return ret

graph = [(-50,-50,-15), (50,-50,-15), (-50,50,-15), (50,50,-15), (-50,-50,15), (50,-50,15), (-50,50,15), (50,50,15),
         (-100,0,0),(100,0,0),(0,-100,0),(0,100,0),(0,0,-100),(0,0,100)]
line = [[1,2],
        [0,3],
        [0,3],
        [1,2],
        [6,5],
        [4,7],
        [4,7],
        [6,5],
        [9],
        [8],
        [11],
        [10],
        [13],
        [12],]
path_point = [(-10 ,-10 ,-15),(-10 ,-20 ,-15),(-20 ,-30 ,-15),(-20 ,-10 ,-15),(-20 ,-40,15)]
path_line = [[1],
             [0,2],
             [1,4],
             [],
             [2]]
look = (0,-1000,0)
move = 1
theta = 0
alpha = 0
press = [0,0,0,0,0,0]
show = []
path_show = []
def update():
    global alpha, theta, press, show, graph, move
    print(theta*180/math.pi, ' ', alpha*180/math.pi)
    print(move)
    for i in range(len(graph)):
        x,y,z = graph[i]
        x = math.cos(theta)*graph[i][0]-math.sin(theta)*graph[i][1]
        y = math.sin(theta)*graph[i][0]*move+math.cos(theta)*graph[i][1]
        graph[i] = x,y,z
        y = math.cos(alpha)*graph[i][1]-math.sin(alpha)*graph[i][2]
        z = math.sin(alpha)*graph[i][1]+math.cos(alpha)*graph[i][2]
        graph[i] = x,y,z
        x*=move
        y*=move
        z*=move
        show[i] = angle_of_vision((x,y,z), look)
    for i in range(len(path_point)):
        x,y,z = path_point[i]
        x = math.cos(theta)*path_point[i][0]-math.sin(theta)*path_point[i][1]
        y = math.sin(theta)*path_point[i][0]+math.cos(theta)*path_point[i][1]
        path_point[i] = x,y,z
        y = math.cos(alpha)*path_point[i][1]-math.sin(alpha)*path_point[i][2]
        z = math.sin(alpha)*path_point[i][1]+math.cos(alpha)*path_point[i][2]
        path_point[i] = x,y,z
        x*=move
        y*=move
        z*=move
        path_show[i] = angle_of_vision((x,y,z), look)
    pt = graph[-6:]
    '''
    for i in range(len(pt)):
        x,y,z = pt[i]
        x = math.cos(theta)*pt[i][0]-math.sin(theta)*pt[i][1]
        y = math.sin(theta)*pt[i][0]+math.cos(theta)*pt[i][1]
        pt[i] = x,y,z
        y = math.cos(alpha)*pt[i][1]-math.sin(alpha)*pt[i][2]
        z = math.sin(alpha)*pt[i][1]+math.cos(alpha)*pt[i][2]
        pt[i] = x,y,z
        x*=move
        y*=move
        z*=move
        pt[i] = (x,y,z)
    '''
    #print(pt)
    canvas.delete("map")
    canvas.delete("path")
    for i in show:
        canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFFFF", tags = "map")
    st = False
    for i in path_show:
        canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFF00" if st else "#00FF00", tags = "path")
        st = True
    for i in range(len(line)):
        for j in line[i]:
            canvas.create_line(origin[0]+show[i][0], origin[1]+show[i][2], origin[0]+show[j][0], origin[1]+show[j][2], fill = "#FFFFFF", tags = "map")
    for i in range(len(path_line)):
        for j in path_line[i]:
            canvas.create_line(origin[0]+path_show[i][0], origin[1]+path_show[i][2], origin[0]+path_show[j][0], origin[1]+path_show[j][2], fill = "#FF0000", tags = "path")
    theta = 0
    alpha = 0
    #move = 10
def start():
    global alpha, theta, press, move
    if press[0]:
        theta+=math.pi/12
    if press[1]:
        theta-=math.pi/12
    if press[2]:
        alpha+=math.pi/12
    if press[3]:
        alpha-=math.pi/12
    if press[4]:
        move+=0.1
    if press[5]:
        move-=0.1
    move = max(move, 0)
    #move = min()
    if(theta>2*math.pi):
        theta-=2*math.pi
    if(theta<0):
        theta+=2*math.pi
    if(alpha>2*math.pi):
        alpha-=2*math.pi
    if(theta<0):
        alpha+=2*math.pi
    update()
    root.after(50, start)
def control(event):
    global alpha, theta, press
    if event.char == 'a' or event.keysym == 'Left':
        press[0] = 1
    elif event.char == 'd' or event.keysym == 'Right':
        press[1] = 1
    elif event.char == 'w' or event.keysym == 'Up':
        press[2] = 1
    elif event.char == 's' or event.keysym == 'Down':
        press[3] = 1
    elif event.char == '+':
        press[4] = 1
    elif event.char == '-':
        press[5] = 1
    elif event.char == 'r':
        theta = 0
        alpha = 0
def release(event):
    global alpha, theta, press
    if event.char == 'a' or event.keysym == 'Left':
        press[0] = 0
    elif event.char == 'd' or event.keysym == 'Right':
        press[1] = 0
    elif event.char == 'w' or event.keysym == 'Up':
        press[2] = 0
    elif event.char == 's' or event.keysym == 'Down':
        press[3] = 0
    elif event.char == '+':
        press[4] = 0
    elif event.char == '-':
        press[5] = 0
root = Tk()
root.title("3D")
root.geometry("1080x720")
root.resizable(0,0)
root.bind("<Key>", control)
root.bind("<KeyRelease>", release)
origin = (540, 360)

canvas = Canvas(root, bg = "#000000", width = 1080, height = 720)

for i in graph:
    show.append(angle_of_vision(i, look))
for i in path_point:
    path_show.append(angle_of_vision(i, look))
canvas.pack()
for i in show:
    canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFFFF", tags = "map")
for i in range(len(line)):
    for j in line[i]:
        canvas.create_line(origin[0]+show[i][0], origin[1]+show[i][2], origin[0]+show[j][0], origin[1]+show[j][2], fill = "#FFFFFF", tags = "map")

for i in path_show:
    canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFF00", tags = "path")
for i in range(len(path_line)):
    for j in path_line[i]:
        canvas.create_line(origin[0]+path_show[i][0], origin[1]+path_show[i][2], origin[0]+path_show[j][0], origin[1]+path_show[j][2], fill = "#FF0000", tags = "path")
start()
root.mainloop()