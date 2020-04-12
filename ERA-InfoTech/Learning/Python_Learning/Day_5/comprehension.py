comp=[x for x in 'human']
print(comp)

#condition can apply
comp1=[x for x in range(10) if x%2==0]
print(comp1)

#nested condition also can apply

comp2=[x for x in range(100) if x%2==0 if x%5==0]
print(comp2)

#transpose Matrix[]

matrix=[[1,2],[3,4],[5,6],[7,8]]
transMatrix=[[row[i] for row in matrix] for i in range(2)]
print("Transpose Matrix is :",transMatrix)


input("Press Enter to Exit")
