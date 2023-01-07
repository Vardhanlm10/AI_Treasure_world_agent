class BFSElement:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
R, C = 5,5

def findPath(M,curr):
    q = []
    q.append([BFSElement(curr[0],curr[1]),[]])
    
    
    while (len(q) != 0):

        x = q[0][0]
        path = q[0][1]
        pathr = []
        pathl = []
        pathu = []
        pathd = []
    
        for i in range(len(path)+1):
            if i==len(path):
                pathr.append("Right")
                pathl.append("Left")
                pathu.append("Up")
                pathd.append("Down")
            else:
                pathr.append(path[i])
                pathl.append(path[i])
                pathu.append(path[i])
                pathd.append(path[i])
        q = q[1:]
 
        i = x.i
        j = x.j

        if (i < 0 or i >= R or j < 0 or j >= C):
            continue
 
        # if they are unvisited (value is 0).
        if (M[i][j] == 0):
            continue

        if (M[i][j] == 2):
            return path
        
        q.append([BFSElement(i,j+1),pathr])
        q.append([BFSElement(i,j-1),pathl])
        q.append([BFSElement(i-1,j),pathu])
        q.append([BFSElement(i+1,j),pathd])

    return None

M = [[0, 2, 0, 0,0],
     [0, 1, 0,0,0],
     [1, 1, 0,0,0],
     [2, 0, 0, 0,0],
     [1, 2, 0, 0,0]]

print(2 in M)
