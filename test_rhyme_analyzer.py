# import pronouncing
import pytest
from rhyme_analyzer import count_syllables, count_line_syllables, get_rhyming_part, words_rhyme, rhyme_pattern

def test_count_syllables():
    assert count_syllables("cat") == 1
    assert count_syllables("tryna") == 2
    assert count_syllables("bm") == 0

def test_count_syllables_invalid_type():
    with pytest.raises(TypeError):
        count_syllables(None)
    with pytest.raises(TypeError):
        count_syllables(8)

def test_count_line_syllables():
    assert count_line_syllables("I'm tryna vibe but the rhythm keeps flowin") == 11
    assert count_line_syllables(" I am a vibe") == 4

def test_get_rhyming_part():
    assert get_rhyming_part("vibe") == "AY1 B"
    assert get_rhyming_part("slatt") == "slatt"

def test_words_rhyme():
    assert words_rhyme("vibe", "bribe")
    assert not words_rhyme("vibe", "died")
    assert not words_rhyme("vibe", "slatt")
    assert words_rhyme("slatt", "slatt")

def test_rhyme_pattern():
    test = [
        "I saw a cat",
        "sitting on a mat",
        "next to a dog",
        "wearing a hat",
    ]
    test2 = [
        "I saw a cat",
        "just stay tryna",
        "sitting on a mat",
        "gotta stay finna",
    ]
    assert rhyme_pattern(test) == ['A', 'A', 'B', 'A']
    assert rhyme_pattern(test2) == ['A', 'B', 'A', 'C']