with open('sample.txt', 'r') as file:
    anagrams = {}

    for line in file:
        word = line.strip()
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    for key, value in anagrams.items():
        formatted_output = f"{' '.join(value)}"
        print(formatted_output)
