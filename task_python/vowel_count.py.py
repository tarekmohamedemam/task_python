def count_vowels(s):
    counter = 0
    vowels = "aeiou"
    for char in s:
        if char.lower() in vowels:
            counter += 1
    return counter