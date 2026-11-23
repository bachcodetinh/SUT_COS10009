FILENAME = 'data.txt' # Put the file name into a variable

class MyRecord():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# returns true if a string contains only digits
def is_numeric(obj):
    if obj.isnumeric():
        return True
    return False

# Sort from largest to smallest age depending on direction
def compare(a, b, direction):
    result = True
    if a > b:
        result = True
    else:
        result = False

    if direction:
        return not result
    else:
        return result
    
# sort list according to direction
def sort(arr, direction):
    item_count = len(arr)
    # Now let's use bubble sort. Swap pairs iteratively as we loop through the
    # array from the beginning of the array to the second-to-last value
    for i in range(item_count - 1):
        # From arr[i + 1] to the end of the array
        for j in range(i + 1, item_count):
            if compare(arr[i].age, arr[j].age, direction):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    return arr

# Read the first line that indicate the number of data
def count_and_validate(aFile):
    count = aFile.readline().strip()
    print(f'first line: {count}')
    if is_numeric(count):
        count = int(count)
    else:
        count = 0
        print('Error: first line of file is not a number')
    return count

# Read the data from the file and print out each line
def read_lines(aFile, count):
    people = []
    index = 0
    while index < count:
        name = aFile.readline().strip()
        age = int(aFile.readline().strip())
        record = MyRecord(name, age)
        people.append(record)
        print(f'Line read: {name}')
        index += 1
    return people

def print_array(list):
    print(f'Printing list: number of elements: {len(list)}')
    i = 0
    while i < len(list):
        print(f'Name: {list[i].name}\nAge: {list[i].age}')
        i += 1
# Load the records into an array
def load_reccords(aFile):
    count = count_and_validate(aFile)
    records = read_lines(aFile, count)
    return records

# Write data to a file then read it in and print it out
def main():
    with open(FILENAME, 'r') as aFile: # open for writing
        people = load_reccords(aFile)
    sorted_people = sort(people, True)
    print_array(sorted_people)
    
if __name__ == '__main__':
    main()