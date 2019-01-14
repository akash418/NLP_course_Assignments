import gensim
from gensim.models import Word2Vec

model=gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

#print(model.most_similar(positive=['woman','king'],negative=['man'],topn=1))
print(model.most_similar(positive=['China','Delhi'],negative=['India'],topn=1))
print(model.most_similar(positive=['USA','ISRO'],negative=['India'],topn=1))


