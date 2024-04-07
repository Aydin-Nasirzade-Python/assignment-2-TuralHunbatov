#import libraries here

def main():
  month = input("Enter a month [ex. March]: ")
  day = int(input("Enter the day [ex. 12]: "))
  if (month == "December" and 22 <= day <= 31) or (month == "January" and 1 <= day <= 19):
      print('Your zodiac sign is Capricorn')
  elif (month == "January" and 20 <= day <= 31) or (month == "February" and 1 <= day <= 18):
      print('Your zodiac sign is Aquarius')
  elif (month == "February" and 19 <= day <= 29) or (month == "March" and 1 <= day <= 20):
      print('Your zodiac sign is Pisces')
  elif (month == "March" and 21 <= day <= 31) or (month == "April" and 1 <= day <= 19):
      print('Your zodiac sign is Aries')
  elif (month == "April" and 20 <= day <= 30) or (month == "May" and 1 <= day <= 20):
      print('Your zodiac sign is Taurus')
  elif (month == "May" and 21 <= day <= 31) or (month == "June" and 1 <= day <= 20):
      print('Your zodiac sign is Gemini')
  elif (month == "June" and 21 <= day <= 30) or (month == "July" and 1 <= day <= 22):
      print('Your zodiac sign is Cancer')
  elif (month == "July" and 23 <= day <= 31) or (month == "August" and 1 <= day <= 22):
      print('Your zodiac sign is Leo')
  elif (month == "August" and 23 <= day <= 31) or (month == "September" and 1 <= day <= 22):
      print('Your zodiac sign is Virgo')
  elif (month == "September" and 23 <= day <= 30) or (month == "October" and 1 <= day <= 22):
      print('Your zodiac sign is Libra')
  elif (month == "October" and 23 <= day <= 31) or (month == "November" and 1 <= day <= 21):
      print('Your zodiac sign is Scorpion')
  elif (month == "November" and 22 <= day <= 30) or (month == "December" and 1 <= day <= 21):
      print('Your zodiac sign is Sagittarius')
  else:
      print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
