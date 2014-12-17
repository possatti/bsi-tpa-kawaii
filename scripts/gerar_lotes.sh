#!/bin/sh

# Série de comandos para gerar lotes de clientes desordenados

for i in 12500 15000 17500 20000
# 50000 100000 150000 200000 250000 300000 350000 400000 450000 500000
do
	echo " >> kwii gerar $i"
	kwii gerar $i
done
