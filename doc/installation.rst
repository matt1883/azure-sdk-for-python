Installation
============

Installation with pip
---------------------

You can install the whole set of stable Azure libraries in a single line:

.. code-block:: console

   $ pip install azure

You can also install individually each library if you don't need everything
and want to save installation space/time.

.. code-block:: console

   $ pip install azure-storage        # Will install the latest Storage runtime library
   $ pip install azure-mgmt-scheduler # Will install the latest Storage management library

Preview packages are not included in the ``azure`` package and can be installed using the ``--pre`` flag.
These packages could have minor breaking changes until the stable release.
Some of the new generated libraries have not yet been tested extensively, and some have known issues.

.. code-block:: console

   $ pip install --pre azure-mgmt-web # will install only the latest Resource Management library

Packages available
------------------

Stable packages
~~~~~~~~~~~~~~~

.. note:: All these packages are installed by the latest ``azure`` meta-package 2.0.0rc6.

===================================== =======
Package name                          Version
===================================== =======
azure-batch                           1.0.0
azure-mgmt-batch                      1.0.0
azure-mgmt-redis                      1.0.0
azure-mgmt-logic                      1.0.0
azure-mgmt-scheduler                  1.0.0
azure-servicebus                      0.20.3
azure-servicemanagement-legacy        0.20.4
azure-storage                         0.33.0
===================================== =======

Preview packages
~~~~~~~~~~~~~~~~

===================================== ========= ===============================
Package name                          Version   Note
===================================== ========= ===============================
azure-mgmt-resource                   0.30.0rc6 Installed by ``azure`` 2.0.0rc6
azure-mgmt-compute                    0.30.0rc6 Installed by ``azure`` 2.0.0rc6
azure-mgmt-network                    0.30.0rc6 Installed by ``azure`` 2.0.0rc6
azure-mgmt-storage                    0.30.0rc6 Installed by ``azure`` 2.0.0rc6
azure-mgmt-keyvault                   0.30.0rc6 Installed by ``azure`` 2.0.0rc6
azure-graphrbac                       0.30.0rc5
azure-mgmt-authorization              0.30.0rc5
azure-mgmt-cdn                        0.30.0rc6
azure-mgmt-cognitiveservices          0.30.0rc6
azure-mgmt-commerce                   0.30.0rc6
azure-mgmt-dns                        0.30.0rc6
azure-mgmt-iothub                     0.1.0
azure-mgmt-notificationhubs           0.30.0rc6
azure-mgmt-powerbiembedded            0.30.0rc6
azure-mgmt-trafficmanager             0.30.0rc6
azure-mgmt-web                        0.30.0rc6   
===================================== ========= ===============================

Install from Github
-------------------

If you want to install ``azure`` from source::

    git clone git://github.com/Azure/azure-sdk-for-python.git
    cd azure-sdk-for-python
    python setup.py install
	
The ``dev`` branch contains the work in progress.
