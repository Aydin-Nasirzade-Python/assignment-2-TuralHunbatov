#import libraries here

def main():
  m=input("Enter name of the month [ex. June]: ")
  d=int(input("Enter the day [ex. 5]: "))
  if m=="March" or m=="April" or m=="May" or m=="June":
      if (m=="March" and d<20) or (m=="June" and d>=21):
          pass
      else:
          print(m,d,"is in Spring")
  else:
  pass

if __name__ == "__main__":
  main()
