print('Calcular precio de venta')

pp = input('Ingrese el Valor del producto = ')

pp = float(pp)

igv = pp * float(0.18)
igv = float(igv)

pv = pp + igv
pv = float(pv)

print('El precio del Producto sin IGv es = ',pp)
print('El precio del Igv (18%) es = ',igv)
print ('El total a pagar es = ', pv)
