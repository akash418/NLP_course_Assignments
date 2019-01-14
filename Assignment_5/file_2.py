#
#Code ref takedn from:
#https://medium.com/@mishra.thedeepak/doc2vec-simple-implementation-example-df2afbbfbad5

import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import os
import math
import string
import re
import operator
import random
import sys


path="20_newsgroups"
path_graphics="20_newsgroups/comp.graphics"

file_data=[]
file_number=[]
file_data_graphics=[]
file_number_graphics=[]

str_data=""
#count=0


for root,dirs,files in os.walk(path):
	count=0
	for item in files:
		if(count==0):
			f=open(os.path.join(root,item),'r')
			#print(item)
			linelist=f.readlines()
			header_sep=0
			try:
				for i in range(0,len(linelist)):
					if(header_sep==0 and linelist[i]=='\n'):
						header_sep=1
					elif(header_sep==1 and linelist[i]!='\n'):
						str_data+=linelist[i]
						count+=1
				file_data.append(str_data)
				file_number.append(item)		
			except Exception as e:
				print(e)			


str_data=""
count=0
for root,dirs,files in os.walk(path_graphics):
	for item in files:
		print(item)
		if(count<20):
			f=open(os.path.join(root,item),'r')
			linelist=f.readlines()
			header_sep=0
			try:
				for i in range(0,len(linelist)):
					if(header_sep==0 and linelist[i]=='\n'):
						header_sep=1
					elif(header_sep==1 and linelist[i]!='\n'):
						str_data+=linelist[i]		
				count+=1
				file_data_graphics.append(str_data)
				file_number_graphics.append(item)
			except Exception as e:
				print(e)			


#print(file_data)
#print(len(file_data))
#print(file_data_graphics)
#print(len(file_data_graphics))
print(file_number)
print("---\n\n-----")
print(file_number_graphics)

train_data=file_data[1:len(file_data)]		##train on some and test on some
tagged_data=[TaggedDocument(words=word_tokenize(_d.lower()),tags=[str(i)]) for i,_d in enumerate(train_data)]
#print(tagged_data)


train_data_graphics=file_data_graphics[1:len(file_data_graphics)]
tagged_data_graphics=[TaggedDocument(words=word_tokenize(_d.lower()),tags=[str(i)]) for i,_d in enumerate(train_data_graphics)]
#print(tagged_data_graphics)

max_epochs=100
vec_size=20
alpha=0.025


model=Doc2Vec(size=vec_size,alpha=alpha,min_alpha=0.00025,min_count=1,dm=1)
model.build_vocab(tagged_data)
for epoch in range(max_epochs):
	print('iteation{0}'.format(epoch))
	model.train(tagged_data,total_examples=model.corpus_count,epochs=model.iter)
	model.alpha-=0.0002
	model.min_alpha=model.alpha

model.save("d2v.model")
print('model saved')

model=Doc2Vec.load("d2v.model")
test_data=word_tokenize(file_data_graphics[0])
v1=model.infer_vector(test_data)
#print(v1)

print("--Sim of doc1 with docs of other classes")
print(model.docvecs.most_similar([v1],topn=19))



model_2=Doc2Vec(size=vec_size,alpha=alpha,min_alpha=0.00025,min_count=1,dm=1)
model_2.build_vocab(tagged_data_graphics)
for epoch in range(max_epochs):
	print('iteration{0}'.format(epoch))
	model_2.train(tagged_data_graphics,total_examples=model_2.corpus_count,epochs=model_2.iter)
	model_2.alpha-=0.0002
	model_2.min_alpha=model_2.alpha

model_2.save("d2v_graphics.model")
print("model saved")	
model_2=Doc2Vec.load("d2v_graphics.model")

test_data_graphics=word_tokenize(file_data_graphics[0])
v1=model_2.infer_vector(test_data_graphics)
print("--Sim of doc1 with docs of same class ")
print(model_2.docvecs.most_similar([v1],topn=19))



