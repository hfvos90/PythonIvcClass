#This program displays the recrods in the
#coffee.txt file

def show():
    #Open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #Read the first record's description field.
    descr = coffee_file.readline()

    #Read the rest of the file.
    while descr != '':
        #Read the quantity field
        qty = float(coffee_file.readline())

        #Strip the \n from description.
        descr = descr.rstrip('\n')

        #Display the record.
        print('Descritption:', descr)
        print('Quantity:', qty)

        #Read the next description
        descr = coffee_file.readline()

    #Close the file.
    coffee_file.close()

show()
