import random

def main():
    
    
    play_words = ["rock","paper","scissors"]

    print("----------ROCK,PAPER,SCISSORS---------------\n")
    
    
    
    
    name = get_name()
    your_score = 0
    computer_score = 0
    
    while True:
       
        
        
        your_score, computer_score = play_game(name,play_words,your_score,computer_score)
        
        plays = True
        
        
        while plays:
                
                play_again = input("Would you like to play again ? ").lower()
                
                if play_again == "yes" or play_again == "y":
                    break
                    
                elif play_again == "no" or play_again == "n":
                    print("Goodbye !!")
                    exit()
            
                else:
                    print("Invalid answer,please try again!")
                    continue
                
    

def get_name():
    
    name = True
    
    while name:
        
        p_name = input("> Please input your name : \n")
        if p_name == "":
            
            print("Name cannot be an empty string,please enter a valid name")
            continue
            
        else :
            print(f">>   Hello ,{p_name} !!!!")
            
    
    
        return p_name
    
    
def play_game(name,play_words,your_score,computer_score)  :
    
       
        
        while True:
            
            
            choice = input("> Please enter rock ,paper or scissors: ").lower()
            if choice not in play_words:
                print("> Wrong choice,please try again")
                continue
            
          
            print('>> Your choice is :',choice)
            
            computer_choice = random.choice(play_words)
            
            print(f">> Computer choice: {computer_choice}\n")
            
            
                
                
                    
                    
            if choice == "rock" and computer_choice == "scissors":
                print(f">>>>   {name} you win    <<<<\n")
                your_score +=1
                
                
            elif choice == "scissors" and computer_choice == "rock":
                print(">>>>   Computer wins    <<<<\n")  
                computer_score +=1  
            elif choice == "rock" and computer_choice == "paper":
                print(f">>>>   {name} you win    <<<<\n")
                your_score +=1  
            elif choice == "paper" and computer_choice == "rock":
                print(">>>>   Computer wins    <<<<\n")
                computer_score +=1
                
            elif choice == "scissors" and computer_choice == "paper":
                print(f" >>>>  {name} you win    <<<<\n")
                your_score +=1
            elif choice == "paper"  and computer_choice == "scissors":
                print(">>>    Computer wins    <<<<\n")
                computer_score +=1
            else:
                choice == computer_choice
                print("~~~~~~Its a tie!~~~~~~\n")
                
            
               
            
            break
        
        
        print(f"Your score: {your_score}\nComputer score: {computer_score}\n")
        return your_score,computer_score   
            


       



            
   

    
if __name__ == "__main__":
    
    main()