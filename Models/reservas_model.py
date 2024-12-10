from Utils.conexion import conectar_db
import psycopg2
from psycopg2.extras import DictCursor

class ReservasModel:
    class Reserva:
        def __init__(self, id, codigo, check_in, check_out, nombre, apellido, correo,estado,tipo, celular, direccion, rut_pasaporte, pais, habitacion, adultos, ninos, precio, procedencia, pago, estado2, noches, estado_pago, precio_unitario, transbank,comentario, facturado, tipo_documento, folio_factura):
            self.id = id
            self.codigo = codigo
            self.check_in = check_in
            self.check_out = check_out
            self.nombre = nombre
            self.apellido = apellido
            self.correo = correo
            self.estado=estado
            self.tipo=tipo
            self.celular = celular
            self.direccion = direccion
            self.rut_pasaporte = rut_pasaporte
            self.pais = pais
            self.habitacion = habitacion
            self.adultos = adultos
            self.ninos = ninos
            self.precio = precio
            self.procedencia = procedencia
            self.pago = pago
            self.estado2 = estado2
            self.noches = noches
            self.estado_pago = estado_pago
            self.precio_unitario = precio_unitario
            self.transbank = transbank
            self.comentario = comentario
            self.facturado = facturado
            self.tipo_documento = tipo_documento
            self.folio_factura = folio_factura
    
    def __init__(self):
        self.connection = conectar_db()  # Usar la función conectar_db para la conexión
        self.cursor = self.connection.cursor(dictionary=True)  # Cambiado a cursor con diccionario

    def _get_cursor(self):
        """Obtiene un cursor para ejecutar consultas."""
        return self.connection.cursor(dictionary=True)


    def add_reservation(self, reserva_data):
        """Inserta una nueva reserva en la base de datos."""
        try:
            self.cursor.execute("""
            INSERT INTO reservas_tkinter (
                codigo,
                check_in, 
                check_out, 
                nombre, 
                apellido,
                correo,
                celular, 
                direccion,
                rut_pasaporte, 
                pais, 
                habitacion, 
                adultos, 
                ninos, 
                precio, 
                procedencia, 
                pago,
                estado2, 
                noches, 
                estado_pago,
                precio_unitario,
                transbank, 
                facturado, 
                tipo_documento,
                folio_factura
            )
            VALUES (
                %s, 
                %s, 
                %s,
                %s,
                %s, 
                %s, 
                %s, 
                %s,
                %s, 
                %s, 
                %s,
                %s, 
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s);
            """, (
                reserva_data.get('codigo', None), 
                reserva_data.get('check_in', None), 
                reserva_data.get('check_out', None), 
                reserva_data.get('nombre', None), 
                reserva_data.get('apellido', None), 
                reserva_data.get('correo', None), 
                reserva_data.get('celular', None), 
                reserva_data.get('direccion', None), 
                reserva_data.get('rut_pasaporte', None), 
                reserva_data.get('pais', None), 
                reserva_data.get('habitacion', None), 
                reserva_data.get('adultos', None), 
                reserva_data.get('ninos', None), 
                reserva_data.get('precio', None), 
                reserva_data.get('procedencia', None), 
                reserva_data.get('pago', None), 
                reserva_data.get('estado2', None), 
                reserva_data.get('noches', None), 
                reserva_data.get('estado_pago',None),
                reserva_data.get('precio_unitario', None), 
                reserva_data.get('transbank', 0), 
                reserva_data.get('facturado', False),  
                reserva_data.get('tipo_documento', None), 
                reserva_data.get('folio_factura', 0)
            ))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def edit_reservation(self, reserva_data):
        """Edita una reserva existente en la base de datos."""
        self.cursor.execute("""
        UPDATE reservas_tkinter
        SET codigo = %s, check_in = %s, check_out = %s, nombre = %s, apellido = %s, pais = %s, rut_pasaporte = %s, 
            celular = %s, direccion = %s, correo = %s, estado = %s, tipo = %s, habitacion = %s, adultos = %s, 
            ninos = %s, procedencia = %s, pago = %s, estado2 = %s, precio = %s, noches = %s, estado_pago = %s, 
            precio_unitario = %s, transbank = %s, comentario = %s, facturado = %s, tipo_documento = %s, 
            folio_factura = %s
        WHERE id = %s;
        """, reserva_data)
        self.connection.commit()

    def delete_reservation(self, reserva_id):
        """Elimina una reserva de la base de datos."""
        self.cursor.execute("""DELETE FROM reservas_tkinter WHERE id = %s;""", (reserva_id,))
        self.connection.commit()

    def list_reservations(self):
        """Obtiene todas las reservas de la base de datos."""
        self.cursor.execute("SELECT * FROM reservas_tkinter rt")
        return self.cursor.fetchall()

    def get_reservation_by_id(self, reserva_id):
        print('reserva_id', reserva_id)
        """Obtiene una reserva por su ID y retorna un objeto Reserva."""
        query = "SELECT * FROM reservas_tkinter WHERE id = %s"
        
        with self._get_cursor() as cursor:
            try:
                cursor.execute(query, (reserva_id,))
                row = cursor.fetchone()
                
                if row:
                    # Creamos una instancia de la clase Reserva con los datos obtenidos
                    reserva = self.Reserva(
                        id=row['id'],
                        codigo=row['codigo'],
                        check_in=row['check_in'],
                        check_out=row['check_out'],
                        nombre=row['nombre'],
                        apellido=row['apellido'],
                        correo=row['correo'],
                        estado=row['estado'],
                        tipo=row['tipo'],
                        celular=row['celular'],
                        direccion=row['direccion'],
                        rut_pasaporte=row['rut_pasaporte'],
                        pais=row['pais'],
                        habitacion=row['habitacion'],
                        adultos=row['adultos'],
                        ninos=row['ninos'],
                        precio=row['precio'],
                        procedencia=row['procedencia'],
                        pago=row['pago'],
                        estado2=row['estado2'],
                        noches=row['noches'],
                        estado_pago=row['estado_pago'],
                        precio_unitario=row['precio_unitario'],
                        transbank=row['transbank'],
                        comentario=row['comentario'],
                        facturado=row['facturado'],
                        tipo_documento=row['tipo_documento'],
                        folio_factura=row['folio_factura']
                    )
                    return reserva  # Retorna el objeto de la reserva
                else:
                    return None
            except Exception as e:
                print(f"Error: {e}")
                return None
    
    
    def update_reservation(self,reserva_data):
        #   reserva_data = {
        #         "id": reserva_id,
        #         "nombre": nombre,
        #         "apellido": apellido,
        #         "correo": correo,
        #         "celular": celular,
        #         "direccion": direccion,
        #         "rut_pasaporte": rut_pasaporte,
        #         "pais": pais,
        #         "check_in": checkin,
        #         "check_out": checkout,
        #         "habitacion": habitacion,
        #         "adultos": adultos,
        #         "ninos": ninos,
        #         "precio": precio,
        #         "procedencia": procedencia,
        #         "pago": metodo_pago,
        #         "tipo_documento": dte,
        #         "estado_pago": estado_pago
        #     }
        try:
            
            # print('Procedencia ',reserva_data['procedencia'])
            self.cursor.execute("""
            UPDATE reservas_tkinter
            SET nombre = %s, apellido = %s, correo = %s, celular = %s, direccion = %s, rut_pasaporte = %s, pais = %s,
                check_in = %s, check_out = %s, habitacion = %s, adultos = %s, ninos = %s, precio = %s, procedencia = %s,
                pago = %s, tipo_documento = %s, estado2 = %s
            WHERE id = %s;
            """, (
                reserva_data.get('nombre', None),
                reserva_data.get('apellido', None),
                reserva_data.get('correo', None),
                reserva_data.get('celular', None),
                reserva_data.get('direccion', None),
                reserva_data.get('rut_pasaporte', None),
                reserva_data.get('pais', None),
                reserva_data.get('check_in', None),
                reserva_data.get('check_out', None),
                reserva_data.get('habitacion', None),
                reserva_data.get('adultos', None),
                reserva_data.get('ninos', None),
                reserva_data.get('precio', None),
                reserva_data.get('procedencia', None),
                reserva_data.get('pago', None),
                reserva_data.get('tipo_documento', None),
                reserva_data.get('estado2', None),
                reserva_data.get('id', None)
            ))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            return None
        return True
        