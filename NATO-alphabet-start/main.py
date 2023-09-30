
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = {row['letter']: row['code'] for (index,row) in df.iterrows()}

def generate_phonetic():
    user_word = input("Give me a word to code: ").upper()
    try:
        code_word = [codes[letter] for letter in user_word]
    except KeyError:
        print("Please enter a word")
        generate_phonetic()
    else:
        print(code_word)

generate_phonetic()