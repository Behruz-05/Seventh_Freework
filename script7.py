firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
thirdnumber = int(input("Enter third number: "))
fourthnumber = int(input("Enter fourth number: "))
fifthnumber = int(input("Enter fifth number: "))
if firstnumber > secondnumber and firstnumber > thirdnumber and firstnumber > fourthnumber and firstnumber > fifthnumber:
    print(f"The highest number is {firstnumber}")
if secondnumber > firstnumber and secondnumber > thirdnumber and secondnumber > fourthnumber and secondnumber > fifthnumber:
    print(f"The highest number is {secondnumber}")
if thirdnumber > firstnumber and thirdnumber > secondnumber and thirdnumber > fourthnumber and thirdnumber > fifthnumber:
    print(f"The highest number is {thirdnumber}")
if fourthnumber > firstnumber and fourthnumber > secondnumber and fourthnumber > thirdnumber and fourthnumber > fifthnumber:
    print(f"The highest number is {fourthnumber}")
if fifthnumber > firstnumber and fifthnumber > secondnumber and fifthnumber > thirdnumber and fifthnumber > fourthnumber:
    print(f"The highest number is {fifthnumber}")