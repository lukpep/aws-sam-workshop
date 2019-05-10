# aws-sam-workshop
workshop about AWS SAM and IaaC concepts

### Prerequisites:

#### AWS and AWS CLI
* log in to AWS console [here](https://console.aws.amazon.com/console/home) and generate Access and Secret Keys for CLI access. How to generate them? [This way](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
* Install the **AWS CLI** -> [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* Configure the **AWS CLI** [this is how](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) using Access and Secret Key generated earlier on. **Remember to use eu-west-1 (Ireland) region!**. If you already have some account configured locally please create a separate profile.
```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: eu-west-1
Default output format [None]: json
```
* Test is AWS CLI is working fine and has access to your account:
```bash
aws lambda list-functions
```
You should receive an empty list

#### Docker (optional)
You need to have Docker installed and running to be able to run serverless projects and functions locally with the AWS SAM CLI.
If you are only planning to use AWS SAM for templates transformations and deployments there is no need for docker. Nevertheless, I will quickly show You how to use mentioned AWS SAM functionality.

#### AWS SAM
* Install it: [this is how](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html)
* check if it works 
```bash
sam --version
```

### Examples
1. [Single lambda (SAM local example)](Example_1)
2. [Single lambda with API gateway (SAM local + Cloud)](Example_2)
3. [S3 -> Lambda -> DynamoDB & SQS (Cloud)](Example_3)
3. [Termination protection and Drift detection](Example_4)