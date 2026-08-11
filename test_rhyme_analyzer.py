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

def test_get_rhyming_part_invalid_type():
    with pytest.raises(TypeError):
        get_rhyming_part(None)
    with pytest.raises(TypeError):
        get_rhyming_part([])

def test_words_rhyme():
    assert words_rhyme("vibe", "bribe")
    assert not words_rhyme("vibe", "died")
    assert not words_rhyme("vibe", "slatt")
    assert words_rhyme("slatt", "slatt")

def test_words_rhyme_invalid_type():
    with pytest.raises(TypeError):
        words_rhyme(None, None)
    with pytest.raises(TypeError):
        words_rhyme("Hello", None)
    with pytest.raises(TypeError):
        words_rhyme(None, "Hi")

@pytest.fixture
def sample_lines_A():
    return [
        "I saw a cat",
        "sitting on a mat",
        "next to a dog",
        "wearing a hat",
    ]

@pytest.fixture
def sample_lines_B():
    return [
        "I saw a cat",
        "just stay tryna",
        "sitting on a mat",
        "gotta stay finna",
    ]
@pytest.fixture
def sample_lines_C():
    return [
        "I saw a cat",
        "just stay tryna",
        ["hello"],
        "gotta stay finna",
    ]
@pytest.fixture
def sample_lines_D():
    return [
        "I saw a cat",
        123,
        "sitting onn a mat",
        "gotta stay finna",
    ]


def test_rhyme_pattern(sample_lines_A, sample_lines_B):

    assert rhyme_pattern(sample_lines_A) == ['A', 'A', 'B', 'A']
    assert rhyme_pattern(sample_lines_B) == ['A', 'B', 'A', 'C']

def test_rhyme_pattern_invalid_types(sample_lines_C, sample_lines_D):
    with pytest.raises(TypeError):
        rhyme_pattern(None)
    with pytest.raises(TypeError):
        rhyme_pattern(sample_lines_C)
    with pytest.raises(TypeError):
        rhyme_pattern(sample_lines_D)