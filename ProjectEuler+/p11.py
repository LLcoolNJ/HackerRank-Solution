def maxx(x):
	max_prod = -1
	for i in range(len(x)):                
		for j in range(len(x[i])-3):      
			horiz = (x[i][j])*(x[i][j+1])*(x[i][j+2])*(x[i][j+3])
			if horiz > max_prod:
				max_prod = horiz
	 
		 
	for i in range(len(x[i])-3):       
		for j in range(len(x)):
			vert = (x[i][j])*(x[i+1][j])*(x[i+2][j])*(x[i+3][j])
			if vert > max_prod:
				max_prod = vert
	 
			
	for i in range(len(x[i])-3):       
		for j in range(len(x[i])-3):
			diag_right = (x[i][j])*(x[i+1][j+1])*(x[i+2][j+2])*(x[i+3][j+3])
			if diag_right > max_prod:
				max_prod = diag_right
	 
				 
	for i in range(3,len(x)):          
		for j in range(len(x[i])-3):
			diag_left = (x[i][j])*(x[i-1][j+1])*(x[i-2][j+2])*(x[i-3][j+3])
			if diag_left > max_prod:
				max_prod = diag_left
	return max_prod

n = []
for i in range(20):
	n.append(map(int,raw_input().split()))
print maxx(n)
