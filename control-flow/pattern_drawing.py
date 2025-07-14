size=int(input("enter the size of the pattern:"))
if size>0:
  for i in range(size):
      for j in range(size):
        print("*", end="")
      print()