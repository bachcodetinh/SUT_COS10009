def read_array(a):
    # Ask for the count and read the items.
    num = int(input('How many exhibits will you visit: '))
    i = 0 
    while i < num:
        exh = input('Enter exhibit: ')
        a.append(exh)
        i += 1
    return a

def print_array(a):
    # Print the numbered items.
    i = 0 
    print('Visit list:')
    while i < len(a):
        print(i + 1,a[i])
        i+=1

def main():
    # Call read_array() and print_array().
    visits = []
    print_array(read_array(visits))


if __name__ == "__main__":
    main()
