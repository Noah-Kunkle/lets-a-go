directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
nodes=[]
nodes_old=[]
class Node():
    def __init__(self,pos,org):
        self.pos=pos
        self.org=org
        
def find_next_move(mazeorg, start, end):
    maze=mazeorg
    nodes=[]
    nodes_old=[]
    if not maze or not maze[0]:
        return ["na maze"]
    rows, cols = len(maze), len(maze[0])
    if not (0 <= start[0] < rows) or not (0 <= start[1] < cols) or not (0 <= end[0] < rows) or not (0 <= end[1] < cols):
        return ["bad maze"]
    ex,ey=end
    sx,sy=start
    if ex==sx and ey==sy:
        return(0,0)
    maze[sx][sy]=1
    maze[ex][ey]=2
    for dr, dc in directions:
        if maze[sx+dr][sy+dc]==2:
            return(dr,dc)
        if maze[sx+dr][sy+dc]==0:
            maze[sx+dr][sy+dc]=1
            n=Node((sx+dr,sy+dc),(dr,dc))
            nodes.append(n)
    while True:
        nodes_old=nodes
        for n in nodes_old:
            selfx,selfy=n.pos
            for dr, dc in directions:
                x,y=selfx+dr,selfy+dc
                if maze[x][y]==2:
                    end=1
                    break
                if maze[selfx+dr][selfy+dc]==0:
                    maze[selfx+dr][selfy+dc]=1
                    n=Node((selfx+dr,selfy+dc),(dr,dc))
                    nodes.append(n)
            if end:
                return(n.org)