def character_word_count(book):
	file1=[]
	for word in book:
		file1.append(word)
	d={}
	for i in file1:
	
		if i not in d:
			d[i]=1
		else:
			d[i]=d[i]+1
	
	
	return d






fin1=open("Book1.txt","r")
fin2=open("Book2.txt","r")
fin3=open("Book3.txt","r")
print(character_word_count(fin1))
print(character_word_count(fin2))
print(character_word_count(fin3))
