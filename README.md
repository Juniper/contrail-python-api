contrail-python-api
===================

python API bindings for Contrail.

Installing
==========

    git clone https://github.com/Juniper/contrail-python-api
    cd contrail-python-api
    python setup.py install

Example Usage
=============

    >>> import pycontrail.client as client
    >>> conn = client.Client(
            url='http://10.84.34.141:8082',
            auth_params={'type':'keystone',
                         'auth_url':'http://10.84.34.141:5000/v2.0',
                         'username':'admin',
                         'password':'secret',
                         'tenant_name':'admin'})
    >>> conn.virtual_networks_list()


License
=======
This software is licensed under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
