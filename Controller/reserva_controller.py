from datetime import date, timedelta
from Models.reservas_model import ReservasModel
from Models.reservas_orm_model import listar_reservas, filtrar_reservas_por_fecha, agregar_reserva,actualizar_reserva,eliminar_reserva, obtener_datos_del_mes
class ReservasController:
    def __init__(self):
        self.model = ReservasModel()

    def agregar_reserva(self, reserva_data):
        """
        Llama al modelo para agregar una nueva reserva a la base de datos.
        Calcula `codigo`, `noches`, y `precio_unitario` antes de agregar la reserva.
        """
        try:
            # Extraer los datos de reserva
            check_in = reserva_data["check_in"]
            checkout = reserva_data["check_out"]
            precio = reserva_data["precio"]
            habitacion = reserva_data["habitacion"]
            
            # Definir la fecha base (1 de enero de 1900)
            fecha_base = date(1900, 1, 1)

            # Calcular la diferencia en días entre la fecha base y el check_in
            dias_transcurridos = (check_in - fecha_base).days
            dias_transcurridos=dias_transcurridos+2 #equivalente a excel
            # El código se forma concatenando los días transcurridos con la habitación
            codigo = str(dias_transcurridos) + habitacion
            # Calcular la cantidad de noches (restar las fechas)
            noches = (checkout - check_in).days

            # Calcular el precio unitario (asumiendo que el precio es un decimal entero en pesos chilenos)
            if noches > 0:
                precio_unitario = precio // noches  # División entera para obtener un precio unitario entero
            else:
                precio_unitario = 0
            
        # Convierte las fechas a cadenas con el formato adecuado
            check_in_str = reserva_data['check_in'].strftime('%Y-%m-%d')
            check_out_str = reserva_data['check_out'].strftime('%Y-%m-%d')
            
            # Actualiza los valores de las fechas en el diccionario de reserva
            reserva_data['check_in'] = check_in_str
            reserva_data['check_out'] = check_out_str
            # Preparar los datos de la reserva con los campos calculados
            reserva_data["codigo"] = codigo
            reserva_data["noches"] = noches
            reserva_data["precio_unitario"] = precio_unitario

            # Agregar la reserva en la base de datos
            # self.model.add_reservation(reserva_data)
            agregar_reserva(reserva_data)   
            return {"status": "success", "message": "Reserva agregada correctamente"}

        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
        
    def listar_reservas(self):
        try:
            return self.model.list_reservations()
        except Exception as e:
             print(e)
             return {"status": "error", "message": str(e)}
    
    def listar_reservas_por_hoy(self):
        try:
            return self.model.list_reservations_by_today()
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
         
    def  get_reserva(self, id_reserva):
        try:
            return self.model.get_reservation_by_id(id_reserva)
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
    def delete_reserva(self, reserva_id):
        try:
            eliminar_reserva(reserva_id)
            return {"status": "success", "message": "Reserva eliminada correctamente"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
    def actualizar_reserva(self,reserva_id, nombre, apellido, correo, celular, direccion, rut_pasaporte, pais, checkin, checkout, habitacion, adultos, ninos, precio, procedencia, metodo_pago, dte, estado_pago):
        try:
            reserva_data = {
                "id": reserva_id,
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "celular": celular,
                "direccion": direccion,
                "rut_pasaporte": rut_pasaporte,
                "pais": pais,
                "check_in": checkin,
                "check_out": checkout,
                "habitacion": habitacion,
                "adultos": adultos,
                "ninos": ninos,
                "precio": precio,
                "procedencia": procedencia,
                "pago": metodo_pago,
                "tipo_documento": dte,
                "estado_pago": estado_pago
            }
            # agregar atributos calculados: codigo, noches, precio_unitario
            # dias transcurridos
            fecha_base = date(1900, 1, 1)
            dias_transcurridos = (checkin - fecha_base).days
            dias_transcurridos=dias_transcurridos+2 #equivalente a excel
            # noches 
            noches = (checkout - checkin).days
            # precio unitario
            if noches > 0:
                precio_unitario = float(precio) // noches  # División entera para obtener un precio unitario entero
                precio_unitario=int(precio_unitario)
            else:
                precio_unitario=0
            #codigo 
            codigo = str(dias_transcurridos) + habitacion
            
            #agregar atributos calculados al diccionario
            reserva_data["codigo"] = codigo
            reserva_data["noches"] = noches
            reserva_data["precio_unitario"] = precio_unitario
            #actualizar reserva
            # self.model.update_reservation(reserva_data)
            actualizar_reserva(reserva_data)
            return True
        except Exception as e:
            print(e)
            return False

    def listar_reservas_orm(self):
        try:
            return listar_reservas()
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
    
    def listar_reservas_por_fecha(self, inicio, fin):
        try:
            return filtrar_reservas_por_fecha(inicio, fin)
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
    
    def obtener_ocupaciones_por_fecha(self, inicio, fin):
        try:
            # Filtrar las reservas en el rango de fechas especificado
            reservas = filtrar_reservas_por_fecha(inicio, fin)
          
            ocupaciones = {}
            for reserva in reservas:
                habitacion_id = int(reserva.habitacion)
                check_in = reserva.check_in
                check_out = reserva.check_out
                cliente = f"{reserva.nombre} {reserva.apellido}"
                pagado = reserva.estado2 == 'Pagado'

                # Asegurar que la habitación exista en el diccionario
                if habitacion_id not in ocupaciones:
                    ocupaciones[habitacion_id] = {}

                # Generar fechas desde check_in hasta el día anterior a check_out
                fecha_actual = check_in
                while fecha_actual < check_out:
                    ocupaciones[habitacion_id][fecha_actual.strftime("%Y-%m-%d")] = {
                        "cliente": cliente,
                        "pagado": pagado
                    }
                    fecha_actual += timedelta(days=1)

            return ocupaciones
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}
        
    def obtener_datos_del_mes(self):
        try:
            return obtener_datos_del_mes()
        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}