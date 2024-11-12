"""Practice with lists"""

# both ways to make an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constuctor

print(my_numbers)

# STRING ANALOGY
# my_name: str = "" # literal
# my_name: str = str() #constructor

# ADDING A VALUE TO A LIST
my_numbers.append(1.5)
my_numbers.append(2.3)
my_numbers.append(2.3)
print(my_numbers)

# ALREADY POPULATED LISTS
game_points: list[int] = [102, 86, 94]  # creates lists of floats
print(game_points)
print(f"The game points are {game_points}!")  # USING F STRING

# INDEXING(subscription notation) WITHIN LISTS
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# MODIFYING BY INDEX
# lists are mutable, and str are not able to do this
game_points[1] = 72
print(game_points)

class_num: str = "110"  # change it to '210'
# class_num[0] = "2"  # doesn't work when you run it because of nature of lists(mutable)

# LENGTH OF LISTS
print(len(game_points))

# REMOVE ITEMS FROM LISTS
game_points.pop(1)  # use index within parentheses
print(game_points)


# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points
def display(int_list: list[int]) -> None:
    """Displays all elemenets of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
