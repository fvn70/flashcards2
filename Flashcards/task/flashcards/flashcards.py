import json
import random


def _add():
    print(f"The card:")
    while True:
        term = input()
        if term not in cards:
            break
        print(f'The term "{term}" already exists. Try again:')
    print(f"The definition of the card:")
    while True:
        dfn = input()
        if dfn not in cards.values():
            break
        print(f'The definition "{dfn}" already exists. Try again:')
    cards[term] = dfn
    print(f'The pair ("{term}":"{dfn}") has been added.')


def _remove():
    term = input('Which card?\n')
    if cards.pop(term, False):
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{term}": there is no such card.')


def _ask():
    num_cards = int(input('How many times to ask?\n'))
    for i in range(num_cards):
        dfn = random.choice(list(cards.keys()))
        answer = input(f'Print the definition of "{dfn}":\n')
        if answer == cards[dfn]:
            print('Correct!')
        else:
            msg = f'Wrong. The right answer is "{cards[dfn]}"'
            if answer in cards.values():
                dfn = [k for k, v in cards.items() if v == answer][0]
                msg += f', but your definition is correct for "{dfn}"'
            print(f'{msg}.')


def _export(fn = ''):
    if not fn:
        fn = input('File name:\n')
    with open(fn, 'w') as fl:
        json.dump(cards, fl)
        print(f'{len(cards)} cards have been saved.')


def _import(fn = ''):
    if not fn:
        fn = input('File name:\n')
    try:
        with open(fn, 'r') as fl:
            cards.update(json.load(fl))
            print(f'{len(cards)} cards have been loaded.')
    except Exception:
        print("File not found.")


cmds = ('add', 'remove', 'import', 'export', 'ask', 'exit',)
cards = {}

while True:
    print()
    cmd = input("Input the action (add, remove, import, export, ask, exit):\n")
    if cmd == 'exit':
        break
    elif cmd in cmds:
        eval(f'_{cmd}()')
print("Bye bye!")
