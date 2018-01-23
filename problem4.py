yours=["yale","MIT","berkely"]
mine=["uw","umich","duke"]
ours1=mine+yours
print(ours1)
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours2)


yours[1]="ucla"
print(ours1)
print(ours2)

#ours1 is a new independent list, which is independent of changes in yours
#ours2 is an appended list, which is subject to changes in yours1


