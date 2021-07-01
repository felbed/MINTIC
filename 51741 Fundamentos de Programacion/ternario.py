condicion = 5 > 7
valor = "días" if condicion else "noches"
print(f"Buenos {valor}")

valor = ("días", "noches")[condicion]
print(f"Buenos {valor}")
