import numpy as np
import random
import copy

fringe = []
action_set = ['l','r','u','d']
goal_state = [[1,2,3],[8,0,4],[7,6,5]]

def gen_state():
    b = random.sample(range(9), 9)
    #reshape matrix
    #b= np.reshape(b,(3,3))
    r_b = [b[0:3], b[3:6], b[6:9]]
    #print(r_b)
    return r_b

def gen_successor():
    pass

def push(state):
    fringe.append(state)
    
def pop():
    return fringe.pop()

def head():
    return fringe.pop(0)

def isGoal(state):
    if state == goal_state:
        return True
    return False

def action(parent_state, ac,pos):
    i = pos[0]
    j = pos[1]
    new_state = np.array(parent_state)
    #print('pos:',i,j)
    #print('parent:',parent_state)
    if ac=='u':
        if i !=0:
            new_state[i][j],new_state[i-1][j] = new_state[i-1][j],new_state[i][j]
            return new_state 
            
    elif ac == 'd':
        if i<2:
            new_state[i][j],new_state[i+1][j] = new_state[i+1][j],new_state[i][j]
            return new_state 
    elif ac == 'r':
        if j<2:
            new_state[i][j],new_state[i][j+1] = new_state[i][j+1],new_state[i][j]
            return new_state 
    elif ac == 'l':
        if j>0:
            new_state[i][j],new_state[i][j-1] = new_state[i][j-1],new_state[i][j]
            return new_state 
    #return None
        

def succsessor_states(parent_state):
    pos = [0,0]
    children = []
    for i in range(3):
        for j in range(3):
            if (parent_state[i][j] == 0 ):
                pos[0]=i
                pos[1]=j
                break
    for ac in action_set:
        child = action(parent_state, ac,pos)#function call: action
        #print('ac:',ac, 'child:', child)
        if isinstance(child, np.ndarray):
            children.append(child)

    children = np.array(children).tolist()
    return children
        

def bfs_search(state):
    visited = []
    fringe.append(state)
    i=10
    while i>0: #fringe:
        i -= 1
        st = fringe.pop(0)
        visited.append(st)
        print(st,"-->")
        if isGoal(st) == True:
            print(st)
            return;
        
        children= succsessor_states(st)
        print(children)
        for ch in children:
            if ch not in visited:
                fringe.append(ch)
        
        
            
if __name__ == "__main__":
    print("8-Puzzle Game..")
    s0= gen_state()
    #s2 = gen_state()
    #push(s1)
    #push(s2)
    print('Initial State:\n',s0)
    #children = succsessor_states(s0)
    #print('Children:\n',children)

    #print("pop:", pop())
    bfs_search(s0)



