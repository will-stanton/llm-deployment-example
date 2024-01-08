# Langchain FastAPI Deployment Example

![PokemonGradioScreenshot](https://github.com/will-stanton/ml-deployment-example/assets/5712192/86407548-8e67-4ef8-9130-544b874c5b85)
![PokemonSwaggerScreenshot](https://github.com/will-stanton/ml-deployment-example/assets/5712192/ad511448-fcdc-4d35-adde-feb6eda7b36f)

## What is it?

This is a small demo of running a Langchain app utilizing the OpenAI ChatGPT API. The app uses Few-Shot Prompting to instruct the Large Language Model to always change the subject to be about *Pokemon*, regardless of what the user asks about. 

## Infrastructure

The app is written in Python and uses a variety of tools and services.

- [Langchain](https://www.langchain.com/) for interacting with the OpenAI API using Few-Shot Prompt Templates. 
- Python's [FastAPI](https://fastapi.tiangolo.com/) package for the API layer. 
- AWS [AppRunner](https://aws.amazon.com/apprunner/) for hosting the API service.
- [CloudFormation](https://aws.amazon.com/cloudformation/) for Infrastructure-as-Code. 
- [GitHub Actions](https://github.com/features/actions) for building a [Docker image](https://www.docker.com/) of the FastAPI app and pushing it to the [AWS Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/), and also for deploying the CloudFormation templates. 
- GitHub Actions authenticates to AWS via [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/), so there's no need for managing AWS access keys! 
- Simple local UI utilizing HuggingFace's [Gradio](https://www.gradio.app/) framework. 

## References

Much of this project depends heavily on existing examples and templates in documentation, especially the infrastructure parts. For example, GitHub Actions provides sample templates for publishing to container registries. Here are some reference links and areas for further reading:

[Langchain Few-Shot Prompt Templates with Examples](https://python.langchain.com/docs/modules/model_io/prompts/few_shot_examples)

[GitHub Actions Build and Push to ECR Workflow Templates](https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service)

[AWS AppRunner CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html)

[AWS Elastic Container Registry CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html)

[GitHub Actions OIDC Configuration](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)

[AWS Blogs: Setting Up IAM Roles for OIDC](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)

[FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)

[OpenAI API Docs](https://platform.openai.com/playground/p/default-chat?mode=complete&model=gpt-3.5-turbo-instruct-0914)

[Gradio](https://www.gradio.app/)