import pronouncing



def count_syllables(word):

    phonemes = pronouncing.phones_for_word(word)
    syllables = 0

    if not phonemes:
        # print("Slang word detected.")
        syllables = count_missed_syllables(word)
        # return None
    else:
       first_pronunc = phonemes[0].split(" ")
       syllables = sum(1 for phoneme in first_pronunc if phoneme[-1].isdigit())

    return syllables


def count_line_syllables(line):
    line = line.lower()
    words = line.split(" ")
    total = 0
    # missedWords = []
    
    for word in words:
        cleanWord = word.strip(",.!?\"'()")
        total += count_syllables(cleanWord)
        # curr = count_syllables(cleanWord)
        # if curr is None:
        #     missedWords.append(cleanWord)
        # else:
        #     total += curr
    
    return total

def count_missed_syllables(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    prev = None
    total = 0

    for letter in word:
        if letter == word[-1] and letter == 'e' and total != 0:
            prev = letter
            continue
        elif (letter in vowels or (letter == 'y' if letter != word[0] else False)) and prev not in vowels:
            total += 1

        prev = letter
        
    return total



if __name__ == "__main__":
    print(count_syllables("hello"))
    print(count_syllables("cat"))
    print(count_syllables("tryna"))
    print(count_line_syllables("I'm tryna vibe but the rhythm keeps flowin"))
    print(count_missed_syllables("cat"))      # expect 1
    print(count_missed_syllables("idea"))     # expect 2
    print(count_missed_syllables("like"))     # expect 1 (silent e)
    print(count_missed_syllables("tryna"))    # your real target word
    print(count_missed_syllables("flowin"))   # your real target word
    print(count_missed_syllables("the"))      # expect 1 (edge case we discussed)