import qrcode 

PRODUCTS = []

def read_from_database():
    f = open("database.txt", "r")

    for line in f:


        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict)
    f.close()

def write_to_database():
  
    with open("database.txt", "w") as f:
        for item in PRODUCTS:
            f.write(f"{item['code']},{item['name']},{item['price']},{item['count']}\n")

            
def show_menu():
    print("1-ADD")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-qrcode")
    print("8-Exit")

def add():
    code = input("Enter code: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    count= input("Enter count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count' : count}
    PRODUCTS.append(new_product)

def edit():
    user_input = int(input("Type your keyword: "))
    print("1-Name")
    print("2-Price")
    print("3-Count")
    if user_input == 1:
        name = input("Enter name: ")
        PRODUCTS.append(name)
        print("Information updated successfully")
    elif user_input == 2:
        price = int(input("Enter price: "))
        PRODUCTS.append(price)
        print("Information updated successfully")
    elif user_input == 3:
        count= int(input("Enter count: "))
        PRODUCTS.append(count)
        print("Information updated successfully")

def remove():
    user_input = input("Type your code: ")
    for product in PRODUCTS:
        if product['code'] == user_input:
           print("The desired product has been successfully removed")
           return
    print("Not found")

def search():
    user_input = input("Type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"]," \t",product["name"], "\t",product["price"])
            break
    else:
        print("Not found")
def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"]," \t",product["name"], "\t",product["price"])

def qrcode():
    
    name =int(input("Enter your code: "))
   
    x = qrcode.make(name)
    x.save("my_Qrcode.png")


def buy():
    code_to_buy = input("Enter the product code to buy: ")
    for product in PRODUCTS:
        if product['code'] == code_to_buy:
            quantity = int(input("Enter the quantity to buy: "))
            if int(product['count']) >= quantity:
                product['count'] = str(int(product['count']) - quantity)
                total_price = float(product['price']) * quantity
                print(f"Purchased: {product['name']} - Quantity: {quantity} - Price: {total_price}")
                return
            else:
                print("Not enough quantity available.")
                return
    print("Product not found.")


print("Receipt:")
total_sum = sum(float(product['price']) * int(product['count']) for product in PRODUCTS)
print(f"Total Sum: {total_sum}")
        


print("Wellcome to MRZ Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        qrcode()
    elif choice == 8:
        write_to_database()
        print("Receipt:")
        total_sum = sum(float(product['price']) * int(product['count']) for product in PRODUCTS)
        print(f"Total Sum: {total_sum}")
        exit(0)
    else:
        print("Again")

