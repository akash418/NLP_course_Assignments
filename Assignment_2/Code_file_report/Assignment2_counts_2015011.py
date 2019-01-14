import os
import sys
import math
import re
import enchant
import string

f_name="train_doc.txt"
path=os.path.normpath("/Users/Desktop/train_doc")
unique_words=dict()
exclude=set(string.punctuation)

#--tot number of words,sentences and paragraphs
tot_eng_words=0			#number of dictonary english words
tot_words=0				#total number of words
tot_sent=0				#total number of sentences	
tot_par=0				#total number of paragraphs	

test_str=""
test_str_orig=""

with open(f_name,"r") as f:
	linelist=f.readlines()
	try:
		for i in range(0,len(linelist)):
			str_data=linelist[i]
			test_str+=str_data.lower()
			test_str_orig+=linelist[i]
			str_data_split=str_data.split(" ")
			#print(len(str_data_split))
			english_dict=enchant.Dict("en_US")		#creating an english dict
			#print(str_data_split)
			count=0
			for item in str_data_split:
				#print(item)
				if(item!="" and english_dict.check(item)==True):
					count+=1
				if(item=='\n'):
					tot_par+=1	
			#print(count)		
			tot_eng_words+=count
			tot_words+=len(str_data_split)
				
	except Exception as e:
		print(type(e))


print(tot_words)
print(tot_eng_words)
print(tot_par)

#print(test_str)

regex_words=r"\w+[-|.|-|']?\w+"		#regex exp for finding number of words 
matches=re.finditer(regex_words,test_str,re.MULTILINE)
#print(type(matches))
print("Total number of words in the text:")
print(len(list(matches)))

regex_para=r"\n\n"
matches=re.finditer(regex_para,test_str,re.MULTILINE)		#regex expression for finding number of paragraphs
print("Total number of paragraphs")
print(len(list(matches)))
#print(test_str)


print("Total number of sentences: ")						#regex exp for fiding number of sentences
regex_sent=r"[\n\.!?]?[A-Z][^.]{6,}[?\.!] ?"
#print(regex_sent)
matches=re.finditer(regex_sent,test_str_orig,re.MULTILINE)
print(len(list(matches)))

print("Another way to find total number of sentences: ")	#regex exp for finding number of sentences
regex_sent_2=r"\w{3,}[.]"
matches=re.finditer(regex_sent_2,test_str_orig,re.MULTILINE)
print(len(list(matches)))

str1=raw_input("Enter word to find number of sentences beggining with this word: ")
str1=str1.lower()
#regex1=r"^for\b |[.] ?for\b\Gfor\b"
regex_beg=r"[.|?|!|\n] ?"+re.escape(str1)+"\\b"+"|\G"+str1+"\\b"		#regex exp for finding number of sentences beggining with a word
matches=re.finditer(regex_beg,test_str,re.MULTILINE)
print("Number of sentences starting with word: "+str1)	
print(len(list(matches)))	

str2=raw_input("Enter word to find number of sentences ending with this word:")
str2=str2.lower()
#regex2=" ?"+str1+"\\b"+" ?[.]|[?]"
regex_end=r" ?"+re.escape(str2)+"\\b"+" ?[.|?|!]"				#regex exp for finding number of sentences ending with a word
matches=re.finditer(regex_end,test_str,re.MULTILINE)
print("Number of sentences ending with word: "+str2)	
print(len(list(matches)))	

str3=raw_input("Enter word to find it's frequency: ")
str3=str3.lower()
regex_freq=r"(?<!\\S)"+re.escape(str3)+"(?!\\S)"
print(len(re.findall(regex_freq,test_str,re.IGNORECASE)))




