# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:23:00 2019

@author: shekh
"""

ff = open('train.txt','r',encoding='utf-8')
A = ff.readlines()
B = [line.split('\t')[0] for line in A]

C= []

my_string = ''
 
for i,word in enumerate(B):
    if word=='meta':
       if i!=0: 
            C.append(my_string)
            my_string = ''
    else:
        my_string+=' '+ word 
        
f=open('train_test_cleaned.csv','w',encoding='utf-8')
f.writelines(['tweet\n'])        
f.writelines(C)
f.writelines(CC)
f.close()

indices = [i for i, x in enumerate(A) if x[0:4] == 'meta']

sentiment = []

for i in indices:
    sentiment.append(A[i][-9:-1])
    
sentiment = [x.replace('\t','') for x in sentiment]
sentiment1 =[]
for i in sentiment:
    if i == 'positive':
        sentiment1.append(i)
    if i == 'negative':
        sentiment1.append(i)  
    if i == 'neutral':
        sentiment1.append(i)    
del sentiment1[-1]    
sentiment1 = [x.replace('positive', '0') for x in sentiment1]
sentiment1 = [x.replace('neutral', '1') for x in sentiment1]
sentiment1 = [x.replace('negative', '2') for x in sentiment1]
sentiment1 = [x+'\n' for x in sentiment1]

f=open('sentiment_cleaned.csv','w',encoding='utf-8')
f.writelines(['sentiment\n'])        
f.writelines(sentiment1)
f.writelines(sentiment2)
f.close()





