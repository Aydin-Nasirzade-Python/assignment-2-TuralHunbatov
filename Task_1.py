#import libraries here
def main():
    l= input("Enter a letter of the alphabet: ")
    if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
        print("Entered alphabet is a vowel!")
    elif l=='y':
        print("Sometimes it is a vowel, and sometimes it is a consonant!")
    else:
        print("Entered alphabet is a consonant!")
    pass

if __name__ == "__main__":
  main()
