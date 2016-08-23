# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AclStatusResult(Model):
    """Data Lake Store file or directory Access Control List information.

    :param acl_status: the AclStatus object for a given file or directory.
    :type acl_status: :class:`AclStatus
     <azure.mgmt.datalake.store.filesystem.models.AclStatus>`
    """ 

    _attribute_map = {
        'acl_status': {'key': 'AclStatus', 'type': 'AclStatus'},
    }

    def __init__(self, acl_status=None):
        self.acl_status = acl_status