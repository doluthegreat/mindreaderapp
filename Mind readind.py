
print("Hello Welcome to Dolly mind games")
print("Enter yes or no where required. All responses in lower case")

playing = str(input("would you like to play: "))


if playing != "yes":
    print("Don't be scared it's just a mind game")
    quit()

else:
     name = input("Please enter your name: ")
     if name!= "jide":
         name1 = input("Jide enter your name: ")
         if name1 != ("jide"):
             print("BOY don't play with me")
             quit()
         print(name1.title() + " answer the following questions honestly after which I'll tell you what's on your mind haha")


gender = input("male or female: ")

if gender != "male":
    print("I feel you are not being honest the game has to end")
    print("game over!")
    quit()

print("great! I already knew your gender though :) ")
print(name.title() + " answer the following questions honestly after which I'll tell you what's on your mind haha")

yoruba_name = input("do you have other yoruba names: ")

if yoruba_name != "yes":
    print("LIE!!!")
    print("Answer the next question honestly ")


Yoruba_name = input("do any of the names have 'Oluwa', 'Olorun', 'Ayo': Enter a, b, or c respectively: ")
if Yoruba_name != "a":
    print("You were not honest ")
    quit()

if Yoruba_name == "a":
    print("Good now think of the names for five seconds ")
    print("Well done but you don't have to look up while thinking")
    done = input("Are you done? : ")
    if done == "yes":
        print("please hold on while I think... ")



Guess_names = ["Oluwademilade, Pablo;) ,Oluwasemilore, oluwagbenga, Oluwafikunayomi, Na ham na ham,Oluwafemi, "
               "Oluwasegun, Oluwalogo, Fiyinfoluwa : "]
for Guess in Guess_names:
    print(Guess)
    Guess_names = input("Are any of your names listed above; ")


if Guess_names == "yes":
    input("Okay do you like eggs: ")
    cakes = input("Do you like pancakes: ")
    if cakes != "yes":
        print("Wow interesting")
    are = input("Are you up to 6ft: ")
    if are == "yes":
        print("Hmm okay")
    print("now look at your left thumb")
    tip = input("Look again do you see anything at the tip: ")
    if tip!= "yes":
        print("Hmmm that leaves me with three options: ")
        print("Okay let's proceed")
    can = input("Final question. Can you remember anything that happened when you were two years old: ")
    if can!= "yes":
        print("wow that's insane")
        print("Anyways that does not affect the trick")
        print("You were a playful kid")
        print("Your Yoruba names remain OLUWAGBENGA, OLUWASEGUN and OLUWACASH ")
    else:
        print("That was quite easy ")
        print("Your Yoruba names are OLUWAGBENGA and OLUWASEGUN *LAUGHS HYSTERICALLY* ")
if Guess_names != "yes":
    print("Don't lie to me little " + name + " I've been doing this for years")

print("Thank you for playing I'd love your feedback! ")
