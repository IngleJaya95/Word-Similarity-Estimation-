import gensim
from scipy.stats import spearmanr as sp
import pandas as pd

model = gensim.models.KeyedVectors.load_word2vec_format('/media/jaya/study stuffs/IITM/2nd_sem/NLP/NLPpa1/google/GoogleNews-vectors-negative300.bin', binary=True)

#word = model.similarity(word1,word2)
df = pd.read_csv('/media/jaya/study stuffs/IITM/2nd_sem/NLP/NLPpa1/google/combined.csv')
word1 = df.values[:,0]
word2 = df.values[:,1]
score_353 = df.values[:,2]
  

scores =[]
for k in range(len(df)):
	tmp = model.similarity(word1[k],word2[k])
	scores.append(tmp)

cor  = sp(scores,score_353)
print(cor)
