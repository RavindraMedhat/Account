list_person=[]
money_for_person=[]
finel_money=[]
temp=[]

i=0 # number of friends
work=7485


while work!=0 :
    if i<2:
        list_person.append(input("enter name of person :-"))
        i+=1
        temp.append(i)      # i=0
    else:
        work=int(input("Enter 0 for exit\nOr enter nonzero for add mor:-"))
        if work != 0:
            list_person.append(input("enter name of person :-"))
            i+=1
            temp.append(i)      # i =0

id =1

print("list of person :-")
for x in list_person:
    print(f"Name :- {list_person[id-1]}  ID :- {id}")
    id += 1

for x in range(i):
    finel_money.append([])
    money_for_person.append([])
    for y in range(i):
        money_for_person[x].append(0)
        finel_money[x].append(0)

# print(money_for_person)

end=7485
spand_id=0
spand_money=0

while end!=0 :
    spand_id=int(input("\nEnter id of person who spand money :-"))-1

    spand_money=int(input("enter money to spand :-"))

    ii=0
    work = 1
    temp = []
    while work != 0:

        temp.append(int(input("\nenter id of person for whom you spand money :-"))-1)
        ii += 1

        if ii != i:
            work = int(input("\nEnter 0 for exit\nOr enter nonzero for add person for mone spand more :-"))
        else:
            work = 0

    # print(money_for_person)
    # print(temp)

    for x in temp:
            # print("\nx=",x)
            # print("money_for_person[x]=",money_for_person[x])
            # print("money_for_person[x][spand_id]=",money_for_person[x][spand_id])

            money_for_person[spand_id][x] = money_for_person[spand_id][x] + (spand_money / ii)

            # print("money_for_person[x][spand_id]=",money_for_person[x][spand_id])
            # print("money_for_person[x]=",money_for_person[x])
            # print("money_for_person=",money_for_person)
            # money_for_person[spand_id][x] = money_for_person[spand_id][x] + (spand_money / ii)

    end = int(input("\nEnter 0 for exit\nOr enter nonzero for spand more money :-"))

for w in range(i):
    for x in range(i):
        finel_money[w][x]=money_for_person[w][x]-money_for_person[x][w]


for w in range(i):
    for x in range(i):

        if finel_money[w][x]<0:
            print(f"\n{list_person[w]} has to give {(finel_money[w][x])*(-1)} rupees to {list_person[x]}")
