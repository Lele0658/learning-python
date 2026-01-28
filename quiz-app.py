from string import ascii_lowercase

name = input("Enter your name: ")
print(f"Hello, {name}!")

QUESTIONS = {
    "When was Michael Jackson born": [
        "1958", "1960", "1955", "1962"
    ],
    "What was his debut solo album": [
        "Got to Be There", "Off the Wall", "Thriller", "Bad"
    ],
    "How many Grammys did he win in one night": [
        "8", "6", "10", "5"
    ],
    "What was the name of his famous dance": [
        "Moonwalk", "Smooth Criminal", "Beat It", "Billie Jean"
    ],
    "Which charity single did he co-write in 1985": [
        "We Are the World", "Heal the World", "Black or White", "Man in the Mirror"
    ],
    "What was the name of his pet chimpanzee": [
        "Bubbles", "Chimp", "Jackson Jr.", "Prince"
    ],
    "What was the title of his last studio album": [
        "Invincible", "Kingdom Come", "Thriller 2", "Bad 2"
    ],
    "What was the name of his famous glove": [
        "The Glove", "White Glove", "Magic Glove", "Jackson Glove"
    ],
    "In which year did he pass away": [
        "2009", "2008", "2010", "2011"
    ],
    "Which record label was he signed to for most of his career": [
        "Epic Records", "Sony Records", "Columbia Records", "Virgin Records"
    ],
    "What was the name of his 1982 album that became the best-selling album of all time": [
        "Thriller", "Bad", "Dangerous", "HIStory"
    ],
    "What was the name of his sister who is also a famous singer": [
        "Janet Jackson", "LaToya Jackson", "Rebbie Jackson", "Jackie Jackson"
    ],
    "What was the name of his ranch in California": [
        "Neverland Ranch", "Jackson Ranch", "Pop Ranch", "Michael Ranch"
    ],
    "Which Michael Jackson album had 6 number one hits in the same week": [
        "Bad", "Thriller", "Music and Me", "Off the Wall"
    ],
    "Which band was Michael Jackson a member of": [
        "The Jackson 5", "Jacksons", "The 5", "The Jacksons"
    ],
    "What's the name of his daughter": [
        "Paris", "Sarah", "Stacie", "Bianca"
    ],
}

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")