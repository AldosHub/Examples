prompt = "I need to see your ID"
prompt += "\nHow old are you? "

while True:
    if input(prompt) >= '21':
        print("you may buy alcohol")
        break #NO BREAK HERE WILL CALL TO PROMPT INFINITE TIMES#
    else: 
        print('You may not buy alcohol')
        break

age = input("How old are you? ")

while True:
    if age >= '21':
        print("you may buy alcohol") #NO BREAK HERE WILL PRINT INFINITY#
    else: 
        print('You may not buy alcohol')
        break

