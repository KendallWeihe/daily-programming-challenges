import pdb

filename = "./words.txt"
f = open(filename, "r")

words = f.read().splitlines()

two_letter_words = []
for w in words:
    if len(w) == 2:
        two_letter_words.append(w)

longest_words = []
for w1 in two_letter_words:
    searching = True
    longer_words = [w1]
    while searching:
        temp_words = []
        for w2 in longer_words:
            for w3 in words:
                if (len(w2) == (len(w3) - 1)) and w2 in w3:
                    temp_words.append(w3)

        if temp_words != []:
            longer_words = temp_words
        else:
            longest_words.append(longer_words)
            searching = False

    # print longest_words

# print longest_words
max_length = ''
for w in longest_words:
    for w1 in w:
        if len(w1) > len(max_length):
            max_length = w1

# print max_length

all_longest_words = []
for w in longest_words:
    for w1 in w:
        if len(w1) == len(max_length) and w1 not in all_longest_words:
            all_longest_words.append(w1)

print "\n"
print "Longest words are:"
print all_longest_words
