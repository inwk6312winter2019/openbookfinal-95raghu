import string



def the_punctuation(line):
    for e in string.punctuation:
             if e in line:
                  line=line.replace(e," ")
    return line




#Function to find unique words
def unique_words(l):
    d=[]
    for word in l:
        if word in d:
           pass
        else:
           d.append(word)
    return d



#Function to count total number of words in the list
def count_the_article(l):
	mylist=["a","the","at","run","to","and","or","for","an","this"]
	c=0
	for word in l:
		if word in mylist:
			c=c+1
		else:
			pass
	return c



#Function to open files and stored the words as list
def opening_file(myfile):
   b=0
   l1=[]
   for line in myfile:
       line=line.strip(string.whitespace+string.punctuation)
       line=the_punctuation(line)
       for word in line.split():
           l1.append(word.lower())
       #b=unique_words(list1)
       d=count_the_article(l1)
   return d


#Opening files
myfile=open("Book1.txt")
res=opening_file(myfile)
print(result)

myfile1=open("Book2.txt")
res1=opening_file(myfile1)
print(result2)

myfile2=open("Book3.txt")
res2=opening_file(myfile2)
print(result3)


