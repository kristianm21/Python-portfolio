#Nickname
#Trying to find nicknames
def villain():
    print("Hello, would you like to know what horror movie villain you are? Just answer these simple questions to find out!")

    being=input("Would you rather be a supernatural being, or a mortal being?")
    if being=="supernatural":
        type=input("Scary! Would you consider as a person who loves the classics (type classic) or an urban legend lover(type urban)?")
        if type=="classic":
            attitude=input("Who doesn't love a classic? Are you the humorous type or silent type?")
            if attitude=="humorous":
                print("You embody the spirit of freddy krueger, a classic 80's villain people who attacks teens in their dreams, and jokes at them while doing so")
            if attitude=="silent":
                print("You are definitely Michael Myers. A well known classic, you silently stalk your victims using teleportation until you attack!")
        if type=="urban":
            fear=input("OMG! Do you grow in power the more people fear you(type fear), or the more they believe in your existence (type believe)?")
            if fear=="fear":
                print("You are Pennywise the dancing clown. An urban legend in the town of Derry, you feed off of childrens fears by turning into their worst nightmares")
            if fear=="believe":
                print("You are the notorious Candyman. Your reputation precedes you, and as people believe in you more and more, your powers grow.")
    if being=="mortal":
        motive=input("You can still be just as deadly! As a killer, would you have a motive (type motive), or are you just a straight psycho (type psycho)?")
        if motive=="motive":
            why=input("Why do you do it then? Is the reason for killing personal(type personal), or do you kill your victims so you can eat them(type eat)?")
            if why=="personal":
                print("Clearly, you are a ghostface killer. You are a mortal being with a very personaly reason for killing your victims.")
            if why=="eat":
                print("Of course, you're hannibal lector! Although you are a human, you also have a taste for humans, and oftentimes kill them to eat them.")
        if motive=="psycho":
            time=input("Crazy! Are you more of a modern psycho, or a very old-fashioned psycho?")
            if time=="modern":
                print("You are the insane Patrick Batemen! You are a modern day human psychopath who kills for fun.")
            if time=="old-fashioned":
                print("You are the crazed Norman Bates. You lived to kill in the 60's. Why? No reason!")
    print("Thank you for playing!")

villain()
