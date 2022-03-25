class nodo:

    def __init__(self, signo, valor):
        self.signo=signo
        self.valor=valor
        self.anterior=None
        self.siguiente=None
        self.arriba=None
        self.abajo=None


class matriz:

    def __init__(self):
        self.inicio=nodo(0,0)

    def crear(self,fila,columna):
        for i in range(int(fila)):
            print('\n')
            for j in range(int(columna)):
                print('*')
            