from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import get_sales_by_one_dimention
app = FastAPI()

origins = ["http://localhost:8000",
           'http://192.168.1.168:8000',
           'http://192.168.1.268:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/sales/{dimention}")
def get_data_in_one_dimention(
    dimention: str
    ) -> dict:
    result = get_sales_by_one_dimention(dimention)
    return result

# @app.get("/sales/slice")
# async def get_data_slice(
#     
#     ) -> dict:
#     