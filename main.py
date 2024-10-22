import re # python module for regular expressions

def capitalize_sentences (filename):
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

        # this is self explanatory
        capitalized_sentences.append(sentence)

    result = ' '.join(capitalized_sentences) # add spaces between sentences
    return result

# change the filename variable to fit your needs
# filename = input('Enter file name after adding it to this directory: ')
filename = 'test.txt' # hardcoded filename, u can change
try:
    with open(filename) as file:
        print ('ORIGINAL FILE: \n' + file.read())
        print('NEW FILE: \n' + capitalize_sentences(filename))
    # using "with open" will close the file automatically
except FileNotFoundError:
    print("That file was not found")
except Exception:
    print("Something went wrong:(")
