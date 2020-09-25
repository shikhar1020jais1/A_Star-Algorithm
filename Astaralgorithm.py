ROW=30
COL=30

class cell:
    def __init__(self,parent_i,parent_j,g,h,f):
        self.parent_i=parent_i
        self.parent_j=parent_j
        self.g = g # Distance to start node
        self.h = h # Distance to goal node
        self.f = f # Total cost


def isvalid(row,col):
    return (row >= 0) and (row < ROW) and (col >=0) and (col < COL)

def isUnblocked(grid,row,col):
    if grid[row][col] ==0:
        return True
    return False


def isdestination(row,col,dest):
    if row == dest[0] and col == dest[1]:
        return True
    return False

import math
def calculatevalue(row,col,dest):
    return math.sqrt(((row-dest[0])**2)+((col-dest[1])**2))

def tracePath(celldetails,dest):
    print("The Path is ")
    row = dest[0]
    col = dest[1]

    path=[]
    
    while not ((celldetails[row][col].parent_i == row) and (celldetails[row][col].parent_j == col)):
        path=[[row,col]]+path
        temp_r = celldetails[row][col].parent_i
        temp_c = celldetails[row][col].parent_j
        row = temp_r
        col = temp_c
    
    path=[[row,col]]+path

    print(path)
    print(len(path))
    return


def astarSearch(grid,src,dest):

    flt_max=1.18973149536e+4932
    if isvalid(src[0],src[1]) == False:
        print("Source is Invalid")
        return 

    if isvalid(dest[0],dest[1]) == False:
        print("Destination is Invalid")
        return 

    if isUnblocked(grid ,src[0],src[1]) == False or isUnblocked(grid,dest[0],dest[1]) == False:
        print("Source or the destination is blocked")
        return

    if isdestination(src[0],src[1],dest) == True:
        print("We are already at the destination")
        return 

    closedlist=[[False]*COL]*ROW
    celldetails=[]

    for i in range(ROW):
        templist=[]
        for j in range(COL):
            num=cell(-1,-1,flt_max,flt_max,flt_max)
            templist.append(num)
        celldetails.append(templist)

    i=src[0]
    j=src[1]
    celldetails[i][j]=cell(i,j,0.0,0.0,0.0)


    openlist= set()
    openlist.add((0.0,i,j))

    foundDest = False

    while (openlist):
        temp=list(openlist)
        temp.sort(key=lambda x:x[0])
        p=temp.pop(0)
        openlist=set(temp)
        i = p[1]
        j = p[2]
        templist=list(closedlist[i])
        templist[j]= True
        closedlist[i] =  templist
        
        gnew = hnew = fnew = 0.0

        #north
        if isvalid(i-1,j) == True:
            if isdestination(i-1,j,dest) == True:
                celldetails[i-1][j].parent_i = i
                celldetails[i-1][j].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i-1][j] == False and isUnblocked(grid,i-1,j) == True:
                
                gnew = celldetails[i][j].g + 1.0
                hnew = calculatevalue(i-1,j,dest)
                fnew = gnew + hnew

                if celldetails[i-1][j].f == flt_max or celldetails[i-1][j].f > fnew:
                    openlist.add((fnew,i-1,j))
                    celldetails[i-1][j] = cell(i,j,gnew,hnew,fnew)

        #South
        if isvalid(i+1,j) == True:
            if isdestination(i+1,j,dest) == True:
                celldetails[i+1][j].parent_i = i
                celldetails[i+1][j].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i+1][j] == False and isUnblocked(grid,i+1,j) == True:
                
                gnew = celldetails[i][j].g +1.0
                hnew = calculatevalue(i+1,j,dest)
                fnew = gnew + hnew

                if celldetails[i+1][j].f == flt_max or celldetails[i+1][j].f >fnew:
                    openlist.add((fnew,i+1,j))
                    celldetails[i+1][j] = cell(i,j,gnew,hnew,fnew)

        #East
        if isvalid(i,j+1) == True:
            if isdestination(i,j+1,dest) == True:
                celldetails[i][j+1].parent_i = i
                celldetails[i][j+1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i][j+1] == False and isUnblocked(grid,i,j+1) == True:
                
                gnew = celldetails[i][j].g +1.0
                hnew = calculatevalue(i,j+1,dest)
                fnew = gnew + hnew

                if celldetails[i][j+1].f == flt_max or celldetails[i][j+1].f >fnew:
                    openlist.add((fnew,i,j+1))
                    celldetails[i][j+1] = cell(i,j,gnew,hnew,fnew)


        #west
        if isvalid(i,j-1) == True:
            if isdestination(i,j-1,dest) == True:
                celldetails[i][j-1].parent_i = i
                celldetails[i][j-1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i][j-1] == False and isUnblocked(grid,i,j-1) == True:
                
                gnew = celldetails[i][j].g +1.0
                hnew = calculatevalue(i,j-1,dest)
                fnew = gnew + hnew

                if celldetails[i][j-1].f == flt_max or celldetails[i][j-1].f >fnew:
                    openlist.add((fnew,i,j-1))
                    celldetails[i][j-1] = cell(i,j,gnew,hnew,fnew)

        #North - East
        if isvalid(i-1,j+1) == True:
            if isdestination(i-1,j+1,dest) == True:
                celldetails[i-1][j+1].parent_i = i
                celldetails[i-1][j+1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i-1][j+1] == False and isUnblocked(grid,i-1,j+1) == True:
                
                gnew = celldetails[i][j].g +1.414
                hnew = calculatevalue(i-1,j+1,dest)
                fnew = gnew + hnew

                if celldetails[i-1][j+1].f == flt_max or celldetails[i-1][j+1].f >fnew:
                    openlist.add((fnew,i-1,j+1))
                    celldetails[i-1][j+1] = cell(i,j,gnew,hnew,fnew)


        #North - West
        if isvalid(i-1,j-1) == True:
            if isdestination(i-1,j-1,dest) == True:
                celldetails[i-1][j-1].parent_i = i
                celldetails[i-1][j-1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i-1][j-1] == False and isUnblocked(grid,i-1,j-1) == True:
                
                gnew = celldetails[i][j].g +1.414
                hnew = calculatevalue(i-1,j-1,dest)
                fnew = gnew + hnew

                if celldetails[i-1][j-1].f == flt_max or celldetails[i-1][j-1].f >fnew:
                    openlist.add((fnew,i-1,j-1))
                    celldetails[i-1][j-1] = cell(i,j,gnew,hnew,fnew)


        #South - East
        if isvalid(i+1,j+1) == True:
            if isdestination(i+1,j+1,dest) == True:
                celldetails[i+1][j+1].parent_i = i
                celldetails[i+1][j+1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i+1][j+1] == False and isUnblocked(grid,i+1,j+1) == True:
                
                gnew = celldetails[i][j].g +1.414
                hnew = calculatevalue(i+1,j+1,dest)
                fnew = gnew + hnew

                if celldetails[i+1][j+1].f == flt_max or celldetails[i+1][j+1].f >fnew:
                    openlist.add((fnew,i+1,j+1))
                    celldetails[i+1][j+1] = cell(i,j,gnew,hnew,fnew)


        #South - West
        if isvalid(i+1,j-1) == True:
            if isdestination(i+1,j-1,dest) == True:
                celldetails[i+1][j-1].parent_i = i
                celldetails[i+1][j-1].parent_j = j
                print("The destination is found")
                tracePath (celldetails,dest)
                foundDest = True
                return

            elif closedlist[i+1][j-1] == False and isUnblocked(grid,i+1,j-1) == True:
                
                gnew = celldetails[i][j].g +1.414
                hnew = calculatevalue(i+1,j-1,dest)
                fnew = gnew + hnew

                if celldetails[i+1][j-1].f == flt_max or celldetails[i+1][j-1].f >fnew:
                    openlist.add((fnew,i+1,j-1))
                    celldetails[i+1][j-1] = cell(i,j,gnew,hnew,fnew)

    if foundDest == False:
        print("Failed to find the Destination call\n")
    
    return 


def main():
    grid=  [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    src=[2,1]

    dest=[29,29]

    astarSearch(grid,src,dest)

    return


if __name__ == "__main__":
    main() 