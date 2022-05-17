from pytest import mark

from structural.adapter import AwsClient, AzureClient, GcpClient, CloudAdapter


aws = AwsClient()
azure = AzureClient()
gcp = GcpClient()


class TestAdapter:

    @mark.parametrize(
        "cloud_provider, return_value, adapted_method",
        [
            (aws, "AWS CLI", aws.aws_cli_client_authenticator()),
            (azure, "AZURE CLI", azure.azure_cli_client_authenticator()),
            (gcp, "GCP CLI", gcp.gcp_cli_client_authenticator()),
        ]
    )
    def test_should_return_match_adapted_method_to_original(
            self,
            cloud_provider,
            return_value,
            adapted_method
    ):
        adapt_cloud = CloudAdapter(cloud_provider, authenticate=adapted_method)

        assert adapt_cloud.authenticate == adapted_method
