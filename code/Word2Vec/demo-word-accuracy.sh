make

#time ./word2vec -train text8 -output Model.txt -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15

echo PLEASE CHECK INPUT Model NAME AND testfile name 


echo "please check for value of N and if condition"

./compute-accuracy1 Model.txt  < test1.txt
./compute-accuracy2 Model.txt  < test1.txt
./compute-accuracy3 Model.txt  < test1.txt



# to compute accuracy with the full vocabulary, use: ./compute-accuracy vectors.bin < questions-words.txt
