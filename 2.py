#Write an python program to enter a string and apply string slicing and indexing to it the user should be able to enter the string and the program should display the first character, last character, substring from index 1 to 4 and substring from index 2 to 6.
s=str(input("Enter a string upon which you have to apply the slicing and indexing to :"))
print("The string you entered is : ",s)
print("The first character of the string is : ",s[0])
print("The last character of the string is : ",s[-1])
print("The substring from index 1 to 4 is : ",s[1:5])
print("The substring from index 2 to 6 is : ",s[2:7])
