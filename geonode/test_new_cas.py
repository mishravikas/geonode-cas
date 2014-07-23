from django.contrib.auth.models import User,UNUSABLE_PASSWORD
from django.test import Client
from django.contrib.auth import get_user_model
from geonode.layers.utils import (
    upload,
    file_upload,
)
from django.conf import settings
import geonode.layers.utils
import geonode.layers.views
import geonode.layers.models
import gisdata
from django.core.urlresolvers import reverse

def create_user():
    user = User.objects.create_user('test_cas', UNUSABLE_PASSWORD)

def login_cas(self):
    """
    I am not too sure about this as login() function does not require password
    have to edit it later
    """
    user = User.objects.get(username='test_cas',password='test_cas')
    user.backend = 'cas_consumer.backends.CASBackend'
    login(self,user)


def test_layer_upload(self):
        """ Here am uploading a new layer and setting its permission so that anonymous 
        users can not access it
        """

        client = Client()
        client.login(username='test_cas', password='test_cas')


        test_cas = get_user_model().objects.get(username="test_cas")
        saved_layer = file_upload(
             os.path.join(gisdata.VECTOR_DATA, "san_andres_y_providencia_poi.shp"),
             name="san_andres_y_providencia_poi_by_test_cas",
             user=test_cas,
             overwrite=True,
        )
        saved_layer.set_gen_level(ANONYMOUS_USERS, saved_layer.LEVEL_NONE)
        save_layer.set_gen_level(test_cas,'layer_readwrite')

        url = reverse('layer_metadata', args=[saved_layer.service_typename])
        resp = client.get(url)
        self.assertEquals(resp.status_code, 200)


def check_detail_page():
    """
    Checking layer detail page
    """
    layer = Layer.objects.get(name="san_andres_y_providencia_poi_by_test_cas")
    c = Client()
    self.assertTrue(c.login(username='test_cas',password='test_cas'))

    response = c.get(reverse('layer_detail', args=(layer.typename,)))
    self.assertEquals(response.status_code, 200)

def check_get_capabilities():
    """
    checking get capabilities
    """
    server_url = settings.OGC_SERVER['default']['LOCATION'] + 'ows?'
    
    metadata = get_layers_metadata(server_url, '1.0.0')
    msg = ('The metadata list should not be empty in server %s'
           % server_url)
    assert len(metadata) > 0, msg
def wms():
    url=()