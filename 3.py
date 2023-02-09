stroka43234 ="ab2{g}3{a2{fg}}"



def sam (stroka,mnog) :
   
    conv1 = True
    conv2 = True
    shcetchik_vlog =int(0) 
    i = 0
    vlog = False
    vihod=str()
    stroka1 =str()
    
    for i in range(len(stroka)) :
        print(stroka[i])
        print(i)
        if (stroka[i] == "}") and (shcetchik_vlog == 0):
            vlog = False
            print(stroka1)
            vihod += sam(stroka1,kolvo_iter)
            stroka1 = str()
            continue
        if (stroka[i] == '{') and (not vlog):
            vlog = True
            stroka1 = str()
            continue
        if vlog:
            if stroka[i] == '{':
                shcetchik_vlog+=1
            if stroka[i] == '}': 
                shcetchik_vlog-=1
            stroka1 += stroka[i]
            
            continue
        try:
            int(stroka[i])
            conv1 = True
        except ValueError:
            conv1 = False
        try:
            int(stroka[i+1])
            conv2 = True
        except ValueError:
            conv2 = False

        if conv1:
            stroka1+=stroka[i]
            if not conv2:
                kolvo_iter=int(stroka1)
            continue      
       
        vihod += stroka[i]    
    return vihod * mnog        


print (sam (stroka43234, 1))

# str = "qwer"
# for i in range(len(str)):
#     print(i)




# try:
#             int(stroka[i])
#             stroka1+=stroka[i]
#         except ValueError:
#             continue
#         try:
#             int(stroka[i+1])
            
#         except ValueError:
#             continue