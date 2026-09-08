from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="CloudOps AI - Dev")

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


@app.get("/hello", response_model=HelloResponse)
async def get_hello():
    return HelloResponse(message=hello_state["message"])


@app.post("/hello", status_code=201, response_model=HelloResponse)
async def create_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"created: {new_message}")


@app.put("/hello", response_model=HelloResponse)
async def replace_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"updated: {new_message}")


@app.patch("/hello", response_model=HelloResponse)
async def update_hello(payload: HelloMessage):
    new_message = payload.message
    hello_state["message"] = new_message
    return HelloResponse(message=f"patched: {new_message}")


@app.delete("/hello")
async def delete_hello():
    previous = hello_state["message"]
    hello_state["message"] = "hello"
    return {"deleted": previous, "message": "hello"}
