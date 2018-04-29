# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Syed Zain Zafar
# MarkUs Login: zafarsy4

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''
    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''

    # Return int value which is sum of the number of times word has occured
    # in puzzle after the puzzle has gone through all possible rotations.
    return((lr_occurrences(puzzle, word)) +
           (lr_occurrences((rotate_puzzle(puzzle)), word)) +
           (lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word)) +
           (lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle
                                                       (puzzle))), word)))


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> (bool)

    >>> in_puzzle_horizontal(PUZZLE1, 'brian')
    False

    >>> in_puzzle_horizontal('zain\npain\nlame', 'ni')
    True

    >>> in_puzzle_horizontal('dan\npan', 'an')
    True

    >>> in_puzzle_horizontal('dan\npan', 'ran')
    False

    Return if word is found horizontally in puzzle or not.
    If word occurs horizontally in puzzle (in one or both horizontal
    directions), return 'True'. If not, return 'False'.
    Only two directions are counted as occurences:
    left-right and right-left or both.
    '''
    # check if word occurs in puzzle, horizontally.
    # horizontal_occurences is the sum of left-right and right-left occurrences
    # of word in puzzle.
    horizontal_occurences = (
        (lr_occurrences(puzzle, word)) +
        (lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word)))

    # check if word occurs in puzzle, vertically.
    # vertical_occurences is the sum of top-bottom and bottom-top occurrences
    # of word in puzzle.
    vertical_occurences = (
        (lr_occurrences((rotate_puzzle(puzzle)), word)) +
        (lr_occurrences(rotate_puzzle(rotate_puzzle
                        (rotate_puzzle(puzzle))), word)))

    # See if word occurs in puzzle horizontally, by checking if horrizontal
    # occurrences for word in puzzle is one or more and if vertical occurrences
    # are 0.
    return((horizontal_occurences >= 1) and (vertical_occurences == 0))


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> (bool)

    >>> in_puzzle_vertical(PUZZLE1, 'brian')
    False

    >>> in_puzzle_vertical('dan\npan', 'aa')
    True

    >>> in_puzzle_vertical('dan\npan', 'ran')
    False

    >>> in_puzzle_vertical('ran\nfar' , 'nr')
    True

    Return if name occurs vertically in puzzle or not.
    If word occurs vertically in puzzle (in one or both vertical directions),
    return 'true'. If not, return 'false'.
    Only two directions are counted as occurences:
    left-right and right-left.
    '''
    # check if word occurs in puzzle, horizontally.
    # horizontal_occurences is the sum of left-right and right-left occurrences
    # of word in puzzle.
    horizontal_occurences = (
        (lr_occurrences(puzzle, word)) +
        (lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word)))

    # check if word occurs in puzzle, vertically.
    # vertical_occurences is the sum of top-bottom and bottom-top occurrences
    # of word in puzzle.
    vertical_occurences = (
        (lr_occurrences((rotate_puzzle(puzzle)), word)) +
        (lr_occurrences(rotate_puzzle(rotate_puzzle
                        (rotate_puzzle(puzzle))), word)))

    # See if word occurs in puzzle vertically, by checking if vertical
    # occurrences for word in puzzle is one or more and if horizontal
    # occurrences are 0.
    return(
        (vertical_occurences >= 1) and
        (horizontal_occurences == 0))


def in_puzzle(puzzle, word):
    '''(str, str) -> (bool)

    >>> in_puzzle(PUZZLE1, 'brian')
    True

    >>> in_puzzle(PUZZLE1, 'hey')
    False

    >>> in_puzzle(PUZZLE2, 'nick')
    True

    Return if word is found in puzzle or not.
    If word is found in puzzle atleast once, return 'True'.
    If word is not found in puzzle, return 'False'.
    All directions are considered as occurences:
    left-right, right-left, top-bottom, and bottom-top.
    '''
    # Using the previous function, total_occurrences, check if the value
    # returned from total_occurrences is greater than or equal to 1, which
    # indicates that word exists in puzzle atleast once, return True.
    # If not, return False.
    check_if_word_exists = total_occurrences(puzzle, word)
    return(check_if_word_exists >= 1)


def in_exactly_one_dimension(puzzle, word):
    '''(str, str) -> (bool)

    >>> in_exactly_one_dimension(PUZZLE1, 'brian')
    False

    >>> in_exactly_one_dimension('dan\npan' , 'an')
    True

    >>> in_exactly_one_dimension('zain\npain','zain is no pain')
    False

    >>> in_exactly_one_dimension('dan\npan', 'aa')
    True

    Return if word exists in only one dimension in puzzle or not.
    If word is found in puzzle in only 1 dimention, return 'True'.
    If word exists in both horizontal or both vertical directions, return True
    If word is not found in puzzle, return 'False'.
    If word is found in both dimentions, return 'False'.
    Horizontal and Vertical are considered as the only two dimensions.
    '''
    # Find if word exists horizontally or vertically.
    # If word does exist in one dimension, corresponding variable below will be
    # assigned 'True'. If word does not exist in a horizontal or vertical
    # dimention corresponding variable will be assigned 'False'.
    word_exists_only_horizontally = in_puzzle_horizontal(puzzle, word)
    word_exists_only_vertically = in_puzzle_vertical(puzzle, word)

    # Check if both assigned values are not equal. As long as one is not equal
    # to the other, return 'True', which indicates that word lies in either
    # horizontal or vertical plane in the puzzle.
    # If both have same value, such as True and True, then return False as this
    # indicates that word exists in both horizontal and vertical plane.
    # If both variables have same False value, return False, as this indicates
    # that word does not exist in puzzle.
    return(word_exists_only_horizontally != word_exists_only_vertically)


def all_horizontal(puzzle, word):
    '''(str, str) -> (bool)

    >>> all_horizontal(PUZZLE1, 'brian')
    False

    >>> all_horizontal('zain\npain' , 'zain')
    True

    >>> all_horizontal('dan\npan' , 'aa')
    False

    >>> all_horizontal('zain \n pain' , 'yes sir')
    True

    Return if all occurrences of word exist ONLY horizontally in puzzle or not.
    If all occurrences of word occur ONLY horizontally in puzzle or if word
    does not exist in puzzle, return 'True'. If word occurs horizontally and
    vertically or just vertically, return False.
    This function is identical to 'in_puzzle_horizontal' function, except the
    only difference is that if word does not exist in puzzle, then return
    'True'.
    '''
    # use previous function to check if word is only horizontal or only
    # vertical in puzzle in either one or both horizontal or vertical
    # directions.
    check_if_word_is_horizontal = in_puzzle_horizontal(puzzle, word)
    check_if_word_is_vertical = in_puzzle_vertical(puzzle, word)

    # If word is horizontal and does not exist vertically in puzzle, return
    # 'True'. If word is vertical in puzzle, return 'False'.
    # If word is not in the puzzle horizontally, return 'True'.
    return(((check_if_word_is_horizontal != check_if_word_is_vertical and
           check_if_word_is_vertical == False)) or
           (check_if_word_is_horizontal == in_puzzle(puzzle, word)))


def at_most_one_vertical(puzzle, word):
    '''(str, str) -> (bool)

    >>> at_most_one_vertical(PUZZLE1 , 'brian')
    False

    >>> at_most_one_vertical('zain \n pain', 'zp')
    True

    >>> at_most_one_vertical('we \n run' , 'far')
    False

    >>> at_most_one_vertical('zain \n pain' , 'aa')
    False

    >>> at_most_one_vertical('zain \n pain' , 'ni')
    False

    Return if word occurs in puzzle only once and if that occurrence is
    vertical.
    Return 'True', Iff word occurs once and is vertical in puzzle.
    Return 'False', if word not in puzzle or if word lies in multiple dimention
    or if word occurs vertically more than once or doesn't occur vertically at
    all.
    '''
    # Find total occurrences of word in puzzle to see if it does occur
    # atleast once
    number_of_occurrences = total_occurrences(puzzle, word)

    # Check to see if the word is vertical or not
    check_if_word_is_vertical = in_puzzle_vertical(puzzle, word)

    # Return 'True', iff word occurs once in puzzle and is vertical.
    return (number_of_occurrences == 1 and check_if_word_is_vertical == True)


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print (lr_occurrences(puzzle, name))

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences((rotate_puzzle(puzzle)), name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print (lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle
          (rotate_puzzle(puzzle))), name))

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'nick'))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE2, 'anya'))
