def append(char, sounds):
    if char.encode("utf-8") not in sounds:
        sounds.append(char.encode("utf-8"))
    return sounds

exceptions = [u':',u'ʰ', u'ʷ']
f = open('words_IPA.txt')

sounds = []

for line in f:
    word = line.decode("utf-8").strip()
    letter = 0
    while letter < len(word):
        if letter < len(word) - 1:
            if word[letter + 1] not in exceptions:
                char = word[letter]
                sounds = append(char, sounds)
                letter += 1
                
            else:
                char = word[letter] + word[letter + 1]
                sounds = append(char, sounds)
                letter += 2
                
        else:
            sounds = append(char, sounds)
            letter += 1
 
f.close()

sounds.sort()

for each in sounds:
    print each.decode('utf-8')
