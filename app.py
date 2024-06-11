Intro to python

"""
Interpreter - A program that executes other programs
Python Shell- an interactive interpreter that can e accessed from the commandline
Data type - A specific kind of data
Exception- An error that can e predicted and handled without causing a crash
Code lock- A collection of code that is interpreted together at indentation level
Function- A named code lock that performs a sequence of actions when it is called
Scope- Area in your program where a specific variale can e called.
"""

print("Hello world!")
print("Hello sun!")
print("Hello sky!")


"""
                                                          Data types

                                       1) Strings
Fundamental uilding locks used to represent textual data.
They are enclosed in single'' or doule quotes
"""                
               my_string = "This is a string"   


               Accessing Strings
#Strings are like sequences(lists)  where each character has its own index position starting fom 0.
#You can access individual characters using[] and the index

first_character = my_string [0]
print(f"The first character is: {first_character}") 
               


               String Length

"""
The len() function determines the length of a string which is the total no of characters it contains.
string_length = len(my_string)"""
print f(f"the length of the string is: {string_length}")
       
       #Strings in python are immutale, if they are created they cannot e modified. to change them you must create a new string

                Escape sequences
#Python provides special sequences preceded y a acklash \ to represent non printale characters or modify interpretation of characters within a string.

"""
\n- inserts a line reak
\t:  this is a tab character
\\:  Backslash character
                """


                                        Multiline Strings
 #Triple quotes are used for long text or incorporating code within comments eg 

 multiline_string = """This is a multiline string.
It can span across multiple lines."""

print(multiline_string)    

                                        String Concatenation
the + operator is used to join two strings into a single string.

greeting = "hello, " + "world."
print(greeting)