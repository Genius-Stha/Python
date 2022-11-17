cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())
age =input("What is your age:")
if (int(age)>18):                  #converting to int to compare to int
    print("you are over 18")
elif(int(age)<18):
    print("you are less then 18")
else:
    print("you are 18")
