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
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer, StorageAccountPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test):
    pass


# EXAMPLE: /Jobs/put/Create job
@try_manual
def step__jobs_put_create_job(test):

    text_file = open("/_/out.txt", "w")
    text_file.write('az storageimportexport job create '
             '--location "West US" '
             '--properties-backup-drive-manifest true '
             '--properties-diagnostics-path "waimportexport" '
             '--properties-drive-list bit-locker-key="238810-662376-448998-450120-652806-203390-606320-483076" drive-he'
             'ader-hash="" drive-id="9CA995BB" manifest-file="\\\\DriveManifest.xml" manifest-hash="109B21108597EF36D57'
             '85F08303F3638" '
             '--properties-job-type "Import" '
             '--properties-log-level "Verbose" '
             '--properties-return-address city="Redmond" country-or-region="USA" email="Test@contoso.com" phone="425000'
             '0000" postal-code="98007" recipient-name="Tets" state-or-province="wa" street-address1="Street1" street-a'
             'ddress2="street2" '
             '--properties-storage-account-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft'
             '.ClassicStorage/storageAccounts/{sa}" '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"')
    text_file.close()

    test.cmd('az storageimportexport job create '
             '--location "West US" '
             '--properties-backup-drive-manifest true '
             '--properties-diagnostics-path "waimportexport" '
             '--properties-drive-list bit-locker-key="238810-662376-448998-450120-652806-203390-606320-483076" drive-he'
             'ader-hash="" drive-id="9CA995BB" manifest-file="\\\\DriveManifest.xml" manifest-hash="109B21108597EF36D57'
             '85F08303F3638" '
             '--properties-job-type "Import" '
             '--properties-log-level "Verbose" '
             '--properties-return-address city="Redmond" country-or-region="USA" email="Test@contoso.com" phone="425000'
             '0000" postal-code="98007" recipient-name="Tets" state-or-province="wa" street-address1="Street1" street-a'
             'ddress2="street2" '
             '--properties-storage-account-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft'
             '.ClassicStorage/storageAccounts/{sa}" '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])

# EXAMPLE: /Jobs/get/Get job
@try_manual
def step__jobs_get_get_job(test):
    test.cmd('az storageimportexport job show '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Locations/get/Get locations
@try_manual
def step__locations_get_get_locations(test):
    test.cmd('az storageimportexport location show '
             '--location-name "{West US}"',
             checks=[])


# EXAMPLE: /BitLockerKeys/post/List BitLocker Keys for drives in a job
@try_manual
def step__bitlockerkeys_post_list_bitlocker_keys_for_drives_in_a_job(test):
    test.cmd('az storageimportexport bit-locker-key list '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Jobs/get/List jobs in a resource group
@try_manual
def step__jobs_get_list_jobs_in_a_resource_group(test):
    test.cmd('az storageimportexport job list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Jobs/get/List jobs in a subscription
@try_manual
def step__jobs_get_list_jobs_in_a_subscription(test):
    test.cmd('az storageimportexport job list',
             checks=[])


# EXAMPLE: /Locations/get/List locations
@try_manual
def step__locations_get_list_locations(test):
    test.cmd('az storageimportexport location list',
             checks=[])


# EXAMPLE: /Jobs/patch/Update job
@try_manual
def step__jobs_patch_update_job(test):
    test.cmd('az storageimportexport job update '
             '--properties-backup-drive-manifest true '
             '--properties-log-level "Verbose" '
             '--properties-state "" '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Jobs/delete/Delete job
@try_manual
def step__jobs_delete_delete_job(test):
    test.cmd('az storageimportexport job delete '
             '--job-name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test):
    pass


class StorageImportExportScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_storageimportexport_myResourceGroup'[:9], key='rg')
    @StorageAccountPreparer(location="eastus")

    def test_storageimportexport(self, resource_group, storage_account):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id(),
            'sa': storage_account
        })

        self.kwargs.update({
            'West US': 'West US',
            'myJob': self.create_random_name(prefix='cli_test_jobs'[:9], length=24),
        })

        setup(self)
        step__jobs_put_create_job(self)
        step__jobs_get_get_job(self)
        step__locations_get_get_locations(self)
        step__bitlockerkeys_post_list_bitlocker_keys_for_drives_in_a_job(self)
        step__jobs_get_list_jobs_in_a_resource_group(self)
        step__jobs_get_list_jobs_in_a_subscription(self)
        step__locations_get_list_locations(self)
        step__jobs_patch_update_job(self)
        step__jobs_delete_delete_job(self)
        cleanup(self)
