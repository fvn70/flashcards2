def add_card(num):
    print(f"The term for card #{i + 1}:")
    while True:
        term = input()
        if term not in cards:
            break
        print(f'The term "{term}" already exists. Try again:')
    print(f"The definition for card #{num}:")
    while True:
        dfn = input()
        if dfn not in cards.values():
            break
        print(f'The definition "{dfn}" already exists. Try again:')
    cards[term] = dfn


def ask():
    for card in cards:
        answer = input(f'Print the definition of "{card}":\n')
        if answer == cards[card]:
            print('Correct!')
        else:
            msg = f'Wrong. The right answer is "{cards[card]}"'
            if answer in cards.values():
                dfn = [k for k, v in cards.items() if v == answer][0]
                msg += f', but your definition is correct for "{dfn}"'
            print(f'{msg}.')


cards = {}

num = input("Input the number of cards:\n")
for i in range(int(num)):
    add_card(i + 1)
ask()
