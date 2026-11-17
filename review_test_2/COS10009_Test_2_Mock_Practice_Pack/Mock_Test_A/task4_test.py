# Import the class and dictionary here.
from task4_board_game import BoardGame, CATEGORY


def main():
    # Complete this function.
    board1 = BoardGame()
    board1.title = 'Pandemic'
    board1.category = 0
    board1.cooperative = True
    print(f'title: {board1.title}')
    print(f'category: {CATEGORY[board1.category]}')
    print(f'cooperative: {board1.cooperative}')


if __name__ == "__main__":
    main()
