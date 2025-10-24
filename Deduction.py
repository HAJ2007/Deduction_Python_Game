#----------------------------------------
#IMPORTS
#----------------------------------------
import random
import  time
#----------------------------------------
#SUBPROGRAM
#----------------------------------------
def starting(countss):
    if countss==0:#allows user to choose whether to output instruction
        print("ABOUT:\n  The purpose of the game is to deduce the correct number using clues provided\n CLUES:",
          "\n  HOT - correct number correct place\n  WARM -correct number wrong place\n  COLD: incorrect number\n", "WARNING:\n  The clues are not arranged respective to  position of number")
    elif countss>0:
        instructionC= input("if you want instructions enter\"Y\"if no enter \"N\"").upper()
        if instructionC =="Y":
             print("ABOUT:\n  The purpose of the game is to deduce the correct number using clues provided\n CLUES:",
          "\n  HOT - correct number correct place\n  WARM -correct number wrong place\n  COLD: incorrect number\n", "WARNING:\n  The clues are not arranged respective to  position of number")
        else:
            print("goodluck")
#-------------------------------------------------------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------------------------------------------------------  
def randomNum():
    numberToGuess=str( random.randint(1000,9999)) #Generating a random 4 digit number and converting it to string datatype to make comparisons easier as input always take string datatype
    #print (type(numberToGuess),numberToGuess)# testing to check if it ca properly converted. This section is to be commented out
    ListNumberGuess = []#Creating a list for easier comparison and randomization of clues
    for number in numberToGuess:#inserting individual digits to as individual items in list
        ListNumberGuess .append(number)
    #print(ListNumberGuess)#checkin is the numbers are being properly inserted. This line will be commented out
    return ListNumberGuess

#-------------------------------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------------------------------- 

def additional():#ONLY WORKS IN CERTAIN PLATFORMS THAT SUPPORT \r  
    print("\n\nGenerating Number")# makes it more interactive 
    text=(".....")
    for i in range(3):# this felt like not too long or short for repetition
        for q in range (len(text)+1):
            time.sleep(0.3)# Makes it appear to be generaing due to the delay
            print(text[:q+1], end="\r",flush=True)#allows the curser to move to the start and print
        print("     ",end="\r")# the print statement is longer than the max lenth of text so that no previous print values remain
    
#-------------------------------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------------------------------- 

def validation(userInput):# Checks if the input is valid before passing onto the next subprogram to ensure robustness
    x=False
    numbers=["0","1","2","3","4","5","6","7","8","9"] #all possible inputs 
    count=0
    if len(userInput) != 4:# if input is less that  cannot properly generate clues and program will crash
        x=True
    elif len(userInput) == 4:# if the input is not a number the program cannot compare in conditional loop so program crashes
        for char in userInput:
            if char not in numbers:
                count=count+1
        if count >= 1:
            x=True
    return x

#-------------------------------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------------------------------- 

def cluegeneration(uInput,randomNums,condition):#Generates clue
    clueList=[]
    R = None
    if not condition:
        for num in range(len(uInput)):
            if uInput[num]==randomNums[num]:
                clueList.append("HOT")
            elif uInput[num] in randomNums:
                clueList.append("WARM")
            elif uInput[num] not in randomNums:
                clueList.append("COLD")
    elif condition:# where the user is told the input is invalid
        print("invalid Input")
        R = "invalid"
    
    return clueList,R
    
#-------------------------------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------------------------------- 

def resultPerGuess(clues):
    c=False
    count2=0
    for clue in clues:
        if clue == "HOT":
            count2+=1
    if count2==4:
        print("You won")
        c=True
    else:
        y=clues.copy()# shuffle is none so for testing I am making a copy so original clues will not be affected. Can also be used for addition features 
        #like multiple mode where one is shuffle and other is not
        random.shuffle(y)
        
        print("your clues are",y)
    
    return c       
#----------------------------------------
#MAIN PROGRMA
#---------------------------------------
uInput2="Y"#Make the while loop run
counts=0#used tomake the program more user friendly
while uInput2 == "Y":
    starting(counts)
    numberList = randomNum()
    additional()
    userInput = input("Enter Your Guess")
    r_x=validation(userInput)
    r_clueList,r_R =cluegeneration(userInput,numberList,r_x)
    while r_R=="invalid":#asks for other input when previous input is not valid
        userInput = input("Enter Your Guess")
        r_x=validation(userInput)
        r_clueList,r_R =cluegeneration(userInput,numberList,r_x)

    condition2=resultPerGuess(r_clueList)


    while not condition2:# if the user have not won the game keeps on going 
        userInput = input("Enter Your Guess")
        r_x=validation(userInput)
        r_clueList,r_R =cluegeneration(userInput,numberList,r_x)
        while r_R=="invalid":
            userInput = input("Enter Your Guess")
            r_x=validation(userInput)
            r_clueList,r_R =cluegeneration(userInput,numberList,r_x)

        condition2=resultPerGuess(r_clueList)
        counts = counts+1#counts how may replyas have been done.Can be beneficial for score boards if more features are being added
    print("Do you want to play again:","\n  if yes enter \"Y\" ","\n  if no enter \"N\" ")
    uInput2 = input("Enter").upper()
    





