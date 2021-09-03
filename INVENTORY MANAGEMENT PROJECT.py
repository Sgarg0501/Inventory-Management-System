#!/usr/bin/env python
# coding: utf-8

# In[1]:


record={1001:{"name":"Kitkat","pieces_avai":100,"price":10,"exp":"10 Jan 2022","net_quantity":"10 g"},
        1002:{"name":"Kitkat","pieces_avai":80,"price":20,"exp":"9 Jan 2022","net_quantity":"20 g"},
        1003:{"name":"Kitkat","pieces_avai":120,"price":60,"exp":"10 Jan 2022","net_quantity":"60 g"},
        1004:{"name":"Dairy_milk","pieces_avai":100,"price":10,"exp":"9 Jan 2022","net_quantity":"10 g"},
        1005:{"name":"Dairy_milk","pieces_avai":90,"price":50,"exp":"10 Feb 2022","net_quantity":"30 g"},
        1006:{"name":"Dairy_milk","pieces_avai":100,"price":90,"exp":"7 Jan 2022","net_quantity":"100 g"},
        1007:{"name":"MilkyBar","pieces_avai":80,"price":10,"exp":"10 Apr 2022","net_quantity":"10 g"},
        1008:{"name":"MilkyBar","pieces_avai":60,"price":100,"exp":"10 Jan 2022","net_quantity":"60 g"},
        1009:{"name":"MilkyBar","pieces_avai":100,"price":200,"exp":"10 Feb 2022","net_quantity":"80 g"},
        1010:{"name":"Perk","pieces_avai":100,"price":20,"exp":"10 March 2022","net_quantity":"10 g"},
        1011:{"name":"Perk","pieces_avai":80,"price":40,"exp":"10 Feb 2022","net_quantity":"20 g"},
        1012:{"name":"Perk","pieces_avai":100,"price":60,"exp":"9 March 2022","net_quantity":"30 g"},
        1013:{"name":"Chocos","pieces_avai":100,"price":80,"exp":"10 Apr 2022","net_quantity":"50 g"},
        1014:{"name":"Chocos","pieces_avai":100,"price":100,"exp":"9 Jan 2022","net_quantity":"100 g"},
        1015:{"name":"Chocos","pieces_avai":100,"price":150,"exp":"10 March 2022","net_quantity":"150 g"},
        1016:{"name":"Chocos","pieces_avai":100,"price":200,"exp":"10 Feb 2022","net_quantity":"200 g"},
        1017:{"name":"Coke","pieces_avai":90,"price":50,"exp":"10 Apr 2022","net_quantity":"50ml"},
        1018:{"name":"Coke","pieces_avai":100,"price":100,"exp":"9 Jan 2022","net_quantity":"100ml"},
        1019:{"name":"Coke","pieces_avai":80,"price":150,"exp":"8 Feb 2022","net_quantity":"150ml"},
        1020:{"name":"Coke","pieces_avai":100,"price":200,"exp":"10 Jan 2022","net_quantity":"200ml"},
        1021:{"name":"Frooti","pieces_avai":100,"price":50,"exp":"10 Apr 2022","net_quantity":"50ml"},
        1022:{"name":"Frooti","pieces_avai":80,"price":100,"exp":"10 Feb 2022","net_quantity":"100ml"},
        1023:{"name":"Frooti","pieces_avai":100,"price":150,"exp":"9 Jan 2022","net_quantity":"150ml"},
        1024:{"name":"Frooti","pieces_avai":100,"price":200,"exp":"10 Apr 2022","net_quantity":"200ml"},
        1025:{"name":"Mirinda","pieces_avai":100,"price":70,"exp":"10 March 2022","net_quantity":"70ml"},
        1026:{"name":"Mirinda","pieces_avai":50,"price":140,"exp":"10 Feb 2022","net_quantity":"140ml"},
        1027:{"name":"Mirinda","pieces_avai":80,"price":200,"exp":"10 Apr 2022","net_quantity":"200ml"},
        1028:{"name":"Mirinda","pieces_avai":100,"price":230,"exp":"10 Jan 2022","net_quantity":"230ml"},
        1029:{"name":"Appy","pieces_avai":100,"price":100,"exp":"10 Feb 2022","net_quantity":"100ml"},
        1030:{"name":"Appy","pieces_avai":100,"price":200,"exp":"10 Jan 2022","net_quantity":"200ml"}}

        
        
        


# In[2]:


import json
js=json.dumps(record)
js


# In[3]:


fd=open("record.json",'w')
fd.write(js)
fd.close()


# In[4]:


fd=open("record.json",'r')
tex=fd.read()
print(tex)
fd.close()


# In[5]:


record=json.loads(tex)
x=record.keys()
x
Total_sales=0


# In[10]:


ui_name=input("enter name of user: ")
ui_pho=input("enter phone number of user: ")
ui_prod=input("enter the product id: ")
ui_quan=input("enter product quantity: ")
ui_gender=input("Gender: ")
ui_quan=int(ui_quan)
flag=0
for i in x:
    if(ui_prod==i):
        flag=1
        if(ui_quan>int(record[i]['pieces_avai'])):
            print("We do not have sufficient amount of stock and available stock quantity is: ",record[i]['pieces_avai'])
        else:
            print("Name: ",record[i]['name'])
            print("Pieces: ",record[i]['pieces_avai'])
            print("Price: ",record[i]['price'])
            print("Expiry: ",record[i]['exp'])
            print("Net_Quantity: ",record[i]['net_quantity'])
            print("Amount: ",ui_quan*record[i]['price'])
            Total_sales=Total_sales+ui_quan*record[i]['price']
if(flag==0):
    print("Product is not available")


# In[11]:


new_record={}
for i in x:
    if(ui_prod==i and ui_quan<=int(record[i]['pieces_avai'])):
        record[i]['pieces_avai']=str(int(record[i]['pieces_avai'])-ui_quan)
    new_record[i]=record[i]
print(new_record)


# In[12]:


js=json.dumps(new_record)
js
fd=open("record.json",'w')
fd.write(js)
fd.close()
fd=open("record.json",'r')
tex=fd.read()
print(tex)
fd.close()


# In[13]:


sale={}
sale["User_Name"]=ui_name
sale["User_required_product_id"]=ui_prod
sale["User_quantity_required"]=ui_quan
sale["User_phoneno"]=ui_pho
sale["User_Gender"]=ui_gender
sale["User_Amount"]=Total_sales

js=json.dumps(sale)
js
fd=open("sales.json",'a')
fd.write(js)
fd.close()
fd=open("sales.json",'r')
tex=fd.read()
print(tex)
fd.close()

