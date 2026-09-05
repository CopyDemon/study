## follow demonstrate error and error traceback
# message = "Hello, World!"
# print(mesage)

## String and String methods
print("Section 1 - \nUpdate variable format with build-in string method:")
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
print("\n")

## Print with Tab and new line
print("Section 2 - \nPrinting message with tab and new line:")
print("\tPython with tab \nPython within a new line")
print("\n")

## remove white space from string
print("To strip string with three methods: \n lstrip(), rstrip(), strip() \n")
print("Section 3 - \nStriping string:")

# left strip
message = " Python"
stripped_message = message.lstrip() # striping from left
print(f"Left striping message \" {message}\" get result: \"{stripped_message}\"")
print("")

# right strip
message = "Python "
stripped_message = message.rstrip() # striping from right
print(f"Right striping message \"{message}\" get result: \"{stripped_message}\"")
print("")

# both sides strip
message = " Python "
stripped_message = message.strip() # striping from both sides
print(f"Both sides striping message \"{message}\" get result: \"{stripped_message}\"")
print("\n")


## Removing prefixes
print("Section 4 - \nRemoving prefixes:\n")
print("To remove prefix in string we use: \nremoveprefix()\n")

# remove https prefix
url = "https://nostarch.com"
url_without_prefix = url.removeprefix("https://")
print(f"Removing https prefix from {url} get result: {url_without_prefix}")
print("\n")


########################################################
## Practice: Try your self
########################################################
# pylint: disable=pointless-string-statement
"""
Save each of the following exercises as a separate file, with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

2-3. Personal Message: Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

2-4. Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.

2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

Albert Einstein once said, “A person who never made a mistake never tried anything new.”

2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""
print("Try your self: \nInstruction is in code\n")

# For convenience, I will save the exercises in the same file as the flow book
# 2-3
print("2-3:")
name = "John"
message = f"Hello {name}!"
print(f"{message}")
print("") # empty line

# 2-4
print("Task 2-4:")
name = "john doe"
name_lower = name.lower()
name_upper = name.upper()
name_title = name.title()
print(f"lower case name:{name_lower}")
print(f"upper case name:{name_upper}")
print(f"title case name:{name_title}")
print("") # empty line

# 2-5, 2-6
print("Task 2-5, 2-6:")
author = "Benjamin Franklin"
quote = "Well done is better than well said."
print(f"{author} once said, \"{quote}\"")
print("") # empty line

# 2-7
print("Task 2-7:")
name = "\t\n John Doe \n\t"
print(f"Original name: '{name}'")
l_stripped_name = name.lstrip()
r_stripped_name = name.rstrip()
stripped_name = name.strip()
print(f"Left stripped name: '{l_stripped_name}'")
print(f"Right stripped name: '{r_stripped_name}'")
print(f"Both sides stripped name: '{stripped_name}'")
print("") # empty line


# 2-8
print("Task 2-8:")
suffix = ".txt"
file_name = "python_notes.txt"
file_name_without_suffix = file_name.removesuffix(suffix)
print(f"Original file name: '{file_name}'")
print(f"Remove suffix '{suffix}' from '{file_name}' get result:'{file_name_without_suffix}'")
print("") # empty line