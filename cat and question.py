print("Hello human! I will ask you some questions to get to know you.")
print('What is your name?')
myName = input()
print('It is nice to meet you, ' + myName)
nummyname = len(myName)
print('Your name has this many characters:')
print (nummyname)
print('How old are you?')
myage = input()
print('Wow! That is ' + str(100 - int(myage)) + ' years away from death, assuming you die at 100!')
print('What is your favorite food?')
favfood = input()
print("EW!! " + favfood + " is gross!!")
print("Do you have a cat?")
cattruth = input()
if cattruth == 'yes':
    print("What is your cat's name?")
else:
    print("GTG SORRY! I only like humans with cats!")
catname = input()
catlove = float(input('On a scale of 1-10, how much do you love ' + catname + " ?"))
if catlove > 10:
    print("You can't possibly love " + catname + " that much!")
else:
    print("Since you don't really love " + catname + ", you might as well kill " + catname + ", " + myName + ".")
print ("Will you kill " + catname + "?")
murder = input()
if murder == 'yes':
       print("I'm calling the police!!")
else:
    print ("Good call, " + myName + "!")
print("Goodbye, " + myName + "! I'll see you and " + catname + " by the litterbox!")
