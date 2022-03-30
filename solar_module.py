import socket, sys, logging, time, datetime, json

####################################################################################
#                                                                                  #
# OBTENER EL ARCHIVO JSON, LEERLO, CARGAR LOS DATOS EN LAS RESPECTIVAS VARIABLES,  #
# CODIFICARLO A BYTES Y ENVIARLO. RECIBIR EL JSON DE SOLARMODULE, DECODIFICARLO,   #
# LEERLO Y MOSTRAR POR PANTALLA EL CONTENIDO.                                      #
#                                                                                  #
####################################################################################


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
        
        # Obtención del archivo json con el contenido del mensaje que se va a enviar a SolarModule
        with open("Response.json", "r") as resp:
        	self.response = json.loads(resp, sys.stdout)
        	
        	# (Control) Mostrar por pantalla el archivo obtenido
        	print(self.response)
        
        
    def run(self):
        """
            Método para poner al socket a escuchar conexiones
        """
        
        # Variable msg para enviar información mientras hago que funcione el json
        #msg = 'Hola'
        #msg = msg.encode('utf-8') 
                
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
            logging.info('Conection done succesfully in the specified port')
            
            while True:
                # Se comprueba si se recibe información del socket cliente
                data = connect.recv(1024)
                data = json.load(data)
                print(data)
                
                # Si se ha recibido información de dicho socket, se responde al cliente a modo de ACK
                if data:
                    connect.sendall(self.response)
                    
                # Si no se ha recibido información se corta la conexión con dicho socket
                else:
                    connect.close()
                    logging.info('Client disconected, bye')
                    break      

