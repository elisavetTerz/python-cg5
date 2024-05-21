# Importing the regular expression module to handle string matching and searching.
import re

#Initialize an empty list to use as a queue:
queue_list = []

def enqueue(queue_list, item):
    queue_list.append(item)

def dequeue(queue_list):
    if queue_list: # Check if the queue is not empty.
        return queue_list.pop(0) # Remove and return the first item
    else:
        print("The list is empty!")

def print_queue(queue_list):
    if queue_list:
        print("Current queue list: ", queue_list)
    else:
        print("The queue list is empty!")

# Function to print the menu options.
def print_menu():
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Print the queue list")
    print("4. q\Q for Quit")

# Function to get the user's choice.
def get_choice():
    return input("Please insert your choice:\n: ")


def main():
    users_input = 0
    num = 0
    out_num = 0
    
    while True:
        print_menu()
        users_input = get_choice()
        # If the user does not enter anything.
        if not users_input:
            continue

        if users_input == 'q' or users_input =='Q':
            break # Exit the loop

        # Pattern to check if the input choice is a single digit.
        pattern = r'^\d$'
        valid = re.match(pattern, users_input)

        if not valid:
            print("Invalid choice")
            continue

        users_input = int(users_input)

        match users_input:
            case 1:
                num = input("Please insert a number: ")
                pattern = r'^\d+$'  # Define a pattern to check if the input is a positive integer.
                valid = re.match(pattern, num)  # Use regex to validate the number.

                if not valid:
                    print("Input is not a possitive integer number.")
                    continue

                num = int(num)
                enqueue(queue_list, num)
                print(str(num) + " inserted")
            case 2:
                out_num = dequeue(queue_list)
                if out_num is not None:
                    print("You removed the number: ", out_num)
            case 3:
                print(queue_list)
            case _:  # Default case for any other input.
                print("Not valid choice")

if __name__ == '__main__':
    main()