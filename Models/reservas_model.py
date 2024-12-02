from Utils.conexion import conectar_db


class ReservasModel:
    def __init__(self):
        self.connection = conectar_db()  # Usar la función conectar_db para la conexión
        self.cursor = self.connection.cursor()

    def add_reservation(self, reserva_data):
        """Inserta una nueva reserva en la base de datos."""
        
        # Verifica que el diccionario tiene los parámetros necesarios
        print(reserva_data)  # Esto imprime los valores de reserva_data para que puedas ver si están todos
        
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
                reserva_data.get('transbank', None), 
                reserva_data.get('facturado', None),  # Facturado en lugar de estado2
                reserva_data.get('tipo_documento', None), 
                reserva_data.get('folio_factura', None)
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
        self.cursor.execute("""
        DELETE FROM reservas_tkinter WHERE id = %s;
        """, (reserva_id,))
        self.connection.commit()

    def list_reservations(self):
        """Obtiene todas las reservas de la base de datos."""
        self.cursor.execute("SELECT * FROM reservas_tkinter")
        return self.cursor.fetchall()

    def get_reservation_by_id(self, reserva_id):
        """Obtiene una reserva por su ID."""
        self.cursor.execute("SELECT * FROM reservas_tkinter WHERE id = %s", (reserva_id,))
        return self.cursor.fetchone()
