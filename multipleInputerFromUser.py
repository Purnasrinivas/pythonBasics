
//taking multiple inputs user
new_customer=True
name=input()
age=int(input())
if new_customer:
    print("Name of the new customer:{}\nage of the new customer:{}\nHe is a new customer".format(name,age))
else:
    print("get the name from database")
