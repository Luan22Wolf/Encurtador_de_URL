from fastapi import FastAPI, HTTPException, Request, Depends, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 
from database import SessionLocal, engine
from datetime import datetime
import models, schemas, utils
import os

templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Página inicial com o formulário
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/encurtar-html", response_class=HTMLResponse)
def encurtar_html(request: Request, long_url: str = Form(...), db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.long_url == long_url).first()
    if db_url:
        short_url = request.url_for("redirecionar", short_code=db_url.short_code)
        return templates.TemplateResponse("resultado.html", {"request": request, "short_url": short_url})

    short_code = utils.generate_short_code()
    new_url = models.URL(long_url=long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    short_url = request.url_for("redirecionar", short_code=short_code)
    return templates.TemplateResponse("resultado.html", {"request": request, "short_url": short_url})

# Faz o encurtamento via JSON (API REST)
@app.post("/encurtar", response_model=schemas.URLInfo)
def encurtar_url(url_data: schemas.URLBase, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.long_url == url_data.long_url).first()
    if db_url:
        return db_url    
    short_code = utils.generate_short_code()
    new_url = models.URL(long_url=url_data.long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

@app.get("/{short_code}", name="redirecionar")
def redirecionar(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL não encontrada.")
    if db_url.expires_at < datetime.utcnow():
        raise HTTPException(status_code=410, detail="Este link expirou.")
    return RedirectResponse(url=db_url.long_url)

# uvicorn main:app --reload