name = input("Enter your name: ")
print("Nice to meet you", name)
age = input("What is your age?")
try:
    print("You were born in", 2025-int(age))
except ValueError:
    print("That is not a valid age")
    print("Nice Try")
except NameError:
    print("You are misspelling something")
except:
    print("I did not see that coming")
else:
    print("Thanks for playing fair")
finally:
    print("Goodbye")

