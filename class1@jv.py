marks=[85,75,65,78,69]
sum=0
for i in range(len(marks)):
    sum+=marks[i]
print(sum/len(marks))
for i in range(4):
    name=str(input())
    dob=int(input())
    student=[name,dob]
    print(student[i])
#indexing th eelements in the lists are same as the indexing in strings starts from 0 untill its len -1 the same concept applies here too 
#___________________________first topic_________________________ (concatenation concept in lists )
#ippudu naa daggaraa oka list undi  daaniki nen oka element concatenate chestunna just like  i did in string 
list1=[1,2,3,4,5]
list1=[0]+list1
# print(list1)
# ## important thing to notice in this is manamm order ela istunnam anedi chaala important ikkada  
# # case1---
list1=list1+[9,0]
print(list1)   #----- ee output verey untadi 
#case2---
list1=[9,0]+list1
print(list1)     #--- ee output verey untadi 
# # i thing order importance is clear for you now........
# #_______________________2nd topic____________________ (nested lists)
sm_lst=[1,["a","b","c"],2,3,44,[1,3,5,7,9]]
# # as the name suggest the concept in this is nested lists 
print(sm_lst[5])
print(sm_lst[1][2])   #   <--------------- this shows us to access the nested list elements using series of []
## as we studied in strings -ve indexing is also a part of the lists 
## here we can use the -ve indexing as a better approach while working with lists that need any reverse operations or something like that
## lists are mutable ( matlab manam lists ni modify cheskovacchu unlike strings and tuples( actually tupules antey endo kuda naaku telvadu aina kuda nen aa example vaaduthuunnna so be carefull at this paricular point ))
# #______________________topic 3_________________________   (append or extend)
lista=[1,2,3]
lista.append(9) ## append can take upto 1 argument only not more than that......
print(lista)
lista.extend('4456')  # <------------- this is extend idi em chestadi antey multiple arguments ni oke saari add chestadi in the list by the order only string ne add chestindi not integers or floating values
print(lista)
#________________________topic 4_________________-----( remove(), pop() and clear())
# remove em chestadi antey aa given item ni total list nundey remove chestundi 
# foe example 
lista=["v","i","s","h","a","l","v","c"]
lista.remove("v") ###############----------remove
print(lista)  #<----------- this remove anedi only first time aa item dorkinappudu maatrame danni rmove chestundi not from the whole list 
# simple ga cheppali antey manaki eppudaithey given item first time vastundo aa list nundi aa item matrame only one time matrame remove aytundi if there arre multiple items we cant delete allof them 
lista.pop(2)  ##<-------- ee command enduku use avuthadi antey if we wnat to remove a specific index element then we need to use pop function manaki ee indexing itemm remove kaavalo andulo pop function lo istey the list will be updated
print(lista)
lista.clear()#<----------- ee commmand clear aa list total ni clear chestundi all the data in the list is gone we use this to empty a list 
print(lista)#################--------------clear
lista.insert(0,"iam")
lista.insert(1,"jogu")
lista.insert(2,"vishal")
print(lista)
b=lista.copy()  #<------------ cpoy function em chestadi antey manaki unnna list ni as it is copy chestadi and we can store it in a single variable 
print(b)
'''
sum=0
lista=[1,2,3,sum] #  lists lo kudaa variables ni store cheskovacchu
print(lista)

'''
list1=[1,22,3]
list2=[2,3,4]
list1.append(4)
list2.extend("vishal")
print(list1)
print(list2)                ## extend aney function multiple elements ni add chestundi as you can see the rseult 
                            ## result =[2, 3, 4, 'v', 'i', 's', 'h', 'a', 'l']  adey nen integr istey error vastundi enduku ?
lest=list1+list2
print(lest)                 ## concatenation of lists (order change ayyindi see )
                            ##[1, 22, 3, 4, 2, 3, 4, 'v', 'i', 's', 'h', 'a', 'l'] numbers first and alphabets next vaccinay
                            ## * operator repeats the no of times the list just like strings maawa
lest                          
del lest[6]                 #<<-- ee vidhanga del keyword ni use chestamu 
print(lest)                 # del can also delete the entire list
del lest[:]                 # del ni two types gaa use cheyyochhu 
print(lest)                 # Alternative Best Practice: clear() vadatam maawa just list ni clear chestundi 

vishal=["vi",'sh','al']
a=vishal.pop(2)                # pop anedi input lo index teeskuntundi 
print(a)                        # pop lo index ivvaka pothey lsat item ni peeki istundi 
                                # remove anedi mana list lo nundi remove chestundi manam icchina input ni 
#vishal.remove(1)               # if manam ichhina input list lo lekapothey error vastundi  == ValueError: list.remove(x): x not in list                 
print(vishal)

# ## append   extend insert  remove pop clear  index 
var=[99,98,97]
b=list(enumerate(var))          #enumerate() ni real-world programming lo pradhanan ga loop run avthunappudu element tho paatu daani position (index) kooda avasaramaina prathi scenario lo vadathamu.
print(b)
list0=[1,'a','b','c','d',3,4,5,2,1,3,4,1,2,4,'a','b']
list2=[]
for i in list0:
    if i not in list2 :
        list2.append(i)
        #list2.sort() 
print(list2) 
list3=[]          # strings and numbers unnappudu sort panicheyyadu error vastundi raa
for item in list2:
    if type(item)==int:
        list3.append(item)
list3.sort()
print(list3)
list4=[]
for item in list2:
    if isinstance(item,int):
        list4.append(item)
list4.sort()
print(list4)
###################################################################################################################################################################################
# looping through lists ************************************************************

fruits=["apple","banana","mango","dragon fruit"]
for fruit in fruits:                    ## one way of accessing all the elements in the list 
    if fruits[0]=="apple":
        print(fruits)
        break
for i in range(len(fruits)):            ## second way of accessing elements in the list
    print(fruits[i])                    ## mujhe this output gives me each element and takes the next element into the next line

[print(x)for x in fruits]               ## third method for accessing all the elements in the list ye bhi each element new line mai print krega
                                        # this is also called short hand for loop 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  
newlist = [x for x in fruits if "a" in x]  ## short hand loop practice krlo JV
print(newlist) 

                                              ## THE END OF LISTS 

#____________________________________________________TUPLES ______________________________________________________________________________________________________________________________
# tuples anevi immmutable avi oka saari input teeskunna tarvatha change cheyyalevu raa 
#single ton tuple 
t=(2,)                              ## , lekapothey manam interpreter dannni integer laga interpret chestundi so we use , for distinguishing between integer and tuple
print(type(t))                      ## <class 'tuple'>
t=()
t1=(1,2,3)
t2=t+t1
print(t2)                           ## tuples can be concatenated repeated indexed and sliced 
#                                     ## ordering and indexing untundi deenilo kuda only idi immutable anthey 
tv=(1,2,3)
#tv.append(2)                          ## AttributeError: 'tuple' object has no attribute 'append' append cheyyalevu raa
#del tv[2]                             ## TypeError: 'tuple' object doesn't support item deletion
#b=tv.pop(1)                           ## AttributeError: 'tuple' object has no attribute 'pop'
#tv.remove(1)                          ## AttributeError: 'tuple' object has no attribute 'remove'
b=tv.count(1)                          ## count chestadi but return cheyyadu aa value ni so oka variable lo store cheskoni daanini print cheskuntam
c=tv.index(4)                          ## inndexing support chestadi but indexing lo icchina element mana tuple lo leka pothey error  vastadi (ValueError: tuple.index(x): x not in tuple)
print(b)                               ## reuturning value of the count 
# print(tv)
## nested tuples 
vishal=(99,98,97)
vishal1=[1,1,1,2]
marks=(0,10,20,vishal,vishal1)
vishal1.append(999)
print(marks)                             ## (0, 10, 20, (99, 98, 97)) tuple inside tuple
                                         ## tuple lopala unna list changable enduku antey the tuple is taking values from the memory address of the list manam list change cheyyochhu but adi tuple error raadu
                                         ## coz the tuple anedi list memory address nundi values ni access chestundi adi fixed gaa undadi only for lists in tuples 
                                         ## a tricky problem( Anduke tuples lopalunna lists ni modify cheyyalante eppudoo .append() or .extend() use cheyyali, += joliki vellakoodadhu.)
                                         ## list loki manam anukunna value add aytundi but assignment of the tuple daggara error vastundi it adds but also shows error
#marks(3).clear()      #******************#***## so tuple lopala unna lists ni reassign cheyyodddu only daani data ni update cheyyali without changing its address(memory address) antheyy             
#print(marks)
vishal1.append("appending done!!!")
print(marks)


  ############## (UNPACKING SEQUENCES) ##############

# assignment of multiple variables to a tuple
det=('Vishal',19,'CSE','Telangana') ## both list and tuples mai ye concept work krta h
name,age,branch,place=det           ## both sides length equal honi cahiye varna error aajaega
print(name)             ## Vishal   ## ValueError: not enough values to unpack (expected 4, got 3)
print(age)              ## 19 
print(branch)           ## CSE
print(place)            ## Telangana
vishal=(99,98,97)
a,*b=vishal
print(a)                  ## 99
print(b)                  ## [98, 97] migitha values oka list lo store aythai not individual important raa gurthupettuko LIST LO STORE AYTHAI NOT INDIVIDUAL
# the reason behid this is goes to the devlopment of python manaki actually mundu enni iterations jaruguthayo teliyadu 
# for example oka range generator undi python ki manam enni iterations generate aythao  mundey teliyadu so if we want to store it in a tuple it much more complicated enduku antey mottam enni iterations aythunnayo manaki mundu teliyadu kabatti 
# so mari list eyy enduku use chestunnam antey append and extend easy gaa cheskovacchu kabatti iterations jaruguthuuntai and list lo ee results add aythu untai so adi oka reason and also manaki length of the list tho problem eyy ledu 
#so that's why python devlopers list gaa output raavadaniki set chesaru thats the reason we are getting lists when we unpack tupels or sets or dictionaries 
 
vishal=('first',2,3,4,5,6,'last')
lst=[]
a,*b,c=vishal
for i in vishal:
    if i>3:                 ## tuple lo unna elements ni nen oka kottha list lo easy gaa append cheyyochhu not that big deal 
        lst.append(i)       
print(lst)
print(a)  # <--- first element 
print(b)  # << the starred one will be in the form of lists not individual (i think JV got the idea why thr developers starred the variable )
print(c)  # <--- last element 