import tabele_print

bias=0
num_inputs=0
start_weight=0
learning_rate=0
training_data=""
table=[]



def main ():
    global bias, num_inputs, start_weight, learning_rate, training_data, table
    print ("starting")
    bias=bool(input("bias neuron: "))
    num_inputs=int(input("number of inputs: "))
    start_weight=input("start weight: ")
    learning_rate=input("learning rate: ")
    training_data=input("training data: ").split(" ")
    if not training_data_test(training_data):
        print("training data is invalid")
        return None
    table_header_create()
    tabele_print.table_print([table])

    
def training_data_test(trainig_data):
    if len(trainig_data) == 2 ** num_inputs:
        return True
    else:
        return False
    
def table_header_create():
    global table
    delta=[]
    weight=[]
    if bias:
        table.append("X_0")
        weight.append("W_0")
        delta.append("ΔW_0")
    for i in range(num_inputs):
        table.append("X_" + str(i+1))
        weight.append("W_" + str(i+1))
        delta.append("ΔW_" + str(i+1))
    table.append("t")
    table.extend(weight)
    table.append("I")
    table.append("Y")
    table.append("t-y")
    table.extend(delta)

    
def weight_matrix_create():
    pass

if __name__ == "__main__":
    main()