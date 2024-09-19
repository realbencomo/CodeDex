# A Drive through simulator

total_order = 0
order_items = []  

def get_item(x):
    global total_order  
    if x == 1:
        total_order += 5.00
        order_items.append('Pizza Margherita')
        return 'A Pizza Margherita'
    
    elif x == 2:
        total_order += 5.50
        order_items.append('Prosciutto Pizza')
        return 'A Prosciutto Pizza'
    
    elif x == 3:
        total_order += 6.00
        order_items.append('Mozzarella Stravaganza')
        return 'A Mozzarella Stravaganza'
    
    elif x == 4:
        total_order += 6.00
        order_items.append('Capricciosa')
        return 'A Capricciosa'
    
    elif x == 5:
        total_order += 7.00
        order_items.append('Mamma Mia')
        return 'A Mamma Mia'
    
    elif x == 6:
        total_order += 9.00
        order_items.append('Madonna Mia (house specialty)')
        return 'The house specialty! A Madonna Mia'
    
    elif x == 7:
        total_order += 2.00
        order_items.append('Beer')
        return 'A Beer'
    
    elif x == 8:
        total_order += 3.00
        order_items.append('Glass of Wine')
        return 'A glass of wine'
    
    elif x == 9:
        total_order += 1.50
        order_items.append('Soda')
        return 'A soda'
    
    else:
        return 'Invalid input, try again'

def welcome_menu():
    print('Welcome to Madonna Mia Pizza\n')
    print('Menu:\n')
    print('1: Margherita $5.00')
    print('2: Prosciutto $5.50')
    print('3: Mozzarella Stravaganza $6.00')
    print('4: Capricciosa $6.00')
    print('5: Mamma Mia $7.00')
    print('6: Madonna Mia $9.00')
    print('7: Beer $2.00')
    print('8: Wine $3.00')
    print('9: Soda $1.50')

def print_order_summary():
    print('\nYour order summary:')
    for item in order_items:
        print(f'- {item}')
    print(f'Total before tip: ${total_order:.2f}')

def calculate_tip():
    while True:
        try:
            tip_percentage = int(input('Choose a tip percentage (10, 15, or 20): '))
            if tip_percentage in [10, 15, 20]:
                tip_amount = (tip_percentage / 100) * total_order
                total_with_tip = total_order + tip_amount
                print(f'Tip: ${tip_amount:.2f} ({tip_percentage}%)')
                print(f'Total with tip: ${total_with_tip:.2f}')
                break
            else:
                print("Please choose 10, 15, or 20.")
        except ValueError:
            print("Invalid input. Please enter 10, 15, or 20.")

welcome_menu()

while True:
    try:
        option = int(input('Add an item to your order (1-9): '))
        print(f'You added: {get_item(option)}')

        exit_order = input('Add another item to your order? Y/N: ').upper()
        if exit_order == 'Y':
            continue
        else:
            print_order_summary()
            calculate_tip()
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
