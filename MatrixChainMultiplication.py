n=int(input()) #Number of matrices
mat=[int(m) for m in input().split()]  #Matrices dimension

n1 = len(mat)-1 #For generating new matrices to calculate parenthesization plus least operations

m=[] #Least operations matrix, below operations are initializing it to zero
m1=[]
for i in range(0, n1):
    for j in range(0, n1):
        m1.append(0)
    m.append(m1)
    m1=[]
    
    
s=[] #Parenthesization matrix
s1=[]
for i in range(0, n1):
    for j in range(0, n1):
        s1.append(0)
    s.append(s1)
    s1=[]

for l in range(2, n1+1): #Least operrations plus optimal parenthesization calculation
    for j in range(0, n-l+1):
        k=j+l-1
        m[j][k]=999999
        for k1 in range(j, k):
            q=m[j][k1] + m[k1+1][k] + mat[j]*mat[k1+1]*mat[k+1]
            if(q<m[j][k]):
                m[j][k]=q
                s[j][k]=k1             
print(m[0][n1-1])

def optimal(s, j, k): #Optimal parenthesization calculation
    if j==k:
        print(str(j+1), end="")
        return
    else:
        print("(", end="")
        optimal(s, j, s[j][k])
        optimal(s, s[j][k]+1, k)
        print(")", end="")    
optimal(s, 0, n-1)
print()
