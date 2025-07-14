#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Step 1: Open the letter template
with open(r"C:\Users\ADMIN\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Step 2: Open the names file
with open(r"C:\Users\ADMIN\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

# Step 3: Create personalized letters
for name in names:
    clean_name = name.strip()  # Remove newline characters
    personalized_letter = letter_contents.replace("[name]", clean_name)

    # Save to a new file
    with open(f"/Users/ADMIN/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{clean_name}.txt", mode="w") as completed_letter:
        completed_letter.write(personalized_letter)


# PLEASE NOTE THAT: This project **relies on the local file paths from the course materials** (names and templates), not from my own code structure.