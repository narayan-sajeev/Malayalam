import os
from random import shuffle, choice

# Mastery points
MASTERY_POINTS = 10

# List length
LIST_LEN = 200


# Read points from file
def read_from_file():
    points = {}

    try:
        # Open file
        fhand = open('points.txt', 'r')

        # Split lines into tuples
        lst = [_.split(' ') for _ in fhand.read().splitlines()]

        # Close file
        fhand.close()

        # Create dictionary
        points = {_[0]: int(_[1]) for _ in lst}

    # If file does not exist
    except:
        pass

    # Return dictionary
    return points


# Retrieve list of mastered words
def get_mastered():
    # Retrieve points
    pts = read_from_file()

    # Return list of mastered words
    return [_ for _ in pts if pts[_] >= MASTERY_POINTS]


# Update list to only include non-mastered words
def update_list(lst):
    # Remove mastered words
    lst2 = [_ for _ in lst if _[1] not in get_mastered()]

    # Return list
    return lst2


# Write mastered words to file
def write_to_file():
    # Open file
    fhand = open('points.txt', 'w+')

    # Sort points in descending order
    pts = {k: v for k, v in sorted(points.items(), key=lambda item: item[1], reverse=True)}

    # Write mastered words to file
    for mal in get_mastered():
        fhand.write('%s %s\n' % (mal, MASTERY_POINTS))

    # Write to file
    for mal, pt in pts.items():
        fhand.write('%s %s\n' % (mal, pt))

    # Close file
    fhand.close()


# Open file
fhand = open('mala.txt', 'r')

# Split lines into tuples and shuffle
lst = [_.split(' ') for _ in fhand.read().splitlines()]

length = len(lst)

# Close file
fhand.close()

# Create points dictionary
points = read_from_file()

try:
    # Repeat forever
    while True:
        # Remove mastered words
        lst = update_list(lst)

        # Retrieve first tuples
        lst = lst[:LIST_LEN]

        # Shuffle list
        shuffle(lst)

        mal2, mal, eng = choice(lst)

        # Clear screen
        os.system('clear')
        # Get number of mastered words
        count_mastered = len(get_mastered())
        # Print number of mastered words
        print('Mastered: %s (%s%%)' % (count_mastered, round(count_mastered / length * 100)))
        # Print malayalam word
        _ = input('%s\t%s ' % (' '.join(list(mal2)), mal.capitalize().lower()))
        # Check if correct
        if _ == eng:
            # Print correct
            input('Correct!')
            points[mal] = points.get(mal, 0) + 1

        else:
            # Print correct answer
            input('%s' % eng)

        # Write mastered words to file
        write_to_file()


except KeyboardInterrupt:
    # Write mastered words to file
    write_to_file()
