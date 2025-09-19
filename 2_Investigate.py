"""
# PRIMM: Investigate 1

## Instructions

Now, let's investigate the code from the "Predict" activity. 
Run the code in a Python environment to see the actual output. 
Then, answer the questions below.

---

### Questions

1.  **First Question:** The first `if` statement checks the condition `age < 13`. Is this condition `True` or `False`? Why?
2.  **Second Question:** The `elif` statement checks the condition `age < 18`. Why does the program check this condition *after* the first `if` statement?
3.  **Flow of Control:** Which of the three `print` statements for the ticket price was executed? Why were the other two skipped?
4.  **Indentation:** What do you think would happen if you removed the indentation (the spaces) before `print("Ticket price: $12 (Teen)")`?

"""

# A simple program to check age for a movie ticket
age = 15

print("Welcome to the theater!")

if age < 13:
    print("Ticket price: $8 (Child)")
elif age < 18:
    print("Ticket price: $12 (Teen)")
else:
    print("Ticket price: $15 (Adult)")

print("Enjoy the show!")
