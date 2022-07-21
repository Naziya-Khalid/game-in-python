import random
def game(comp,u):
    if comp == u:
        print("It's a tie")
    if comp=='r':
        if u=='p':
            win=True
        elif u=='s':
            win=False
    elif comp=='p':
        if u=='s':
            win=True
        elif u=='r':
            win=False
    elif comp=='s':
        if u=='r':
            win=True
        elif u=='p':
            win=False
    return win
    
print("Computer's turn enter Rock(r) Paper(p) or Scicers(s)")
print("\nYour's turn enter Rock(r) Paper(p) or Scicers(s)")
u=input()
ch=random.randint(1,3)
if ch==1:
    comp='r'
elif ch==2:
    comp='p'
elif ch==3:
    comp='s'
result=game(comp,u)
print(f"\nComputer chose {comp}")
print(f"\nYou chose {u}")

if result:
    print("\nYou win the game")
else:
    print("\nYou lose")