odd = [1,3,5,7,9]
even= [2,4,6,8,]

#min, max, len are the functions

print(max(even))
print(min(even))
print(max(odd))
print(min(odd))
even.append(10)  # append is method called on even object and 10 is argument. It comes as python built int method
print(len(even))
print(len(odd))
print(even)
print("mississpie".count("is"))

empty_list=[]
odd = [1,3,5,7,9]
even= [2,4,6,8,]

merge = even+odd
print(merge)

sort_list=sorted(merge)
print(sort_list)
# creating a list from different methods below
more_num=list(merge)  #1
#more_num=merge[:]  #2
#more_num=merge.copy()  #3

charsort=sorted("789456123")
print(charsort)
cre_list=list("789456123")
print(cre_list)
more_sort_list=list(sort_list)
print(more_sort_list)