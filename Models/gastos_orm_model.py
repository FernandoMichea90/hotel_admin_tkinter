from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from Utils.Database import db,Base
from sqlalchemy.sql import func
from sqlalchemy import extract
from datetime import datetime, timedelta
from Models.categorias_orm_model import Categoria


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(255), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    monto = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    metodo_pago = Column(String(50))
    proveedor = Column(String(100))
    notas = Column(String)

    categoria = relationship("Categoria")


    def obtener_gastos_mes():
        """
        Obtiene el total de gastos del mes actual y los distribuye por categorías con nombres de categoría.

        Args:
            db (Session): Sesión de la base de datos.

        Returns:
            dict: Un diccionario con el total de gastos y la distribución por categorías.
        """
        # Fecha actual
        fecha_actual = datetime.now()

        # Calcular el primer día del mes
        primer_dia_mes = fecha_actual.replace(day=1)

        # Calcular el último día del mes (primer día del próximo mes menos un día)
        if fecha_actual.month == 12:
            ultimo_dia_mes = datetime(fecha_actual.year + 1, 1, 1) - timedelta(days=1)
        else:
            ultimo_dia_mes = datetime(fecha_actual.year, fecha_actual.month + 1, 1) - timedelta(days=1)

        primer_dia_mes = primer_dia_mes.date()
        ultimo_dia_mes = ultimo_dia_mes.date()
        
        

        # Consulta para obtener el total de gastos del mes actual
        total_gastos_mes = db.query(func.sum(Gasto.monto)).filter(
            Gasto.fecha >= primer_dia_mes,
            Gasto.fecha <= ultimo_dia_mes
        ).scalar()

        # Consulta para obtener los gastos distribuidos por categorías
        gastos_por_categoria = db.query(
            Categoria.nombre.label("nombre_categoria"),
            func.sum(Gasto.monto).label("total_categoria")
        ).join(Categoria, Gasto.categoria_id == Categoria.id).filter(
            Gasto.fecha >= primer_dia_mes,
            Gasto.fecha <= ultimo_dia_mes
        ).group_by(Categoria.id).all()

        # Formatear los resultados
        distribucion_categorias = [
            {"categoria": nombre_categoria, "total": total}
            for nombre_categoria, total in gastos_por_categoria
        ]

        # Construir el resultado final
        resultado = {
            "total_gastos_mes": total_gastos_mes or 0,
            "gastos_por_categoria": distribucion_categorias
        }

        return resultado