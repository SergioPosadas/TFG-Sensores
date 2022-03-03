import socket, sys, time, datetime

class Client(object):
    """
        Creación de la clase cliente para probar la conexión con SolarModule
    """
    
    msg = 'hola'
    
    def __init__(self, host, port):
        """
            Creación del constructor init para inicializar el socket del cliente a través del puerto
        """
        # Asignación de los valores correspondientes a las variables para crear
        # y poner a escuchar el socket del cliente
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
        
    def run(self):
        """
            Método para conectar con el módulo y enviar mensajes
        """
        # Comando para conectarse con el socket del módulo
        self.socket.connect((self.host, self.port))
                
        while True:
            # Una vez conectado con el socket del módulo, enviar el mensaje
            self.sendall(msg)
                        
            # Al haber realizado la conexión guardamos la información recibida en la variable data
            data = self.socket.recv(1024)
            
            # Si se ha recibido información del socket del módulo, se va mostrando una enumeración
            # cada seguundo hasta que no se envíe nada o se corte la conexión
            if data:            
                msg = 0
                print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Data received from SolarModules socket:', msg1)
                # logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Data received from SolarModules socket:', msg1)
                msg++
                time.sleep(1)
                
            # Si no se recibe nada se corta la conexión creada
            else:
                self.socket-close()
                break
        
