

Q1 = """Which language has the more native speakers? 
a. English
b. Spanish
c. Chinese
d. French"""

Q2 = """What artist has the most streams on Spotify?
a. Drake
b. Kanye West
c. Michael Jackson
d. The Beatles
"""

Q3 = """When was Netflix founded? 
a. 1997
b. 2001 
c. 2009
d. 2015
"""

Q4 = """Which country invented tea?
a. Great Britain
b. Japan
c. India
d. China
"""

questions = {Q1: "c", Q2: "a", Q3: "a", Q4: "d"}


lives = 3
score = 0


def new_game():
    global lives, score
    for i in questions:
        while lives > 0:
            print(i)
            player_answer = input("What is the right answer: a, b, c or d ? ").lower()
            if player_answer == questions[i]:
                score += 1
                print("-----------------------------------")
                print(f"Good job! This is the right answer. Your score is {score}")
                print("-----------------------------------")
                break
            else:
                lives -= 1
                if score > 0:
                    score -= 1
                else:
                    ""
                print("-----------------------------------")
                print(f"Too bad! that is not the correct answer. You have {lives} live(s) left")
                print("-----------------------------------")
                if lives == 0:
                    print(f"You lose. Your final score is {score}")
                    break
        if score == 4:
            print(f"You answered every question correctly! Your final score is {score}")
            break


print("Welcome to our quizz!\nYou have 3 lives.")
print("------------------------")
new_game()


"""
score=0

for i in questions:
    while life > 0:
        def ask_the_question():
            for i in questions:
                print(i)
                player_answer = input("What is the right answer: a, b, c or d ? ").lower()
        
        def the_score():
            global score
            if player_answer == questions[i]:
                score += 1
                print("-----------------------------------")
                print(f"Good job! This is the right answer. Your score is {score}")
                print("-----------------------------------")
        break
            else:
                life -= 1
                if score > 0:
                    score -= 1
                else:
                    ""
                        print("-----------------------------------")
                        print(f"Too bad! that is not the correct answer, You have {life} life(s) left")
                        print("-----------------------------------")
                        if life == 0:
                            print(f"You lose. Your final score is {score}")
                            break
                if score == 4:
                    print(f"You answered every question correctly! Your final score is {score}")
                    break
"""