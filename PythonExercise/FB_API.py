import facebook
import json

token = ['']
graph = facebook.GraphAPI(token)
fields = ['id, name, birthday, hometown']
profile = graph.get_object('me', fields = fields)
print (json.dumps(profile, indent=4))