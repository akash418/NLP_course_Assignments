import spacy

nlp=spacy.load('en_core_web_sm')
input_string="Hello my name is Davis and I am very bad at puns.I dont know how this issue can get resolved.By the way how many of you know that Apple makes crappy phones."
doc=nlp(input_string)

print("Lemmaization and POS Tagging--")
print("TEXT,LAEMMA,POS TAG")
##lemmaization and POS tagging
for token in doc:
	print(token.text,token.lemma_,token.pos_)

print("NER tagging--")
print("TEXT,LABEL")
##NER resoution
for ent in doc.ents:
	print(ent.text,ent.label_)	

print("Word similarity")
word1=nlp("dog")
word2=nlp("cat")
print(word1,word2)
print(word1.similarity(word2))
