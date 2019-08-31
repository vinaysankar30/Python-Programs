value = input()
rAnge = int(input())
a = 0
for i in range(rAnge,len(value),rAnge):
	if(len(value[a:i]) == rAnge):
		C = value[a:i]
		print(C)
		a = i
	


	