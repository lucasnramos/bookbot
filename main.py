def count_words(file):
    words = file.split()
    print(len(words))
    return len(words)

def count_chars(file):
    dict = {}
    normalized = file.lower()
    for char in normalized:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    print(dict)

    return dict

def count_alpha_chars(file):
    alpha_dict = {}
    normalized = file.lower()
    for char in normalized:
        if ord(char) >= 97 and ord(char) <= 122:
            if char in alpha_dict:
                alpha_dict[char] += 1
            else:
                alpha_dict[char] = 1
    return dict(sorted(alpha_dict.items(), key=lambda item: item[1],  reverse=True))

def report_file(file):
    content = file.read()
    word_count = count_words(content)
    word_dict = count_alpha_chars(content)
   
    # print the report
    # sort the dict reverse of count

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")

    for key in iter(word_dict):
        print(f"The '{key}' character was found {word_dict[key]} times")

    print("--- End report ---")
    

def main():
    with open('./books/frankenstein.txt') as f:
        # file_contents = f.read()
        report_file(f)
main()
