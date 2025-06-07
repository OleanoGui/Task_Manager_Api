from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Task, SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/")
def create_task(title: str, description: str, db: Session = Depends(get_db)):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, description: str, completed: bool, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = title
    task.description = description
    task.completed = completed
    db.commit()
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Tarefa deletada com sucesso"}