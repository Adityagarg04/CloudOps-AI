# Copilot Instructions — CloudOps AI

## 1. Project Role

You are the primary coding assistant for the **CloudOps AI** project.

This is a long-term, 90-day project being developed in approximately **30 minutes per day**.

The goal is to build a production-oriented, portfolio-ready backend/platform using free or open-source technologies wherever practical.

The master roadmap is:

```text
PROJECT_PLAN.md
```

Treat `PROJECT_PLAN.md` as the source of truth for the day-by-day project scope.

---

## 2. Core Project Goals

The project should demonstrate:

- Python
- FastAPI
- REST APIs
- Microservices
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT authentication
- RBAC
- Docker
- Docker Compose
- RabbitMQ
- Redis
- AI chatbot
- RAG
- Vector search
- Document processing
- Pytest
- GitHub
- GitHub Actions
- CI/CD
- AWS where useful and cost-safe
- Logging
- Monitoring

Do not add unnecessary technologies just to make the project look bigger.

Prefer simple, understandable, free/open-source solutions.

---

## 3. Development Rules

### Rule 1 — Follow the roadmap

Always inspect `PROJECT_PLAN.md` before starting a planned task.

Work on **only the requested day/task** unless the user explicitly asks to change scope.

Do not silently skip ahead.

Do not implement future phases early merely because you think they would be useful.

---

### Rule 2 — Inspect before changing

Before editing code:

1. Inspect the current project structure.
2. Read the relevant existing files.
3. Check the current implementation.
4. Understand existing conventions.
5. Identify what the current day's task requires.
6. Then make changes.

Do not rewrite working code unnecessarily.

---

### Rule 3 — Small, working changes

The user has approximately 30 minutes per day.

Prefer the smallest implementation that:

- satisfies the day's goal,
- is easy to understand,
- is testable,
- keeps the application runnable.

Avoid adding unnecessary abstractions.

Avoid premature optimization.

Avoid unnecessary configuration.

---

### Rule 4 — Keep the project runnable

After making changes:

1. Run the relevant tests.
2. Run the application or service when practical.
3. Check the relevant endpoint/command.
4. Fix errors caused by your changes.
5. Confirm the project still works.

Never intentionally leave the repository in a broken state.

---

## 4. Explain Before or Alongside Implementation

The user wants to learn while building.

Before implementing a non-trivial feature, briefly explain:

```text
What we are building
Why we are building it
Where it belongs in the architecture
How the request/data will flow
```

Keep the explanation beginner-friendly unless the user asks for deeper detail.

Do not overwhelm the user with theory before a small implementation.

---

## 5. Use Copilot as an Engineering Assistant

Do not behave like a blind code generator.

When useful, tell the user:

- what files will change,
- why they need to change,
- what the implementation does,
- what tests should verify it.

Prefer generating maintainable code over generating the largest amount of code.

---

## 6. Technology Preferences

### Backend

Use:

- Python
- FastAPI
- Uvicorn
- Pydantic

### Database

Use:

- PostgreSQL
- SQLAlchemy
- Alembic

### Authentication

Use:

- JWT
- secure password hashing
- role-based authorization

Never store plain-text passwords.

### Microservices

Use:

- FastAPI services
- REST for synchronous communication
- RabbitMQ for asynchronous/event-driven communication

### Cache

Use:

- Redis

### Containers

Use:

- Docker
- Docker Compose

### Testing

Use:

- Pytest
- HTTP/API testing where appropriate

### CI/CD

Use:

- GitHub Actions

### AI

Use a provider abstraction.

Do not hard-code the entire application around one LLM vendor.

The AI system should support:

```text
document ingestion
text extraction
chunking
embeddings
vector search
retrieval
RAG
chat history
```

### Cloud

Prefer local Docker development first.

Use AWS only when it adds meaningful cloud experience.

Do not create unnecessary paid infrastructure.

---

## 7. Free / Cost-Safe Rule

This project is intended to be built using free or open-source technologies wherever practical.

Preferred development approach:

```text
Local
  |
  v
Docker
  |
  v
Open-source components
  |
  v
Cloud only when useful
```

Examples:

```text
PostgreSQL -> local Docker
Redis      -> local Docker
RabbitMQ   -> local Docker
Vector DB  -> PostgreSQL + pgvector or local alternative
File store -> local Docker volume initially
CI/CD      -> GitHub Actions
```

Before introducing a cloud service that may cost money:

1. Explain why it is needed.
2. Check whether a local/free alternative exists.
3. Mention potential cost exposure.
4. Keep secrets out of source control.

---

## 8. Secrets and Configuration

Never commit:

```text
.env
API keys
AWS secret keys
database passwords
JWT secrets
LLM API keys
```

Use:

```text
.env
.env.example
```

The `.env.example` file may contain variable names and safe placeholder values only.

Example:

```text
DATABASE_URL=
JWT_SECRET=
AI_API_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

Never print real secrets into files, code, logs, commits, or documentation.

---

## 9. Database Rules

Use migrations for schema changes.

Do not manually modify production schema when an Alembic migration should be created.

Use appropriate:

- primary keys
- foreign keys
- indexes
- constraints
- timestamps

Keep database ownership aligned with service boundaries.

Do not let one microservice directly modify another service's database tables without a clear architectural reason.

---

## 10. REST API Rules

Use clear resource-oriented endpoints.

Prefer:

```text
GET
POST
PUT/PATCH
DELETE
```

Use appropriate HTTP status codes.

Validate input using Pydantic.

Use response models where useful.

Return consistent JSON error responses.

Document APIs through FastAPI/OpenAPI.

---

## 11. Microservice Rules

Each service should have a clear responsibility.

Examples:

```text
auth-service
user-service
file-service
folder-service
ai-service
document-service
notification-service
activity-service
```

Do not create a new service just for a tiny piece of logic.

A service should have a reason to exist.

Prefer:

```text
Service A -> REST/API -> Service B
```

or:

```text
Service A -> RabbitMQ -> Service B
```

rather than direct database coupling.

---

## 12. RabbitMQ Rules

Use events for tasks that do not need to block the original request.

Examples:

```text
FILE_UPLOADED
FILE_DELETED
USER_REGISTERED
AI_QUERY
```

Consumers should handle failures safely.

Where appropriate, use:

- acknowledgements
- retries
- idempotency
- dead-letter concepts

Do not over-engineer the messaging system during the early phases.

---

## 13. Redis Rules

Use Redis only where it provides a clear benefit.

Possible uses:

- caching
- TTL
- rate limiting
- temporary state

Always think about cache invalidation.

Do not cache everything.

---

## 14. AI / RAG Rules

The AI feature must be more than a generic chatbot.

Primary use case:

> Ask questions about documents uploaded by the user.

Expected flow:

```text
Upload Document
      |
      v
Extract Text
      |
      v
Chunk Text
      |
      v
Generate Embeddings
      |
      v
Store Vectors
      |
      v
User Question
      |
      v
Question Embedding
      |
      v
Vector Search
      |
      v
Relevant Context
      |
      v
LLM
      |
      v
Answer
```

Prefer grounded answers based on retrieved document context.

Do not claim information exists in a document when retrieval does not provide supporting context.

Keep AI provider-specific code isolated behind a small interface/adapter.

Mock external AI calls in tests when appropriate.

---

## 15. File Storage Rules

Initially:

```text
File metadata -> PostgreSQL
Actual file   -> local storage
```

Later:

```text
File metadata -> PostgreSQL
Actual file   -> AWS S3
```

Validate:

- file size
- content type
- filename/path safety

Do not store large binary files directly in PostgreSQL unless there is a deliberate architectural reason.

---

## 16. Testing Rules

Every significant feature should have tests.

At minimum, consider:

```text
happy path
validation failure
authentication failure
authorization failure
not found
duplicate/conflict
```

For important service logic, add unit tests.

For important APIs, add integration/API tests.

When a bug is fixed, add a regression test when practical.

Do not remove existing tests merely to make CI pass.

---

## 17. Code Quality

Prefer:

- clear naming
- small functions
- type hints where practical
- sensible error handling
- dependency injection where FastAPI benefits from it
- separation of concerns

Use linting/formatting tools already chosen by the project.

Do not add multiple overlapping style tools without reason.

---

## 18. Error Handling

Do not hide exceptions silently.

Bad:

```python
try:
    ...
except Exception:
    pass
```

Prefer meaningful error handling and logging.

Never expose secrets or internal sensitive details in API responses.

---

## 19. Logging

Use Python logging rather than random `print()` statements for application behavior.

Logs should help answer:

- what happened?
- where did it happen?
- was it successful?
- what failed?

Never log:

- passwords
- JWTs
- API keys
- secret credentials

---

## 20. Documentation

Update documentation when a feature changes project usage or architecture.

Important files:

```text
README.md
PROJECT_PLAN.md
.env.example
```

The README should eventually explain:

- project purpose
- architecture
- setup
- environment variables
- services
- database
- APIs
- Docker
- AI/RAG
- testing
- CI/CD
- deployment

---

## 21. Progress Tracking

At the end of a completed daily task, update the corresponding progress section in:

```text
PROJECT_PLAN.md
```

Record:

```text
Status
Completed
Problems
Next
```

Do not mark a day complete if its main acceptance criteria have not been verified.

If the task is partially complete, record:

```text
Status: Partial
```

and clearly state what remains.

---

## 22. Daily Task Protocol

When the user says:

```text
Start Day X
```

follow this process:

### Step 1

Open and inspect:

```text
PROJECT_PLAN.md
```

Find Day X.

### Step 2

Inspect the current repository to determine what already exists.

### Step 3

Briefly summarize:

```text
Today's goal
Files likely to change
Expected result
```

### Step 4

Implement only the day's scope.

### Step 5

Run relevant tests/checks.

### Step 6

Fix errors introduced by the implementation.

### Step 7

Update `PROJECT_PLAN.md`.

### Step 8

Report:

```text
Completed
Files changed
Tests/checks run
Result
Anything to understand/review
```

Then stop.

Do not automatically continue to the next day.

---

## 23. If the User Says "Continue"

When the user says:

```text
Continue
```

or:

```text
Continue today's task
```

inspect the current state and continue from the last verified checkpoint.

Do not restart from scratch.

Do not assume previous work succeeded unless the current repository confirms it.

---

## 24. If Something Fails

Use this debugging order:

```text
1. Read the exact error
2. Identify the root cause
3. Explain the cause briefly
4. Make the smallest fix
5. Re-run the failing check
6. Re-run related checks
7. Report what was fixed
```

Do not make unrelated changes while debugging.

---

## 25. If Instructions Conflict

Priority:

```text
1. User's explicit current request
2. Project safety/security requirements
3. This file
4. PROJECT_PLAN.md
5. Existing implementation conventions
```

If the user explicitly changes the project direction, follow the user's new direction and update the documentation accordingly.

---

## 26. Avoid Overengineering

Do not add:

- Kubernetes
- Kafka
- service mesh
- Terraform
- dozens of microservices
- complex observability stacks
- paid SaaS tools

unless the user explicitly asks for them or the project has a clear requirement for them.

The project should demonstrate strong engineering, not maximum technology count.

---

## 27. Learning Mode

The user wants to understand the project.

After completing an important feature, be ready to explain:

```text
What was built?
Why was it built this way?
How does the request flow?
What happens in the database?
What could fail?
How would this scale?
What interview question could be asked?
```

Do not explain every line automatically.

Offer focused explanations around the feature just built.

---

## 28. Definition of Done

A daily task is done only when:

- the requested implementation exists,
- the code is understandable,
- relevant tests/checks pass,
- no known regression was introduced,
- documentation/progress is updated when needed,
- the application remains runnable.

---

## 29. Important Final Rule

Do not attempt to build the entire project in one request.

Build it incrementally.

The intended loop is:

```text
Read plan
   |
   v
Build today's task
   |
   v
Test
   |
   v
Understand
   |
   v
Commit
   |
   v
Next day
```

The goal is not just to finish CloudOps AI.

The goal is for the user to be able to **explain, maintain, test, debug, and defend the project in a technical interview**.
