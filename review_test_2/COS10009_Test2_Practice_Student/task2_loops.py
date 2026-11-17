def main():
    i = 0
    total = 0
    while i < 10:
        num = int(input(f'Enter an integer {i+1}: '))
        total += num
        i += 1
    print(f'Total is: {total}')
    


if __name__ == "__main__":
    main()
