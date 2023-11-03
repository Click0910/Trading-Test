'''

["amor", "roma", "nadar", "andar", "martillo", "camila"]

'''

anagram_list = ["amor", "roma", "nadar", "andar", "martillo", "camila", "amigo", "imago", "life", "file", "lool"]

anagrams_words = {}

for word in anagram_list:

    sorted_string = ''.join(sorted(word))

    if sorted_string not in anagrams_words:

        anagrams_words[sorted_string] = [word]

    elif sorted_string in anagrams_words:

        anagrams_words[sorted_string].append(word)

print(anagrams_words)

