from sqlalchemy.orm import Session
from Models.categorias_orm_model import Categoria

def crear_categoria(db: Session, nombre: str):
    nueva_categoria = Categoria(nombre=nombre)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

def listar_categorias(db: Session):
    return db.query(Categoria).all()

def eliminar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).get(categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()

def actualizar_categoria(db: Session, categoria_id: int, nuevo_nombre: str):
    categoria = db.query(Categoria).get(categoria_id)
    if categoria:
        categoria.nombre = nuevo_nombre
        db.commit()
