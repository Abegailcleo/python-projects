import random
import string

def Password_generator():
    
    print("--------------PASSWORD GENERATOR-----------------")
    length =password_length()
    result = Randomise(length)
    print("YOUR PASSWORD IS : ",result)






def password_length():
    
    while True:
        try:
    
            p_length = int(input("Enter the required length for your password:"))
            if p_length <= 0:
                print("Length required cannot be less or equal to zero,try again\n")
                continue
            else:
                return p_length
            
        except:
            print("Length can only be a numeric value ,please try again !\n")
    
    
def Randomise(length)  :
    
    number = string.digits
    punc = string.punctuation
    letters = string.ascii_letters
    all_char =number + punc +letters
    
    password = "".join(random.choice(all_char)for i in range(length))
    return password
    
    
if __name__ == "__main__":
    Password_generator()