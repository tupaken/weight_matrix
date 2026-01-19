import tabele_print

bias=0
num_inputs=0
start_weight=0
learning_rate=0
training_data=""
table=[]
weight=[]
epoche=[]
tr_d=[]
mod=1



def main ():
    global bias, num_inputs, start_weight, learning_rate, training_data, table,weight,epoche,tr_d
    print ("starting")
    bias=int((input("bias neuron: ")))
    num_inputs=int(input("number of inputs: "))
    start_weight=(input("start weight: "))
    learning_rate=input("learning rate: ")
    training_data=input("training data: ").split(" ")
    weight=start_weights(start_weight)
    epoche=epoche_tabelle(num_inputs)
    if not training_data_test(training_data):
        print("training data is invalid")
        return None
    tr_d=training_data_split(training_data)
    tab_h=table_header_create(bias)
    weight_matrix_create(tab_h)
   # tabele_print.table_print(calculated_input(epoche,tab_h,weights=weight))
    
    

    
def training_data_test(trainig_data):
    if len(trainig_data) == 2 ** num_inputs:
        return True
    else:
        return False
    
def table_header_create(bias):
    table=[]
    delta=[]
    weight=[]
    if bias>0:
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
    return table

    
def weight_matrix_create(tab_h):
    global mod
    while mod>0:
        mod=0
        tabele_print.table_print(calculated_input(epoche,tab_h,weights=weight))


def epoche_tabelle(n):
    bits_row=[]
    all_rows=[]
    for k in range(2 ** n):
        bits=format(k, f"0{n}b")
        if bias>0:
            bits_row.append(1)
        for j in bits:
            bits_row.append(int(j))
        all_rows.append(bits_row)
        bits_row=[]
    return all_rows

def start_weights(start_weight):
    weights=[]
    if bias>0:
        weights.append(0)
    for i in start_weight:
        weights.append(int(i))
    return weights

def training_data_split(tr_d):
    data=[]
    for i in tr_d:
        data.append(int(i))
    return data


def calculated_input(epoche,tb_h,weights):
    global weight,mod
    all_rows=[]
    all_rows.append(tb_h)
    for i in range(len(epoche)):
        input=0
        weights_row=[]
        row=[]
        epoche_row=epoche[i]
        for z in range(len(epoche_row)): # add x0....
            var=epoche_row[z]
            row.append(var)
            weights_row.append(weights[z])

            if var>0: #Berechnet Input
                weight=var*weights[z]
                input+=weight

        row.append(tr_d[i])
        row.extend(weights_row)
        weights_row=[]
        row.append(input)

        output=neuron(input) # Y
        row.append(output)

        if tr_d[i] != output:
            mod=1
            delta_row=[]
            delta = tr_d[i] - output
            row.append(delta)#t-y
            for z in range(len(epoche_row)):
                if epoche_row[z]>0:
                    delta_row.append(delta)
                    weights_row.append(weights[z]+delta)
                else:
                    delta_row.append(0)
                    weights_row.append(weights[z])
            weights=weights_row
            row.extend(delta_row)
        else: 
            row.append(0)



        all_rows.append(row)
    
    weight=weights
    return all_rows

    
def neuron(input): # Y check
    if input>=0:
        return 1
    else:
        return 0
    return all_rows


    

    
            
            
            



if __name__ == "__main__":
    main()