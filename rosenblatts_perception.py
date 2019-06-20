'''
Algorithm:
1. Pick the starting weight and assume the learning rate alpha=0.1
2. Compute the desired output by
d = ALL_SUM of WEIGHTi x INPUTi
3. If the actual output Y=sign(net_value) is not equal to desired output, update the weights using this equation
W^n = W^n-1 + alpha(desired output - Y) x X^(n-1)
4. Repear the step 2 & 3 until weights cease to change significantly
'''
#--------------- TRANSPOSE MATRIX FUNCTION, THATS USELESS
def transpose_matrix(matrix_list):
    #you don't need to make the matrix horizontal 
    # :P it's not your notebook
    vals = matrix_list
    for d in vals:
        print(d)

#--------------- SIGN ACTIVATION FUNCTION, AS DESIRED RESPONSE IS +1 & -1
def sign_activation(value):
    if value>=0:
        return 1
    else:
        return -1

#--------------- MULTIPLY 2 MATRIX FOR NET VALUE FINDING
def matrix_multiply(weight, input_val):
    length=len(weight)
    net_val=0

    for i in range(0,length):
        #print(weight[i]," ", input_val[i])
        net_val = net_val+ (weight[i]*input_val[i])
    
    #print(net_val)
    return net_val

#--------------- UPDATE THE WEIGHTS
def weight_updater(weights, alpha, error_value, input_val):
    length=len(input_val)
    temp_val=alpha*error_value
    temp_list=list()

    #alpha*(desired output - Y) x X^(n-1)
    for i in range(0, length):
        input_val[i] = input_val[i]*temp_val
    
    #add the weights and input value together
    for i in range(0, length):
        temp_list.append(weights[i]+input_val[i])
    
    return temp_list


#--------------- MAIN()
if __name__ == "__main__":
    input_val=[[1, -2, 0, -1],[0, 1.5, -0.5, -1],[-1, 1, 0.5, -1]]
    weights=[1, -1, 0, 0.5]
    desired_output=[-1, -1, 1]
    
    alpha=0.1           #learning rate
    net_val=0           #net(i)
    actual_output=0     #Y
    error_value=0
    temp_list=list()

    #LOOP THIS PART SEVERAL TIMES FOR GETTING THE ACTUAL VALUE
    #ALSO UPDATE THE PIVOTS
    
    input_pivot=0       #0 to 2
    desired_output_pivot=0

    #running the operation several times
    for i in range(1,8):
        print(">>>>>>>>>STEP: ",i)
        net_val=matrix_multiply(weights,input_val[input_pivot])
        actual_output=sign_activation(net_val)
        #print(actual_output)
        error_value=desired_output[desired_output_pivot] - actual_output

        if error_value!=0:
            temp_list=weight_updater(weights, alpha, error_value, input_val[input_pivot])
            weights=temp_list
        print("NEW WEIGHTS: ",weights, " X=",input_pivot)
        input_pivot = input_pivot+1
        desired_output_pivot=desired_output_pivot+1

        if input_pivot>2:
            input_pivot=0
        if desired_output_pivot>2:
            desired_output_pivot=0
