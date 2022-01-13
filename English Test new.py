from random import shuffle


def start():
    """
    Choose English to Korean test or Korean to English test.
    """
    begin = input("1. English to Korean\n2. Korean to English\n")
    if begin == "1":
        read_words(1)
    elif begin == "2":
        read_words()


def read_words(type=2):
    """
    Returns a dictionary of day to a dictionary of word-meaning pairs from
    "Words.txt".
    """
    word_data = dict()
    with open("Words.txt", "r", encoding="utf-8") as file:
    # with open("Words.txt", "r") as file:
        if type == 1:
            for line in file:
                line = line.strip()
                try:  # line contains a day
                    day = int(line)
                    word_data[day] = dict()
                except:  # line contains a word-meaning pair
                    word, meaning = line.split(" ", 1)
                    word, meaning = meaning, word
                    word_data[day][meaning] = word

        elif type == 2:
            for line in file:
                line = line.strip()
                try:  # line contains a day
                    day = int(line)
                    word_data[day] = dict()
                except:  # line contains a word-meaning pair
                    word, meaning = line.split(" ", 1)
                    word_data[day][meaning] = word


    return word_data

data = read_words()

def check_word(word, answer):
    """
    Returns True if word can be accepted as an answer, False otherwise.
    """
    return word == answer

def test_day(pairs, pass_rate=90):
    """
    Use data to test words for a corresponding day.
    """
    # pairs is a word-meaning dictionary
    meanings = list(pairs.keys())
    correct_words = dict()
    incorrect_words = dict()
    shuffle(meanings)
    for i, meaning in enumerate(meanings, start=1):
        # Get user input
        user_answer = input(f"{i}. {meaning}:")
        correct_answer = pairs[meaning]
        if user_answer == correct_answer:
            correct_words[f"{meaning}"] = pairs[meaning]
            print("Correct\n")
        elif user_answer == 'exit':
            main()
        else:
            incorrect_words[f"{meaning}"] = pairs[meaning]
            print(f"Wrong\nThe answer is {correct_answer}\n")
    report(pairs, correct_words, incorrect_words, pass_rate)

    while True:
        choice = input("1. Retry wrong words\n2. Retry another day\n3. Exit\n")
        if choice == "1":
            test_day({meaning: pairs[meaning] for meaning in incorrect_words})
            return
        elif choice == "2":
            main()
            return
        elif choice == "3":
            return

def test_days(days):
    """
    It makes several days in one test.
    """
    pairs = dict()
    for i in days:
        pairs.update(data[int(i)])
    test_day(pairs)

def report(pairs, correct_words, incorrect_words, pass_rate):
    """
    Report the test result.
    """
    num_correct = len(correct_words)
    num_incorrect = len(incorrect_words)
    num_total = num_correct + num_incorrect
    answer_rate = num_correct / num_total * 100
    if answer_rate == 100:
        print("Perfect!")
    elif answer_rate >= pass_rate:
        print("Pass")
        print(f"{num_correct}/{num_total}\nThe Answer Rate is {answer_rate}%")
        print(f"맞춘 단어들 : {correct_words}\n")
        print(f"틀린 단어들 : {incorrect_words}")
    else:
        print("Fail")
        print(f"{num_correct}/{num_total}\nThe Answer Rate is {answer_rate}%")
        print(f"맞춘 단어들 : {correct_words}\n")
        print(f"틀린 단어들 : {incorrect_words}")

def main():
    """
    Choose only one day test or several days in one test.
    """
    while True:
        day = input("\nDay:")
        try:
            day = int(day)
            test_day(data[day])
        except:
            days = day.split(', ')
            test_days(days)

main()

start()