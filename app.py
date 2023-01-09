from fastapi import FastAPI
main  = FastAPI()
@main.get('/') #this the path/route
def index():
    return "This is the front page"