from web3 import Web3
#fetch the nasdaq closing index on Sep.29 https://www.bloomberg.com/quote/CCMP:IND

Stockprice = 1925228
#assuming the closing index is 19252.28 (change this number to the real index of Sep.29) times 100

s=[]
for i in range(1000):
    s.append([i+1,Web3.sha3(i+1+Stockprice)])
#Calculating the hashes of each tokenID

p = sorted(s,key=(lambda x:x[1]))
#Sort 1000 hashes from small to large

for i in range(1000):
    print("image_id:"+str(i+1)+" for token_id "+str(p[i][0])+" with Hash:"+p[i][1].hex())
#Get the imageID corresponding to each TokenID
