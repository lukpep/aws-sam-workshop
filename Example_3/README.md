### Example 3 - S3 + lambda + SQS + DynamoDb integration

This time we will create simple serverless app that sends information about S3 bucket file uploads into SQS queue and (for decoupling) and later on consumes those messages and stores them in DynamoDb. This example will show how **NOT** to `hard-code` other AWS Infrastructure resources ARNs into templates and how to provide them together with all the necessary privileges. 

All commands should be invoked from `Example_3` directory

---
#### validate template:
```bash
sam validate
```

#### Deploy it to the Cloud!
Remember to use correct bucket name (crated in previous examples)

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
   --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 \
   --capabilities CAPABILITY_IAM
```
* watch stack is being created in AWS Console [here](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1)

#### Test that our serverless stack is working as expected
* open S3 dashboard in AWS Console
* upload some file into our input bucket
* open DynamoDb table and check if uploaded files meta data is present there