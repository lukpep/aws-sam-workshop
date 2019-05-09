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

or be fancy and provide You name! `http://127.0.0.1:3000/hello?name=eugeniusz`