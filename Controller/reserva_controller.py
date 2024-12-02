from datetime import date
from Models.reservas_model import ReservasModel
class ReservasController:
    def __init__(self):
        self.model = ReservasModel()

    def agregar_reserva(self, reserva_data):
        """
        Llama al modelo para agregar una nueva reserva a la base de datos.
        Calcula `codigo`, `noches`, y `precio_unitario` antes de agregar la reserva.
        """
        try:
            print("llego aqui")
            # Extraer los datos de reserva
            check_in = reserva_data["check_in"]
            checkout = reserva_data["check_out"]
            precio = reserva_data["precio"]
            habitacion = reserva_data["habitacion"]
            print(check_in)
            print(checkout)
            # Definir la fecha base (1 de enero de 1900)
            fecha_base = date(1900, 1, 1)

            # Calcular la diferencia en días entre la fecha base y el check_in
            dias_transcurridos = (check_in - fecha_base).days
            print(dias_transcurridos)
            dias_transcurridos=dias_transcurridos+2 #equivalente a excel
            print(dias_transcurridos)
            # El código se forma concatenando los días transcurridos con la habitación
            codigo = str(dias_transcurridos) + habitacion
            print(codigo)
            # Calcular la cantidad de noches (restar las fechas)
            noches = (checkout - check_in).days

            # Calcular el precio unitario (asumiendo que el precio es un decimal entero en pesos chilenos)
            if noches > 0:
                precio_unitario = precio // noches  # División entera para obtener un precio unitario entero
            else:
                precio_unitario = 0
            print(noches)
            print(precio_unitario)


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
            print(reserva_data)
            self.model.add_reservation(reserva_data)
            return {"status": "success", "message": "Reserva agregada correctamente"}

        except Exception as e:
            print(e)
            return {"status": "error", "message": str(e)}