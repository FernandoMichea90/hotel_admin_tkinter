from Models.categorias_orm_model import Categoria
from Utils.Database import db

def crear_categoria( nombre: str):
    nueva_categoria = Categoria(nombre=nombre)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

def listar_categorias():
    return db.query(Categoria).all()

def eliminar_categoria( categoria_id: int):
    categoria = db.query(Categoria).get(categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()

def actualizar_categoria( categoria_id: int, nuevo_nombre: str):
    categoria = db.query(Categoria).get(categoria_id)
    if categoria:
        categoria.nombre = nuevo_nombre
        db.commit()
def obtener_categoria_por_id( categoria_id: int):
    return db.query(Categoria).get(categoria_id)
