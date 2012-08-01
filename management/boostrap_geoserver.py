from django.core.management.base import BaseCommand, CommandError
from local_settings import GEOSERVER_USER, GEOSERVER_PASSWORD
from local_settings import GEOSERVER_BASE_URL,WORKSPACE,DATASTORE,FEATURE
from settings import DATABASES 
import requests

PG_USER = DATABASES['default']['USER']
PG_PASSWORD = DATABASES['default']['PASSWORD']
PG_PASSWORD = DATABASES['default']['NAME']
PG_HOST = DATABASES['default']['HOST'] or 'localhost'
PG_PORT = DATABASE['default']['PORT'] or '5432'


class Command(BaseCommand):
    help = "Sets up the rfi model in GeoServer"

    def handle(self, *args, **options):

        headers = {'Content-type': 'text/xml'}

        # Create the rfi workspace

        url = "%s/geoserver/rest/workspaces" % (GEOSERVER_BASE_URL)

        data = '''<workspace>
                    <name>%s</name>
                  </workspace>''' % (WORKSPACE)
        try:
            r = requests.put(url, data=data, headers=headers, auth=(GEOSERVER_USER, GEOSERVER_PASSWORD))
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise CommandError('Error creating workspace: %s' % e.strerror)

        # Connect to the postgis datastore

        url = "%s/geoserver/rest/workspaces/%s/datastores" % (GEOSERVER_BASE_URL, WORKSPACE)

        data = '''<dataStore>
                  <name>%s</name>
                  <connectionParameters>
                    <host>%s</host>
                    <port>%s</port>
                    <database>%s</database>
                    <user>%s</user>
                    <passwd>%s</passwd>
                    <dbtype>postgis</dbtype>
                    <Estimated extends>false</Estimated extends>
                  </connectionParameters>
                </dataStore>''' % (DATASTORE, PG_HOST, PG_PORT, PG_DATABASE, PG_USER, PG_PASSWORD)
        try:
            r = requests.put(url, data=data, headers=headers, auth=(GEOSERVER_USER, GEOSERVER_PASSWORD))
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise CommandError('Error creating datastore: %s' % e.strerror)

        # Publish the rfi featuretype

        url = "%s/geoserver/rest/workspaces/%s/datastores/%s/featuretypes" % (GEOSERVER_BASE_URL, WORKSPACE, FEATURE)

        data = ''''<featureType>
                    <name>%s</name>
                    </featureType>''' % (FEATURE)

        try:
            r = requests.put(url, data=data, headers=headers, auth=(GEOSERVER_USER, GEOSERVER_PASSWORD))
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise CommandError('Error creating featuretype: %s' % e.strerror)
