#print(len(M))
#print(M.pop())
#print(boat[0])
#---DEFINE THE INITIAL VALUES
RM=[]
RC=[]
boat=[]
M=["M", "M", "M"]
C=["C", "C", "C"]

def successor(M, C):
    i=0    

    #SHOW INITIAL STACK
    show()
    #-----------------------------------------------
    while(len(RC)+len(RM) < 6):

        print(i, "------")
        #2 Cannibal will go right if they are atleast 2 or there is no
        #Missionary in left
        if((len(C)<=len(M) or len(M)==0) and len
        (C)>=2 and (len(M)==3 or len(M)==0)):
            boat.append(C.pop())
            boat.append(C.pop())
        
        #2 Missionary will go right if Right side doesn't have any
        #or to maintain equalityin right side
        elif(len(M)>len(C) and len(M)>=2) or (len
        (M)==len(C) and len(RM)==len(RC)):
            boat.append(M.pop())
            boat.append(M.pop())

        show()

        #when the boat reachesat Right side, passengers will go to
        #their respected place
        if(boat[1]=='C'):
            RC.append(boat.pop())
        elif(boat[1]=='M'):
            RM.append(boat.pop())
        if(boat[0]=='M'):
            RM.append(boat.pop())
        elif(boat[0]=='C'):
            RC.append(boat.pop())

        show()
        
        #right to left arriving people will now enter into the boat
        if(len(M)==len(C) and len(M)==0):
            print("The solution found.")
            break

        #IF both side has equal number of lives numbered more than 0
        #1 missionary and one cannibal will go Left
        elif(len(M)==len(C) and len(M)>0):
            boat.append(RM.pop());
            boat.append(RC.pop());

        else:
            boat.append(RC.pop());
        show()
        
        #when the boat returns to Left, passengers will move their
        #respected land
        if(len(boat)>1):
            if(boat[1]=='C'):
                C.append(boat.pop())
            elif(boat[1]=='M'):
                M.append(boat.pop())
        if(boat[0]=="M"):
            M.append(boat.pop())
        elif(boat[0]=="C"):
            C.append(boat.pop())
            

        show() 
        i += 1
        
def show():
    print("Left: ",M ,C ,"--Boat: ",boat, "--Right: ", RM, RC)
    
if __name__ == "__main__":
    successor(M, C);


    
