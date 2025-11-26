from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def initial_placement():
    pass

@app.post("/assignWithCsv/{path}")
def post_csv(path):
    pass



