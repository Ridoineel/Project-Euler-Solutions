
"""
	| problem data:
	| a < b < c
	| a^2 + b^2 = c^2
	| a + b + c = 1000
	| Find a*b*c

	a^2 + b^2 = c^2 and c = 1000 - a - b  	-> a + b = 500 + ab/1000
	a + b = 500 + ab/1000 				  	-> a = (500 - b)/(1 - b/1000)    -> b < 500
	a + b > c and c = 1000 - a - b  		-> a + b > 500
	a + b > 500 and b > a 					-> b > 250

	| Resume:
	| 250 < b < 500
	| a = (500 - b)/(1 - b/1000)
	| c = 1000 - a - b

	iterate b from 251 to 499 and break if a is integer
"""

c = int()

for b in range(251, 500):
	a = (500 - b)/(1 - b/1000)

	if a.is_integer():
		c = 1000 - a - b
		break
		
result = a*b*c

# print(a, b, c)
print(int(result))