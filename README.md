# Intro-into-Programming-Coding-Project
**Authors**: XXX
# Group Project
This is a group project carried by out students of the University of St. Gallen in the spring semester 2022 as part of the following courses:
- 3,793,1.00 - Skills: Programming - Introduction Level
- 7,789,1.00 - Skills: Programming with Advanced Computer Languages
# About
The goal of this Python project is to process a data file which contains the top 50 bestselling books on Amazon from 2009-2019. A list of all books is created from which the user may select from various functions to get a subset of books which match the selected criteria.
# Instructions
1. Open the project.py Python project and run it
2. Read the menu option the program will display
3. Choose the option you want to perform
4. Input the variables that are asked
5. Inspect the final list of books that meet your criteria in the console
6. To quit the program input "q" or "Q" in the menu
# Description
In a first step, all of the relevant libraries were downloaded. A list was then created with all books in the data file. Afterwards the list was cleaned to be processed and displayed in a more comprehensive manner. Finally, the following 4 main functions for the menu option were defined:

- The first function is the search for books that reached bestseller within a certain year range. The program asks the user for two years, the beginning year and the ending year, and then returns all books that reached number 1 in this timeframe. If the user selects an invalid input, the program will display an appropriate error message. For the program to work the code associates the first day of the year to the beginning year and the last day of the year to the ending year. This way the subset includes all books that reached success between those years. The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates. The subset of books will be displayed in a table format sorted by date.

- The second function is the search by a specific month and year. The program asks the user for two inputs, a month and a year. If the user selects an invalid input, the program will display an appropriate error message. The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates. The subset of books that reached number 1 in that specific month and year will then be displayed sorted by date.

- The third function is the search by the author of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. If the user selects an invalid input, the program will display an appropriate error message. All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1. If the user selects an invalid input, the program will display an appropriate error message.

- The fourth function is the search by the title of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. If the user selects an invalid input, the program will display an appropriate message. All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1.

Finally, the loop for the menu function was defined. The user can input "1", "2", "3" or "4" to run the first, second, third or fourth function, respectively. If the user selects an invalid input, the program will display an appropriate error message. The loop continues to run until the user decides to quit the program by entering "q" or "Q".
# Sample output
## Look up year range
```
What task do you want to perform?
 1: Look up year range
 2: Look up month/year
 3: Search for an author
 4: Search for title
 5: Quit
1
Enter beginning year: 2011
Enter ending year

All titles between 2005 and 2005:
4th of July, by James Patterson (5/22/2005)
A Breath of Snow and Ashes, by Diana Gabaldon (10/16/2005)
A Feast For Crows, by George R. R. Martin (11/27/2005)
Anansi Boys, by Neil Gaiman (10/9/2005)
At First Sight, by Nicholas Sparks (11/6/2005)
Chill Factor, by Sandra Brown (9/4/2005)
Eleven On Top, by Janet Evanovich (7/10/2005)
Honeymoon, by James Patterson (3/6/2005)
Knife of Dreams, by Robert Jordan (10/30/2005)
Lifeguard, by James Patterson (7/31/2005)
Mary, Mary, by James Patterson (12/4/2005)
No Place Like Home, by Mary Higgins Clark (4/24/2005)
Point Blank, by Catherine Coulter (9/11/2005)
Polar Shift, by Clive Cussler (9/18/2005)
Predator, by Patricia Cornwell (11/13/2005)
S Is For Silence, by Sue Grafton (12/25/2005)
The Broker, by John Grisham (1/30/2005)
The Closers, by Michael Connelly (6/5/2005)
The Historian, by Elizabeth Kostova (7/3/2005)
The Lincoln Lawyer, by Michael Connelly (10/23/2005)
The Mermaid Chair, by Sue Monk Kidd (6/26/2005)
The Rising, by Tim LaHaye (4/3/2005)
True Believer, by Nicholas Sparks (5/1/2005)
1776, by David McCullough (6/12/2005)
A Deadly Game, by Catherine Crier (4/3/2005)
Blink, by Malcolm Gladwell (2/6/2005)
Blood Brother, by Anne Bird (3/20/2005)
Juiced, by Jose Canseco (3/6/2005)
My Life So Far, by Jane Fonda (4/24/2005)
On Bull----, by Harry G. Frankfurt (6/5/2005)
Our Endangered Values, by Jimmy Carter (11/20/2005)
Teacher Man, by Frank McCourt (12/4/2005)
The City of Falling Angels, by John Berendt (10/16/2005)
The Fairtax Book, by Neal Boortz (8/21/2005)
The Truth (With Jokes), by Al Franken (11/13/2005)
The World Is Flat, by Thomas L. Friedman (5/15/2005)
```

## Look up month/year
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
2
Enter month (as a number, 1-12): 3
Enter year: 2005

All titles in month 3 of 2005:
Honeymoon, by James Patterson (3/6/2005)
Blood Brother, by Anne Bird (3/20/2005)
Juiced, by Jose Canseco (3/6/2005)
```

## Search for an author
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
3
Enter an author's name (or part of a name): bennet

All titles of an author with name (or part of name) 'bennet':
The Book of Virtues, by William J. Bennett (1/16/1994)
The Death of Outrage, by William J. Bennett (10/4/1998)
```

## Search for title
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
4
Enter a title (or part of a title): potter

All titles with title (or part of title) 'potter':
From Potter's Field, by Patricia Cornwell (8/27/1995)
Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
Harry Potter and the Prisoner of Azkaban, by J. K. Rowling (9/26/1999)
Harry Potter and the Sorcerer's Stone, by J. K. Rowling (8/15/1999)
```
## Quit
```
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
q
Quitting the program.
```
