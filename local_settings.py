#Base url for GeoServer (no trailing slash)

GEOSERVER_BASE_URL = "http://localhost:8080"

GEOSERVER_USER = "admin"

GEOSERVER_PASSWORD = "geoserver"

# Eventually we'll set these in Geoserver via restconfig

# Workspace in Geoserver that holds the PostGIS connection

WORKSPACE = "rfi"

# Store that represents PostGIS

DATASTORE = "rfi"


# Layer that represents the RequestForImage model/table

FEATURE = "rfi_requestforimagery"

# PostGIS settings

PG_HOST = "localhost"
PG_PORT = "5432"
PG_DATABASE = 
PG_USER =
PG_PASSWORD = 
