#!/bin/sh

# Script para a ordenação dos arquivos criados
for i in 12500 15000 17500 20000
# 50000 100000 150000 200000 250000 300000 350000 400000 450000 500000
do
	for metodo in 'quick' 'shell' 'default'
	# 'selection' 'insertion' 'quick' 'shell' 'default'
	do
		echo "\n >> kwii ordenar \"$i-clientes.pkl\" \"ordenados/$i-clientes-ordenados.pkl\" --metodo \"$metodo\""
		kwii ordenar "$i-clientes.pkl" "ordenados/$i-clientes-ordenados.pkl" --metodo "$metodo"
	done
done
