def reverse_string(s: str) -> str:
    if len(s) in [0, 1]:
        return s
    else:
        return reverse_string(s[len(s) // 2:len(s)]) + reverse_string(s[:len(s) // 2])
    
print(reverse_string('python'))