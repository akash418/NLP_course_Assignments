import os
import sys
import numpy as np 
import pickle


#function for creating empty list of given size
def create_empty_list(len_list):
	new_list=[None]*len_list
	return new_list

#function for assigning number to a word,tag pair
def number_assign(corpus_list):
	word_name=[]
	tag_name=[]
	#both these items will be returned
	word_dict=dict()
	tag_dict=dict()
	num_corpus=[]	#a list contaning word to tag mapping in form of numbers 
	word_tag_uniq_set=[]
	tag_freq_dict=dict()
	for sent in corpus_list:
		num_sent=[]
		for word,tag in sent:
			#print(word,tag)
			word_tag_uniq_set.append((word,tag))
			uniq_word=word_dict.setdefault(word.lower(),len(word_dict))
			word_tag_uniq_set.append((word,tag))
			uniq_tag=tag_dict.setdefault(tag,len(tag_dict))
			num_sent.append((uniq_word,uniq_tag))
			if(tag in tag_freq_dict):
				tag_freq_dict[tag]+=1
			else:
				tag_freq_dict[tag]=1

		num_corpus.append(num_sent)

	#word_dict.setdefault('UNK',len(word_dict))
	#tag_dict.setdefault('None',len(tag_dict))
	#num_sent.append(('UNK',None))
	#num_corpus.append(num_sent)
	#print(tag_freq_dict)

	word_name=create_empty_list(len(word_dict))
	tag_name=create_empty_list(len(tag_dict))
	for word,index in word_dict.items():
		word_name[index]=word
	word_tag_uniq_set.append(word_dict)	
	for tag,index in tag_dict.items():
		tag_name[index]=tag
	word_tag_uniq_set.append(tag_dict)	
	#print(word_name[55])
	#print(tag_name)
	return word_name,tag_name,word_dict,tag_dict,num_corpus,tag_freq_dict					


##main logic 
file_name='train_file.txt'
file_obj=open(file_name,"r")
corpus_list=[]	#orig corpus
num_corpus=[]
count=0
curr_sent=[]
for line in file_obj:
	if(line!='\n'):
		curr_line=line.split('\t')
		curr_line=tuple(curr_line)
		curr_sent.append(curr_line)
	else:
		corpus_list.append(curr_sent)
		curr_sent=[]

#print(corpus_list[664])
word_dict=dict()
tag_dict=dict()
tag_freq_dict=dict()
word_name,tag_name,word_dict,tag_dict,num_corpus,tag_freq_dict=number_assign(corpus_list)		##imp step

#print(word_dict)
#print(tag_dict)
#print(word_name)
#print(tag_name)
#print(num_corpus)

data_pickle=[]
data_pickle.append(word_name)
data_pickle.append(tag_name)
data_pickle.append(word_dict)
data_pickle.append(tag_dict)
data_pickle.append(num_corpus)
data_pickle.append(tag_freq_dict)
pickle_obj=open('model.pickle','wb')
pickle.dump(data_pickle,pickle_obj)
pickle_obj.close()




