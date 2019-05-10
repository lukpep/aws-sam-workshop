### Example 3 - S3 + lambda + SQS + DynamoDb integration

This time we will create a simple serverless app that sends information about S3 bucket file uploads into SQS queue and (for decoupling) and later on consumes those messages and stores them in DynamoDb. This example will show how **NOT** to `hard-code` other AWS Infrastructure resources ARNs into templates and how to provide them together with all the necessary privileges. 

All commands should be invoked from `Example_3` directory

---
#### validate template:
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
   --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 \
   --capabilities CAPABILITY_IAM
```
* watch stack is being created in AWS Console [here](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1)

#### Test that our serverless stack is working as expected
* open S3 dashboard in AWS Console
* upload some file into our input bucket
* open DynamoDb table and check if uploaded files metadata is present there

#### Cloud formation changesets
*When you need to update a stack, understanding how your changes will affect running resources before you implement them can help you update stacks with confidence. Change sets allow you to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the changeset, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another changeset.*

* make some change in our template - e.g change SQS binding batch size
* package (template processing part is important) template
```bash
sam package \
   --template-file template.yaml \
   --output-template-file generated-template.yaml \
   --s3-bucket BUCKET_NAME
```
* create change set
```bash
aws cloudformation create-change-set --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 --template-body file://generated-template.yaml --change-set-name MyChange --capabilities CAPABILITY_IAM
```

* describe changeset
```bash
aws cloudformation describe-change-set --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 --change-set-name MyChange
```
You should see something like this:
```bash
"Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "SaveFileInfoToDbSQSEvent",
                "PhysicalResourceId": "cf9e3e68-1714-4164-8888-6692de3822fa",
                "ResourceType": "AWS::Lambda::EventSourceMapping",
                "Replacement": "False",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "BatchSize",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    }
                ]
            }
        }
    ],

```
Important parts are: ``Replacement`` and ``RequiresRecreation`` keys - where we are provided with information if our proposed stack change will delete / replace resources - which may be not a good idea if we're talking about the database for example ;-)

* delete proposed stack change
```bash
aws cloudformation delete-change-set --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 --change-set-name MyChange
```

* change batch size to nominal 1 and this time lets change ``AttributeName`` in our DynamoDb database schema and attributes configuration.

* generate changeset once more and describe it. You should end up with something like this:
```bash
"Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "FileDb",
                "PhysicalResourceId": "AWS-SAM-WORKSHOP-EXAMPLE-3-FileDb-1NIAQPBH0TRNQ",
                "ResourceType": "AWS::DynamoDB::Table",
                "Replacement": "True",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "KeySchema",
                            "RequiresRecreation": "Always"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    },
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "AttributeDefinitions",
                            "RequiresRecreation": "Conditionally"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    }
                ]
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "SaveFileInfoToDb",
                "PhysicalResourceId": "AWS-SAM-WORKSHOP-EXAMPLE-3-SaveFileInfoToDb-PQ13D4IETNZJ",
                "ResourceType": "AWS::Lambda::Function",
                "Replacement": "False",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Role",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Dynamic",
                        "ChangeSource": "ResourceAttribute",
                        "CausingEntity": "SaveFileInfoToDbRole.Arn"
                    },
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Environment",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "ResourceReference",
                        "CausingEntity": "FileDb"
                    }
                ]
            }
        },
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "SaveFileInfoToDbRole",
                "PhysicalResourceId": "AWS-SAM-WORKSHOP-EXAMPLE-3-SaveFileInfoToDbRole-2YMSWZZPMTO3",
                "ResourceType": "AWS::IAM::Role",
                "Replacement": "False",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Policies",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "ResourceReference",
                        "CausingEntity": "FileDb"
                    }
                ]
            }
        }
    ],

```

which basically tells You that DynamoDb needs to be replaced - but not only - also lambdas and policies that interact with it need to be updated.
* viewing changesets in AWS Console is also a valid option:

![](https://s3-eu-west-1.amazonaws.com/aws-sam-workshop-huuuge-dev/change-set.png)

* What can be done with changesets?

```bash
aws cloudformation delete-change-set --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 --change-set-name MyChange
```

```bash
aws cloudformation execute-change-set --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3 --change-set-name MyChange
```

---

#### Further reading:
* [Prevent Updates to Stack Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html)
