#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

    for name in names:
        name = name.strip()
        with open("Input/Letters/starting_letter.txt") as file_letter:
            letter_content = file_letter.read()
            with open(f'Output/ReadyToSend/{name}.txt', mode="w") as file_final:
                letter_content = letter_content.replace('[name]',f'{name}')
                file_final.write(letter_content)

