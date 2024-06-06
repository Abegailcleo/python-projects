def Calculation():
    
    
    
    while True:
        try :
            
            a = int(input('Input first number : '))
            
            b = int(input('Input second number: '))
            
            print(f"The result is : {operand(a,b)}")
            break
            
        except:
            print("invalid input , please try again!")   
            
            
            
            
def operand(a,b) :          
            while True:
                list_operands = ("+", "-", "*", "/")
                operation = input("Input operation (+,-,*,/) ")
                if operation not in list_operands:
                    print("Invalid operand,please try again!")
                    continue
                else:
                    result =perform_operation(a,b,operation)
                    if result is not None:
                        return result
                        
                    
                
                
            
def perform_operation(a, b, operation):
        if operation == "+":
            return addition(a, b)
        elif operation == "-":
            return subtraction(a, b)
        elif operation == "*":
            return multiplication(a, b)
        elif operation == "/":
            if b == 0:
                print("Cannot be divisible by 0, try again.")
                return None
            else:
                return division(a, b)
        else:
    
            return None          
                   
    
def addition(a,b):
    
    return a + b

def subtraction(a,b):
    
    return a - b


def multiplication(a,b):
    
    return a * b

def division(a,b):
    
    return a/ b
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ =="__main__":
    
    Calculation()
