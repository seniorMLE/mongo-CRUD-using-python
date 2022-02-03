import pymongo
import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()

from sklearn.cluster import KMeans


connection_url="mongodb://localhost:27017/" 

client=pymongo.MongoClient(connection_url)
client.list_database_names()   # To display the databases we use list_database_names() method.
database_name="first"
student_db=client[database_name]    
collection_name="firstApp_geeksmodel"  
collection=student_db[collection_name]
student_db.list_collection_names() #To list the available collections in a database we can use the below command.

############################################## Insert collections
#insert single document into collection        
# document={"Name":"Raj",
# "Roll No":  153,
# "Branch": "CSE"}
# response = collection.insert_one(document)

# #insert multidocuments into collection
# documents=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},
#            {"Name":"Rahim","Roll No":155,"Branch":"CSE"},
#            {"Name":"Ronak","Roll No":156,"Branch":"CSE"}]
# res = collection.insert_many(documents)

# print(res.inserted_ids)

############################################## Read the data from the collection
#Retrieving single document
# query={"Name":"Raj"}
# print(collection.find_one(query))

# #Retrieving multiple documents
# query={"Branch":"CSE"}
# result=collection.find(query)
# for i in result:
#     print(i)
    
#To retrieve all the documents
context =[]
result=collection.find({}) #.limit(2)
for i in result:
#    print(float(i["score"]))
    context.append(float(i["score"]))
  
    
a = len(context)


x = []
for i in range (0, a):
    x.append(i)
#print(x)
#print(context)
x = np.array(x)
y = np.array(context)
#print(x)
#print(y)
#plt.scatter(x,y)
xx=np.array([x,y])
xx=xx.transpose()

model = KMeans(n_clusters = 6)                     

model.fit(xx)              

labels = model.predict(xx)              
labels = labels+0
print(labels)
xs = xx[:,0]       
ys = xx[:,1]           
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(xs,ys,c=colors[labels])              

centroids = model.cluster_centers_              

centroids_x = centroids[:,0]       
centroids_y = centroids[:,1]              

plt.scatter(centroids_x,centroids_y,marker='D', s=50)       
plt.show()  




#context["dataset"] = result     
#s = context["dataset"]

#print(result[1])
#scorejson = result['id'][0]
#print(scorejson)



# #filter query 
# query={"Roll No":{"$eq":153}}
# print(collection.find_one(query))

############################################## Update the data from the collection    
#Update single document
# query={"Roll No":{"$eq":153}}
# present_data=collection.find_one(query)
# new_data={"$set":{"Name":'Ramesh'}}
# collection.update_one(present_data,new_data)



# #Update multiple document
# present_data1={"Branch":"CSE"}
# new_data1={"$set":{"Branch":"ECE"}}
# collection.update_many(present_data1,new_data1)    
    
############################################## Delete the data from the collection   
# Delte single document
# query={"Roll No":153}
# collection.delete_one(query)

# #Delete multiple document
# query={"Branch":"ECE"}
# collection.delete_many(query)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    