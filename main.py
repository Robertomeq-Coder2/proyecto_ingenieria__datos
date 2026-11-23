import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["Laptop", "Mouse" , "Teclado" , "Monitor"],
    "precio" : [15000,400,800,4500],
    "cantidad" : [2,5,3,1]
})

ventas

ventas["ingresos"] = ventas["precio"] * ventas["cantidad"]

ventas


def calcular_resumen(df):
    resumen = {
        "total_proudctos": len(df),
        "ingresos_totales" : df["ingresos"].sum(),
        "unidades_vendidas": df["cantidad"].sum(),
        "precio_promedio": df ["precio"].mean()
    }

    return resumen

resumen = calcular_resumen(ventas)

print(resumen)


