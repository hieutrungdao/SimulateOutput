import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


app = FastAPI(title='FPT_Xray')
app.mount("/output", StaticFiles(directory="output"), name="output")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get('/')
# async def home():
#     return RedirectResponse("http://127.0.0.1:3000/")


@app.get('/output')
async def get_output():
    return RedirectResponse("http://127.0.0.1:5001/output/output.json")


@app.get("/test") 
async def test(): 
	return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5001)