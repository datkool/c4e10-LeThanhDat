import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds139428.mlab.com:39428/pvc

host = "ds139428.mlab.com"
port = 39428
db_name = "pvc"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())