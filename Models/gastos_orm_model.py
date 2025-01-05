from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from Utils.Database import Base

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    metodo_pago = Column(String(50))
    proveedor = Column(String(100))
    notas = Column(String)

    categoria = relationship("Categoria")
