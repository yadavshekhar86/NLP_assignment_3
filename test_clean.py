# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 23:49:23 2019

@author: shekh
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:23:00 2019

@author: shekh
"""

ff = open('test.txt','r',encoding='utf-8')
A = ff.readlines()
B = [line.split('\t')[0] for line in A]

CC= []

my_string = ''
 
for i,word in enumerate(B):
    if word=='meta':
       if i!=0: 
            CC.append(my_string)
            my_string = ''
    else:
        my_string+=' '+ word 
        
f=open('test_cleaned.csv','w',encoding='utf-8')        
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
sentiment2 = [x+'\n' for x in sentiment1]

f=open('sentiment_test_cleaned.csv','w',encoding='utf-8')     
f.writelines(sentiment2)
f.close()