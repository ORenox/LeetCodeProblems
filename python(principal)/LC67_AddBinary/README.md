**Diferencia entre divisones**

En este ejercicio estoy aprendiendo bastante sobre como funciona los diferenctes tipos de divisiones.

Tenemos:
* división entera //
* Módulo de división %
* División real /

## Lenguaje
Python

## Enfoque
Bit manipulation / simulación

## Complejidad
- Tiempo: O(n)
- Espacio: O(1)

## Código
```python

ans=[]
carry = 0
i = len(a) - 1
j = len(b) -1

while i>=0 or j>=0 or carry==1:
    if i>=0:
        carry += int(a[i])
        i-=1
    if j>=0:
        carry += int(b[j])
        j-=1
    ans.append(str(carry % 2))
    carry //= 2
return ''.join(reversed(ans))
...