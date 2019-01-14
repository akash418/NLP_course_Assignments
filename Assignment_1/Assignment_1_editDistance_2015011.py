import numpy as np

def min_edit_dist(m,n,str1,str2):
	#dp=[]
	#dp=[[0 for i in range(n+1)] for i in range(m+1)]
	dp=np.zeros((m+1,n+1),dtype=int)
	#initialising the dp matrix
	for i in range(0,m+1):
		for j in range(0,n+1):
			if(i==0):
				dp[i][j]=j
			elif(j==0):
				dp[i][j]=i

	for i in range(1,m+1):
		for j in range(1,n+1):
			if(str1[i-1]==str2[j-1]):
				dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
			elif(str1[i-1]!=str2[j-1]):
				dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)	

	print("-----MIN EDIT DISTANCE MATRIX-------")			
	#matrix display			
	for i in range(0,m+1):
		for j in range(0,n+1):
			print(dp[i][j],end=' ')
		print()
	print()

	#backtrack logic---
	print("Operations required to change "+str1.upper()+" into "+str2.upper())
	req_operations=[]
	p=m
	q=n
	while(1):
		if(p==0 or q==0):
			break
		elif(str1[p-1]==str2[q-1]):
			#print("no change")
			req_operations.append("no change")
			p=p-1
			q=q-1
		elif(dp[p][q]==dp[p-1][q-1]+2):
			#print("subsitute")
			req_operations.append("subsitute")
			p=p-1
			q=q-1
		elif(dp[p][q]==dp[p-1][q]+1):
			#print("delete")
			req_operations.append("delete")
			p=p-1
		elif(dp[p][q]==dp[p][q-1]+1):
			#print("delete")
			req_operations.append("delete")
			q=q-1					

	#print(req_operations)		
	while(len(req_operations)!=0):
		print(req_operations.pop())

	return dp[m][n]


#min distance for coverting str1 to str2
#str1="intention"
#str2="execution"
str1=input("Enter string1: ")
str2=input("Enter string2: ")
min_dist_val=min_edit_dist(len(str1),len(str2),str1,str2)
print()
print("MIN EDIT DISTANCE:")
print(min_dist_val)
