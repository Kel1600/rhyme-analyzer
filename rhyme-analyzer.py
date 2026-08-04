import pronouncing
import string

# Counts the number syllables in each word
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

# Counts the number of syllables in each line of words
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

# Counts the number of syllables for any word not in the CMU dictionary
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

# Gets the rhyming part of a word
def get_rhyming_part(word):
    phonemes = pronouncing.phones_for_word(word)
    if not phonemes:
        print("Phonemes not found for slang word.")
        return None
    else:
        return pronouncing.rhyming_part(phonemes[0])
    
# Determines if two words rhyme by returning true or false
def words_rhyme(word1, word2):
    rhyme1, rhyme2 = get_rhyming_part(word1), get_rhyming_part(word2)

    if rhyme1 and rhyme2:
        if rhyme1 == rhyme2:
            return True
    else:
        print("One or both of the words not available in CMU dictionary.")
        return None

    return False

def rhyme_pattern(lines):

    memoryBank = {}
    pattern = []
    counter = 0
    
    for line in lines:
        line = line.lower()
        lastWord = line.split(" ")[-1].strip(",.!?\"'()")
        rhyme = get_rhyming_part(lastWord)
        if rhyme in memoryBank:
            pattern.append(memoryBank[rhyme])
        else:
            memoryBank[rhyme] = string.ascii_uppercase[counter]
            pattern.append(memoryBank[rhyme])
            counter += 1
        
    return pattern
        



if __name__ == "__main__":
    print(count_syllables("hello"))
    print(count_syllables("cat"))
    print(count_syllables("tryna"))
    print(count_line_syllables("I'm tryna vibe but the rhythm keeps flowin"))
    # print(count_missed_syllables("cat"))      # expect 1
    # print(count_missed_syllables("idea"))     # expect 2
    # print(count_missed_syllables("like"))     # expect 1 (silent e)
    # print(count_missed_syllables("tryna"))    # your real target word
    # print(count_missed_syllables("flowin"))   # your real target word
    # print(count_missed_syllables("the"))      # expect 1 (edge case)
    # print(get_rhyming_part("cat"))
    # print(get_rhyming_part("hat"))
    # print(get_rhyming_part("hello"))
    # print(get_rhyming_part("flow"))
    # print(get_rhyming_part("tryna"))
    print(words_rhyme("cat", "hat"))
    print(words_rhyme("cat", "dog"))
    print(words_rhyme("tryna", "hat"))
    test = [
        "I saw a cat",
        "sitting on a mat",
        "next to a dog",
        "wearing a hat",
    ]
    print(rhyme_pattern(test))