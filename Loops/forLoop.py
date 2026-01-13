# For Loops
motorbike = ['TVS','Bajaj','Yamaha','Honda','Hero','Suzuki','BMW'];
for i in motorbike:
    print(i);

bird = 'Peacock';
for i in bird:
    print(i);

# Break
for i in motorbike:
    if i == "Suzuki":
      break;
    print(i)

# Continue
for i in motorbike:
    if i == "Suzuki":
      continue;
    print(i)
