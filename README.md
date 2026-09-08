CloudOps AI — scaffold + REST API + validation + docs basics

Quick start:
1. Create a virtual environment: python -m venv .venv
2. Activate it: .\\.venv\\Scripts\\activate (Windows) or source .venv/bin/activate (Unix)
3. Install deps: pip install -r requirements.txt
4. Run dev server: uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

Endpoints:
- GET /health -> health check
- GET / -> welcome message
- GET /hello -> returns the current hello message
- POST /hello -> create or replace the hello message (validates non-empty message under 50 chars)
- PUT /hello -> replace the hello message
- PATCH /hello -> update the hello message
- DELETE /hello -> reset to default hello message
- GET /docs -> Swagger UI for exploring the API
- GET /openapi.json -> machine-readable schema
- GET /redoc -> alternative API docs UI

Validation note:
- The /hello request payload uses Pydantic models.
- Empty strings and values exceeding 50 characters are rejected with 422.

See PROJECT_PLAN.md for daywise tasks.