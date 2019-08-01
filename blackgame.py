import random
import os
clear = lambda: os.system('cls')
List_type=['spade','hearts','diamond','clubs']
List_specific=['2','3','4','5','6','7','8','9','10','ace','jack','king','queen']
dictionary={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':10,'queen':10,'king':10,'ace':11}
class dealer:

    def __init__(self):
        self.List=[]
        self.List=['Not allowed to see']
        self.count=0
    def card(self):
        type=random.choice(List_type)
        specific=random.choice(List_specific)
        s=(f'{specific} of {type}')
        self.List.append(s)
        if specific=='ace':
            if (self.count+dictionary[specific])>21:
                dictionary[specific]=1
        self.count+=dictionary[specific]
        dictionary['ace']=11
    def display(self):
        for i in self.List:
            print(i)
        print()
        print(f"Total of dealer is:{self.count}")
    def delete(self):
        del(self.List[0])
class custumer:
    def __init__(self):
        self.List=[]
        self.count=0
    def card(self):
        type=random.choice(List_type)
        specific=random.choice(List_specific)
        self.List.append(f'{specific} of {type}')
        if specific=='ace':
            if (self.count+dictionary[specific])>21:
                dictionary[specific]=1
        self.count+=dictionary[specific]
        dictionary['ace']=11
    def display(self):
        for i in self.List:
            print(i)
        print()
        print(f"Total of custumer is:{self.count}")
amount=1000
print("{0:-^200}".format('Wlcome tp BlackJack!!!'))
while True:
    print(f'The total ammount is {amount}')
    print("Enter amount to bet")
    if amount==0:
        print("YOUR COINS IS ZERO")
        break
    while True:
        bet=int(input())
        if bet>1000 or bet<=0:
            print("Invalid Input , Please reenter ammount for bet")
            continue
        break
    amount-=bet
    print("GAME STARTS!!!")
    clear()
    Dealer=dealer()
    Dealer.card()
    print(f'The total ammount is {amount}')
    print()
    print("{0:-^200}".format('Dealer'))
    Dealer.display()
    Custumer=custumer()
    Custumer.card()
    Custumer.card()
    print()
    print("{0:-^200}".format('Custumer'))
    Custumer.display()
    def dis():
        clear()
        print(f'The total ammount is {amount}')
        print("{0:-^200}".format('Dealer'))
        Dealer.display()
        print()
        print("{0:-^200}".format('Custumer'))
        Custumer.display()
        
    while True:
        print()
        print()
        print()
        print("Enter 'H' for HIT or 'S' for stand")
        choice=input()
        if choice=='S':
            break
        elif choice!='H' and  choice!='S':
            print("invalid input")
            continue
        else:
            Custumer.card()
            dis()
        if Custumer.count>21:
            break
    if Custumer.count>21:
        print("Dealer Won")
        print("enter 'Y' for play again or 'N' to exit")
        b=input()
        if b=='N':
            break
        else:
            clear()
            continue
    Dealer.delete()
    while Dealer.count<=17:
        Dealer.card()
        dis()
    print()
    if Dealer.count>21 or Custumer.count>21:
        if Dealer.count>21:
            print("YOU won")
            amount+=2*bet
        else:
            print("Dealer Won")
    else: 
        if Dealer.count>Custumer.count:
            print("Dealer Won")
        elif Dealer.count==Custumer.count:
            print("Game draw")
            amount+=bet
        else:
            print("YOU won")
            amount+=2*bet
    print(f'The total ammount is {amount}')
    print("enter 'Y' for play again or 'N' to exit")
    b=input()
    if b=='N':
        break
    else:
        clear()
