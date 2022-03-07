import socket, sys, logging, time, datetime

class SolarModule(object):
    """
	Creación de la clase SolarModule para probar el modulo a implementar 
    """
    
    
    def __init__(self, host, port):       
        """
            Creación del constructor init para inicializar el socket del módulo a través del puerto
	"""
	# Asignación de los valores correspondientes a las variables para crear 
        # y poner a escuchar el socket del módulo
        self.host = host
        self.port = port      
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 
        
                 
    def run(self):
        """
            Método para poner al socket a escuchar conexiones
        """
        # Comando para indicarle al socket en qué puerto escuchar las conexiones
        self.socket.bind((self.host, self.port))
                
        # Comando para que el socket acepte conexiones, el 1 indica que sólo se aceptará una conexión
        self.socket.listen(1)        
        
        while True:
        # Comando para estar a la espera de conexiones, devolviendo la conexión del cliente 
        # (guardada en connect) y la dirección (host y puerto) de dicha conexión 
            
            connect, address = self.socket.accept()            
            
            # Mensaje que informa sobre la dirección del cliente que se ha conectado, de momento solo saca la hora y la fecha
            # Mostramos el puerto de conexión
            logging.info('Conection finished succesfully in the specified port')
            
            while True:
                # Se comprueba si se recibe información del socket cliente
                data = connect.recv(1024)
                
                # Si se ha recibido información de dicho socket, se responde al cliente a modo de ACK
                if data:
                    connect.sendall(data)
                    
                # Si no se ha recibido información se corta la conexión con dicho socket
                else:
                    connect.close()
                    logging.info('Client disconected, bye')
                    break      

