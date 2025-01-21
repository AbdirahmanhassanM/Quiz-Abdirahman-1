import random

def quiz_game():
    questions = [
        {"question": "What is the capital city of France?", "options": ["Paris", "Lyon", "Marseille", "Nice"], "answer": "Paris"},
        {"question": "Which river runs through Paris?", "options": ["Seine", "Loire", "Rhine", "Danube"], "answer": "Seine"},
        {"question": "What is the national symbol of France?", "options": ["Eagle", "Rooster", "Lion", "Tiger"], "answer": "Rooster"},
        {"question": "What is the French national anthem called?", "options": ["La Marseillaise", "God Save the Queen", "Ode to Joy", "The Star-Spangled Banner"], "answer": "La Marseillaise"},
        {"question": "Which French king was known as the Sun King?", "options": ["Louis XIV", "Louis XVI", "Napoleon", "Henry IV"], "answer": "Louis XIV"},
        {"question": "What is the French term for the celebration of Bastille Day?", "options": ["Fête Nationale", "Fête de la Liberté", "Jour de France", "Liberté Fête"], "answer": "Fête Nationale"},
        {"question": "What is the most famous museum in France?", "options": ["Louvre", "Musée d'Orsay", "Pompidou Center", "Musée Rodin"], "answer": "Louvre"},
        {"question": "Which French region is known for producing Champagne?", "options": ["Bordeaux", "Provence", "Champagne", "Alsace"], "answer": "Champagne"},
        {"question": "What is the tallest structure in France?", "options": ["Eiffel Tower", "Mont Blanc", "Louvre Pyramid", "Notre Dame Cathedral"], "answer": "Eiffel Tower"},
        {"question": "What is the currency used in France?", "options": ["Euro", "Franc", "Pound", "Dollar"], "answer": "Euro"}
    ]

    random.shuffle(questions)

    print("Welcome to the France Quiz Game!")
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}! Let's begin the quiz.")

    score = 0
    total_questions = len(questions)

    for idx, q in enumerate(questions, start=1):
        # Shuffle options
        shuffled_options = q["options"][:]
        random.shuffle(shuffled_options)
        
        # Track the correct answer's new position
        correct_index = shuffled_options.index(q["answer"])
        
        print(f"\nQuestion {idx}: {q['question']}")
        for i, option in enumerate(shuffled_options, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

        if answer - 1 == correct_index:
            score += 1

    print(f"\n{player_name}, you completed the quiz!")
    print(f"Your final score is {score}/{total_questions}.")

    if score == 10:
        print("Incroyable, tu dois être français!")
    elif 8 <= score <= 9:
        print("Great job!")
    elif 5 <= score <= 7:
        print("Nice, but can be better.")
    elif 1 <= score <= 4:
        print("Better hit em' books.")
    else:
        print("Looks like you didn't get any correct answers. Better luck next time!")

if __name__ == "__main__":
    try:
        quiz_game()
    except KeyboardInterrupt:
        print("\nQuiz exited. Goodbye!")
