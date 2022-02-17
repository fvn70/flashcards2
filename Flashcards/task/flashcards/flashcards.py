cards = []

num = input("Input the number of cards:\n")
for i in range(int(num)):
    cards.append([input(f"The term for card #{i + 1}:\n")])
    cards[i].append(input(f"The definition for card #{i + 1}:\n"))

for j in range(len(cards)):
    answer = input(f'Print the definition of "{cards[j][0]}":\n')
    if answer == cards[j][1]:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{cards[j][1]}".')
