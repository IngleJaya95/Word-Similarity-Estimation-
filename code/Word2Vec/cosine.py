import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial
import sys
from scipy.stats import spearmanr as sp
import pandas as pd 

emb_size = int(sys.argv[1]) # size of embedding 
f = open("Model.txt","r")
data  =f.read()
list_of_vectors = data.split("\n") #contains lines of text file 
dict = {}


for i in range(2,len(list_of_vectors)):
	vector = list_of_vectors[i].split(" ") 
	word = vector[0] # for geting specific english word as key
	vector1 = np.array(vector[1:emb_size])   #vector size = embedding size 
	embedding = vector1.astype(float) #conversion from string to float
	dict.update({word:embedding})


#vec1 = dict[sys.argv[1]] 
#vec2 = dict[sys.argv[2]]
#sim = 1 - spatial.distance.cosine(vec1,vec2)
#print("Cosine Similarity :",sim)





#word = model.similarity(word1,word2)
df = pd.read_csv('/media/jaya/study stuffs/IITM/2nd_sem/NLP/NLPpa1/code/wordsim353.csv')
#df = pd.read_csv('/media/jaya/study stuffs/IITM/2nd_sem/NLP/NLPpa1/code/wordSim_reuter.csv')
word1 = df.values[:,0]
word2 = df.values[:,1]
score_353 = df.values[:,2]
  

scores =[]
for k in range(len(df)):
	tmp = 1 - spatial.distance.cosine(dict[word1[k]],dict[word2[k]])
	scores.append(tmp)


cor  = sp(scores,score_353)
print(cor)
