def write_data_to_file(file_name):
    file = open(file_name, "w")
    file.write("5\n")
    file.write("Fred\n")
    file.write("Sam\n")
    file.write("Jill\n")
    file.write("Jenny\n")
    file.write("Zorro\n")
    file.close()


def read_data_from_file(file_name):
    file = open(file_name, "r")
    count = int(file.readline())
    print(str(count))
    for i in range(count):
        print(file.readline(), end='')
    file.close()

def main(): 
    write_data_to_file("mydata.txt")

    read_data_from_file("mydata.txt")


main()
