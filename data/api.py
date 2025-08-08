import http.client

conn = http.client.HTTPSConnection("real-time-amazon-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "507af5a54bmsh16dc51ded399ee7p14ae28jsn06be26559850",
    'x-rapidapi-host': "real-time-amazon-data.p.rapidapi.com"
}

conn.request("GET", "/product-details?asin=B07ZPKBL9V&country=US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))