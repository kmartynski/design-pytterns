class AwsClient:

    def aws_cli_client_authenticator(self):
        return "AWS CLI"


class AzureClient:

    def azure_cli_client_authenticator(self):
        return "Azure CLI"


class GcpClient:

    def gcp_cli_client_authenticator(self):
        return "GCP CLI"


class CloudAdapter:
    def __init__(self, obj, **authentication_method):
        self.obj = obj
        self.__dict__.update(authentication_method)

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == '__main__':
    cloud_clis = []

    aws = AwsClient()
    azure = AzureClient()
    gcp = GcpClient()

    adapt_aws = CloudAdapter(aws, authenticate=aws.aws_cli_client_authenticator())

    print(adapt_aws.original_dict())
    print(adapt_aws.authenticate)
