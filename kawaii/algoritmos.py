#!/usr/bin/python3
'''
Vários algoritmos de ordenação interna, foram recolhidos de
vários links diferentes e postos nesse arquivo para serem
usados. As referências aos seus lugares de origem estão
mantidas em comentários próximos a cada um deles.
'''

##################
# Selection Sort #
##################

# http://pt.wikipedia.org/wiki/Selection_sort#C.C3.B3digo_em_Python
# http://www.geekviewpoint.com/python/sorting/selectionsort
def selectsort (L):
	n=len(L)
	for i in range(n-1):
		mini = i

		for j in range(i+1,n):
			if(L[j]<L[mini]):
				mini=j

		L[i],L[mini]=L[mini],L[i]

##################
# Insertion Sort #
##################

# http://pt.wikipedia.org/wiki/Insertion_sort#Python
def insertionSort(v):
	for j in range(1, len(v)):
		chave = v[j]
		i = j - 1
		while i >= 0 and v[i] > chave:
			v[i + 1] = v[i]
			i -= 1
		v[i + 1] = chave

##############
# Quick Sort #
##############

# http://pt.wikipedia.org/wiki/Quicksort#Python
# http://hetland.org/coding/python/quicksort.html
def quicksort_simple(v):
	if len(v) <= 1:
		return v # uma lista vazia ou com 1 elemento ja esta ordenada
	less, equal, greater = [], [], [] # cria as sublistas dos maiores, menores e iguais ao pivo
	pivot = v[0] # escolhe o pivo. neste caso, o primeiro elemento da lista
	for x in v:
		# adiciona o elemento x a lista correspondeste
		if x < pivot:
			less.append(x)
		elif x == pivot:
			equal.append(x)
		else:
			greater.append(x)

	# concatena e retorna recursivamente as listas ordenadas
	return quicksort_simple(less) + equal + quicksort_simple(greater)

def partition(v, left, right):
	i = left
	for j in range(left + 1, right + 1):
		if v[j] < v[left]: # Se um elemento j for menor que o pivo
			i += 1 # .. incrementa-se i
			v[i], v[j] = v[j], v[i] # .. e troca o elemento j de posicao o elemento i
	v[i], v[left] = v[left], v[i] # O pivo e' colocado em sua posicao final
	return i

def quicksort_inplace(v, left, right):
	if right > left: # Verifica se a lista tem 2 ou mais itens
		pivotIndex = partition(v, left, right) # Pega a posicao do pivo
		quicksort_inplace(v, left, pivotIndex - 1) # Ordena recursivamente os itens menores que o pivo
		quicksort_inplace(v, pivotIndex + 1, right) # Ordena recursivamente os itens maiores que o pivo

# http://stackoverflow.com/questions/18262306/quick-sort-with-python
def qsort(arr):
	if len(arr) <= 1:
		return arr
	else:
		return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

##############
# Shell Sort #
##############

# http://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Shell_sort#Python
def shellSort(array):
	"Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
	gap = len(array) // 2
	# loop over the gaps
	while gap > 0:
		# do the insertion sort
		for i in range(gap, len(array)):
			val = array[i]
			j = i
			while j >= gap and array[j - gap] > val:
				array[j] = array[j - gap]
				j -= gap
			array[j] = val
		gap //= 2

# http://runnable.com/UrTcfTe_GDtiAAMV/algorithms-shell-sort-python
def sort_shell(my_list):

	count_sublist = len(my_list)//2
	while count_sublist > 0:

		for pos_start in range(count_sublist):
			sort_gap_insertion(my_list,pos_start,count_sublist)

		count_sublist = count_sublist // 2

def sort_gap_insertion(my_list, start, gap):

	for i in range(start + gap, len(my_list), gap):

		val_current = my_list[i]
		pos = i
		while pos>=gap and my_list[pos-gap] > val_current:

			my_list[pos] = my_list[pos-gap]
			pos = pos-gap

		my_list[pos] = val_current



