# Simple To-Do List

todo_list = []

def add_to_list(add):
    todo_list.append(add)

def remove_from_list(remove):
    todo_list.remove(remove)

def view_list():
    if not todo_list:
        print("Your To-do-List is empty.")
    else:
        print("This is your To-do-List: ")
        for list in todo_list:
            print(f"- {list}")  

def main():
    while True:
        user = input("Chose an options between (add/remove/view/quit): ").lower()
        try:
            if user == "add":
                add = input("What Task you wanna add?: ")
                add_to_list(add)
            elif user == "remove":
                remove = input("What Task do you wanna remove?: ")
                if remove in todo_list:
                    remove_from_list(remove)
                else:
                    print(f"Your Task isn't in the To-do-List")
            elif user == "view":
                view_list()
            elif user == "quit":
                break
        except (NameError, TypeError):
            print("There was a NameError or TypeError.")
main()