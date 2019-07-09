

def display(bpass1, bpass2):
    print("\n")
    
    for i in range(0,fm):
        print(" M ", end="")
    for i in range(0,fc):
        print(" C ", end="")

    if flg==0:
        print("----water-----B0(",bpass1, "," ,bpass2, ")", end="")
    else:
        print("    B0(",bpass1, "," ,bpass2, ")----water-----", end="")
        
    for i in range(0,im):
        print(" M ", end="")
    for i in range(0,ic):
        print(" C ", end="")

def win():
    return 0 if fc==3 and fm==3 else 1

'''
1-Boat's location
2-Passengers grouping
3-Make trip
4-Won
5-Repeat
'''

def solution(im, ic, fm, fc, status, flg, select):
    #print(win())
    while(win()):
        if flg == 0:
            if select >= 0:
                if select==1:
                    display('C', ' ')
                    ic+=1
                    break
                if select==2:
                    display('C', 'M')
                    ic+=1
                    im+=1
                    break
                
            if ((im-2) >= ic and (fm+2) >=fc) or (im-2) == 0:
                im -= 2
                select = 1
                display('M', 'M')
                flg=1
            elif (ic - 2) < im and fm == 0 or (fc + 2) <= fm or im == 0:
                ic -= 2
                select = 2
                display('C', 'C')
                flag = 1
            elif (ic-1) <= (im-1) and (fm+1) >= (fc+1):
                ic -=1
                im -=1
                select = 3
                display('M', 'C')
                flag=1
        else:
            if select>=0:
                if select==1:
                    display('M', 'M')
                    fm+=2
                    break
                if select==2:
                    display('C', 'C')
                    fc+=2
                    break
                if select==3:
                    display('M', 'C')
                    fc+=1
                    fm+=1
                    break
            if win()==1:
                if fc>1 and fm==0 or im==0:
                    fc-=1
                    select = 2
                    display('C', ' ')
                    flag=0
                elif ic+2 > im:
                    fc-=1
                    fm-=1
                    select = 2
                    display('C', 'M')
                    flag=0
            


if __name__ == "__main__":

    im=3
    ic=3
    i=0
    fm=0
    fc=0

    status=0
    flg=0
    select=0

    print("Missionary and cannibal solution")
    display(' ', ' ')
    solution(im, ic, fm, fc, status, flg, select)
    display(' ', ' ')

    x=input()












