# The Mood Checker

"""
happy = "It is great to see you happy!"
nervous = "Take a deep breath 3 times."
sad = "Cheer up. You will do better the next time."
excited = "Did something good happened to you? Your seem restless."
relaxed = "Lets use our break to calm down."
"""

my_question = "In which mood are you right know?"
print(my_question)
mood = input("")


if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Cheer up. You will do better the next time.")
elif mood == "excited":
    print("Did something good happened to you? Your seem restless.")
elif mood =="relaxed":
    print("Lets use our break to calm down.")
else:
    print("i don´t recognize this mood")
