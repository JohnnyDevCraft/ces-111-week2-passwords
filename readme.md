# CSE111 W02 Project: Password Strength

## Purpose

Prove that you can write functions with parameters and call those functions multiple times with arguments.

## Project

### Background

You are a junior software developer working for a cellular phone service provider. Your company employs hundreds of workers ranging from customer support to cell tower engineers. The security team has recently discovered a breach of security that they attribute to users using easy to guess passwords. To help train users to create better passwords, management has asked your team to create a password strength checker. This tool will allow employees to get feedback on the strength of their passwords.

### User Requirements

María García, from the security team has provided the following requirements and resources to help create the password strength checker.

1. The password checker should allow users to check passwords until they choose to quit. The hope 
   is that by using the password checker tool employees will learn how to create better passwords.
2. Passwords should be checked against both a list of known passwords and a list of dictionary of 
   words. María has provided both a dictionary file that contains about 70,000 words and a file 
   that contains the top 1 million passwords used.
3. The tool will allow a user to enter a password, the tool will calculate the strength of the password (from 0 to 5), a message should be shown to inform the user the strength of the password.
4. María would like the strength calculator created as a function so it can be used in other future projects.
5. A password’s strength is calculated based on several factors including, is the password a dictionary word, is the password a known password, the length of the password and the complexity of the password. Here are the requirements:

   1. If the password is in the dictionary file. (this should be a case insensitive match)
        1. Print the message. "Password is a dictionary word and is not secure."
        2. Return a strength value of 0.
   2. If the password is in the toppassword list. (this should be a case sensitive match)

      1. Print the message "Password is a commonly used password and is not secure."
      2. Return a strength value of 0
      
   3. If the password is shorter than the minimum password length of 10
      1. Print the message "Password is too short and is not secure."
      2. Return a strength value of 1
      
   4. If the password is longer than 15 characters, the password is strong
      1. Print the message "Password is long, length trumps complexity this is a good password."
      2. Return the strength value of 5
      
   5. For the remainder of the cases the strength will be determined by the complexity of the password. Passwords are more difficult to crack if they contain multiple kinds of characters. For this program there are 4 kinds of characters, upper case letters, lower case letters, numeric digits, and special symbols. The complexity score is a number from 1 to 4 that indicates how many of the different types of characters are used in the password. E.g. if the password only had upper case characters it would have a complexity score of 1, if it had upper and lower case characters, it would have a complexity score of 2, etc.
   
      1. The strength score will be calculated as a base score of 1 plus the complexity score.
      2. Return the strength score.

### Design

The requirements were sent to Sven Larson, one of our software architects, to provide design assistance with the program.

Sven and his team developed the following program architecture. Use this information to create your program. As a junior programmer, you must use the functions defined by Sven, you must use exact function names and parameters.

Function Specifications

Function Name	Parameters
Return Type	Description
word_in_file	Parameters
word,
filename,
case_sensitive

Return Tpe
Boolean	This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False
word_has_character	Parameters
word,
character_list

Return Tpe
Boolean	This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter. If any of the characters in the word are present in the character list return a true, If none of the characters in the word are in the character list return false
word_complexity	Parameters
word

Return Tpe
Integer	This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)
password_strength	Parameters
password,
min_length,
strong_length

Return Tpe
Integer	This function checks length requirements, calls word_complexity to calculate the words complexity then determines the password's strength based on the user requirements. It should print the messages defined in the requirements and return the password's strength as a number from 0 to 5. The min_length parameter should have a default value of 10. The strong_length parameter should have a default value of 16
main		Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or "Q" call the password_strength function and report the results to the user. If the user enters "q" or "Q", quit the program.
Other helpful information.

Sven is aware that you are a junior programmer and offered a few tips to help you.

Include the following python code at the bottom of your program, this code will help the testing team ensure your program runs correctly. Sven has scheduled training for your team to introduce you to software testing in the near future.
if __name__ == "__main__":
    main()
Copy
When you open the password and dictionary files make sure you include the encoding parameter and pass it the value utf-8. This will ensure python knows how to read the file properly.
open(filename, "r",encoding="utf-8")
Copy
When you read a line from the file, use the strip() function of the string to remove the newline character from the end of the string. If you don't your word comparisons will not return the expected result.
You may use the following definitions for the lists of character types

```python
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
```

### Milestone

Start your project by writing the outline of your program. Follow these steps:

Create a folder for this week's project, name it whatever you want.
Open the folder you just created in VSCode.
Create a file named passwords.py.
Add the Constants that define the character lists given from Sven to the top of your code.
Create a function definition for each of the functions defined by Sven. Since you won't have any code in your functions yet just add the word pass as the body of your function.
Pass
If I were to create a function named area that I want to code later but I want to include the function definition now it might look like this:

def area(radius):
    pass
Remember to remove the word pass when you add code to the function.

Download the following files and save them in your project directory:
List of 1 million most frequently used passwords toppasswords.txt.
Dictionary words wordlist.txt
Add code to your main function as described in the requirements list. Since the password_strength function will not be completed just print a message that displays the password the user entered.
Milestone Submission

On or before the due date, return to Canvas and report your progress on this milestone.

Project Completion

Finish your project by completing the code for each function. Ensure your code accomplishes the requirements specified above.

Exceeding the Requirements

If your program fulfills the requirements for this assignment as described above, your program will earn 93% of the possible points. In order to earn the remaining 7% of points, you will need to add one or more features to your program so that it exceeds the requirements. Use your creativity to add features. Add a comment to the top of your code that explains your enhancement(s).

Document your enhancements:
If you choose to "exceed requirements" place a comment at the top of your code file that describes what you did to enhance your program.

Testing

You can test your program using the following information.

Password	Strength	Additional Message
afterthought	0	Password is a dictionary word and is not secure.
iloveny	0	Password is a commonly used password and is not secure.
withfaithhopeandcharity	5	Password is long, length trumps complexity this is a good password
ijepqnjp	1	Password is too short and is not secure.
ijepqnjpqz	2	
ijepqnjpqz!	3	
iJepqnjpqz!	4	
iJepqnjpqz!9	5	
