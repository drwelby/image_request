import requests
url = 'http://localhost:8000/rfi/api/rfi/'
headers = {'Content-Type' : 'application/json'}

# Get the API
# curl -v http://localhost:8000/rfi/api
def get_api_test():
    r = requests.get(url)
    assert r.status_code == 200

# Add a request
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
def add_request_test():
    data = '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'
    r = requests.post(url, data=data, headers=headers)
    print r.text
    assert r.status_code == 201

# Test - request must have a requestor name
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"} }'  http://localhost:8000/rfi/api/rfi/
def has_name_test():
    data = '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"} }'
    r = requests.post(url, data=data, headers=headers)
    assert r.status_code == 400

# Test - request must have geometry
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{ "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
def has_geom_test():
    data = '{ "requestor_name": "Curl Request"}'
    r = requests.post(url, data=data, headers=headers)
    assert r.status_code == 400

# Test - request must have valid geometry in bounds
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
def valid_geom_test():
    data = '{"bounds": {"coordinates": [[[11], [30, 9], [31, 9    ], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'
    r = requests.post(url, data=data, headers=headers)
    assert r.status_code == 400
 
# Test - request bounds must be a polygon
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]], "type": "LineString"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
def poly_geom_test():
    data = '{"bounds": {"coordinates": [[30, 11], [30, 9], [31    , 9], [31, 11], [30, 11]], "type": "LineString"}, "requestor_name": "Curl Request"}'
    r = requests.post(url, data=data, headers=headers)
    assert r.status_code == 400

# Test - request bounds must be valid geographic coordinates
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [300, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
def valid_bounds_test():
    data = '{"bounds": {"coordinates": [[[30, 11], [300, 9], [    31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'
    r = requests.post(url, data=data, headers=headers)
    assert r.status_code == 400

