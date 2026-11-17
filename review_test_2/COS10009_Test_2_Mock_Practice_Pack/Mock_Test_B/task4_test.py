# Import the class and dictionary here.
from task4_exhibit import Exhibit, ZONE

def main():
    # Complete this function.
    exh1 = Exhibit()
    exh1.name = 'Robot Arm'
    exh1.zone = 3
    exh1.interactive = True
    print(f'name: {exh1.name}')
    print(f'zone: {ZONE[exh1.zone]}')
    print(f'interactive: {exh1.interactive}')


if __name__ == "__main__":
    main()
