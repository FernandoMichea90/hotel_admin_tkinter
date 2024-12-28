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


Base = declarative_base()

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
DATABASE_URL = "mysql+mysqlconnector://root:123@localhost/hotel_ecomusic"
engine = create_engine(DATABASE_URL)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Funciones del modelo
def listar_reservas():
    return session.query(Reserva).all()

def filtrar_reservas_por_fecha(inicio, fin):
    return session.query(Reserva).filter(
            or_(
            Reserva.check_in.between(inicio, fin),
            Reserva.check_out.between(inicio, fin)
        )).all()