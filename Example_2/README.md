### Example 2 - Hello World from lambda with API gateway integration

Same greetings lambda as in Example 1 - but this time with api gateway integration and possibility to deploy it to the world!

All commands should be invoked from `Example_2` directory

---
#### validate template:
```bash
sam validate
```
---
#### start local api

```bash
 sam local start-api
```
You should see something like this:
```bash
$ sam local start-api
2019-05-09 11:57:41 Found credentials in shared credentials file: ~/.aws/credentials
2019-05-09 11:57:41 Mounting GetCurrentConfig at http://127.0.0.1:3000/hello [GET]
2019-05-09 11:57:41 You can now browse to the above endpoints to invoke your functions. You do not need to restart/reload SAM CLI while working on your functions, changes will be reflected instantly/automatically. You only need to restart SAM CLI if you update your AWS SAM template
2019-05-09 11:57:41  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

---
#### test it
just go to `http://127.0.0.1:3000/hello`

or be fancy and provide Your name! `http://127.0.0.1:3000/hello?name=wojtek`

---

#### Deploy it to the Cloud!
* create S3 bucket for our template data:
```bash
aws s3 mb s3://BUCKET_NAME
```
remember that bucket name needs to be unique **globally** on AWS so names like 'tempbucket' would probably be taken.
This name will be used later on in every deploy command - so keep it in mind.

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
   --stack-name AWS-SAM-WORKSHOP-EXAMPLE-2 \
   --capabilities CAPABILITY_IAM
```

* watch stack is being created in AWS Console [here](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1)
* test it online: Api url should be visible in the `Outputs` section of stack details page or You could use:
```bash
aws cloudformation describe-stacks --stack-name AWS-SAM-WORKSHOP-EXAMPLE-2
```
and look up `Outputs` key