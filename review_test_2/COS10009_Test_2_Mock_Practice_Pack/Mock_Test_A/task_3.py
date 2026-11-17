def read_array(a):
    # Ask for the count and read the items.
    num = int(input('How many items are you packing: '))
    i = 0
    while i < num:
        item = input('Enter item: ')
        a.append(item)
        i += 1
    return a


def print_array(a):
    i = 0
    while i < len(a):
        print(i, a[i])
        i += 1


def main():
    items = []
    print_array(read_array(items))


if __name__ == "__main__":
    main()
