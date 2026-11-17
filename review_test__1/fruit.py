import input_functions as in_fnc

class Fruit:
    def __init__(self, fruit_id, origin, variety, crate_num, weight_kilo, org_flag):
        self.fruit_id = fruit_id
        self.origin = origin
        self.variety = variety
        self.crate_num = crate_num
        self.weight_kilo = weight_kilo
        self.org_flag = org_flag

def read_a_fruit():
    fruit_id = in_fnc.read_integer('Enter fruit id: ')
    origin = in_fnc.read_string('Enter fruit origin: ')
    variety = in_fnc.read_string('Enter fruit variety: ')
    crate_num = in_fnc.read_integer('Enter fruit crate number: ')
    weight_kilo = in_fnc.read_float('Enter fruit weight in kilograms: ')
    org_flag_raw = in_fnc.read_string('Is the fruit organic (y/n): ').lower()

    if org_flag_raw == "y":
        org_flag = True
    elif org_flag_raw == "n":
        org_flag = False
    else:
        org_flag is None

    return Fruit(fruit_id, origin, variety, crate_num, weight_kilo, org_flag)

def read_fruits(): 
    num_fruit = in_fnc.read_integer('How many fruits are you entering: ')
    fruit_array = []
    for i in range(num_fruit):
        fruit_array.append(read_a_fruit())
    return fruit_array

def print_a_fruit(fruit):
    print('Id', fruit.fruit_id)
    print('Origin', fruit.origin)
    print('Variety', fruit.variety)
    print('Crate Number', fruit.crate_num)
    print('Weight', f'{fruit.weight_kilo:.1f}')
    print('Organic', fruit.org_flag)

def print_fruits(fruits):
    for i in range(len(fruits)):
        print_a_fruit(fruits[i])

def main():
    print_fruits(read_fruits())

if __name__ == '__main__':
    main()


