from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(
    title="CloudOps AI",
    description="Local FastAPI API for the CloudOps AI project. This app is used for health checks, minimal REST examples, and API documentation review.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

hello_state = {"message": "hello"}


class HelloMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=50)

    @field_validator("message")
    @classmethod
    def normalize_message(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("message cannot be empty")
        return cleaned


class HelloResponse(BaseModel):
    message: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "CloudOps AI - FastAPI scaffold"}


@app.get("/hello", response_model=HelloResponse, summary="Get the current hello message")
async def get_hello():
    return HelloResponse(message=hello_state["message"])


@app.post("/hello", status_code=201, response_model=HelloResponse, summary="Create or set a hello message")
async def create_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"created: {new_message}")


@app.put("/hello", response_model=HelloResponse, summary="Replace the hello message")
async def replace_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"updated: {new_message}")


@app.patch("/hello", response_model=HelloResponse, summary="Update the hello message")
async def update_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"patched: {new_message}")


@app.delete("/hello", summary="Reset the hello message to the default value")
async def delete_hello():
    previous = hello_state["message"]
    hello_state["message"] = "hello"
    return {"deleted": previous, "message": "hello"}
