# CloudOps AI — 30-Minutes-a-Day End-to-End Python Project

## 1. Project Goal

Build a portfolio-grade, end-to-end cloud file and document management platform using **Python**.

The project should demonstrate:

- Python
- FastAPI
- REST APIs
- Microservices
- PostgreSQL / DBMS
- SQLAlchemy
- Alembic
- JWT authentication
- Docker
- RabbitMQ
- Redis
- AI chatbot
- RAG (Retrieval Augmented Generation)
- Git + GitHub
- GitHub Actions CI/CD
- Testing with Pytest
- AWS free-tier/free-usage-friendly services where practical
- Monitoring and logging

The project must be developed gradually. The target pace is **30 minutes per day**.

> Important: "Free" means we should prefer software that is free/open source and services with free tiers or local alternatives. Cloud services can incur charges if limits are exceeded. Always verify current AWS pricing/free-tier terms before deploying.

---

# 2. Development Principles

1. Build one small working feature at a time.
2. Do not create all microservices on Day 1.
3. Every feature should be tested.
4. Commit working progress regularly.
5. Do not commit secrets.
6. Keep each service independently understandable.
7. Prefer local Docker development before paying for cloud resources.
8. Use AI coding assistance carefully: understand every generated piece of code.
9. Keep the README updated as the project grows.
10. At the end of every day, the project should remain runnable.

---

# 3. Proposed Architecture

```text
                    Client / Frontend
                           |
                           v
                    API Gateway
                           |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
   Auth Service       File Service       User Service
        |                  |                  |
        |                  v                  |
        |                 S3/local            |
        |                                     |
        +------------------+------------------+
                           |
                     PostgreSQL
                           |
                      RabbitMQ
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        AI Worker     Notification   Activity Log
             |
             v
        Vector Store
             |
             v
             LLM
```

Later:

```text
GitHub
   |
   v
GitHub Actions
   |
   +--> Lint
   +--> Unit Tests
   +--> API Tests
   +--> Docker Build
   +--> Security Checks
   |
   v
Deployment
```

---

# 4. Free / Low-Cost Technology Choices

## Core

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL
- Pytest

## Microservices

- FastAPI
- Docker
- Docker Compose

## Communication

- RabbitMQ

## Cache

- Redis

## Storage

Development:
- Local Docker volume

Cloud:
- AWS S3 only when needed

## AI

Prefer a provider with a free tier if available.

The application should be designed so the LLM provider can be replaced.

Possible structure:

```text
AI Service
   |
   +--> LLM Provider Adapter
            |
            +--> Provider A
            +--> Provider B
            +--> Local model
```

This prevents the whole application from depending on one AI provider.

## Vector Storage

Start locally with:

- pgvector with PostgreSQL, OR
- ChromaDB

Prefer PostgreSQL + pgvector if practical because it reduces the number of infrastructure components.

## CI/CD

- GitHub Actions

## Monitoring

Start with:

- Python logging
- Docker logs

Later:

- Prometheus
- Grafana

---

# 5. Final Features

## Authentication

- Register
- Login
- Password hashing
- JWT
- Refresh token
- Logout
- Roles
- Protected endpoints

## Users

- View profile
- Update profile
- Delete account

## Files

```text
POST   /files/upload
GET    /files
GET    /files/{id}
DELETE /files/{id}
GET    /files/{id}/download
```

## Folders

```text
POST   /folders
GET    /folders
GET    /folders/{id}
PUT    /folders/{id}
DELETE /folders/{id}
```

Example:

```text
My Drive
|
+-- Projects
|   +-- Python
|   +-- AWS
|   +-- DSA
|
+-- Documents
|
+-- Resume
```

## AI Assistant

Users can ask questions about uploaded documents.

Examples:

```text
"What AWS services are mentioned in this document?"

"Summarize my Python interview notes."

"What does this document say about Docker?"

"Compare the concepts discussed in these two documents."
```

## Document Processing

```text
Upload PDF
    |
    v
Store file
    |
    v
Publish event
    |
    v
Document Worker
    |
    +--> Extract text
    +--> Split text
    +--> Generate embeddings
    +--> Store vectors
```

## Activity Logs

Examples:

```text
USER_REGISTERED
USER_LOGIN
FILE_UPLOADED
FILE_DELETED
FOLDER_CREATED
AI_QUERY
```

---

# 6. Database Design

Start with PostgreSQL.

Suggested tables:

```text
users
roles
user_roles
files
folders
document_chunks
activity_logs
chat_sessions
chat_messages
```

Important principle:

> A microservice should own its data. Other services should communicate through APIs/events rather than directly modifying another service's tables.

Initially, one PostgreSQL container can host multiple databases or schemas.

Do not over-engineer database infrastructure at the beginning.

---

# 7. Repository Structure

Target structure:

```text
cloudops-ai/
|
+-- services/
|   +-- auth-service/
|   +-- user-service/
|   +-- file-service/
|   +-- folder-service/
|   +-- ai-service/
|   +-- document-service/
|   +-- notification-service/
|   +-- activity-service/
|
+-- gateway/
|
+-- shared/
|
+-- infrastructure/
|
+-- tests/
|
+-- .github/
|   +-- workflows/
|
+-- docker-compose.yml
+-- .env.example
+-- .gitignore
+-- README.md
+-- PROJECT_PLAN.md
```

Do not create every directory immediately. Create services when their phase begins.

---

# 8. Git Strategy

Use:

```text
main
develop
feature/*
```

Example:

```text
feature/auth-register
feature/auth-login
feature/file-upload
feature/ai-rag
feature/ci-pipeline
```

Basic workflow:

```bash
git checkout develop
git checkout -b feature/my-feature

# work

git add .
git commit -m "feat: add user registration"

git push -u origin feature/my-feature
```

Merge into `develop` after testing.

Merge `develop` into `main` for stable milestones.

---

# 9. Daily 30-Minute Rule

Every day:

### First 5 minutes

Review:

- Yesterday's work
- Today's goal
- Any errors

### Next 20 minutes

Implement exactly one small task.

### Final 5 minutes

- Run tests
- Run the application
- Commit changes
- Write a short progress note

If a task takes longer than 30 minutes:

> Stop at a working checkpoint and continue tomorrow.

Do not rush.

---

# 10. 60-Day Plan

## WEEK 1 — Project Foundation

### Day 1 — Project Setup

Goal:

- Create GitHub repository
- Create local project
- Create README
- Create PROJECT_PLAN.md
- Create `.gitignore`
- Create `.env.example`

Checkpoint:

```text
cloudops-ai/
README.md
PROJECT_PLAN.md
.gitignore
.env.example
```

Commit:

```text
chore: initialize project
```

---

### Day 2 — Python Environment

Learn/setup:

- Python virtual environment
- pip
- requirements
- basic project structure

Create:

```text
services/
tests/
```

Commit:

```text
chore: setup python environment
```

---

### Day 3 — FastAPI Basics

Create a tiny FastAPI application.

Implement:

```text
GET /
GET /health
```

Expected:

```json
{
  "status": "ok"
}
```

---

### Day 4 — REST API Concepts

Learn:

- GET
- POST
- PUT
- PATCH
- DELETE
- HTTP status codes
- Request/response JSON

Create a small temporary `/hello` endpoint.

---

### Day 5 — Pydantic

Learn:

- Request models
- Response models
- Validation

Create:

```text
UserCreate
UserResponse
```

---

### Day 6 — API Documentation

Explore:

- Swagger
- OpenAPI
- `/docs`
- `/openapi.json`

Document the health endpoint.

---

### Day 7 — Review + Git

Do not add a major feature.

Tasks:

- Test the API
- Clean code
- Update README
- Commit
- Push

Milestone 1:

> Python + FastAPI foundation working.

---

# WEEK 2 — PostgreSQL + DBMS

### Day 8 — PostgreSQL

Run PostgreSQL locally.

Learn:

- Database
- Table
- Row
- Primary key
- Foreign key

---

### Day 9 — SQLAlchemy

Install/configure SQLAlchemy.

Create database connection.

---

### Day 10 — First Table

Create `users`.

Fields:

```text
id
email
password_hash
created_at
updated_at
```

---

### Day 11 — CRUD

Implement:

```text
POST /users
GET /users
GET /users/{id}
```

---

### Day 12 — Update/Delete

Implement:

```text
PUT /users/{id}
DELETE /users/{id}
```

---

### Day 13 — Alembic

Learn:

- Migration
- Upgrade
- Downgrade

Create the first migration.

---

### Day 14 — Database Review

Test:

- Create
- Read
- Update
- Delete
- Migration

Milestone 2:

> FastAPI + PostgreSQL + SQLAlchemy + Alembic working.

---

# WEEK 3 — Authentication

### Day 15 — Password Hashing

Implement secure password hashing.

Never store plain-text passwords.

---

### Day 16 — Registration

Create:

```text
POST /auth/register
```

---

### Day 17 — Login

Create:

```text
POST /auth/login
```

Return JWT.

---

### Day 18 — JWT Authentication

Create authentication dependency.

Protect:

```text
GET /users/me
```

---

### Day 19 — Roles

Create:

```text
roles
user_roles
```

Roles:

```text
USER
ADMIN
```

---

### Day 20 — Authorization

Create role checks.

Example:

```text
USER -> normal endpoints
ADMIN -> admin endpoints
```

---

### Day 21 — Auth Testing

Test:

- Registration
- Duplicate email
- Wrong password
- Correct login
- Invalid token
- Protected endpoint

Milestone 3:

> Secure authentication system working.

---

# WEEK 4 — Microservice Architecture

### Day 22 — Create Auth Service

Move authentication into:

```text
services/auth-service/
```

---

### Day 23 — User Service

Create:

```text
services/user-service/
```

---

### Day 24 — Service Communication

User Service communicates with Auth Service through REST.

---

### Day 25 — Docker Basics

Create Dockerfile for Auth Service.

---

### Day 26 — Docker Compose

Create:

```text
docker-compose.yml
```

Run:

```bash
docker compose up
```

---

### Day 27 — Two Services

Run:

```text
auth-service
user-service
postgres
```

in Docker.

---

### Day 28 — Review

Verify:

- Services start
- APIs work
- Database works
- Containers communicate

Milestone 4:

> First real microservices architecture working.

---

# WEEK 5 — File + Folder Management

### Day 29 — File Service

Create:

```text
services/file-service/
```

---

### Day 30 — File Metadata

Create:

```text
files
```

fields:

```text
id
user_id
filename
size
content_type
storage_path
created_at
```

---

### Day 31 — Upload API

Create:

```text
POST /files/upload
```

Initially store files locally.

---

### Day 32 — List Files

Create:

```text
GET /files
```

Only return files belonging to authenticated user.

---

### Day 33 — Download/Delete

Implement:

```text
GET /files/{id}/download
DELETE /files/{id}
```

---

### Day 34 — Folder Service

Create folder microservice.

---

### Day 35 — Folder Hierarchy

Implement parent/child folders.

Example:

```text
Projects
  |
  +-- Python
  |
  +-- AWS
```

Milestone 5:

> Working cloud-drive-style file and folder system.

---

# WEEK 6 — API Gateway + Redis

### Day 36 — API Gateway

Introduce gateway.

All external requests should eventually go through:

```text
/api/...
```

---

### Day 37 — Routing

Configure gateway routes:

```text
/api/auth/*
/api/users/*
/api/files/*
/api/folders/*
```

---

### Day 38 — Redis

Run Redis with Docker.

---

### Day 39 — Redis Caching

Cache:

```text
GET /users/me
```

---

### Day 40 — Cache Expiration

Learn:

- TTL
- Cache invalidation

---

### Day 41 — Rate Limiting

Implement basic rate limiting using Redis.

---

### Day 42 — Review

Milestone 6:

> Gateway + Redis working.

---

# WEEK 7 — RabbitMQ + Events

### Day 43 — RabbitMQ

Run RabbitMQ locally.

Learn:

- Producer
- Consumer
- Queue
- Exchange

---

### Day 44 — First Event

File Service publishes:

```text
FILE_UPLOADED
```

---

### Day 45 — Activity Consumer

Activity Service consumes the event.

---

### Day 46 — Activity Database

Store events in:

```text
activity_logs
```

---

### Day 47 — Notification Service

Create notification consumer.

---

### Day 48 — Failure Handling

Learn:

- Retry
- Acknowledgement
- Dead-letter concepts

Keep implementation simple.

---

### Day 49 — Review

Milestone 7:

> Event-driven microservice communication working.

---

# WEEK 8 — AI + RAG

### Day 50 — AI Service

Create:

```text
services/ai-service/
```

Design the service around a provider abstraction.

---

### Day 51 — Basic Chat API

Create:

```text
POST /ai/chat
```

First make a simple question/answer flow.

---

### Day 52 — Document Text Extraction

Add PDF text extraction.

---

### Day 53 — Text Chunking

Split documents into manageable chunks.

Example:

```text
Document
   |
   +-- Chunk 1
   +-- Chunk 2
   +-- Chunk 3
```

---

### Day 54 — Embeddings

Generate embeddings for chunks.

Keep the embedding provider replaceable.

---

### Day 55 — Vector Database

Use PostgreSQL + pgvector or ChromaDB.

Store:

```text
document_id
chunk_text
embedding
```

---

### Day 56 — Retrieval

Given a question:

```text
Question
   |
   v
Embedding
   |
   v
Vector Search
   |
   v
Relevant chunks
```

---

### Day 57 — RAG

Send:

```text
Question
+
Relevant document context
```

to the LLM.

---

### Day 58 — Chat History

Create:

```text
chat_sessions
chat_messages
```

Store conversation history.

---

### Day 59 — Document Chat

Implement:

```text
POST /ai/chat
```

where the answer is grounded in uploaded documents.

---

### Day 60 — AI Milestone

Test:

```text
Upload PDF
      |
      v
Extract text
      |
      v
Chunk
      |
      v
Embedding
      |
      v
Vector DB
      |
      v
Ask question
      |
      v
Retrieve chunks
      |
      v
LLM answer
```

Milestone 8:

> Working document-aware AI chatbot.

---

# WEEK 9 — Testing + Code Quality

### Day 61 — Pytest

Set up:

```text
pytest
```

---

### Day 62 — Auth Tests

Test:

- Registration
- Login
- Authentication
- Authorization

---

### Day 63 — File Tests

Test:

- Upload
- List
- Download
- Delete

---

### Day 64 — Folder Tests

Test folder hierarchy.

---

### Day 65 — AI Tests

Test:

- Text extraction
- Chunking
- Retrieval

Mock external AI calls where appropriate.

---

### Day 66 — API Integration Tests

Use HTTP client testing.

---

### Day 67 — Code Quality

Add:

- Ruff
- Formatting
- Type hints where practical

---

### Day 68 — Security Review

Check:

- Secrets
- Password handling
- JWT
- Input validation
- File validation
- CORS
- SQL injection protection

Milestone 9:

> Tested and cleaner backend.

---

# WEEK 10 — CI/CD

### Day 69 — GitHub Actions

Create:

```text
.github/workflows/ci.yml
```

---

### Day 70 — Automated Tests

Pipeline:

```text
Push
 |
 v
Install dependencies
 |
 v
Run pytest
```

---

### Day 71 — Linting

Add:

```text
ruff
```

to CI.

---

### Day 72 — Docker Build

CI should build Docker images.

---

### Day 73 — Security Scan

Add a free/open-source security scanning step.

---

### Day 74 — Branch Protection

Configure GitHub so important branches require successful CI.

---

### Day 75 — CI Review

Target:

```text
Push
 |
 v
GitHub Actions
 |
 +--> Tests
 +--> Lint
 +--> Docker Build
 +--> Security
 |
 v
PASS
```

Milestone 10:

> Automated CI pipeline working.

---

# WEEK 11 — Cloud Deployment

### Day 76 — AWS Planning

Before creating resources:

- Check current AWS free-tier/free-plan terms
- Estimate cost
- Decide what remains local

---

### Day 77 — AWS IAM

Create least-privilege deployment/user permissions.

Do not use root credentials for application work.

---

### Day 78 — AWS S3

Configure S3 for file storage.

---

### Day 79 — Environment Configuration

Separate:

```text
development
production
```

Never commit secrets.

---

### Day 80 — EC2

Deploy Dockerized application to an EC2 environment if the current AWS free allowance makes sense.

---

### Day 81 — Database Strategy

Decide between:

```text
Local PostgreSQL
```

and:

```text
AWS RDS
```

Use RDS only if cost/free allowance is appropriate.

---

### Day 82 — Deployment Test

Verify:

```text
Internet
   |
   v
Gateway
   |
   v
Services
   |
   +--> PostgreSQL
   +--> S3
   +--> Redis/RabbitMQ
```

Milestone 11:

> Cloud deployment working within chosen free/low-cost limits.

---

# WEEK 12 — Production Polish

### Day 83 — Logging

Add structured application logs.

---

### Day 84 — Health Checks

Create:

```text
/health
/ready
```

where appropriate.

---

### Day 85 — Monitoring

Add basic Prometheus metrics if practical.

---

### Day 86 — Grafana

Create a basic dashboard.

---

### Day 87 — API Documentation

Clean Swagger/OpenAPI documentation.

---

### Day 88 — README

Document:

- Architecture
- Setup
- APIs
- Database
- Docker
- AI
- CI/CD
- Deployment

---

### Day 89 — Architecture Diagram

Create a final architecture diagram.

---

### Day 90 — Final Review

Run the entire system.

Check:

```text
Authentication
       +
REST APIs
       +
Database
       +
Microservices
       +
File Storage
       +
RabbitMQ
       +
Redis
       +
AI/RAG
       +
Testing
       +
CI/CD
       +
Cloud
       +
Monitoring
```

Milestone 12:

> Portfolio-ready end-to-end project.

---

# 11. What "Done" Means

The project is complete when a new developer can clone the repository and understand:

1. What the project does.
2. Why microservices are used.
3. How services communicate.
4. How authentication works.
5. Where files are stored.
6. How PostgreSQL is used.
7. How RabbitMQ is used.
8. How Redis is used.
9. How RAG works.
10. How CI runs.
11. How deployment works.
12. How to run everything locally.

---

# 12. Important Free-Stack Rule

Do not add a paid technology just because it appears in a tutorial.

Preferred approach:

```text
Local first
   |
   v
Docker
   |
   v
Free/open-source software
   |
   v
Cloud free tier when useful
```

For example:

```text
PostgreSQL -> local Docker
Redis      -> local Docker
RabbitMQ   -> local Docker
Vector DB  -> PostgreSQL/pgvector or local Chroma
Storage    -> local Docker volume initially
AI         -> provider with suitable free tier or local model
CI/CD      -> GitHub Actions
```

AWS should be introduced after the application works locally.

---

# 13. AI Coding Assistant Rules

GitHub Copilot can help write code, but use it as an assistant.

For every generated code block:

1. Read it.
2. Understand it.
3. Run it.
4. Test it.
5. Modify it yourself where appropriate.

Useful prompts:

```text
Explain this FastAPI code line by line.
```

```text
Write a pytest test for this endpoint.
```

```text
Find security problems in this authentication code.
```

```text
Explain why this database query works.
```

Avoid:

```text
Build the entire project for me.
```

The objective is to learn while building.

---

# 14. Daily Progress Log

At the bottom of this file, maintain:

```text
## Progress

### Day 1
Status: Not Started
Completed:
Problems:
Next:

### Day 2
Status: Not Started
Completed:
Problems:
Next:
```

Update this every day.

---

# 15. Definition of Success

At the end of the project, you should be able to explain in an interview:

### Python

- Why Python?
- How FastAPI works
- Pydantic
- Async vs sync
- Dependency injection

### REST

- HTTP methods
- Status codes
- Authentication
- API versioning
- Validation

### DBMS

- Primary/foreign keys
- Indexes
- Transactions
- Normalization
- SQLAlchemy
- Migrations

### Microservices

- Why microservices?
- Service boundaries
- Database ownership
- REST communication
- Event-driven communication
- Failure handling

### RabbitMQ

- Producer
- Consumer
- Queue
- Exchange
- Acknowledgement

### Redis

- Caching
- TTL
- Rate limiting
- Cache invalidation

### AI

- Embeddings
- Vector search
- Chunking
- RAG
- Prompt construction
- Hallucination mitigation

### Docker

- Images
- Containers
- Dockerfile
- Compose
- Volumes
- Networks

### CI/CD

- GitHub Actions
- Tests
- Linting
- Docker builds
- Deployment

### Cloud

- IAM
- EC2
- S3
- RDS
- Security
- Cost management

---

# 16. Final Resume Project Description

Do not use this until the project is actually completed.

Suggested final description:

> Built an end-to-end cloud-based document management platform using Python and FastAPI with microservices, REST APIs, PostgreSQL, Redis, RabbitMQ, Docker, and GitHub Actions CI/CD. Implemented secure JWT authentication, file and folder management, asynchronous event processing, document ingestion, vector search, and a RAG-based AI assistant for querying uploaded documents. Containerized the platform and deployed selected components using AWS services with automated testing and CI/CD.

---

# 17. Golden Rule

## 30 minutes every day > 5 hours once a month.

Never skip the project because you only have 30 minutes.

A small commit every day will eventually become a complete system.

Start with **Day 1 only**.

Do not jump ahead until Day 1 works.
