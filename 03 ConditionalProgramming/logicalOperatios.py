itMarks = 35;
tamilMarks = 85;

# We can you '&' sing or 'and' here.
if(itMarks>50) & (tamilMarks>50):
    print("You passed both exams");
else:
    print("You failed in the exams");
# We can you '&' sing or 'and' here.

# We can you '|' sing or 'or' here.
if(itMarks<50) | (tamilMarks<50):
    print("You failed one of the above exams");
else:
    print("You passed all exams");

if not (itMarks>50):
    print("you failed in IT subject");