from sqlalchemy.orm import Session
from Models.gastos_orm_model import Gasto
from Utils.Database import db

def crear_gasto( descripcion, categoria_id, monto, fecha, metodo_pago, proveedor, notas):
    nuevo_gasto = Gasto(
        descripcion=descripcion,
        categoria_id=categoria_id,
        monto=monto,
        fecha=fecha,
        metodo_pago=metodo_pago,
        proveedor=proveedor,
        notas=notas
    )
    db.add(nuevo_gasto)
    db.commit()
    db.refresh(nuevo_gasto)
    return nuevo_gasto

def listar_gastos():
    return db.query(Gasto).all()

def eliminar_gasto( gasto_id: int):
    gasto = db.query(Gasto).get(gasto_id)
    if gasto:
        db.delete(gasto)
        db.commit()

def actualizar_gasto( gasto_id: int, **kwargs):
    gasto = db.query(Gasto).get(gasto_id)
    if gasto:
        for key, value in kwargs.items():
            setattr(gasto, key, value)
        db.commit()
def obtener_gastos_mes():
    try:
        return Gasto.obtener_gastos_mes()
    except Exception as e:
        return {"status": "error", "message": str(e)}

