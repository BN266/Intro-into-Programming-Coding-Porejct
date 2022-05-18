import requests

def download_bestsellers():
    try:
        r = requests.get("https://s2.smu.edu/~devans/1342/Bestsellers.txt")
        with open("bestsellers.txt", "wb") as f:
            f.write(r.content)
        return True
    except:
        return False

def read_in_bestsellers():
    try:
        with open("bestsellers.txt", "r") as f:
            return [tuple([element[:-1] if index == 4 else element for index, element in enumerate(line.split("\t"))]) for line in f.readlines()][:-1]  # ERROR IN LAST ITEM OF FILE
    except:
        return False

def selection_menu(inpt=None):
    if inpt in ("1", "2", "3", "4", "q", "Q"):
        return inpt
    if inpt is not None:
        print("Please enter a valid choice.")
        print("")
    print("What would you like to do?", "1: Look up year range", "2: Look up month/year", "3: Search for author", "4: Search for title", "Q: Quit", sep="\n")
    return selection_menu(input())

def books_year(bestsellers):
    while True:
        start = input("Enter beginning year: ")
        try:
            start = int(start)
            break
        except:
            print("Please enter a valid beginning year.")
    while True:
        end = input("Enter ending year: ")
        try:
            end = int(end)
            break
        except:
            print("Please enter a valid ending year.")
    print("")
    if start > end:
        temp = end
        end = start
        start = temp
    print(f"All titles between {start} and {end}:")
    c = 0
    for book in bestsellers:
        year = int(book[3][-4:])
        if year >= start and year <= end:
            print(f"{book[0]}, by {book[1]} ({book[3]})")
            c += 1
    if c == 0:
        print("No books within the specified years were found.")
    print("")

def books_month(bestsellers):
    while True:
        month = input("Enter month (as a number, 1-12): ")
        try:
            month = int(month)
            if month in range(1, 13):
                break
            else:
                raise Exception
        except:
            print("Please enter a valid month.")
    while True:
        year = input("Enter year: ")
        try:
            year = int(year)
            break
        except:
            print("Please enter a valid year.")
    print("")
    print(f"All titles in month {month} of {year}:")
    c = 0
    for book in bestsellers:
        book_year = int(book[3][-4:])
        book_month = int(book[3][:book[3].index("/")])
        if month == book_month and year == book_year:
            print(f"{book[0]}, by {book[1]} ({book[3]})")
            c += 1
    if c == 0:
        print("No books for the specified month and year were found.")
    print("")

def books_author(bestsellers):
    author = input("Enter an author's name (or part of a name): ")
    print("")
    print(f"All titles of an author with name (or part of name) '{author}':")
    c = 0
    for book in bestsellers:
        book_author = book[1]
        if author.lower() in book_author.lower():
            print(f"{book[0]}, by {book[1]} ({book[3]})")
            c += 1
    if c == 0:
        print("No books for the specified author were found.")
    print("")

def books_title(bestsellers):
    title = input("Enter a title (or part of a title): ")
    print("")
    print(f"All titles with title (or part of title) '{title}':")
    c = 0
    for book in bestsellers:
        book_title = book[0]
        if title.lower() in book_title.lower():
            print(f"{book[0]}, by {book[1]} ({book[3]})")
            c += 1
    if c == 0:
        print("No books with the specified title were found.")
    print("")


if __name__ == "__main__":
    if not download_bestsellers():
        print("ERROR: Could not download the Bestsellers. Program is exiting...")
        exit()
    ri = read_in_bestsellers()
    if not ri:
        print("ERROR: Could not construct the Bestsellers. Program is exiting...")
        exit()
    while True:
        sl = selection_menu()
        """
        7.  Your program will handle erroneous user inputs.
        If there are any problems with a particular user input,
        your program will display the menu and allow the user
        to select another option.

        --> IMO it's a nicer solution to reask the user e.g. user enters year
        20P0, then we should just ask him again to enter a valid year instead
        of restarting in the selection menu.
        """
        if sl == "1":
            books_year(ri)
        elif sl == "2":
            books_month(ri)
        elif sl == "3":
            books_author(ri)
        elif sl == "4":
            books_title(ri)
        else:
            print("Quitting the program.")
            break
