def read_array(items):
    num_items = int(input('How many items are you entering: '))
    i = 0 
    while i < num_items:
        item = input('Enter item: ')
        items.append(item)
        i += 1
    return items


def print_array(a):
    print('Shopping list:')
    i = 0
    while i < len(a):
        print(i, a[i])
        i += 1


def main():
    items = []
    print_array(read_array(items))


if __name__ == "__main__":
    main()
