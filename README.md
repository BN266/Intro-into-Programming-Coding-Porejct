# Intro-into-Programming-Coding-Project
**Authors**: XXX
# Group Project
This is a group proect carried by out students of the University of St. Gallen in the spring semester 2022 as part of the following course:
- 7,789 | 8,789: Skills: Programming with Advanced Computer Languages
# About
The goal of this Python project is to process a data file which contains the top 50 bestselling books on Amazon from 2009-2019. A list of all books is created from which the user may select from various functions to get a subset of books which match the selected criteria.
# Prerequisites
TBA
# Instructions
1. Open the main.py Python project and run it
2. Read the menu option the program will display
3. Choose the option you want to perform
4. Input the variables that are asked
5. Inspect the final list of books that meet your criteria either in the console or through the generated PDF file
6. To quit the program input "q" or "Q" in the menu
# Description
In a first step, all of the relevant libraries were downloaded. A list was then created with all books in the data file. Afterwards the list was cleaned to be processed and displayed in a more comprehensive manner. Finally, the following 4 main functions for the menu option were defined:

- The first function is the search for books that reached bestseller within a certain year range. The program asks the user for two years, the beginning year and the ending year, and then returns all books that reached number 1 in this timeframe. If the user selects an invalid input, the program will display an appropriate error message. For the program to work the code associates the first day of the year to the beginning year and the last day of the year to the ending year. This way the subset includes all books that reached success between those years. The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates. The subset of books will be displayed in a table format sorted by date.

- The second function is the search by a specific month and year. The program asks the user for two inputs, a month and a year. If the user selects an invalid input, the program will display an appropriate error message. The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates. The subset of books that reached number 1 in that specific month and year will then be displayed sorted by date.

- The third function is the search by the author of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. If the user selects an invalid input, the program will display an appropriate error message. All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1. If the user selects an invalid input, the program will display an appropriate error message.

- The fourth function is the search by the title of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. If the user selects an invalid input, the program will display an appropriate message. All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1.

Finally, the loop for the menu function was defined. The user can input "1", "2", "3" or "4" to run the first, second, third or fourth function, respectively. If the user selects an invalid input, the program will display an appropriate error message. The loop continues to run until the user decides to quit the program by entering "q" or "Q".
# Sample output
TBA
# Sources
TBA
# Licensing
TBA
