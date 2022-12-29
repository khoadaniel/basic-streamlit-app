# https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92
# https://levelup.gitconnected.com/fastapi-fundamentals-getting-faster-with-fastapi-866545b841ca

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from utils import cal


class user_input(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.get("/")
def health_check():
    return 'Hello World'


@app.post("/calculate")
def operate(input: user_input):
    result = cal(input.operation, input.x, input.y)
    return result


# if __name__ == '__main__':
#     uvicorn.run(app, port=8001, host='0.0.0.0')