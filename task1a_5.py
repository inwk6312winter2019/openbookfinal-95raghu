def starts_with_vow(book):
	file1=[]
	count=0
	for word in book:
		file1.append(word)
	for word in file1:
		if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
			count=count+1
	return count

fin1=open("Book1.txt","r")
fin2=open("Book2.txt","r")
fin3=open("Book3.txt","r")
print(starts_with_vow(fin1))
print(starts_with_vow(fin2))
print(starts_with_vow(fin3))
