def count_words(book_contents):
    split_list = book_contents.split()
    word_count = 0
    for i in split_list:
        word_count += 1
    return word_count

def count_chars(book_contents):
    chars_dict = {}
    lower = book_contents.lower()
    for char in lower:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def report (chars_dict):
    chars_list = []
    def sort_on(dict):
        return dict["num"]
    for char in chars_dict:
        char_dict = {"char": char, "num": chars_dict[char]}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list