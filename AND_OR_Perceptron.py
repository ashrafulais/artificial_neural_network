#SOLVING FOR AND GATE
#AUTHOR: ASHRAFUL ISLAM(32.6 - 018)

def step_function(value):
    if value>0:
        return 1
    else:
        return 0
    
def is_it_okey(value):
    if value==0:
        return True
    else:
        return False

#input these values from user
#value definition
input_vals = [[0,0,1,1], [0, 1, 0, 1]]
output_vals = [0,0,0,1]
weights=[0.2,0.1]
bias=-1
learning_rate=0.1

actual_output=0
error_val=0
lets_stop=0

#***
#improve this by an unconditional loop


for j in range(0, 50):
    #feeding the input pattern
    print("STEP:------",j)
    
    for i in range(0,4):
        net_val=weights[0]*input_vals[0][i] + weights[1]*input_vals[1][i] - bias
        actual_output = step_function(net_val)
        error_val = output_vals[i] - actual_output

        print("    W: ",weights," X:",input_vals[0][i], "", input_vals[1][i],"-",is_it_okey(error_val))
        #print("    BIAS: ",bias)
        lets_stop=0
        if is_it_okey(error_val)==False:
            weights[0] = weights[0] + (learning_rate*error_val*input_vals[0][i])
            weights[1] = weights[1] + (learning_rate*error_val*input_vals[1][i])
            bias = ((learning_rate*-1)*error_val)+bias

            lets_stop=1
            break
    #print(weights)
    if lets_stop==0:
        break
