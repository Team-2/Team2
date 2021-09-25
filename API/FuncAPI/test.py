from API.Show.make_app import client

res = client.get('/ship/3' )
print(res.get_json())
res = client.get('/ship/all')
print(res.get_json())
# r