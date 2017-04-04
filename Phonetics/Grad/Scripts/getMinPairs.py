#coding:utf8
def split_word(word):
    letter = 0
    chars = []
    while letter < len(word):
        if letter < len(word) - 1:
            if word[letter + 1] not in exceptions:
                chars.append(word[letter])
                letter += 1
            else:
                chars.append(word[letter] + word[letter + 1])
                letter += 2        
        else:
            chars.append(word[letter])
            letter += 1

    return chars

def get_pairs(lines):
    pairs = {}
    for word1 in range(len(lines)):
        for word2 in range(len(lines)):                     
            if not word1 == word2:                                      #avoid considering word being a minimal pair of itself
                if len(lines[word1]) == len(lines[word2]):              #consider only words of the same length
                    shared = []                                         #IPA characters that are shared between word1 and word2
                    not_shared = []                                     #IPA characters  that are shared between word1 and word2
                    for char in range(len(lines[word1])):
                        if lines[word1][char] == lines[word2][char]:    #check to see if chars in position of word 1 and word 2 match
                            shared.append(lines[word1][char])           #if they match then append to a "shared characters" list
                        else:                                           
                            if lines[word1][char] not in not_shared:    
                                not_shared.append(lines[word1][char])   #if they do not match then append both mismatching characters to a "not shared characters" list
                                not_shared.append(lines[word2][char])   
                    not_shared.sort()
                    if len(shared) == len(lines[word1]) - 1:            #if every letter except one is shared between word 1 and word 2
                        pair = not_shared[0] + ", " + not_shared[1]
                        if pair not in pairs:                           #check to see if a list for a minimal pair already exists
                            pairs[pair] = []                            #if that list does not exist yet then create an empty list
                        if ''.join(lines[word1]) not in pairs[pair]:    #check to see if word 1 exists in list for that pair
                            pairs[pair].append(''.join(lines[word1]))   #if word 1 does not exist yet then append word 1
                        if ''.join(lines[word2]) not in pairs[pair]:    #check to see if word 2 exists in list for that pair
                            pairs[pair].append(''.join(lines[word2]))   #if word 2 does not exist yet then append word 2

    return pairs                            

exceptions = [u':',u'ʰ',u'ʷ']
f = open('words_IPA.txt')

lines = []

for line in f:
    word = line.decode("utf-8").strip()
    lines.append(split_word(word))

pairs = get_pairs(lines)

for i in pairs:
    to_print = ''
    to_print += i + '\t'
    for word in range(len(pairs[i])):
        to_print += pairs[i][word]
        if word < len(pairs[i]) - 1:
            to_print += '\t'
    print to_print
