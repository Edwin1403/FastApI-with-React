from fastapi import APIRouter ,HTTPException,status ,Depends
from database import get_db
from sqlalchemy.orm import Session
from auth import current_user
import model , schema
from typing import List

route = APIRouter(
    tags=['Vote']
)

@route.get('/vote')
def vote(data : schema.vote , db : Session=Depends(get_db) , current_user = Depends(current_user)):
    print(data.dir)
    check =db.query(model.Post).filter(model.Post.id == data.post_id).first()
    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="Post not found")
        
    if data.dir == 0:
        check = db.query(model.Vote).filter(model.Vote.user_id == current_user , model.Vote.post_id == data.post_id)
        if check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="You already voted")
            
        vote = model.Vote(user_id = current_user , post_id = data.post_id )
        db.add(vote)
        db.commit()
        db.refresh(vote)
        return(vote)
    elif data.dir == 1:
        check = db.query(model.Vote).filter(model.Vote.user_id == current_user , model.Vote.post_id == data.post_id)
        if not check.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Didn't vote this post")
        check.delete(synchronize_session=False)
        db.commit()
        return {"your vote remoted"}