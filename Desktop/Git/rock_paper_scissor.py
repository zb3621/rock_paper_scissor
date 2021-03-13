import random

def game(comp, u):
    if comp == 'scissor':
        if u == 'paper':
            print('you lose')
        elif u == 'rock':
            print ('you win')
        else:
            print('tie')
    if comp == 'paper':
        if u == 'scissor':
            print('you win')
        elif u == 'rock':
            print ("you lose")
        else:
            print('tie')
    if comp == "rock":
        if u == 'paper':
            print('you win')
        elif u == 'scissor':
            print("you win")
        else:
            print('tie')


print('comp turn: rock(r), paper(p) or scissor(s): ')
comprandom = random.randint(1, 3)
if comprandom == 1:
    comp = "rock"
elif comprandom == 2:
    comp = 'paper'
elif comprandom == 3:
    comp = 'scissor'

u = input ('rock, paper or scissor: ')

print (f'computer chose {comp}')
print (f'you chose {u}')

game(comp, u)