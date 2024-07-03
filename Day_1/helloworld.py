#1 check version
import sys
import math

version = sys.version_info;

print(f'Python version: {version.major}.{version.minor}.{version.micro}')

#2 use 3 & 4 with operands
print(3 + 4) # addition(+)
print(3 - 4) # subtraction(-)
print(3 * 4) # multiplication(*)
print(3 % 4) # modulus(%)
print(3 / 4) # division(/)
print(4 ** 3) # exponential(**)
print(3 // 4) # floor division operator(//) 

#3 make some strings
name = 'Gauthamram'
family_name = 'Gopinath'
country = 'Australia'
slogan = 'something something'

#4 check type
print(type(10)) # 10
print(type(9.8)) # 9.8
print(type(3.14)) # 3.14
print(type(4 - 4j)) # 4 - 4j
print(type(['ram', 'python', 'Australia'])) # ['Asabeneh', 'Python', 'Finland']
print(type(name)) # Your name
print(type(family_name)) # Your family name
print(type(country)) # Your country

#5 
print(1) #Integer
print(1.2) #Float
print(1 - 2j) #Complex)
print('Ram') #String
print(False) #Boolean
print(['Ram', '23', 'Australia']) #List
print((12, 13, 14, 15, 16)) #Tuple
print ({12, 13, 14}) #Set
print({ 'name': 'Ram', 'country':'Australia'}) # Dictionary.

#6 find ecludian distance
def ecludian_distance(point1, point2):
    line_square = (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2
    return math.sqrt(line_square)

print(ecludian_distance((2,3),(10,8)))