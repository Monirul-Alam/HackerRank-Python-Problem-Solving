# number = range(int(input("value:")))
#
# for item  in number:
#     square =item*item
#     print(square)



#  another sollution
number = range(int(input("value:")))
print(*[num**2 for num in number],sep='\n')

# sep is use for speration .

# after print(  there is *, which is use for separation