# Python program to check if a number is Automorphic 

# Function to check Automorphic number 
def isAutomorphic(N): 

	# Store the square 
	if N < 0: 
	N = -N 
	sq = N * N 
	
	# Start Comparing digits 
	while (N > 0) : 

		# Return false, if any digit of N doesn't 
		# match with its square's digits from last 
		if (N % 10 != sq % 10) : 
			return False
	
		# Reduce N and square 
		N //= 10
		sq //= 10
	
	return True
	
# Driver code 
N = 5
if isAutomorphic(N) : 
	print ("Automorphic") 
else : 
	print ("Not Automorphic") 
	
# This Code is contributed by Nikita Tiwari. 
