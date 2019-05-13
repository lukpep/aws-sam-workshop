### Example 5 - Nested applications

This example will present Nested applications concept.

![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2018/12/14/nested-app-1024x710.png)

*Nested applications build off a concept in AWS CloudFormation called nested stacks. With nested applications, serverless applications are deployed as stacks, or collections of resources, that contain one or more other serverless application stacks. You can reference resources created in these nested templates to either the parent stack or other nested stacks to manage these collections of resources more easily.*

We will use a slightly modified version of Example 3 template. This time our stack will be enriched with a simple CRUD functionality for our file info database - all in a form of a serverless application taken from AWS Serverless Application Repository.

All commands should be invoked from `Example_5` directory

---
#### Validate template:
```bash
sam validate
```
#### Deploy it to the Cloud!
Remember to use the correct bucket name (created in previous examples)

* package project and generate processed template:
```bash
sam package \
   --template-file template.yaml \
   --output-template-file generated-template.yaml \
   --s3-bucket BUCKET_NAME
```
* deploy stack
```bash
sam deploy \
   --template-file generated-template.yaml \
   --stack-name AWS-SAM-WORKSHOP-EXAMPLE-5 \
   --capabilities CAPABILITY_IAM
```
* watch stack is being created in AWS Console [here](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1)

* at this point, we should have had a working stack - exactly like one in example 3. Test it by uploading some file to our input bucket.

#### Introduce nested application

* Add new resource to the template

```bash
  microservicehttpendpoint:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:077246666028:applications/microservice-http-endpoint
        SemanticVersion: 1.0.3
      Parameters: 
        TableNameParameter: !Ref FileDb  
      
```

* package and deploy - **remember to add new capability to the deploy command** -> `CAPABILITY_AUTO_EXPAND`
```bash
sam deploy \
   --template-file generated-template.yaml \
   --stack-name AWS-SAM-WORKSHOP-EXAMPLE-5 \
   --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
```
* Test new endpoint (find api gateway with resource name `MyResource`) and provide `TableName` parameter in query string

![](https://s3-eu-west-1.amazonaws.com/aws-sam-workshop-huuuge-dev/uc_endpoint.png)