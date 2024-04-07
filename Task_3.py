#import libraries here

def main():
  wavelength=int(input("Enter the wavelength in nm: "))
  if 380 <= wavelength < 450:
      print("The relevant color is Violet")
  elif 450 <= wavelength < 495:
      print("The relevant color is Blue")
  elif 495 <= wavelength < 570:
      print("The relevant color is Green")
  elif 570 <= wavelength < 590:
      print("The relevant color is Yellow")
  elif 590 <= wavelength < 620:
      print("The relevant color is Orange")
  elif 620 <= wavelength <= 750:
      print("The relevant color is Red")
  else:
        print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
