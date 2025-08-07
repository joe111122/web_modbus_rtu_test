from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
origins = ["http://0.0.0.0:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/static", StaticFiles(directory="static"), name="static")
# template = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))
template = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root():
    return {"message": "Hello"}


@app.get("/get_template", response_class=HTMLResponse)
async def read_template(request: Request):
    return template.TemplateResponse(
        request=request, name="main4.html",context={"modbus_data":63})

if __name__ == "__main__":
    uvicorn.run("main3:app", host="0.0.0.0", port=8000, reload=True)
