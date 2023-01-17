from tabulate import tabulate

class Shoe:
    '''
    Class representing shoe in inventory
    '''
    
    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialise shoe attributes

        Inputs
        ------
        
        country : str
            country of shoe
        code : str
            code of shoe
        product: str
            name of product
        cost : str
            cost of shoe
        quantity : str
            quantity of shoe
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)
        
    def get_cost(self):
        '''
        Return the cost of the shoe.
        '''
        return(self.cost)
    
    def get_quantity(self):
        '''
        Return the quantity of the shoes.
        '''
        return(self.quantity)
    
    def calc_total_cost(self):
        '''
        Return total cost of stock
        '''
        return(float(self.cost)*self.quantity)
    
    def __str__(self):
        '''
        Returns a string representation of class.
        '''
        return([self.country,self.code,self.product,self.cost,str(self.quantity)])

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    '''
    Read from inventory.txt and add shoes to shoe_list
    '''
    #read file
    try:
        with open('inventory.txt') as f:
            lines = f.readlines()[1:]
    except:
        print("File doesn't exist; data not read")
        return
    
    #create shoes and add to list
    for l in lines:
        shoe_attr = l.strip('\n').split(',')
        try:
            new_shoe = Shoe(shoe_attr[0],shoe_attr[1],shoe_attr[2],shoe_attr[3],shoe_attr[4])
            shoe_list.append(new_shoe)
        except:
            print('Invalid shoe entry; not stored')
    
    print("Reading file data complete\n")
    
def capture_shoes():
    '''
    Add shoe to list using user input
    '''
    #ask user for shoe details
    country = input('Enter Country: ')
    code = input('Enter shoe code: ')
    product = input('Enter shoe name: ')
    cost = input('Enter price: ')
    quantity = input('Enter quantity: ')
    
    #create shoe and add to list
    new_shoe = Shoe(country,code,product,cost,quantity)
    shoe_list.append(new_shoe)
    print('Shoe added\n')

def view_all():
    '''
    Print shoe details in shoe_list as a table
    '''
    string_lists = [s.__str__() for s in shoe_list]
    table = tabulate(string_lists,headers=['Country','Code','Product','Cost','Quantity'])
    print(table)
    
def re_stock():
    '''
    Restock lowest quantity shoe
    '''
    #find mininum quantity
    quantities = [s.get_quantity() for s in shoe_list]
    minq_ind = quantities.index(min(quantities))
    
    #ask user how many to add and add to object
    input_prompt = f"{shoe_list[minq_ind].product} has lowest quantity of {min(quantities)}.\n"\
          "How many to restock? "
    add_quant = input(input_prompt)
    try:
        shoe_list[minq_ind].quantity += int(add_quant)
    except:
        print('Invalid entry for quantity')
    
    #write new values to file
    with open('inventory.txt','w') as f:
        f.writelines(['Country,Code,Product,Cost,Quantity\n']+[','.join(s.__str__())+'\n' for s in shoe_list])
        
def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    #ask user for code 
    code = input('Enter shoe code: ')
    
    #return item with matching code if exists
    code_list = [s.code for s in shoe_list]
    
    try:
        return shoe_list[code_list.index(code)]
    except:
        print('Shoe not found')

def value_per_item():
    '''
    Show total value per shoe
    '''
    #construct table of total value and print
    table_data = [[s.product,s.calc_total_cost()] for s in shoe_list]
    table = tabulate(table_data,headers=['Product','Total Value'])
    print(table)

def highest_qty():
    '''
    Print that the highest quantity shoe is on sale
    '''
    #find max quantity
    quantities = [s.get_quantity() for s in shoe_list]
    maxq_ind = quantities.index(max(quantities))
    
    #print as on sale
    print(f'{shoe_list[maxq_ind].product} is on sale!\n')


#==========Main Menu=============

while True:
    menu_text = 'Choose an option:\n'\
            '1: Add all shoes from file data\n'\
            '2: Enter new shoe manually\n'\
            '3: View all shoes in inventory\n'\
            '4: Restock lowest inventory shoe\n'\
            '5: Search shoes by code\n'\
            '6: Show total value per shoe\n'\
            '7: Put highest quantity shoe on sale\n'\
            '8: Quit\n:'
    
    try:
        user_choice = int(input(menu_text))
    except:
        print('Invalid Choice; choose 1-8')
        continue
    
    if user_choice == 1:
        #read all shoes
        read_shoes_data()
    elif user_choice == 2:
        #ask user to enter own data
        capture_shoes()
    elif user_choice == 3:
        #view table of all shoes
        view_all()
    elif user_choice == 4:
        #restock lowest quantity shoe
        re_stock()
    elif user_choice == 5:
        #find shoe and print
        shoe = seach_shoe()
        print(tabulate([shoe.__str__()],headers=['Country','Code','Product','Cost','Quantity']))
        print('')
    elif user_choice == 6:
        #view table of value by item
        value_per_item()
    elif user_choice == 7:
        #put highest quantity shoe on sale
        highest_qty()
    elif user_choice == 8:
        exit()
        break
    else:
        print('Invalid Choice\n')
