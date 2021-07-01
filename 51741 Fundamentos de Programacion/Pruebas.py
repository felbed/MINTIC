info = [[2.698, -76.680, 63],
        [2.724, -76.693, 20],
        [2.606, -76.742, 680],
        [2.698, -76.690, 15]]

def verificador_coor(latitud, longitud):
    latitud_sup = 2.766
    latitud_inf = 2.548
    longitud_or = -76.493
    longitud_occ = -76.879

    if latitud_inf <= valor <= latitud_sup or longitud_occ <= valor <= longitud_or:
        coordenadas[i][j] = valor
    else:
        print("Error coordenada")

