### Example 3 - S3 + lambda + SQS + DynamoDb integration

This time we will create simple serverless app that stores information about S3 bucket file uploads into DynamoDb and sends information also to the SQS Queue. This example will show how NOT to `hard-code` other AWS Infrastructure resources into templates - instead how to provide them dynamically. 

All commands should be invoked from `Example_3` directory

