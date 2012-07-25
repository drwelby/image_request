#!/bin/bash

# Get the API
# curl -v http://localhost:8000/rfi/api

# Add add a request
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/

# Test - request must have a requestor name
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"} }'  http://localhost:8000/rfi/api/rfi/

# Test - request must have geometry
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{ "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/

# Test - request must have valid geometry in bounds
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[11], [30, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/

# Test - request bounds must be a polygon
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[30, 11], [30, 9], [31, 9], [31, 11], [30, 11]], "type": "LineString"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/

# Test - request bounds must be valid geographic coordinates
curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"bounds": {"coordinates": [[[30, 11], [300, 9], [31, 9], [31, 11], [30, 11]]], "type": "Polygon"}, "requestor_name": "Curl Request"}'  http://localhost:8000/rfi/api/rfi/
