import numpy
import cv2
import sys
Floor = 1
fpath = '.\\F'+str(Floor)+'.png'
img = cv2.imread(fpath)
F = []
path = []
point = []
edge = []
fpoint = open('.\\point.txt', 'w')
fedge = open('.\\edge.txt', 'w')
fwifi = open('.\\wifi.txt', 'w')
def Search(y, x, last_point, last_pass):
    test = [[1,1,0,0], [0,0,1,1]]
    global edge, point, path, F
    path[y][x] = 1
    p = 0
    count = [0,0,0,0] #上 下 左 右
    if(x+1<len(F[y])):
        if(F[y][x+1]):
            count[3] = 1
    if(x-1>=0):
        if(F[y][x-1]):
            count[2] = 1
    if(y+1<len(F)):
        if(F[y+1][x]):
            count[1] = 1
    if(y-1>=0):
        if(F[y-1][x]):
            count[0] = 1

    if not(count in test):
        p = 1
    
    if(p):
        print(x, y, F[y][x])
        print(count)
        
        point.append([x,y])
        now_point = len(point)-1
        if(last_point != -1):
            edge.append([now_point, last_point])
        #print([])
        print(p, now_point, last_point)
    if(count[0]):
        if((not path[y-1][x]) or (([x, y-1] in point) and [y-1,x] != last_pass)):
            Search(y-1, x, now_point if p else last_point, [y, x])
    if(count[1]):
        if((not path[y+1][x]) or (([x, y+1] in point) and [y+1,x] != last_pass)):
            Search(y+1, x, now_point if p else last_point, [y, x])
    if(count[2]):
        if((not path[y][x-1]) or (([x-1, y] in point) and [y,x-1] != last_pass)):
            Search(y, x-1, now_point if p else last_point, [y, x])
    if(count[3]):
        if((not path[y][x+1]) or (([x+1, y] in point) and [y,x+1] != last_pass)):
            Search(y, x+1, now_point if p else last_point, [y, x])
def color(point):
    b = [0,0,0]
    w = [255,255,255]
    bc = True
    wc = True
    for i in range(3):
        if(point[i] != b[i]):
            bc = False
            break
    if bc:
        return 1
    
    for i in range(3):
        if(point[i] != w[i]):
            wc = False
            break
    if wc:
        
        return 0
    print(point)
    return 2
sys.setrecursionlimit(121040)
cntpt = 0
cnted = 0
for Floor in range(1,9):
    fpath = '.\\F'+str(Floor)+'.png'
    img = cv2.imread(fpath)
    F.clear()
    path.clear()
    for i in range(len(img)):
        F.append([])
        path.append([])
        for j in range(len(img[i])):
            F[i].append(color(img[i][j]))
            path[i].append(0)
            #print(color(img[i][j]), end = '')
        #print('')
    for i in range(len(F)):
        for j in range(len(F[i])):
            if(F[i][j]==1 and not path[i][j]):
                print('new', i, j)
                Search(i, j, -1, [-1,-1])
                
    l,r,u,d = 10000,0,10000,0
    for i in point:
        l = min(l, i[0])
        r = max(r, i[0])
        u = min(u, i[1])
        d = max(d, i[1])
    midl = (l+r)//2
    midu = (u+d)//2
    #print(point)
    for i in range(len(F)):
        print(F[i])
        for j in range(len(F[i])):
            if(F[i][j] == 2):
                print(i, j)
                fwifi.writelines('['+str(midl-j)+','+str(i-midu)+','+str((Floor*(-30))+135)+'],\n')
    while(cntpt<len(point)):
        fpoint.writelines('['+str(midl-point[cntpt][0])+','+str(point[cntpt][1]-midu)+','+str((Floor*(-30))+135)+'],\n')
        cntpt+=1
    while(cnted<len(edge)):
        fedge.writelines('['+str(edge[cnted][0])+','+str(edge[cnted][1])+'],\n')
        cnted+=1
    #print(edge)
fpoint.close()
fedge.close()
fwifi.close()