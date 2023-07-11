from fastapi import APIRouter,Depends
from database.db import db_session,User
from sqlmodel import Session,select
from base.model import UserResponse,UserModel
from fastapi.exceptions import HTTPException
router = APIRouter()



@router.get("/user",response_model=list[UserResponse])
async def get_user(offset:int=1,per_page:int=10,db:Session=Depends(db_session)):
    query = select(User).offset(offset).limit(per_page)
    print(query)
    users = db.exec(query).all()
    return users
    
    
@router.post("/user",status_code=201)  
async def create_user(user: User, db: Session = Depends(db_session)):
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete('/user/{id}',status_code=204)
async def delete_user(id:int,db: Session = Depends(db_session)):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
    
    

