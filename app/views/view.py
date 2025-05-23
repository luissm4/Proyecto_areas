def mostrar_datos(lista_datos):
    for idx, dato in enumerate(lista_datos, start=1):
        print(f"{idx}. Área Protegida: {dato['area_protegida']}")
        print(f"   Municipio: {dato['municipio']}")
        print(f"   Área Jurisdicción: {dato['area_declarada_en_la_jurisdiccion']}")
        print(f"   Área Total: {dato['area_total_ha']}")
        print(f"   Declaratoria: {dato['declaratoria']}")
        print(f"   Plan Manejo: {dato['plan_de_manejo_ambiental']}")
        print(f"   Acuerdo Redelimitación: {dato['no_acuerdo_redelimitacion']}")
        print("-" * 40)
