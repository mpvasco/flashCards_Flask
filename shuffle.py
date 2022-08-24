from random import randint, shuffle
tpl = ((1, 'a', 'b'),(2, 'c', 'd'),(3, 'e', 'f'),(4, 'g', 'h'),(5, 'i', 'j'),(6, 'k', 'l'),(7, 'a', 'b'),(8, 'c', 'd'),(9, 'e', 'f'),(10, 'g', 'h'),(11, 'i', 'j'),(12, 'k', 'l'))
# tpl = ((1, 'a', 'b'),(2, 'c', 'd'),(3, 'e', 'f'),(4, 'g', 'h'))

def shuffle_def(x):
  size = len(x)
  list= []
  count = 0
  # lista de 0 a size-1 
  while count < size:
    list.append(count)
    count+=1
  print(list)
  #shuffle lista
  list_shuffled = shuffle(list)
  print(list_shuffled)
  # pegar slice de 10 ou total size se maior ou menor que 10.
  if size > 10:
    list = list[0:10]
    return list
  elif size <= 10:
    list = list[0:size]
    return list

b = shuffle_def(tpl)

print("b",b)

index=0
def click(index):
  index+=1
  print(index)
  return index
  
# index = click(index)
# index = click(index)
# index = click(index)

def show_card(b):
  index = click(index)
  print(b[index])

show_card(b)