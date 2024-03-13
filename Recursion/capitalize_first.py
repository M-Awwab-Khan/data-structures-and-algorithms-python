def capitalize_first(words: list) -> list:
    if len(words) == 0:
        return []
    return [words[0].title()] + capitalize_first(words[1:])

print(capitalize_first(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']