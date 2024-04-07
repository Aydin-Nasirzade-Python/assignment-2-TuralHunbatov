#import libraries here

def main():
  x=float(input("Enter x: "))
  y=float(input("Enter y: "))
  if ((x-2)**2-3<y and x<abs(y) and y<0)or(x>=abs(y) and y>0 and y>(x-2)**2-3):
      print("The point is in the shaded area")
  else:
      print("The point is not in the shaded area")
  pass

if __name__ == "__main__":
  main()
