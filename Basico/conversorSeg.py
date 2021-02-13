segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = segundos // 86400
segundos = segundos % 86400
hora = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos2 = segundos % 60
print(dia,"dias,", hora,"horas,", minutos, "minutos e", segundos2,"segundos")