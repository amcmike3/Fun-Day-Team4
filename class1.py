scriptChoice = ""

while scriptChoice != "q":
    scriptChoice = input("Please choose script 1-4 or q to quit")

    if scriptChoice == "1":
        print("This Mad-lib is called Can We Go Home Now?")
        input1 = input("Please Enter Adjective ")
        input2 = input("Please Enter Noun-Plural ")
        input3 = input("Please Enter silly nickname ")
        input4 = input("Please Enter Verb-past tense ")
        input5 = input("Please Enter a Place plural")
        input6 = input("Please Enter silly nickname ")
        input7 = input("Please Enter Noun ")
        input8 = input("Please Enter Verb-pastense ")
        print("The music roaring out of the speakers was loud and " + input1 + 
              ". Why did I agree to come with them here? \n" + 
              "My two sisters were dancing and singing along with the musicians on stage. " +
              "At least they were having fun, right? \n" +
              "Me being the only boy in our small family, " +
              "I was expected to do these kinds of things with my " + input2 + 
              ", even though I absolutely HATED these kinds of things! \n" +
              "I was practically dragged to " + input5 + " against my will. \n" +
              "I looked over to my older sister" +
              ", Katie, and whispered into her ear, " + input3 +
              " When can we leave? \nI'm getting bored She looked my way and shrugged, " +
              "as if she didn't know. Ask Zoe, after all it was her idea in the first place Katie said shortly after. \n" +
              "I nodded and " + input4 + 
              " my way in the crowd of people, the exact reason I hate going to these kinds of things, " +
              "looking for my younger sister, Zoe. \nWhen I finally found her I tapped her shoulder. " +
              "She turned around and looked into my green eyes Why aren't you having fun, Kyle She asked. \n" +
              "Because I don't really like going to " + input5 + 
              ". Can we go home now I " + input6 +
              ". \nZoe waved a finger at me saying, One more " + input7 + 
              ", and then we can leave I was grateful to hear this, since I wanted to leave as soon as possible. \n" +
              "I walked back through the crowd to tell Katie the details on our leaving time. Man, I was so " + input8 +  "to leave!")
    elif scriptChoice == "2":
        print("FIX ME")
    elif scriptChoice == "3":
        print("FIX ME")
    elif scriptChoice == "4":
        print("FIX ME")
    elif scriptChoice == "q":
        print("Program closing...")
        break
    else:
        print("sorry that was not a valid choice type a number between 1 and 4 or q to quit")

