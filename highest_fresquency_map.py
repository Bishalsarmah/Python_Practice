n = [1,2,4,1,7,6,2,1,8,7]
dic ={}
for i in range(0,len(n)):
    if n[i] in dic:
        dic[n[i]] += 1
    else:
        dic[n[i]] = 1
high_key = max(dic, key = dic.get)
print(dic)
print(f"key with highest frequency is {high_key} and which has occured {dic[high_key]} times")