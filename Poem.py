from time import sleep
import sys


name = input ("Here is Overlook Hotel. I am Jack Torrence, caretaker here.\
               \nI've been writing here for 5 months. You'd better not distract me.\
               \nWhat's your name?")

boy = {("boy"), ("man"), ("male")}
girl = {("girl"), ("woman"), ("female")}

while True:
    gender = input ("What's your gender?")
    if gender in boy:
    	genderend = ("boy")
    	break

    elif gender in girl:
    	 genderend = ("girl")
    	 break

    else:
    	print ("What do you mean?")
    	continue


writing = input ("Do you want to read my work?")
if writing != ("yes"):
   print ("Get the F out of here. Do not interupt me again!")
   sys.exit()

print (".")
sleep(0.5)
print (".")
sleep(0.5)
print (".")
sleep(0.5)
    
waittime = 70
done = 0
while waittime is not done:
	print ("All work and no play makes" +
       " " + name + " " + "a dull" + " " + genderend)
	sleep(0.5)
	waittime -= 1

