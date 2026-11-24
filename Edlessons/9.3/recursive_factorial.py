import sys

# Complete the following
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    if len(sys.argv) != 2:
        print('Incorrect argument - need a single argument with a value of 0 or more.')
        return
    num = int(sys.argv[1])
    if num < 0:
        print('Incorrect argument - need a single argument with a value of 0 or more.')
    else:
        
        print(factorial(num))

if __name__ == "__main__":
    main()