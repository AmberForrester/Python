student = ['Paul', '2 abc street', 'abcd, ON', 9051234678, True]
print(student)


# Using the index to assign a new value to it:

# For example - change the student name Paul to Chris
print("Before:", student)

# Use the index to access the first element `Paul`
student[0] = 'Chris' # Then assign `Chris` to that specific index changes it from Paul to Chris

print("After:", student)
print(student)