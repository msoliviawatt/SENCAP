import re  # python module for regular expressions

def capitalize_sentences(filename, new_file):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # for preserving emojis 
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F" # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+", flags=re.UNICODE
    )

    emoji_matches = emoji_pattern.findall(text)
    placeholders = [f"{{EMOJI_{i}}}" for i in range(len(emoji_matches))]
    for placeholder, emoji in zip(placeholders, emoji_matches):
        text = text.replace(emoji, placeholder)

    # preserve delimiters and whitespace while splitting
    sentences = re.split(r'(?<=[.!?])(\s+)', text)
    capitalized_sentences = []

    for sentence in sentences:
        if sentence.strip():
            sentence = sentence[0].upper() + sentence[1:]

            # standalone 'i' and 'i' in contractions
            sentence = re.sub(r'\bi\b', 'I', sentence)
            sentence = re.sub(r"\bi\b|\bi'\w+", lambda match: match.group(0).capitalize(), sentence)

            # days of the week
            for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                sentence = re.sub(rf'\b{day}\b', day.capitalize(), sentence)

            # months
            for month in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
                sentence = re.sub(rf'\b{month}\b', month.capitalize(), sentence)

        capitalized_sentences.append(sentence)

    result = ''.join(capitalized_sentences)

    # replace placeholders with original emojis
    for placeholder, emoji in zip(placeholders, emoji_matches):
        result = result.replace(placeholder, emoji)

    # write to new file 
    with open(new_file, 'w', encoding='utf-8') as new_file:
        new_file.write(result)
    
    return result

filename = input('Enter the name of your file (without .txt extension): ') + '.txt'
new_file = input('What do you want the new file to be named (without .txt extension)?: ') + '.txt'

try:
    new_text = capitalize_sentences(filename, new_file)
    print("Capitalized file created successfully.")
except FileNotFoundError:
    print("That file was not found.")
except Exception:
    print("Something went wrong :(")
