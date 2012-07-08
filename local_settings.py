#Base url for GeoServer (no trailing slash)

GEOSERVER_BASE_URL = "http://localhost:5432"

# Eventually we'll set these in Geoserver via restconfig

# Workspace in Geoserver that holds the PostGIS connection

WORKSPACE = "rfi"

# Store that represents PostGIS

DATASTORE = "rfi"


# Layer that represents the RequestForImage model/table

FEATURE = "rfi_RequestForImagery"
