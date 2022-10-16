
from requests import options
import random 



options_available=['rock','paper','scissors']


#user input
def from_user():
    while True:
        user_input= input(f'What do you want to choose {options_available}')
        user_input= user_input.lower()
        if user_input not in options_available:
            print("Enter choice is incorrect")
        else: 
            return user_input
    




#computer generated input
def from_computer():
    computer_input=random.choice(options_available)
    print(f"The computer choose {computer_input}")
    return computer_input
  


#Comparing between user and computer
def comparision(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "IT'S A TIE"
    elif ((user_choice=='rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock')):
        return 'You Won'
    else:
        return 'Computer Won'


#Score_Card= To keep track of the score
def score_card(result,uscore,cscore):
    val= {'result': result, 'user_score':uscore, 'computer_score':cscore}
    if result=="IT'S A TIE":
        print("{result} \n Your score is {user_score} \n Computer score is {computer_score}".format(**val))
       
    elif result=='You Won':
        val['user_score'] +=1
        print("{result} \n Your score is {user_score} \n Computer score is {computer_score}".format(**val))
      
    else:
        val['computer_score'] +=1
        print("{result} \n Your score is {user_score} \n Computer score is {computer_score}".format(**val))
     
    return  val['user_score'], val['computer_score']





def main():
    user_score=0
    computer_score=0  
    options= ['P', ' Q']


    while True:
        user= input("If you want to play press {}, to quit press {}".format(*options))
        user==user.lower()
       
        if user == 'p':
            user_choice=from_user()
            computer_choice=from_computer()
            result=comparision(user_choice,computer_choice)
            user_score, computer_score= score_card(result,user_score,computer_score)
        else:
            print(f"Your Score was {user_score} and Computer Score was {computer_score}")
            print("Thanks for playing")
            break


main()