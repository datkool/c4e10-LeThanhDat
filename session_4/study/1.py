while True:

    data = input("Input: ")

    letter_counts = {}

    for letter in data:
        letter_counts[letter] = letter_counts.get(letter, 0) +1

        print(letter_counts)
