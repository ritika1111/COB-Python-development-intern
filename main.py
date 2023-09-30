'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
#list of 30 questions for quiz
Quiz_questions= [{"question":"National animal of India?", "answer":"Tiger"},{"question":"What is the colour of sky?", "answer":"Blue"},{"question":"What does KFC stands for?", "answer":"Kentucky Fried Chicken"},{"question":"What is the colour of snow?", "answer":"White"},{"question":"What is the world's fastest bird?", "answer":"The Peregrine Falcon"},{"question":"How many bones do we have in an ear?", "answer":"3"},{"question":"What is the 4th letter of Greek alphabet?", "answer":"Delta"},{"question":"Aureolin is a shade of what?", "answer":"Yellow"},{"question":"How many elements are in there periodic table?", "answer":"118"},{"question":"Who was the Ancient Greek God of the Sun?", "answer":"Apollo"},{"question":"What year was the United Nations established?", "answer":"1945"},{"question":"What artist has the most streams on spotify?", "answer":"Drake"},{"question":"Which Planet in the milkyway is the hottest?", "answer":"Venus"},{"question":"What phone company produced the 3310?", "answer":"Nokia"},{"question":"Where is the strongest human muscle located?", "answer":"Jaw"},{"question":"What planet is closest to the Sun?", "answer":"Mercury"},{"question":"How many dots appear on a pair of dice?", "answer":"42"},{"question":"What is a group of crows called?", "answer":" A Murder"},{"question":"How many colours are used in South African Flag?", "answer":"6"},{"question":"What is the only flag that does not have 4 sides?", "answer":"Nepal"},{"question":"What country drink the most coffee?", "answer":"Finland"},{"question":"Where did sushi originate?", "answer":"China"},{"question":"Animals that only eat plants are called?", "answer":"Herbivores"},{"question":"What is the nickname of the Academy Awards?", "answer":"The Oscars"},{"question":"Where did the olympics originate?", "answer":"Greece"},{"question":"People from Denmark are called?", "answer":"Danes"},{"question":"The Hawaiian islands were formed by?", "answer":"Volcanoes"},{"question":"Top number on a fraction called?", "answer":"Numerator"},{"question":"Planet outside our solar system called?", "answer":"Extrasolar"},{"question":"Nori is which type of sushi ingredient?", "answer":"Seaweed"}]

def quiz_question():
    random_question = random.choice(Quiz_questions)
    question_ask = random_question["question"]
    right_answer = random_question["answer"]
    
    player_answer = input(question_ask + "\nYour Answer: ").strip()
    
    if player_answer.lower() == right_answer.lower():
        print("Correct!\n")
    else:
        print(f"Sorry, the correct answer is {right_answer}.\n")

# forming loop for quiz
while True:
    input("Press Enter to start the quiz...")
    
    # Ask 30 random questions
    for i in range(30):
        quiz_question()
    
    try_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if try_again != "yes":
        break

print("Thank You ")
