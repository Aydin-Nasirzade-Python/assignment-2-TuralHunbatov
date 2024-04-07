#import libraries here

def main():
  
  m=input("Enter a month [ex. March]: ")
  d=int(input("Enter the day [ex. 12]: "))
    
  if d>31 or d<0 or m not in ["December","January","February","March","April","May","June","July","August","September","October","November"]or (d>30 and m in ["April","June","September","November"])or(d>29 and m=="February"):
        print("Either a month or a day is invalid!")
  else:
      if m=="December" or m=="January":
          if (m=="December" and d<22)or(m=="January" and d>19):
              pass
          else:
              print("Your zodiac sign is Capricorn")
      if m=="January" or m=="February":
          if (m=="January" and d<20)or(m=="February" and d>18):
              pass
          else:
              print("Your zodiac sign is Aquarius")
      if m=="February" or m=="March":
          if (m=="February" and d<19)or(m=="March" and d>20):
              pass
          else:
              print("Your zodiac sign is Pisces")
      if m=="March" or m=="April":
          if (m=="March" and d<21)or(m=="April" and d>19):
              pass
          else:
              print("Your zodiac sign is Aries")
      if m=="April" or m=="May":
          if (m=="April" and d<20)or(m=="May" and d>20):
              pass
          else:
              print("Your zodiac sign is Taurus")
      if m=="May" or m=="June":
          if (m=="May" and d<21)or(m=="June" and d>20):
              pass
          else:
              print("Your zodiac sign is Gemini")
      if m=="June" or m=="July":
          if (m=="June" and d<21)or(m=="July" and d>22):
              pass
          else:
              print("Your zodiac sign is Cancer")
      if m=="July" or m=="August":
          if (m=="July" and d<23)or(m=="August" and d>22):
              pass
          else:
              print("Your zodiac sign is Leo")
      if m=="August" or m=="September":
          if (m=="August" and d<23)or(m=="September" and d>22):
              pass
          else:
              print("Your zodiac sign is Virgo")
      if m=="September" or m=="October":
          if (m=="September" and d<23)or(m=="October" and d>22):
              pass
          else:
              print("Your zodiac sign is Libra")
      if m=="October" or m=="November":
          if (m=="October" and d<23)or(m=="November" and d>21):
              pass
          else:
              print("Your zodiac sign is Scorpion")
      if m=="November" or m=="December":
          if (m=="November" and d<22)or(m=="December" and d>21):
              pass
          else:
              print("Your zodiac sign is Sagittarius")
  pass

if __name__ == "__main__":
  main()
