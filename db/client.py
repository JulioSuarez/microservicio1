from pymongo import MongoClient


db_client = MongoClient(
    "mongodb+srv://julicosuarez:C4u25fum!@cluster0.rcirqnd.mongodb.net/?retryWrites=true&w=majority").test
    # "mongodb+srv://julicosuarez:C4u25fum!@cluster0.rcirqnd.mongodb.net/test?retryWrites=true&w=majority")

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/
