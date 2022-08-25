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
        input1 = input("Please Enter Ethnicity ")
        input2 = input("Please Enter Person name ")
        input3 = input("Please Enter Noun ")
        input4 = input("Please Enter Noun ")
        input5 = input("Please Enter type of food ")
        input6 = input("Please Enter adjective ")
        input7 = input("Please Enter Plural Noun ")
        input8 = input("Please Enter noun ")
        input9 = input("Please Enter number ")
        input10 = input("Please Enter shape ")
        input11 = input("Please Enter food ")
        input12 = input("Please Enter food ")
        input13 = input("Please Enter number ")
      
        print("Pizza was invented by a " + input1 +
                "chef named " + input2 + ". \nTo make a pizza you need to " + 
                "take a lump of " + input3 + ",and make a thin, round " + 
                "" + input4 + ".\n Then you cover it with " + 
                "" + input5 + " sauce, " + input6 + " cheese, and fresh " + 
                "chopped " + input7 + ".\n Next you have to bake it in a very " + 
                "hot " + input8 + ".\n When it is done, cut into " + input9 + " " + input10 + ".\n " + 
                "Some kids like " + input11 + " pizza the best, but my favorite is " + 
                "the " + input12 + " pizza. \nIf I could, I would eat pizza " + input13 + " times " + 
                "a day!")
    elif scriptChoice == "3": 
         input1 = input("Please Enter Color ")
         input2 = input("Please Enter Superlative ending is est ")
         input3 = input("Please Enter adjective ")
         input4 = input("Please Enter body part plural")
         input5 = input("Please Enter body part")
         input6 = input("Please Enter noun ")
         input7 = input("Please Enter animal plural")
         input8 = input("Please Enter adjective ")
         input9 = input("Please Enter adjective ")
         input10 = input("Please Enter adjective ")

         print("The " + input1 + 
               " Dragon is the " + input2 + 
               " Dragon of all. It has " + input3 + " " +  input4 +  
               " , and a  " + input5 + 
               " shaped like a  " + input6 + 
               ". It loves to eat  " + input7 + 
               ", although it will feast on nearly anything. It is  " + input8 + 
               " and  " + input9 + 
               ". You must be  " + input10 + 
               " around it, or you may end up as it`s meal!")
    elif scriptChoice == "4":
        input1 = input("Please Enter Noun ")
        input2 = input("Please Enter Noun ")
        input2AndAHalf = input("Please Enter Noun ")
        input3 = input("Please Enter occupation ")
        input4 = input("Please Enter Verb ")
        input5 = input("Please Enter Place ")
        input6 = input("Please Enter Verb ending in ED ")
        input7 = input("Please Enter Noun ")
        input8 = input("Please Enter Verb ending in ING ")
        input9 = input("Please Enter Noun plural ")
        input10 = input("Please Enter Noun ")
        input11 = input("Please Enter Emotion ")

        print("It was during the battle of  " + input1 + 
               " when I was running through a  " + input2 + 
               " when a  " + input2AndAHalf + 
               " went off right next to my platoon. Our  " + input3 + 
               " yelled for us to  " + input4 + 
               " to the nearest " + input5 + 
               " we could find. When we got to the " + input5 + 
               " we " + input6 + 
               " to start a fire. As we were starting the fire the enemy saw the " + input7 + 
               " from the fire and started " + input8 + 
               " " + input9 + 
               " at us. we all quickly ducked behind the " + input10 + 
               " at the " + input5 + 
               " and returned fire. we quickly eliminated the enemy and were " + input11 + 
               " that we had won the battle.")
    elif scriptChoice == "q":
         print("Program closing...")
         break
    else:
         print("sorry that was not a valid choice type a number between 1 and 4 or q to quit")

