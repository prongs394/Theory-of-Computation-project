#recieves #(I) returns a,b,c
def num2abc(num):
    num = num+1
    a = 0
    b = 0
    c = 0
    while (num%2 == 0):
        a = a+1
        num = num/2
    num = num-1
    num = num/2
    num = num+1
    while(num%2 == 0):
        b = b+1
        num = num/2
    num = num-1
    num = num/2
    c = int(num)
    return [a,b,c]


#____________________________________________________________________


#vars = ['DUMMY' , 'Y' ,'X1', 'Z1', 'X2', 'Z2', 'X3', 'Z3', 'X4', 'Z4', 'X5', 'Z5', 'X6', 'Z6', 'X7', 'Z7', 'X8', 'Z8', 'X9', 'Z9', 'X10', 'Z10', 'X11', 'Z11', 'X12', 'Z12', 'X13', 'Z13', 'X14', 'Z14', 'X15', 'Z15' , 'X16']
#labels = ['DUMMY','A1', 'B1', 'C1', 'D1', 'E1', 'A2', 'B2', 'C2', 'D2', 'E2', 'A3', 'B3', 'C3', 'D3', 'E3', 'A4', 'B4', 'C4', 'D4', 'E4', 'A5', 'B5', 'C5', 'D5', 'E5']


#____________________________________________________________________

def abc2code(arr):
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if a>0:
        L = labels[a]

    V = vars[c+1]

    if b<3:

        if b == 0:
            if a>0:
                formatted_string = f'[{L}] {V} <- {V}'
            if a==0:
                formatted_string = f'{V} <- {V}'

        if b == 1:
            if a>0:
                formatted_string = f'[{L}] {V} <- {V} + 1'
            if a==0:
                formatted_string = f'{V} <- {V} + 1'

        if b == 2:
            if a>0:
                formatted_string = f'[{L}] {V} <- {V} - 1'
            if a==0:
                formatted_string = f'{V} <- {V} - 1'

    if b>2:

        L_ = b-2
        if a>0:
            formatted_string = f'[{L}] IF {V} != 0 GOTO {labels[L_]}'
        if a==0:
            formatted_string = f'IF {V} != 0 GOTO {labels[L_]}'

    return formatted_string


 

#____________________________________________________________________

#Enter numbers separated by space for instructions:
instructions_input = input()
instructions_number = [int(num) for num in instructions_input.split()]

#Enter numbers separated by space for vars:
vars_inputs = input()
vars_input = [int(num) for num in vars_inputs.split()]
#____________________________________________________________________

abc_arr = []



for i in instructions_number:
    abc_arr.append(num2abc(i))
    #print(abc2code(num2abc(i)))

#vars and labels arrays:
biggest_variable = -1
biggest_label = -1
for i in range (len(abc_arr)):
    curr_var = abc_arr[i][2] + 1
    curr_label = abc_arr[i][0] 
    if (curr_var > biggest_variable):
        biggest_variable = curr_var
    if (curr_label > biggest_label):
        biggest_label = curr_label

for i in range (len(abc_arr)):
    if (abc_arr[i][1]>2):
        curr_goto_label = abc_arr[i][1]
        if(curr_goto_label > biggest_label):
            biggest_label = curr_goto_label

#++++++++++++++++++++++++++++++++++++++++++
def generate_vars_array(biggest_variable):
    vars_array = ['DUMMY', 'Y']  # Start with these two variables
    if biggest_variable%2 == 1:
        num_pairs = (biggest_variable) // 2  # Calculate the number of X-Z pairs
    if biggest_variable%2 == 0:
        num_pairs = (biggest_variable) // 2
        num_pairs-=1

    for i in range(1, num_pairs+1):
        xi = f'X{i}'
        zi = f'Z{i}'
        vars_array.extend([xi, zi])

    # If biggest_variable is odd, we need to add an additional X variable
    if biggest_variable % 2 == 0:
        vars_array.append(f'X{num_pairs + 1}')

    return vars_array

if biggest_variable > 0:
    vars = generate_vars_array(biggest_variable)
else:
    vars = ['DUMMY' , 'Y']
#print(vars)

#++++++++++++++++++++++++++++++++++++++++++
def generate_labels_array(biggest_label):
    labels_array = ['DUMMY']
    number_of_fives = biggest_label // 5
    for i in range(1, number_of_fives+2):
        ai = f'A{i}'
        bi = f'B{i}'
        ci = f'C{i}'
        di = f'D{i}'
        ei = f'E{i}'
        labels_array.extend([ai,bi,ci,di,ei])
    return labels_array
if biggest_label > 0:
    labels = generate_labels_array(biggest_label)
else:
    labels = ['DUMMY']
#print(labels)
 

#____________________________________________________________________

instructions = [] #a 3D matrix. for each instruction contains a,b, and c
decoded = []
for i in instructions_number:
    ins = num2abc(i)
    instructions.append(ins)
    decoded.append(abc2code(ins))
    #print(abc2code(ins))
#print(instructions)

#____________________________________________________________________

vars_values = [0] * len(vars) #contains values of variables
num_inputs = len(vars_input)

#initialize values (Xis in input)
for i in range(num_inputs): 
    vars_values[(i+1)*2] = vars_input[i]
#print(vars_values)

#____________________________________________________________________


#count the variable with biggest #(V):
biggest_x = -1
biggest_z = -1
#print(instructions)
num_of_ins = len(instructions)
biggest = -1
for i in range(len(instructions)):
    curr = instructions[i][2] + 1
    if curr%2 == 0:
        if curr > biggest_x:
            biggest_x = curr
    elif curr%2 == 1:
        if curr > biggest_z:
            biggest_z = curr

if (biggest_x != -1):
    #print("biggest variable is: ",vars[biggest_x] , " with code number ",biggest_x)
    num_of_x = int(biggest_x/2) #how many Xs are used
elif (biggest_x == -1):
    #print("no Xi variables")
    num_of_x = 0
if (biggest_z != -1):
    #print("biggest local var: ", vars[biggest_z], ' with code number ', biggest_z)
    num_of_z = int((biggest_z-1)/2) #how many Zs are used
elif (biggest_z == -1):
    #print("no local vars used")
    num_of_z = 0


#____________________________________________________________________


#add dummy array to start of instructions:
dummy_array = [[0,0,0]]
instructions = dummy_array + instructions
#print(instructions)

#____________________________________________________________________

def snapshot(num_of_x , num_of_z , line): 
    snap = []
    snap.append(line)
    for i in range(num_of_x):
        snap.append(vars_values[(i+1)*2])
    for i in range(num_of_z):
        snap.append(vars_values[(i+1)*2 + 1])
    snap.append(vars_values[1]) #for y

    return snap

#____________________________________________________________________


#for i in decoded:
#    print(i)
state = True
line = 1
snap = snapshot(num_of_x , num_of_z, line)
snap_string = ' '.join(map(str, snap))
print(snap_string)
while (state):
    a = instructions[line][0] #label
    b = instructions[line][1] #instrunction
    c = instructions[line][2] #variable
    
    if (b==0):
        next_line = line + 1
        #no change to vars_values array

    elif (b==1):
        next_line = line + 1
        vars_values[c+1]+=1 #increment

    elif (b==2):
        next_line = line + 1
        if (vars_values[c+1]>0):
            vars_values[c+1]-=1

    elif (b>2):
        if (vars_values[c+1] != 0):
            #print(1)
            goto_label = b-2
            if goto_label %5 == 0: # it is E
                #print(2)
                next_line = num_of_ins + 1
            else:
                #print(3)
                #look which line has goto_label
                found = 0
                for i in range(1,len(instructions)):
                    if (instructions[i][0] == goto_label):
                        #print(4)
                        next_line = i
                        found = 1
                if (found == 0): #if goto L where L does not exist, goto next line
                    #print(5)
                    #next_line = line + 1
                    next_line = num_of_ins + 1
            
        elif (vars_values[c+1] == 0):
            #print(6)            
            next_line = line+1

    #snap = snapshot(num_of_x , num_of_z, line)
    snap = snapshot(num_of_x , num_of_z, next_line)
    if(snap[0] <= num_of_ins):
        snap_string = ' '.join(map(str, snap))
        print(snap_string)
        line = next_line
    if (next_line > num_of_ins):
        state = False


    


