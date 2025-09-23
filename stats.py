def count_words(text):
    return len(text.split())


def sort_on(items):
    return items["num"]

def count_characters(text):
    seen = {}
    list_of_char_num = []
    for letter in text.lower():
        if letter in seen:
            seen[letter] += 1
        else:
            seen[letter] = 1 #start at 1 if first time seeing
    for ch, num in seen.items():
        if ch.isalpha():
            list_of_char_num.append({"char":ch, "num":num})
    list_of_char_num.sort(reverse=True, key=sort_on)
    return list_of_char_num