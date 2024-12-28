from datetime import date
from Controller.reserva_controller import ReservasController

rc=ReservasController()
inicio = date(2024, 12, 1)
fin = date(2024, 12, 30)
print(inicio, fin)
ocupaciones = rc.obtener_ocupaciones_por_fecha(inicio, fin)

print(ocupaciones)
