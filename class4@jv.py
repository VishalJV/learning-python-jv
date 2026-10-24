## similarities and differences in lists and tuples
## list                 tuple 
## ordered              ordered 
## allow duplicate      allow duplicate 
## allow diff data type   allow diff data type 
## mutable                not mutable 
## SET 
# denoted by {}    <----------set
## set is not ordered not duplicate value only unique elements ,not indexed 
set={"a","a"}
print(set) ## set mai  only different values store kr skte h if you stror the same values agaioni and agian then it will ignore the repeated values 
## set mai list store nhi krskte 
s1={}  # empty set not like this  
## empty set is made like this 
print(s1)   
# question can we convert the list to set?   ANS = Yeppp

s2 = {10,20,10,13,99,40}
print(s2) ## allow 
#s2={[10,20],[2,4,5,6]}  ## error unhashable type: 'list'
print(s2)
## indexing nhi h na so we cant run the range loop in the set but we can use the other method in this like (for i in s2)  we can use this 
#################__________SET OPERATIONS__________####################
s2.add("vishal")
s2.remove(10)
print(s2) ## here we use addd and remove kahi bi add ho jayega no indexing naa so mehnat not required 
## UNION 
sa={1,2,3}
sb={3,4,5}
print(sa | sb)  ## dono set mai union kedenge
print(sa & sb)  ## dono set mai intersection output denge
print(sa - sb)  ## s1 set se s2 set remove ke denge
print(sb - sa)  ## s2 set se s1 set poora nikalenge 
print(sa ^ sb)  ## dono set se union krke undono sets kaa intersection remove ke denge
