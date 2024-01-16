"""
Las tuplas son inmutables, no se pueden modificar
"""

tuplas=("uno","dos","tres")

print(tuplas[2])

tuplasVariosDatos=(12,True,23.5,"El gato",12+4j)
print(tuplasVariosDatos)

tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasVariosDatos[0:2])

a,b,c=tuplas
print(a)
print(b)
print(c)

tuplaNueva=tuplas+tuplasVariosDatos
print(tuplaNueva)

