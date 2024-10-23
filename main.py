import re # python module for regular expressions

def capitalize_sentences (filename, new_file):
    # open file for reading
    with open(filename, 'r') as file:
        words = file.read()

    sentences = re.split(r'(?<=[.!?])\s+', words) # split by punctuation
    capitalized_sentences = []

    for sentence in sentences:
        # capitalizes sentence 
        sentence = sentence.capitalize()

        # capitalizes standalone i's with teh \b bounds
        sentence = re.sub(r'\bi\b', 'I', sentence)

        sentence = re.sub(r'\bi\b|\bi\'\w+', lambda match: match.group(0).capitalize(), sentence) # contractions

        # names - add more if you want
        sentence = re.sub(r'\bob\b', 'Bob', sentence)

        # this is self explanatory
        capitalized_sentences.append(sentence)

    result = ' '.join(capitalized_sentences) # add spaces between sentences

    with open(new_file, 'w') as new_file:
        new_file.write(result)
    return result


# change the filename variable to fit your needs
# filename = input('Enter file name after adding it to this directory: ')
# run in terminal if you want to be able to enter input
# otherwise, just hard-code your filename 
filename = input('Enter the name of your file after moving it to this directory (.txt not included): ')
new_file = input('What do you want the new file to be named?: ')
try:
    with open(filename) as file:
        new_text = capitalize_sentences(filename, new_file)
    # using "with open" will close the file automatically
except FileNotFoundError:
    print("That file was not found")
except Exception:
    print("Something went wrong:(")
