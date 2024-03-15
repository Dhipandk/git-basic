import pymongo
import requests
client = pymongo.MongoClient("mongodb+srv://dhipandhanush57:TmgTq6UTs8ke2Y4A@cluster0.lihz0qa.mongodb.net/")
db = client.sample_mflix 
collection = db.movies
items = collection.find().limit(5)
hf_token=""
embedding_url=""
def generate_embedding(text: str) -> list[float]:
    
    response = requests.post( embedding_url,
                    { headers ="Authorization": f"Bearer {hf_token}"}, 
                     json={"inputs": text})
    
    if response. status_code != 200:
        raise ValueError(f"Request failed with status code {response. status_code}: {response. text}")
    return response. json( )