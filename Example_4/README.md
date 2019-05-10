### Example 4 - Termination protection and Drift detection

This example will present Termination protection and Drift detection functionalities. Using stack from Example_3. It all can be done from AWS CLI or AWS Console.

All commands should be invoked from `Example_4` directory

---
* enable stack termination protection
* try to delete stack
```bash
aws cloudformation delete-stack --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3
```
it should result in:
```bash
An error occurred (ValidationError) when calling the DeleteStack operation: Stack [AWS-SAM-WORKSHOP-EXAMPLE-3] cannot be deleted while TerminationProtection is enabled
```
* ofcourse it can be set via IAM role / privileges who can enable / disable stack termination - more on that [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html)
 ---
 * enable drift detection
 ```bash
aws cloudformation detect-stack-drift --stack-name AWS-SAM-WORKSHOP-EXAMPLE-3
```
 * wait for drift status ``IN_SYNC`` (use id returned from previous command)
 ```bash
aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id c1d59480-7318-11e9-b69b-024e38e0666a
```

* introduce some DRIFT

![drift](https://media.giphy.com/media/ErIP6WHxI6avC/giphy.gif)

* detect it and view details:

![](https://s3-eu-west-1.amazonaws.com/aws-sam-workshop-huuuge-dev/drift.png)

* You can (and should) automate stack drift detection ... using yet another stack! from [here](https://medium.com/@mitchplanck/cloudformation-drifts-312e11d870d4)