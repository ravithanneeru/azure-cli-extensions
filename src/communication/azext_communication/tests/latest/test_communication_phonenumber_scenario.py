# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer, CommunicationResourcePreparer
from .utils import get_test_source_phonenumber, get_new_phonenumber

import os


class CommunicationPhonenumberScenarios(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_list_phonenumbers(self, communication_resource_info):
        if self.is_live:
            get_new_phonenumber(communication_resource_info[1])
            os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        phonenumber_list = self.cmd(
            'az communication phonenumbers list-phonenumbers').get_output_in_json()
        assert len(phonenumber_list) > 0

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_show_phonenumbers(self, communication_resource_info):
        phonenumber = get_test_source_phonenumber(self.is_live)
        if phonenumber is None:
            phonenumber = get_new_phonenumber(communication_resource_info[1])

        self.kwargs.update({'phonenumber': phonenumber})

        if self.is_live:
            os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        phonenumber_info = self.cmd(
            'az communication phonenumbers show-phonenumber --phonenumber \"{phonenumber}\"').get_output_in_json()
        self.assertIsNotNone(phonenumber_info['id'])
        self.assertIsNotNone(phonenumber_info['assignmentType'])
        self.assertIsNotNone(phonenumber_info['capabilities'])
        self.assertIsNotNone(phonenumber_info['cost'])
        self.check(phonenumber_info['phoneNumber'], phonenumber)
