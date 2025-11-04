from fastapi import FastAPI 

app = FastAPI()

#standard get request
@app.get('/hello-world')
def hello_world():
    return {'message': 'Hello World'}

    