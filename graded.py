# main function to call all my other functions
def main():
    person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
    stupid_array_tricks(person_array)
    quit_func()
    data_list_func()
    min_max_sum()
    make_your_own()


def stupid_array_tricks(anyArray):
    for x in range(len(anyArray)): # looks for the 2nd and 3rd elements in any array passed and prints them individually
        if x == 1 or x == 2:
            print(anyArray[x])
    print(anyArray[-2:]) # uses a slice range to list the last two elements in a given array
    anyArray.insert(2, "Chuck") # inserts Chuck into the 2 index position of the array
    print(anyArray)
    del anyArray[1] # deletes the 2nd element in the array
    print(anyArray)

# basic quit function to stop when q is entered
def quit_func():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter anything or 'q' to quit: ")


def data_list_func():
    data_list = ['GOOD_DATA',
                 'DECENT_DATA',
                 'BAD_DATA',
                 'DECENT_DATA',
                 'GOOD_DATA'
                 'BAD_DATA',
                 'GOOD_DATA',
                 'DECENT_DATA',
                 'BAD_DATA',
                 'GOOD_DATA']
    # prints the length of the array, deletes any instances of bad_data then prints the new length
    print(f"The starting length of the data list is {len(data_list)}")
    for allData in data_list:
        if allData == "BAD_DATA":
            data_list.pop(data_list.index(allData))
    print(f"The ending length of the array is {len(data_list)}")

# gets the sum, minimum value, and maximum value in the array inside the function
def min_max_sum():
    score_list = [21,14,6,8,28,42,21]
    print(f"The sum of the numbers is {sum(score_list)}")
    print(f"The maximum of the numbers is {max(score_list)}")
    print(f"The minimum of the numbers is {min(score_list)}")


def make_your_own():
    # assign empty values to start my loop
    new_item = ""
    user_list = []
    while new_item != "x":
        new_item = input("Enter anything to be added to the list. Press 'x' when you've added all you want: ")
        if new_item != "x": # this keeps x from showing up in the final list
            user_list.append(new_item)
    print(user_list)


main()
