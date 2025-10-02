a = 50
b=40
c =39

def suma():
    print("Suma total: ", a + b +c )

suma()

def generar_datos_ventas():
    dias=["LUN", "MAR", "MIE", "JUEV", "VIE"]
    ventas = [120, 230,450,140,870]
    return dias, ventas

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total/len(ventas)

    return {
        "dias":dias,
        "Ventas":ventas,
        "total" :total,
        "promedio":promedio

    }

datos = resumen_analitica()
print("Total de ventas: ", datos["total"])
print("Promedio diario: ", datos["promedio"])