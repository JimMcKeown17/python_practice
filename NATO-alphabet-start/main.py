student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # print(row['student'])
    # print(row['score'])
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = {row['letter']: row['code'] for (index,row) in df.iterrows()}
print(codes)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Give me a word to code: ").upper()

code_word = [codes[letter] for letter in user_word]
print(code_word)
# code_word = []
# for letter in user_word:
#     code_word.append(codes[letter])

print(code_word)