from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Enum,
    DECIMAL,
    Text,
    Boolean,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from Utils.Database import Base,db
from datetime import datetime, timedelta


session=db;



class Reserva(Base):
    __tablename__ = 'reservas_tkinter'  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, nullable=False)
    codigo = Column(Integer, unique=True)
    check_in = Column(Date)
    check_out = Column(Date)
    nombre = Column(String(50))
    apellido = Column(String(50))
    pais = Column(String(50))
    rut_pasaporte = Column(String(20))
    celular = Column(String(15))
    direccion = Column(String(100))
    correo = Column(String(100))
    estado = Column(String(20))
    tipo = Column(String(20))
    habitacion = Column(String(20))
    adultos = Column(Integer)
    ninos = Column(Integer)
    procedencia = Column(Enum('Booking', 'Pagina web', 'Whatsapp', 'Walking', 'Pendiente'))
    pago = Column(Enum('Tarjeta', 'Transferencia', 'Efectivo', 'Pendiente'))
    estado2 = Column(Enum('Pagado', 'Pendiente'))
    precio = Column(Integer)
    noches = Column(Integer)
    estado_pago = Column(String(20))
    precio_unitario = Column(Integer)
    transbank = Column(Integer)
    comentario = Column(Text)
    facturado = Column(Boolean)
    tipo_documento = Column(
        Enum('Factura', 'Factura de exportacion', 'Boleta', 'Efectivo', 'Pendiente')
    )
    folio_factura = Column(Integer)


# Configuración de SQLAlchemy con MySQL


# Funciones del modelo
def listar_reservas():
    print("Listar reservas")
    return session.query(Reserva).all()

def filtrar_reservas_por_fecha(inicio, fin):
    return session.query(Reserva).filter(
            or_(
            Reserva.check_in.between(inicio, fin),
            Reserva.check_out.between(inicio, fin)
        )).all()
    
def agregar_reserva(reserva_data):
    reserva = Reserva(**reserva_data)
    session.add(reserva)
    session.commit()
    return reserva

def actualizar_reserva(reserva_data):
    reserva_id = reserva_data.pop("id")
    session.query(Reserva).filter(Reserva.id == reserva_id).update(reserva_data)
    session.commit()
    
def eliminar_reserva(reserva_id):
    session.query(Reserva).filter(Reserva.id == reserva_id).delete()
    session.commit()


def obtener_datos_del_mes():
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Obtener el primer y último día del mes actual
    inicio_mes = fecha_actual.replace(day=1)
    fin_mes = fecha_actual.replace(day=28) + timedelta(days=4)  # esto asegura que la fecha sea en el mes siguiente
    fin_mes = fin_mes - timedelta(days=fin_mes.day)  # obtener el último día del mes

    # Filtrar reservas de este mes por check_in
    reservas_mes = session.query(Reserva).filter(
        Reserva.check_in >= inicio_mes,
        Reserva.check_in <= fin_mes
    ).all()

    # Calcular la suma de precios del mes
    total_precio = sum(reserva.precio for reserva in reservas_mes)

    # Calcular el total de noches en todas las reservas
    total_noches = sum(reserva.noches for reserva in reservas_mes)

    # Calcular el promedio de ventas por noche
    if total_noches > 0:
        promedio_ventas_por_noche = total_precio / total_noches
    else:
        promedio_ventas_por_noche = 0

    # Devolver los resultados
    return {
        "total_reservas": len(reservas_mes),
        "total_precio": total_precio,
        "total_noches": total_noches,
        "promedio_ventas_por_noche": promedio_ventas_por_noche
    }
