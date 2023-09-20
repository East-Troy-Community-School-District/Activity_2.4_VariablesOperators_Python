'''
Concatenation
Pawelski
9/20/2023
Introduction to Computer Science

Instructions  
Read the code and run the program. Were you surprised
by the results? Let’s first focus on the line that reads...

print("21" + "2")

Instead of printing 23, this line prints 212. The reason
this happens is because "21" and "2" are string literals!
This means that Python does not treat them like numbers.
Instead, Python treats them like pieces of text, which are
“added” differently. In fact, Python “adds” strings by
combining them into a single piece of text. This process
is called concatenation. We see this action with the remaining
lines of code in this program. Using these lines of code as examples,
answer the following questions...
* When you add string literals, spaces are not automatically
  added between them. How would you add a space between
  string literals?
* Is there another way you could write these lines
  of code to simplify them?

Before we wrap-up operators, just a quick warning! You cannot
concatenate strings and numbers. For example, the following
line of code would not work (Hint: Type it into a program and
run it if you want proof.)...

print("I've got " + 2 + " tickets to paradise.")

In the case of this line, the computer gets confused because
it does not know how to perform the operation. We will learn
about a way to fix this problem in a bit.
'''

print("21" + "2")
print("Hello " + "Dolly")
print("There " + "are" + "no" + "spaces" + "here.")
print("Add " + "spaces at the end of string literals.")
print("Or" + " at the beginning.")
print("Or add it" + " " + "as a sperate string literal.")
