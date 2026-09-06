# Writing a Python program to apply string functions repeatedly until the user exits.
s=str(input("Enter a string upon which you have to apply the function to :"))
print("The string you entered is : ",s)
print("-----------The string functions available are :--------------")
print("1. capitalize()")
print("2. casefold()")
print("3. center()")
print("4. count()")
print("5. encode()")
print("6. endswith()")
print("7. expandtabs()")
print("8. find()")
print("9. format()")
print("10. format_map()")
print("11. index()")
print("12. isalnum()")
print("13. isalpha()")
print("14. isascii()")
print("15. isdecimal()")
print("16. isdigit()")
print("17. isidentifier()")
print("18. islower()")
print("19. isnumeric()")
print("20. isprintable()")
print("21. isspace()")
print("22. istitle()")
print("23. isupper()")
print("24. join()")
print("25. ljust()")
print("26. lower()")
print("27. lstrip()")
print("28. partition()")
print("29. replace()")
print("30. rfind()")
print("31. rindex()")
print("32. rjust()")
print("33. rstrip()")
print("34. split()")
print("35. splitlines()")
print("36. startswith()")
print("37. strip()")
print("38. swapcase()")
print("39. title()")
print("40. upper()")
print("0. Exit")
print("------------------------end---------------------------------")

while True:
    ch=int(input("Enter the function choice you want to apply to the string (0 to exit): "))
    if ch == 0:
        print("Exiting the program.")
        break

    if ch==1:
        print(s.capitalize())
    elif ch==2:
        print(s.casefold())
    elif ch==3:
        print(s.center(10))
    elif ch==4:
        print(s.count("a"))
    elif ch==5:
        print(s.encode())
    elif ch==6:
        print(s.endswith("!"))
    elif ch==7:
        print(s.expandtabs())
    elif ch==8:
        print(s.find("o"))
    elif ch==9:
        print(s.format(name="Alice", age=25))
    elif ch==10:
        print(s.format_map({"name": "Alice", "age": 25}))
    elif ch==11:
        print(s.index("o"))
    elif ch==12:
        print(s.isalnum())
    elif ch==13:
        print(s.isalpha())
    elif ch==14:
        print(s.isascii())
    elif ch==15:
        print(s.isdecimal())
    elif ch==16:
        print(s.isdigit())
    elif ch==17:
        print(s.isidentifier())
    elif ch==18:
        print(s.islower())
    elif ch==19:
        print(s.isnumeric())
    elif ch==20:
        print(s.isprintable())
    elif ch==21:
        print(s.isspace())
    elif ch==22:
        print(s.istitle())
    elif ch==23:
        print(s.isupper())
    elif ch==24:
        print(s.join(["Hello", "World"]))
    elif ch==25:
        print(s.ljust(10))
    elif ch==26:
        print(s.lower())
    elif ch==27:
        print(s.lstrip())
    elif ch==28:
        print(s.partition(" "))
    elif ch==29:
        print(s.replace("World", "Python"))
    elif ch==30:
        print(s.rfind("o"))
    elif ch==31:
        print(s.rindex("o"))
    elif ch==32:
        print(s.rjust(10))
    elif ch==33:
        print(s.rstrip())
    elif ch == 34:
        print(s.split())
    elif ch == 35:
        print(s.splitlines())
    elif ch == 36:
        print(s.startswith("H"))
    elif ch == 37:
        print(s.strip())
    elif ch == 38:
        print(s.swapcase())
    elif ch == 39:
        print(s.title())
    elif ch == 40:
        print(s.upper())
    else:
        print("Invalid choice")