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


"""
Investigate Activity 2: Grade Boundaries

Task: Run this code with different values for `score`.
Answer the questions in the comments below.
"""

score = 80 # Try changing this value! (e.g., 89, 90, 91)

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
else:
  grade = "Needs Improvement"

print(f"A score of {score} gets a grade of {grade}.")

"""
Questions:

1. What is the lowest score you can get and still receive a "B"?
   Why does this happen?

2. What happens if you enter a score of 89.9? What about 90?
   What does the `>=` operator mean?

3. If the first `if` statement was `if score > 90:`, how would that
   change the grade for a score of 90?
"""

"""
Investigate Activity 3: Nested Conditions

Task: Run this code and observe its behavior.
Answer the questions in the comments below.
"""

is_logged_in = True
is_admin = False # Try changing this to True!

if is_logged_in:
  print("Welcome to the system.")
  if is_admin:
    print("You have admin privileges.")
  else:
    print("You have standard user privileges.")
else:
  print("Please log in to continue.")


"""
Questions:

1. What two conditions must be true for the message "You have admin privileges."
   to be printed?

2. Why is the second `if/else` block indented inside the first `if` block?
   What does this indentation tell Python?

3. What is printed if `is_logged_in` is `False`? Does the program even
   check if the user is an admin in that case? Why?
"""


