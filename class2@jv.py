# # ##pop concept 
# # #pop em chestadi antey remove the last one on the like pulling a book from a stack of books
# marks=[1,2,3,4,5,6,7,8]
# # marks.insert(2,"vishal")

# # print(marks)
# max=0
# min=marks[0]
# for i in range(len(marks)):
#     if marks[i]>max:
#         max=marks[i]
#     if marks[i]<min:
#         min=marks[i]
# print(max)
# print(min)


##################################  SETS  #################################
# represented by {} elements seperated by , not ordered , cannot contain repetative elements only unique ones are stored  , no fixed length .

# a=['apple','banana','mango','apple','guava','kiwi']    ## this is a list 
# a=set(a)                                               ## converting it into a set 
# print(a)                                               ## {'guava', 'mango', 'banana', 'apple', 'kiwi'}
# print(type(a))                                         ##<class 'set'>


# ## set addition (union)
# a={1,2,3}
# b={2,3,4}
# c=a | b                                                 ## {1, 2, 3, 4}
# print(c)


# ## set intersection (common values)
# a={1 , 2 , 3 , 4 , "vishal"}
# b={"vishal" , "CSE" , 1 , 2 , 3}
# c= a & b                                                  ## {'vishal', 1, 2, 3}  and represents the common values in the sets
# print(c)


# ## set difference                   
# a={1 , 2 , 3 , 4}
# b={0 , 9 , 8 , 7 , 6 , 5 , 4}                               ## remember (a-b) is not same as (b-a)
# c= a - b                                                    ## removing all the values of b from a
# d= b - a                                                    ## removing all the values of a from b
# print(c)
# print(d)


# ## set symmetric difference (total - intersection !!!)  ---> (A | B)-(A & B) ## refer the diagram in JV's notes (CSE notes)
# a={1,2,3,4,5,6,7}
# b={2,3,4,5,6,7,8,9,0,23,4,5,23434,24,324,456}
# c=a.symmetric_difference(b)
# print(c)                                                      ## {0, 1, 8, 9, 23434, 324, 456, 23, 24}


# ## clearing the set 
# a={12234,345,567,457,6478}
# a.clear()
# print(a)                                                        ## set() empty set hehehe


# ## copying a set 
# vishal={"vishal",19,"CSE"}
# c=vishal.copy()                                                  ## {19, 'vishal', 'CSE'}  see the order it doesnt matter in set it can be in any order
# print(c)                                                         ##  JV remember that here order doesn't matter i think you will forget this thing in set so its a warning to remember the point that order doesnot matter in set


# ## difference update 
# a={1,2,3,4,5,6,7,8,9,0}
# b={3,4,5,6,7,"vishal","Cd","github"}                                ## Python lo perulo _update ani unte (difference_update, intersection_update, update lanti methods), avi kotha set create cheyyakunda unna set ne in-place direct ga marchipothayi. Andukey vatiki return value undadu (None vasthundi).
# c=b.difference_update(a)                                           ## b lo a elements untey vaatini anni remove chestadi and directly set ni update chestadi doesnot returns a new one
# print(b)

## discarding of a set 
# a={"Vishal","Varshith","Mallesham","Manjula"}
# a.discard("Vishal")                                                 ## See ? you are not in your family
# print(a)                                                            ## {'Manjula', 'Mallesham', 'Varshith'}


# ## intersection of given sets
# a={1,2,3,4,54,5,65,6}                                               ## Andukey edo oka set ni base ga theesukuni daani meeda .intersection() ani call chestham:
# b={2,3,4,5,6,7,8,90,435}                                            ##********************* Base set edi theesukunna result maaradu**************
# c={"vishal",2,3,4,5,"mallesham"}                                    ## Mugguriki common ga unna elements kavali kabatti, evaro okarini reference (base) ga pettukuni migatha vaallani brackets lo petti compare chesthunnam, anthe!
# d={1}
# e=d.intersection(a,b,c)                                             ## set() emty set enduku antey there are no common values in all the sets 
# print(e)


## intersection_ update  ((remember all the update function existing sets ni update chestai they doesnot return a new set..............))
# a={'vishal',1,2,3,4,54,6,7,8,98,00,1234256,123434567}
# b={1,2,3,4,5,6,7,9,9,0,8567,56,37,1255,458,23}
# b.intersection_update(a)                                             ## intersection_update() anedi oka set lo unna elements lo kevalam common elements ni matrame unchi, migatha elements anni theesi padesthundi (in-place modification).
# print(b)                                                             ## aa set lo and given set lo unna commom elements ni unci migitha elements ni remove chestundi and aa first set ne update chestundi not any other ones 


# ## another example :: 
# a = {"Baahubali", "RRR", "KGF", "Pushpa"}
# b = {"RRR", "KGF", "Kalki", "Salaar"}

# # a meeda intersection_update call chesthunnam:
# a.intersection_update(b)

# print(a)
# # Output: {'RRR', 'KGF'}

# ## isdisjoint 
# a={1,2,3}
# b={7,8,9}
# print(b.isdisjoint(a))    ## i think bool return chestadi anukunta i think  yepppp its returning me a bool (True) 


# ## issubset 
# a={1,2,3,4,5}
# b={3,4,5}
# print(b.issubset(a))        ## idi kuda same bool return chestadi anukunta yepp its returning me a boolean value (True)


# ## issuperset 
# a={'vishal','syam','bruhan','aditya','akash','chaitanya',1,2,3,4,5}
# b={'vishal',1,2,3,4,5}
# print(a.issuperset(b))          ## super set condition Condition: Set $B$ lo unna prathi okka element, compulsory ga Set A lo kooda undali.
# ## a is superior set than b. Antey b lo unna anni elements a lo unnai but not the reverse case 
# ## first superior set raasi daani tarvartha migilina set raastham


# ## pop concept (in sets)
# set1={1,2,3,4,5}
# set1.pop()                                 ## TypeError: set.pop() takes no arguments (1 given) ikkada order pani cheyyadu so if you give a index it will give you error that in set pop doesnot takes any argument.
# print(set1)                                ## eeyy elment pop avutundo etla telustadi ??
# ## poped element manaki return vastundi  so no worries that to find which element is poped but we can'y predect which element would pop next adi hashing concept lo vastundi anta IDK hashing so leave it for now 
# ## # hash randomization 


# ## remove()    i think oka particular element ni remove cheyyadaniki use chestam anukunta 
# a={1,2,3,4,5,6,7,8,9,0}

# a.remove(7)
# print(a)                                      ## simple 

# ## symmetric difference                                         ## mundey cheppinattu [ A union B - A intersection B ]
# a={'BAHUBALI','KGF','RRR',"KALKI","PUSHPA"}
# b={"BAHUBALI","MAGADHEERA",'PUSHPA2','BAHUBALI2'}
# print(a.symmetric_difference(b))


# ## symmetric difference update 
# a={'BAHUBALI','KGF','RRR',"KALKI","PUSHPA"}
# b={"BAHUBALI","MAGADHEERA",'PUSHPA2','BAHUBALI2'}
# b.symmetric_difference_update(a)                                 ## B set ni change chestadi without the requirement of a new set direct b set ni update chestudi 
# print(b)                                                         ## works same as the symmetric difference but unna set lo ne modify cheyyaddanik manam update aney new type of function ni use chestam 

## union (basic)
a={1,2,3}
b={'vishal'}
print(b.union(a))                                                  ## return a set consisting of the union of given set
## basically inko variable lo store cehsukoni aa vasriable ni pront cheskovacchu but i choose the different way



## update()                                                        ## basically idi em chestundi antey its union and the given sets union ni manam icchina set lo update chestundi i think manam initially ichhina set ni modiify chestundi aukunta
a={1,2,3}
b={4,3,5,6}
a.update(b)                                                        ## yupp it updateed the initially given set with the unnion of every set given in the paranthesis
print(a)