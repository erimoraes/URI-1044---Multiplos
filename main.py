#URI 1044 - Múltiplos

'''Leia 2 valores inteiros (A e B). Após, o programa deve mostrar 
uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", 
indicando se os valores lidos são múltiplos entre si.

Entrada:
A entrada contém valores inteiros.

Saída:
A saída deve conter uma das mensagens conforme descrito acima.'''

valores = list(map(int,input().split()))
a = valores[0]
b = valores[1]
if ((a % b) == 0 ) or (b % a) == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
  