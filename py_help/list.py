city=['kathmandu','hetauda','butwal']
city[2]='butwal' #replace the list
city.insert(0,'solukhumbu')
#del city[3]     #removing using the del form list
city.pop(1)      #removing using pop 
city.remove("butwal")   #removing using name 
#if you have more than one apperence then you should use loop
city.append("bardia")   #appending
print(sorted(city))     #this sorts but donot affect the order
print(city)
print(reversed(city))   #points to the reversed memory address
print(list(reversed(city))) #reverse
city.reverse()              #another easy way
print(city)
city.sort()             #it sort permanently in alphabetical 
print(city[0] + city[1] + city[2])
print(len(city))
print(city[-1]+"\n")     #prevent form error to print the last 
city.append("kathmandu")
#looping through the list
for x in city:      #colon matters ':'
    print(x.title()+', is beautiful city')
print("\n")                 #indentation matters remember 
for x in range(0,len(city)):    #for loop form 0 to length of list
    print(x)                    #x is integer in this (0 1 2 3)
numbers=list(range(2,10,2))     #even
print(numbers)          

square=[]
for x in range(1,10):
    square.append(x**2) #or squares = [value**2 for value in range(1,11)] 
print(square)
print(min(square))      #min max in list
print(sum(square))      #sum of all the elements

#slicing the list
print(square[:5])       #[2:8],[2:]and so on...
#you can even loop through slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for x in players[:3]:
    print(x.title())
#copying the list situation in which copying a list is useful.
# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:]). This tells Python to
# make a slice that starts at the first item and ends with the last item, produc-
# ing a copy of the entire list
retired = players[:]
print(retired)

#tuple (cannot change value)
dimentions=(600,600)
print(dimentions)
#all same as list but we use () bracket instead
#to change dimentions=(100,100)
    