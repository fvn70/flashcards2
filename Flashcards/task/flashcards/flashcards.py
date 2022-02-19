import io
import json
import logging
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
            try:
                errors[dfn] += 1
            except:
                errors[dfn] = 1
            msg = f'Wrong. The right answer is "{cards[dfn]}"'
            if answer in cards.values():
                dfn = [k for k, v in cards.items() if v == answer][0]
                msg += f', but your definition is correct for "{dfn}"'
            print(f'{msg}.')


def _export(fn=''):
    if not fn:
        fn = input('File name:\n')
    with open(fn, 'w') as fl:
        json.dump([cards, errors], fl)
        print(f'{len(cards)} cards have been saved.')


def _import(fn=''):
    if not fn:
        fn = input('File name:\n')
    try:
        with open(fn, 'r') as fl:
            data = json.load(fl)
            cards.update(data[0])
            errors.update(data[1])
            print(f'{len(cards)} cards have been loaded.')
    except Exception:
        print("File not found.")


def _hardest():
    global list
    if errors:
        max_v = max(list(errors.values()))
    else:
        print("There are no cards with errors.")
        return
    hards = [k for k, v in errors.items() if v == max_v]
    if len(hards) == 1:
        print(f'The hardest card is "{hards[0]}". You have {max_v} errors answering it.')
    else:
        list = '", "'.join(hards)
        print(f'The hardest cards are "{list}". You have {max_v} errors answering them.')


def _log():
    fn = input('File name:\n')
    content = output.getvalue()
    with open(fn, 'w') as fl:
        fl.write(content)
    print(f'The log has been saved.')


def _reset():
    errors.clear()
    print("Card statistics have been reset.")


old_input = input
old_print = print


def input(string=""):
    log.info(string.rstrip())
    string_in = old_input(string)
    log.info(string_in.rstrip())
    return string_in


def print(string="", string2=""):
    old_print(string, string2)
    log.info(string.rstrip())


cmds = ('add', 'remove', 'import', 'export', 'ask', 'list', 'exit', 'log', 'hardest card', 'reset stats')
cards = {}
errors = {}
output = io.StringIO()
logging.basicConfig(stream=output, level=logging.INFO, format='%(message)s')
log = logging.getLogger()
fn_out = ''

while True:
    print()
    cmd = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
    if cmd == 'exit':
        break
    elif cmd in cmds:
        eval(f'_{cmd.split()[0]}()')
print("Bye bye!")
