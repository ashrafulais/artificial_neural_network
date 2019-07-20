#back propagation program
import math as mt

'''
#input from user
for i in range(0,2):
    input_x.append(float(input()))
    
for i in range(0,3):
    for j in range(0, 2):
        x = float(input())
        weights[i].append(x)

for i in range(0,3):
    bias.append(float(input()))
'''

input_x=[0.2, 0.3]
weights=[[0.1,0.2],[0.3,0.4],[0.5,0.6]]
bias=[0.1,0.2,0.3]
learning_rate=0.1
desired_output=0.1

#main function starts here
h_in=[0,0]
h_out=[0,0]
o_in=[0]
o_out=[0]
error=0

while True:
    #1. calculate hidden layer net input, output
    for i in range(0,2):
        h_in[i]=(input_x[0]*weights[0][i])+(input_x[1]*weights[i][1])+bias[i]
        h_out[i]=round(1/(1+mt.exp(-1*h_in[i])), 1)

        #print("NET INPUT: ",h_in[i], " ", h_out[i])
    #2. calculate net input to each output layer

    o_in[0]=h_out[0]*weights[2][0] + h_out[0]*weights[2][1] + bias[2]
    o_out[0]=round(1/(1+mt.exp(-1*o_in[0])), 1)
    
    #print("NET OUTPUT: ",o_in[0], " ", o_out[0])
    temp = round(o_out[0], 1)
    
    if(desired_output != temp):
        #error calc, update weights & bias
        error=(desired_output-o_out[0])*o_out[0]*(1-o_out[0])
        print(o_out[0])

        for i in range(0,3):
            if(i<2):
                weights[i][0] = weights[i][0]+(learning_rate*error*input_x[0])
                weights[i][1] = weights[i][1]+(learning_rate*error*input_x[1])
            if(i>1):
                weights[i][0] = weights[i][0]+(learning_rate*error*h_out[0])
                weights[i][1] = weights[i][1]+(learning_rate*error*h_out[1])
            bias[i] = bias[i]+(learning_rate*error)

        #print("WEIGHTS: ", weights)
        
    #STOPPING CRITERIA    
    if(desired_output == temp):
        print("No error remaining.")
        print("Error=", error, " Output:", o_out)
        break
