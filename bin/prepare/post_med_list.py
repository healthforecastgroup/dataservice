fname = u'rxnorm_mappings.txt'

with open(fname,'r') as f:
    content = f.read()
raw_drug_list = content.split('\n')
drug_list = []
for n,drug in enumerate(raw_drug_list):
    #print(drug.split('|'))
    try:
        (ha,num,rxcui,name,what)=tuple(drug.split('|'))
        drug_list.append(
            {'rxcui':rxcui,
            'drugname':name,}
        )
    except:
        pass

print(len(drug_list))

# persist to db
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.hfg
lib_drugs = db.lib_drugs
result = lib_drugs.insert_many(drug_list)
