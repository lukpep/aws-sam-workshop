### Example 1 - Hello World from lambda

Just some basic greetings lambda without any integrations

All commands should be invoked from `Example_1` directory

---
####validate template:
```bash
sam validate
```
---
#### prepare lambda invocation event

```bash
 sam local generate-event apigateway aws-proxy > event.json 
```
or skip it and use the sample one provided in `example_event.json`

---
#### invoke lambda locally
```bash
sam local invoke --event example_event.json
```
or
```bash
sam local invoke --event event.json
```

You should se something like this:
```bash
$ sam local invoke --event example_event.json                                                                                 1 ↵
2019-05-09 10:57:03 Found credentials in shared credentials file: ~/.aws/credentials
2019-05-09 10:57:03 Invoking hello_world.lambda_handler (python3.6)

Fetching lambci/lambda:python3.6 Docker container image......
2019-05-09 10:57:05 Mounting /home/lukpep/work/aws-sam-workshop/Example_1/src as /var/task:ro,delegated inside runtime container
START RequestId: 0a6ad0f5-b39d-4e3c-b7b9-3584f44e4da0 Version: $LATEST
[INFO]	2019-05-09T08:57:06.425Z	0a6ad0f5-b39d-4e3c-b7b9-3584f44e4da0	Saying hello from AWS lambda ... 

END RequestId: 0a6ad0f5-b39d-4e3c-b7b9-3584f44e4da0
REPORT RequestId: 0a6ad0f5-b39d-4e3c-b7b9-3584f44e4da0 Duration: 0 ms Billed Duration: 100 ms Memory Size: 128 MB Max Memory Used: 19 MB

{"statusCode": "200", "body": "Hello there lpe from serverless world"}

```