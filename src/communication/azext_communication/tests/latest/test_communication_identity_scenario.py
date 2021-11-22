from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer, CommunicationResourcePreparer
from .utils import get_test_identity_id
import os

class CommunicationIdentityScenarios(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_issue_access_token(self, communication_resource_info):
        
        if self.is_live:
            os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]

        val = self.cmd('az communication identity issue-access-token --scope chat').get_output_in_json()
        self.assertIsNotNone(val['token'])


    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @CommunicationResourcePreparer(resource_group_parameter_name='rg')
    def test_issue_access_token_with_id(self, communication_resource_info):
        
        if self.is_live:
            os.environ['AZURE_COMMUNICATION_CONNECTION_STRING'] = communication_resource_info[1]
        
        id = get_test_identity_id(self.is_live)
        self.kwargs.update({'id' : id })

        val = self.cmd('az communication identity issue-access-token --scope chat --userid {id}').get_output_in_json()
        self.assertIsNotNone(val['token'])