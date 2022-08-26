import random

rights = int(input('How many credits do you give me for this game? '))

maximum = int(input('I need to find a number between 1 and which number, so what is the maximum value of the number range? '))

question_point = float(100/rights)

print('I have {} rights for this game.I will try to find between 1 to {}, you kept a number '.format(rights, maximum))

mininum = 0
go_on = True
while go_on:
   if rights > 0:
      computer_guess=random.randint(mininum ,maximum)
      guess=input('I guess it is {}, if it is true write (t), for high (h), for low (l): '.format(computer_guess))

      if guess == 't':
         print(f'I won, I guess, i got {100 -(100 - question_point * rights)} over 100 ')
         go_on = False

      elif guess == 'h':
         print('I see, You are a lucky pimp ')
         maximum = computer_guess
      
      
      elif guess=='l':
         print('What the fuck, i lost a right ')
         minimum = computer_guess

      else:
         print('Invalid character')
        
      
   
   else:
      print('Ok,I am not able to find number which you hold')
      go_on = False
      
   rights -= 1
