# Communication resource Preparer and its shorthand decorator

from azure.cli.testsdk.scenario_tests import SingleValueReplacer
from azure.cli.testsdk.preparers import NoTrafficRecordingPreparer, ResourceGroupPreparer
from azure.cli.testsdk.exceptions import CliTestError
from azure.cli.testsdk.reverse_dependency import get_dummy_cli
import os

# pylint: disable=too-many-instance-attributes
class CommunicationResourcePreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', location='Global', data_location='United States', length=24,
                 parameter_name='communication_resource', resource_group_parameter_name='resource_group', skip_delete=True,
                 dev_setting_name='AZURE_CLI_TEST_DEV_COMMUNICATION_RESOURCE_NAME', key='cr'):
        super(CommunicationResourcePreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.location = location
        self.data_location = data_location
        self.resource_group_parameter_name = resource_group_parameter_name
        self.skip_delete = skip_delete
        self.parameter_name = parameter_name
        self.key = key
        self.dev_setting_name = os.environ.get(dev_setting_name, None)

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)

        if not self.dev_setting_name:

            template = 'az communication create --name {} --location {} --data-location "{}" --resource-group {} '
            self.live_only_execute(self.cli_ctx, template.format(
                name, self.location, self.data_location, group))
        else:
            name = self.dev_setting_name

        try:
            account_key = self.live_only_execute(self.cli_ctx,
                                                 'az communication list-key --name {} --resource-group {} --query "primaryConnectionString" -otsv'
                                                 .format(name, group)).output.strip()
        except AttributeError:  # live only execute returns None if playing from record
            account_key = None

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name,
                self.parameter_name + '_info': (name, account_key or 'endpoint=https://sanitized.communication.azure.com/;accesskey=fake===')}

    def remove_resource(self, name, **kwargs):
        if not self.skip_delete and not self.dev_setting_name:
            group = self._get_resource_group(**kwargs)
            self.live_only_execute(self.cli_ctx, 'az communication delete --name {} --resource-group {} --yes'.format(name, group))

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create a communication resource a resource group is required. Please add ' \
                       'decorator @{} in front of this communication resource preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))
