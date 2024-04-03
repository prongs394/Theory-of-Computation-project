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


#vars = ['DUMMY' , 'Y' ,'X1', 'Z1', 'X2', 'Z2', 'X3', 'Z3', 'X4', 'Z4', 'X5', 'Z5', 'X6', 'Z6', 'X7', 'Z7', 'X8', 'Z8', 'X9', 'Z9', 'X10', 'Z10', 'X11', 'Z11', 'X12', 'Z12', 'X13', 'Z13', 'X14', 'Z14', 'X15', 'Z15', 'X16']
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

inputs = input()
numbers = inputs.split()
numbers = [int(num) for num in numbers]
abc_arr = []



for i in numbers:
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

#__________________________________________
def generate_vars_array(biggest_variable):
    vars_array = ['DUMMY', 'Y']  # Start with these two variables
    num_pairs = biggest_variable // 2  # Calculate the number of X-Z pairs

    for i in range(1, num_pairs + 1):
        xi = f'X{i}'
        zi = f'Z{i}'
        vars_array.extend([xi, zi])

    # If biggest_variable is odd, we need to add an additional X variable
    if biggest_variable % 2 != 0:
        vars_array.append(f'X{num_pairs + 1}')

    return vars_array

if biggest_variable > 0:
    vars = generate_vars_array(biggest_variable)
else:
    vars = ['DUMMY' , 'Y']
#print(vars)

#___________________________________________________
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
    
for i in abc_arr:
    print(abc2code(i))

    

