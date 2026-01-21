#Forloop
motorBike =['TVS', 'Bajaj', 'Yamaha', 'Honda', 'Hero', 'Suzuki', 'BMW'];
for i in motorBike:
    print(i);

#Print letters
bird = "Peacock";
for i in bird:
    print(i);

#Break;
print(motorBike);
for i in motorBike:
    print(i)
    if i == "Honda":
        break;

print();
print(motorBike);
for i in motorBike:
    if i == "Honda":
        continue;
    print(i);
