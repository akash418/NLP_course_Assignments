import pickle
import numpy as np 
import os
import operator

file_name='model.pickle'
pickle_obj=open(file_name,"rb")
data_received=pickle.load(pickle_obj)

tag_dict=dict()
word_dict=dict()
num_corpus=dict()
word_name=dict()
tag_name=dict()
tag_freq_dict=dict()

word_name=data_received[0]
tag_name=data_received[1]
tag_dict=data_received[3]
word_dict=data_received[2]
num_corpus=data_received[4]
tag_freq_dict=data_received[5]


def print_matrix(arr):
	#print("coming here")
	#print(arr)
	return True

def check_max_score(score,alpha,t,s2):
	alpha_mat=alpha
	if(score>alpha_mat[t,s2]):
		return True

def viterbi(param,observation):
	#print("Inside viterbi")
	temp_check_param=[]
	pi,transition_mat,observation_mat=param
	temp_check_param.append(pi)
	#print(pi)	
	#print(transition_mat)
	#print(observation_mat)
	num_observation=len(observation)
	temp_check_param.append(transition_mat)
	num_states=pi.shape[0]

	temp_check_param.append(num_states)
	alpha=np.zeros((num_observation,num_states))
	alpha[:,:]=float('-inf')
	temp_check_param.append(observation_mat)
	backpointers=np.zeros((num_observation,num_states), 'int')

	print_matrix(backpointers)

	#base case
	alpha[0, :]=pi * observation_mat[:,observation[0]]

	curr_iterations_val=[]
	#recursive case
	for t in range(1,num_observation):
		curr_iterations_val.append(t)
		for s2 in range(num_states):
			curr_iterations_val.append(s2)
			for s1 in range(num_states):
				curr_iterations_val.append(s1)
				score=alpha[t-1,s1]*transition_mat[s1,s2]*observation_mat[s2,observation[t]]
				if(check_max_score(score,alpha,t,s2)==True):
					alpha[t,s2]=score
					backpointers[t,s2]=s1
		
			

	#backtack logic				
	produced_seq=[]
	forward_seq=dict()		#check if rev of back==forward
	produced_seq.append(np.argmax(alpha[num_observation-1,:]))
	for i in range(num_observation-1,0,-1):
		forward_seq[i]=np.argmax(alpha[i,:])
		produced_seq.append(backpointers[i,produced_seq[-1]])

	return list(reversed(produced_seq))		


tot_num_tags=len(tag_dict)
tot_num_words=len(word_dict)

#intialse
fact=0.1
#pi=[]
#transition_mat=[[]]
#observation_mat=[[]]
viterbi_param_mat=[]
pi=fact * np.ones(tot_num_tags)
viterbi_param_mat.append(pi)
transition_mat=fact * np.ones((tot_num_tags,tot_num_tags))
viterbi_param_mat.append(transition_mat)
observation_mat=fact * np.ones((tot_num_tags,tot_num_words))
viterbi_param_mat.append(observation_mat)

#print(transition_mat)
#count 
for sent in num_corpus:
	last_tag=None
	for word,tag in sent:
		#print(word,tag)
		viterbi_param_mat.append((word,tag))
		observation_mat[tag,word] +=1
		if last_tag!=None:
			pi[tag] +=1	
		else:
			transition_mat[last_tag,tag] +=1
		viterbi_param_mat.append((word,tag))		
		last_tag=tag		

#print(transition_mat)
#normalise
for i in range(0,len(pi)):
	pi[i]=pi[i]/np.sum(pi)

#pi /=np.sum(pi)

for i in range(tot_num_tags):
	observation_mat[i,:] /=np.sum(observation_mat[i,:])

sorted_tag_freq_dict=list(reversed(sorted(tag_freq_dict.items(),key=operator.itemgetter(1))))
#print(sorted_tag_freq_dict)

for s in range(tot_num_tags):
	transition_mat[s, :] /=np.sum(transition_mat[s, :])


#print(transition_mat)	


file_name_test='test_file.txt'
file_obj_test=open(file_name_test,"r")
word_list_test=[]
test_corpus=[]
for line in file_obj_test:
	#print(line)
	if(line!='\n'):
		curr_line=line.split('\t')
		#print(curr_line[0])
		word_list_test.append(curr_line[0])
	else:
		test_corpus.append(word_list_test)
		word_list_test=[]	

#print(word_dict)
print("Words in testing set:")
print(test_corpus)

#print(word_list_test)	
word_list_test_num=[]		#numbered observation for test set

for item in test_corpus:
	curr_word_num=[]
	for word in item:
		if(word not in word_dict):
			curr_word_num.append(7)
		else:	
			curr_word_num.append(word_dict[word])
	word_list_test_num.append(curr_word_num)	

"""
for curr_list in word_list_test_num:
	curr_word_list_num=curr_list
	output_sequence=viterbi((pi,transition_mat,observation_mat),curr_word_list_num)
	for item,val in zip(curr_word_list_num,output_sequence):
		print'%2s\t%5s' %(word_name[item],tag_name[val])
"""

for curr_list,curr_list_num in zip(test_corpus,word_list_test_num):
	curr_word_list=curr_list
	output_sequence=viterbi((pi,transition_mat,observation_mat),curr_list_num)
	print'%2s\t%5s' %('WORD','PREDICTED TAG')
	for item,val in zip(curr_word_list,output_sequence):
		print'%2s\t%5s' %(item,tag_name[val])


