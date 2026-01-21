itMarks=30;
tamilMarks=67;

if(tamilMarks>50):
    print("You passed the Tamil exam");
    if(itMarks>50):
        print("And you passed in IT exam too.");
    else:
        print("But you failed in IT exam.");
else:
    print("You failed in Tamil exam.");
    if(itMarks>50):
        print("But you passed in IT exam.");
    else:
        print("And you failed in IT exam too.");