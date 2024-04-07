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
  if m=="June" or m=="July" or m=="August" or m=="September":
      if (m=="June" and d<21)or(m=="September" and d>=22):
          pass
      else:
          print(m,d,"is in Summer")
  else:
      pass
  if m=="October" or m=="November" or m=="December" or m=="September":
      if (m=="September" and d<22) or(m=="December" and d>=21):
          pass
      else:
          print(m,d,"is in Fall")
  else:
      pass
  if m=="January" or m=="February" or m=="December" or m=="March":
      if (m=="December" and d<21) or(m=="March" and d>=20):
          pass
      else:
          print(m,d,"is in Winter")
  pass

if __name__ == "__main__":
  main()
 
