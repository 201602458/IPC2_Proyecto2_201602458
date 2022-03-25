import os.path
import carga
class Index:
    
    
    def __init__ (self, opcion):
        self.opcion=opcion

def main():
        var=carga.Carga_archivo()
       
        menu='''Menu Principal:
        1.- Cargar Archivo
        2.- Elejir ciudad
        3.- Elejir robot
        4.- Mostrar Grafica
        5.- Salir'''

        while True:
            print(menu)
            op=input("Ingrese una opcion: ")

            if op == '1':               
                rt=input("Ingrese la ruta del archivo: ")
                ext=os.path.splitext(rt)
            
                if ext[1]==".xml":    
                
                    var.archivoCarga(rt)                 
                else:
                    print("Archivo incorrecto")

            elif op == '2':  
                rt=input("Ingrese el nombre de la ciudad: ")
                var.cargaCiudad(rt)

                          
            elif op == '3':
                rt=input("Ingrese el nombre del robot: ")
                
                

            elif op == '4':
               
                print("Ordenes en cola: ")#mostrar
            
            elif op == '5':
                break
            else:
                print("Opcion Invalida")
                #break

    


if __name__ == "__main__":
    main()
