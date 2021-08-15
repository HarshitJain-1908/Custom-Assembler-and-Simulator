# str="Hello world in this summer"
# s1=str.split()
# print(s1)
# s2=' '.join(s1[1:])
# print(s2)

# dic={}
# dic["ans"]="hello"
# dic["yay"]="world"
# if("he" not in dic):
#     print(True)
# if("yay" in dic):
#     print(True)

def takeInput():
    ans=input()
    ans1=ans+'1'
    ans2=ans+'2'
    return ans1,ans2
l1,l2=takeInput()
print(l1,"----------",l2)