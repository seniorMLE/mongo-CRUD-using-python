
from pymongo import MongoClient



# initialized the Flask APP


class Crud:  # MongoDB Model for ToDo CRUD Implementation
    def __init__(self, data):   # Fetchs the MongoDB, by making use of Request Body
        self.client = MongoClient("mongodb://localhost:27017/")
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def insert_data(self, data):    # Create - (1) explained in next section
        new_document = data
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output
    
    def insert_data_many(self, data):    # Create - (1) explained in next section
        new_document = data
        response = self.collection.insert_many(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_ids)}
        return output

    def read_all(self):                 # Read - (2) explained in next section
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    
    def read_multi(self, query):                 # Read - (2) explained in next section
        documents = self.collection.find(query)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output
    
    def read_single(self, query):                 # Read - (2) explained in next section
        documents = self.collection.find_one(query)
        output = documents
        return output

    def update_single(self,data):          # Update - (3) explained in next section
        filter = data['Filter']
        present_data = self.collection.find_one(filter)        
        updated_data = {"$set": data['DataToBeUpdated']}
        response = self.collection.update_one(present_data, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    
    def update_many(self,data):          # Update - (3) explained in next section
        filter = data['Filter']
        updated_data = {"$set": data['DataToBeUpdated']}
        response = self.collection.update_many(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete_single(self, data):    # Delete - (4) explained in next section
        filter = data
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    
    def delete_many(self, data):    # Delete - (4) explained in next section
        filter = data
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    
    def delete_all(self ):    # Delete        
        self.collection.drop({})
        



data = {"database":"student_database",
        "collection":"computer science"        
        }
documents=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},
           {"Name":"Rahim","Roll No":155,"Branch":"CSE"},
           {"Name":"Ronak","Roll No":156,"Branch":"CSE"}]
document={"Name":"Raj",
          "Roll No":  153,
          "Branch": "CSE"}

query_single = {"Name":"Raj"}
query_multi={"Branch":"CSE"}

# create databasse and delete all the collections and insert documents and read single {"Name":"Raj"}
test = Crud(data)  #create database and collection
test.delete_all()
test.insert_data(document)
out = test.read_single(query_single)
#print(out)

# delete_all()

test.insert_data_many(documents)
out = test.read_all()
#print(out)


will_update_data = {"Filter":{"Branch":"CSE"},
        "DataToBeUpdated":{"Branch":"ECE"}}
test.update_single(will_update_data)
out = test.read_all()
#print(out)

test.update_many(will_update_data)
out = test.read_all()
print(out)

test.delete_single(query_single)
out= test.read_all()
#print(out)

test.delete_all()
out =test.read_all()
print(out)

























