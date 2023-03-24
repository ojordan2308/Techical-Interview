from main import calculate_score, assign_letters, create_bag

def test_score_function_guardian():
    assert calculate_score('guardian') == 10

def test_score_function_box():
    assert calculate_score('box') == 12

def test_score_function_dog():
    assert calculate_score('dog') == 5

def test_letters_assigned_length():
    assert len(assign_letters()) == 7

def test_letters_assigned_type():
    assert isinstance(assign_letters(), str)
    
def test_letters_are_letters():    
    for letter in assign_letters():
        assert letter.isalpha()

def test_create_bag_size():
    assert len(create_bag()) == 98

def test_number_of_e():
    assert create_bag().count('E') == 12

def test_find_word():
    assert find_word('SADXXXX') == 'sad'

def test_no_word_found():
    assert find_word('EEEEEEE') == 'No word found'
