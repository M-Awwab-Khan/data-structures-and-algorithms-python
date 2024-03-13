def capitalize_words(words: list) -> list:
    if len(words) == 0:
        return []
    return [words[0].upper()] + capitalize_words(words[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalize_words(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']