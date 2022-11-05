import ctypes

biblioteca = ctypes.CDLL("libfuncao.so")

biblioteca.funcao.argtypes= [ctypes.c_double]

valor = biblioteca.funcao(ctypes.c_double(2.3).value)

print(valor)
