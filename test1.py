mydict ={'surender': ['abcd','surender.kumar',5000] , 'rakesh': ['abcd','rakesh.kumar',10000]}
user_input= input("Enter your username : " )
if user_input in mydict:
    a = input("kindly provude your password : ")
    if a in mydict[user_input][0]:
        result = list(mydict[user_input])
        print ('your wallet value is :', result[-1])
    else:
        print ("Password is not correct")
else:
        print ("USer NAme is not correct")

