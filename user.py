from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
import model,schema, passcode , auth
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post('/insert')
async def insert (data:schema.create,db:Session=Depends(get_db)):
    encode = passcode.passcode(data.password)
    data.password = encode
    new=model.user(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return(new)

@app.get('/gets')
def gets ( db:Session=Depends(get_db)):
    gts=db.query(model.user).all()
    return(gts)

@app.get('/get')
def get (db:Session=Depends(get_db) , current_user =Depends(auth.current_user)):
    gt=db.query(model.user).filter(model.user.id==current_user).first()
    return(gt)

@app.put('/change')
def change (data:schema.create,db:Session=Depends(get_db) , current_user = Depends(auth.current_user)):
    ch=db.query(model.user).filter(current_user==model.user.id)
    ch.update(data.dict(),synchronize_session = False)
    db.commit()
    return ch.first()

@app.delete('/remove')
def remove (db:Session=Depends(get_db) , current_user = Depends(auth.current_user)):
    rem=db.query(model.user).filter(current_user==model.user.id)
    if not rem.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The id -{current_user} is not found")
    rem.delete(synchronize_session=False)
    db.commit()
    return rem.first()


@app.post('/login')
def login (data: OAuth2PasswordRequestForm = Depends(), db:Session= Depends(get_db)):
    user = db.query(model.user).filter(model.user.email == data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email is not found")
        
    print(user.password, data.password)
    check = passcode.verify(data.password, user.password)
    if not check:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "user credential is no valid")
    token = auth.create_token(data={"id":user.id})

    return {"access_token":token , "token_type":"bearer"}

@app .get("/api")
async def root():
    return{"message":"Welcome to Fast API"}