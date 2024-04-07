#import libraries here

def main():
  n=int(input("Enter the year [ex. 2021]: "))
  if n<0:
      print("Invalid year!")
  elif n%12==8:
      print(n,"is the year of the Dragon")
  elif n%12==9:
      print(n,"is the year of the Snake")
  elif n%12==10:
      print(n,"is the year of the Horse")
  elif n%12==11:
      print(n,"is the year of the Sheep")
  elif n%12==0:
      print(n,"is the year of the Monkey")
  elif n%12==1:
      print(n,"is the year of the Rooster")
  elif n%12==2:
      print(n,"is the year of the Dog")
  elif n%12==3:
      print(n,"is the year of the Pig")
  elif n%12==4:
      print(n,"is the year of the Rat")
  elif n%12==5:
      print(n,"is the year of the Ox")
  elif n%12==6:
      print(n,"is the year of the Tiger")
  elif n%12==7:
      print(n,"is the year of the Hare")
  pass

if __name__ == "__main__":
  main()
