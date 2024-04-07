#import libraries here

def main():
  n=input("Enter a letter of the alphabet: ")
  p='aeiou'
  if n in p:
      print("Entered alphabet is a vowel!")
  elif n=="y":
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
      print("Entered alphabet is a consonant!")
  pass

if __name__ == "__main__":
  main()
