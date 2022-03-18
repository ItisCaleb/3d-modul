from tkinter import *
import math
def angle_of_vision(point, watcher):
    vec = (point[0]-watcher[0], point[1]-watcher[1], point[2]-watcher[2])
    k = watcher[1]/vec[1] * -1
    ret = [0,0,0]
    for i in range(3):
        ret[i] = watcher[i]+vec[i] * k;
    return ret

graph = [(-50,-50,-15), (50,-50,-15), (-50,50,-15), (50,50,-15), (-50,-50,15), (50,-50,15), (-50,50,15), (50,50,15)]
line = [[1,2],
        [0,3],
        [0,3],
        [1,2],
        [6,5],
        [4,7],
        [4,7],
        [6,5]]
look = (0,-1000,0)
move = 1
theta = 0
alpha = 0
press = [0,0,0,0,0,0]
show = []
def update():
    global alpha, theta, press, show, graph, move
    print(theta, ' ', alpha)
    for i in range(len(graph)):
        x,y,z = graph[i]
        x = math.cos(theta)*graph[i][0]*move-math.sin(theta)*graph[i][1]*move
        y = math.sin(theta)*graph[i][0]*move+math.cos(theta)*graph[i][1]*move
        y = math.cos(alpha)*graph[i][1]*move-math.sin(alpha)*graph[i][2]*move
        z = math.sin(alpha)*graph[i][1]*move+math.cos(alpha)*graph[i][2]*move
        show[i] = angle_of_vision((x,y,z), look)
    canvas.delete("map")
    for i in show:
        canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFFFF", tags = "map")
    for i in range(len(line)):
        for j in line[i]:
            canvas.create_line(origin[0]+show[i][0], origin[1]+show[i][2], origin[0]+show[j][0], origin[1]+show[j][2], fill = "#FFFFFF", tags = "map")

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
        move-=0.2
    move = max(move, 0)
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
canvas.pack()
for i in show:
    canvas.create_oval(origin[0]+i[0]+2, origin[1]+i[2]+2, origin[0]+i[0]-2, origin[1]+i[2]-2, fill = "#FFFFFF", tags = "map")
for i in range(len(line)):
    for j in line[i]:
        canvas.create_line(origin[0]+show[i][0], origin[1]+show[i][2], origin[0]+show[j][0], origin[1]+show[j][2], fill = "#FFFFFF", tags = "map")
start()
root.mainloop()