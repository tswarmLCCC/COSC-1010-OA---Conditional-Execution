"""
# PRIMM: Modify 1

## Instructions

Here is the same code snippet again. Your task is to make the following modifications. For each change, first **predict** the new output, then run the code to **verify** your prediction.

---

### Modifications

1.  **Change the `age`:**
    * **Modification:** Change the line `age = 15` to `age = 65`.
    * **Predict:** What will the new output be?
    * **Verify:** Run the code. Was your prediction correct?

2.  **Add a Senior Discount:**
    * **Modification:** Add a new `elif` block to give a discount to seniors (age 65 and over). The price should be $10. Place this new block *before* the final `else`.
    * **Predict:** With `age` still set to 65, what will the output be now?
    * **Verify:** Run the code. Was your prediction correct?

3.  **Combine Conditions:**
    * **Modification:** Let's say there's a special student discount. Modify the `elif age < 18:` line to also check if the person has a student ID. The code might look something like this (you'll need to add a new variable for the student ID): `elif age < 18 and has_student_id == True:`.
    * **Predict:** What do you need to add to the program for this to work? How will the output change if `age` is 16 and `has_student_id` is `False`?
    * **Verify:** Make the changes and run the code to check your prediction.
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
