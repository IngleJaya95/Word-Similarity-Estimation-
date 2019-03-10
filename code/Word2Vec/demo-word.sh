make

echo PLEASE CHECK INPUT FILE NAME AND OUTPUT MODEL NAME 



# for reuters.txt change cosine.py also 



time ./word2vec -train data.txt -output Model.txt -cbow 0 -size 200 -window 15 -negative 20 -hs 0 -sample 1e-4 -threads 20 -binary 0 -iter 20


#time ./word2vec -train reuters_data.txt -output Model.txt -cbow 0 -size 500 -window 4 -negative 20 -hs 0 -sample 0 -threads 20 -binary 0 -iter 15

./distance Model.txt



# please change model output at 2 places 1. after "-output" 2. after "./distance"
#if cbow =1 --> cbow 
#cbow =0 ---> skipgram
#size = embedding size 
#window = window size
#negtive = number of negative samples 
#hs = 
#sample = The subsampling randomly discards frequent words while keeping the ranking same
#threads =  
#binary = 
#iter = number of iterations 

