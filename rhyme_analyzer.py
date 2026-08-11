import pronouncing
import string

# Counts the number syllables in each word
def count_syllables(word):

    if not isinstance(word, str):
        raise TypeError("Word must be a string.")

    phonemes = pronouncing.phones_for_word(word)
    syllables = 0

    if not phonemes:
        syllables = count_missed_syllables(word)
    else:
       first_pronunc = phonemes[0].split(" ")
       syllables = sum(1 for phoneme in first_pronunc if phoneme[-1].isdigit())

    return syllables

# Counts the number of syllables in each line of words
def count_line_syllables(line):
    line = line.lower()
    words = line.split(" ")
    total = 0
    
    for word in words:
        cleanWord = word.strip(",.!?\"'()")
        total += count_syllables(cleanWord)
    
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
    if not isinstance(word, str):
        raise TypeError("Word must be a string")

    phonemes = pronouncing.phones_for_word(word)
    if not phonemes:
        return word
    else:
        return pronouncing.rhyming_part(phonemes[0])
    
# Determines if two words rhyme by returning true or false
def words_rhyme(word1, word2):
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Both words must be strings to be compared")
    return get_rhyming_part(word1) == get_rhyming_part(word2)

# Returns the rhyme pattern of the list of lines given
def rhyme_pattern(lines):

    if not isinstance(lines, list):
        raise TypeError("Input is not a list of lines.")

    memoryBank = {}
    pattern = []
    counter = 0
    
    for line in lines:
        if not isinstance(line, str):
            raise TypeError("The list needs to contain strings only.")
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
    print()
    print(count_syllables(""))
    print(count_syllables(None))
