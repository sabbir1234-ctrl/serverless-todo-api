# Serverless Todo API

A serverless REST API for todo items, built with **AWS Lambda (Python 3.11)**, **API Gateway** and **DynamoDB**, and deployed with **AWS SAM**.
I made it for my Service-Oriented Architecture coursework (spring 2026).

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) ![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda) ![DynamoDB](https://img.shields.io/badge/AWS-DynamoDB-4053D6?logo=amazondynamodb) ![SAM](https://img.shields.io/badge/IaC-AWS%20SAM-orange)

## Architecture

```
Client ──▶ API Gateway ──▶ Lambda (one per operation) ──▶ DynamoDB table "TodoTable"
```

The whole stack (table, functions, IAM policies, API routes) is defined as infrastructure-as-code in [`template.yaml`](template.yaml).

## Endpoints

| Method | Path | Lambda |
|--------|------|--------|
| `POST` | `/todos` | `create_todo` |
| `GET` | `/todos` | `get_todos` |
| `GET` | `/todos/{id}` | `get_todo` |
| `DELETE` | `/todos/{id}` | `delete_todo` |

## Deploy

```bash
sam build
sam deploy --guided
```

## Structure

```
create_todo/  get_todos/  get_todo/  delete_todo/   one Lambda handler (app.py) each
template.yaml                                       SAM / CloudFormation template
requirements.txt
```
