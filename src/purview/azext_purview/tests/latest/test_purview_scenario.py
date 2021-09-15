# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer, VirtualNetworkPreparer


class TestPurviewScenario(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_purview', location='eastus2')
    def test_purview_account(self, resource_group):
        self.kwargs.update({
            'purview': self.create_random_name('pv-', 10)
        })

        purview_account = self.cmd('purview account create -n {purview} -g {rg}',checks=[
            self.check('friendlyName', '{purview}'),
            self.check("contains(id, 'resourceGroups/{rg}/providers/Microsoft.Purview/accounts/{purview}')", True),
            self.check('name', '{purview}'),
            self.check('tags', None),
            self.check('location', 'eastus2'),
            self.check('resourceGroup', '{rg}'),
            self.check('provisioningState', 'Creating')
        ]).get_output_in_json()

        self.cmd('purview account wait --created -g {rg} -n {purview}')
        self.cmd('purview account update -n {purview} -g {rg} --tags tag=test', checks=[
            self.check('friendlyName', '{purview}'),
            self.check("contains(id, 'resourceGroups/{rg}/providers/Microsoft.Purview/accounts/{purview}')", True),
            self.check('name', '{purview}'),
            self.check('tags', {'tag':'test'})
        ])

        self.kwargs.update({
            'purview_id': purview_account['createdByObjectId']
        })

        self.cmd('purview account add-root-collection-admin -n {purview} -g {rg} --object-id {purview_id}')
        self.cmd('purview account list-key -n {purview} -g {rg}', checks=[
            self.check("length(@)", 2),
        ])

        self.cmd('purview account show -n {purview} -g {rg}', checks=[
            self.check('createdByObjectId', purview_account['createdByObjectId']),
            self.check('friendlyName', '{purview}'),
            self.check("contains(id, 'resourceGroups/{rg}/providers/Microsoft.Purview/accounts/{purview}')", True),
            self.check('name', '{purview}')
        ])
        self.cmd('purview account list', checks=[
            self.check('type(@)', 'array')
        ])
        self.cmd('purview account delete -g {rg} -n {purview} --y')


    @ResourceGroupPreparer(name_prefix='cli_test_purview', location='eastus2')
    def test_purview_default_account(self, resource_group):
        self.kwargs.update({
            'purview': self.create_random_name('pv-', 10)
        })

        purview_account = self.cmd('purview account create -n {purview} -g {rg}', checks=[
            self.check('friendlyName', '{purview}'),
            self.check("contains(id, 'resourceGroups/{rg}/providers/Microsoft.Purview/accounts/{purview}')", True),
            self.check('name', '{purview}'),
            self.check('tags', None),
            self.check('location', 'eastus2'),
            self.check('resourceGroup', '{rg}'),
            self.check('provisioningState', 'Creating')
        ]).get_output_in_json()
        self.cmd('purview account wait --created -g {rg} -n {purview}')
        self.kwargs.update({
            'tenant_id': purview_account['identity']['tenantId']
        })

        self.cmd('purview default-account set -n {purview} -g {rg} '
                 '--subscription-id 0b1f6471-1bf0-4dda-aec3-cb9272f09590 --scope-tenant-id {tenant_id}', checks=[
            self.check('accountName', '{purview}'),
            self.check('resourceGroupName', '{rg}'),
            self.check('scopeTenantId', purview_account['identity']['tenantId']),
            self.check('scopeType', 'Tenant')
        ])

        self.cmd('purview default-account show --scope-tenant-id {tenant_id} --scope-type Tenant',checks=[
            self.check('accountName', '{purview}'),
            self.check('resourceGroupName', '{rg}'),
            self.check('scopeTenantId', purview_account['identity']['tenantId']),
            self.check('scopeType', 'Tenant')
        ])

        self.cmd('purview default-account remove --scope-tenant-id {tenant_id} --scope-type Tenant')
        self.cmd('purview account delete -g {rg} -n {purview} --y')