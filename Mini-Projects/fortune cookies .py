import random

lucky = random.randint(1,100)

fourtune = random.randint(1,10)

fourten_text = ""

if fourtune == 1:
    fourtune_text = "you will get a dog!" 
if fourtune == 2:
    fourtune_text = "you will get a bear!" 
if fourtune == 3:
    fourtune_text = "you will have a baby!"  
if fourtune == 4:
    fourtune_text = "you will get a pen!" 
if fourtune == 5:
    fourtune_text = "you will get a high score!" 
if fourtune == 6:
    fourtune_text = "you will have a great day!" 
if fourtune == 7:
    fourtune_text = "you will win the lottery!" 
if fourtune == 8:
    fourtune_text = "you will dance tonight!"
if fourtune == 9:
    fourtune_text = "you will have a nice day!" 
if fourtune == 10:
    fourtune_text = "you will work hard and succeed!"  
         

print(f"{fourtune_text} your lucky number is: {lucky} ")