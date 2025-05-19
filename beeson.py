# This project calculate the number of bees (at a certain generation) if the population of bees satisfies the Fibonacci Sequence

Gen = int(input("If Beeson is the first, enter the number of generation(s) before Beeson(starting from 2): "))

while Gen < 1:
  print("Please enter a positive integer.")
  Gen = int(input("If Beeson is the first, enter the number of generation(s) before Beeson(starting from 2): "))

Bees = [1,1]
for x in range(0, Gen):
  Bees.append(Bees[x] + Bees[x+1])

Number = Bees[Gen-1]
Gen = str(Gen)

if Gen.endswith("1"):
  print("The number of bees of the {}st generation is {} ".format(Gen, Number))
elif Gen.endswith("2"):
  print("The number of bees of the {}nd generation is {} ".format(Gen, Number))
elif Gen.endswith("3"):
  print("The number of bees of the {}rd generation is {} ".format(Gen, Number))
else:
  print("The number of bees of the {}th generation is {}".format(Gen, Number))

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
# if gen = 3, [1,1,2,3]
