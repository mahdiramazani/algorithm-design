import numpy

n=5
m=40 #وزن کوله پشتی

weight=[8,6,10,3,15,20]
value=[12,18,5,15,30,10]
final_value=0
sum_weight=0
result={}

array=numpy.random.randint(0,1,size=(n,3))


#division value / weight
for i in range(n):

    result[i+1]=value[i]/weight[i] 

#=============================================== sort dict =================================
sorted_footballers_by_goals = sorted(result.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_footballers_by_goals)
print(converted_dict)
#=========================================================================================================


for k,v in converted_dict.items():

    
    if ((weight[k-1] + sum_weight) <= m):

        final_value+=value[k-1]
 
        sum_weight+=weight[k-1]
       

    elif (weight[k-1] + sum_weight > m ):
   
        a= m - sum_weight

        if a>0:
    
            final_value+=(a / weight[k-1]) * value[k-1]
            sum_weight+=weight[k-1]

print(final_value)
