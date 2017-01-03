# Working steps
1. Create bucket to put artifacts
```
    aws s3 mb s3://lambda-pipeline
```
2. Transform the template-file an upload the artifacts
```
    aws cloudformation package --template-file get_container.yaml --output-template-file get_container_cf.yml --s3-bucket lambda-pipeline
```
3. Deploy the function
```
    aws cloudformation deploy --template-file get_container_cf.yml --stack-name lambda-pipeline --capabilities CAPABILITY_IAM
```
# Links
- [Cloudformation package](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html)
- [Cloudformation transform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html)
- [SAML intro](https://aws.amazon.com/blogs/compute/introducing-simplified-serverless-application-deplyoment-and-management/)
- [Python-programming-model](http://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)
- [API Gateway create](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-from-example.html)
- [Lambda-python-how-to-create-deployment](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
- [Deploying Lambda Functions](http://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html)
- [CodePipeline Access Permissions](http://docs.aws.amazon.com/codepipeline/latest/userguide/access-permissions.html)

# TODO
- Prepare console screen walk-trough.
- Create diagrams to show what we build.
- Tweak the lambda-pipeline/ServerlessPipeline.yaml pipeline Cloudformation file.
