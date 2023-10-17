attendees = ["shyam", "ruthvika", "manasa", "mouni"]
print(attendees.clear())
print(type(attendees))
print(attendees)

attendees =["mouni", "ruthvika", "manasa"]
del attendees[0]
print(attendees)
del attendees


attendees1 = input("Enter Attendees Name:")
attendees2 = input("Enter Attendees Name:")
attendees3 = input("Enter Attendees Name:")
attendees=[]
attendees.append(attendees1)
attendees.append(attendees2)
attendees.append(attendees3)
print(attendees)


lst =[1,5,6,8,2,3,]
lst.sort()
print(lst)


lst=[1,5,6,2,3]
lst.reverse()
print(lst)


tpl =(1,2,3)
print(type(tpl))


tpl=tuple((1,2,3))
print(type(tpl))


tpl= tuple((1,2,3,1))
print(tpl.count(1))

tpl=tuple((1,2,3,1))
print(tpl.index(2))

tpl =list(tpl)
print(type(lst))
