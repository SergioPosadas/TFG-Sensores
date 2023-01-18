import socket, sys, logging, time, datetime, json, noise

import numpy as np

import matplotlib.pyplot as plt


class SolarModule(object):
    """
    Creación de la clase SolarModule para probar el modulo a implementar
    """

    def __init__(self, host, port, m, n, REQUEST, RESPONSE):
        """
        Creación del constructor init para inicializar el socket del módulo a través del puerto y las dimensiones del plano
        """

        # Asignación de los valores correspondientes a las variables para crear
        # y poner a escuchar el socket del módulo
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m = m
        self.n = n
        self.REQUEST = REQUEST
        self.RESPONSE = RESPONSE
       

    def run(self):
        """
        Método para poner al socket a escuchar conexiones y generar el plano del módulo

        """

        # Creación de la variable shape que contendrá las dimensiones del plano con las variables (m,n)
        # y generación del plano con 0's para después generar el plano con ruido de perlin

        shape = (self.m, self.n)
        pl = np.zeros(shape)

        logging.info(pl)

        # Creación de las variables que se utilizarán para la generacion del ruido de perlin en el plano

        scale = 100.0  # Proporcion entre el plano dibujado y el real
        octaves = 6  # Número de nivel de detalle que se quiere tenga el ruido de perlin
        persistence = (
            0.75  # Número que determina cuánto contribuye una octava a la forma general
        )
        lacunarity = 2.0  # Número que hace que la imagen sea mas heterogénea

        # Creación del ruido de perlin en el plano a través de dos bucles for y la funcion noise importada más arriba

        for i in range(shape[0]):
            for j in range(shape[1]):
                pl[i][j] = noise.pnoise2(
                    i / scale,
                    j / scale,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=1000,
                    repeaty=1000,
                    base=100,
                )

        # Obtención de los valores máximos, mínimos, media, desviación y varianza del plano para obtener el dominio aleatorio del plano generado

        logging.info("Showing generated plain info...:")

        maxim = np.amax(pl)
        logging.info("Maximun's value is: " + str(maxim))

        minim = np.amin(pl)
        logging.info("Minimun's value is: " + str(minim))

        med = np.mean(pl)
        logging.info("Medium's value is: " + str(med))

        desv = np.std(pl)
        logging.info("Standard deviation's value is: " + str(desv))

        var = np.std(pl)
        logging.info("Variance's value is: " + str(var))

        # El dominio aleatorio generado será el rango de valores entre el valor mínimo y el máximo de nuestro plano

        logging.info("Random domain generated is: [" + str(minim) + ", " + str(maxim) + "].")

        # Dibujado del plano creado a través de matplotlib

        fig, ax = plt.subplots()
        ax.imshow(pl)
        plt.show()

        # Una vez que se sabe el dominio aleatorio, es necesario ponderarlo con el dominio "real" que hay en España,
        # para saber la irradiación "real" de nuestro plano en el plano que hemos generado, nuestros puntos se encuentran
        # entre [-0,432342351 y 0,463847239], en el dominio que hemos elegido, varían entre [2,47 y 4,65].
        # Por lo tanto, se guardarán dichos valores en diferentes variables, se hará una ponderación del dominio real y
        # se creará la variable dominio donde guardaremos el dominio del plano ponderado previa inicialización igual a 0.

        dom = np.zeros(shape)
        mxdom = 4.65
        mndom = 2.47

        for i in range(shape[0]):
            for j in range(shape[1]):
                x = pl[i][j] - minim
                p = (x * (mxdom - mndom)) / (maxim - minim)
                r = mndom + p
                dom[i][j] = r

        logging.info("Showing weighted plane information:")
        logging.info(dom)

        maximum = np.amax(dom)
        logging.info("Maximum's value is: " + str(maximum))

        minimum = np.amin(dom)
        logging.info("Minimum's value is: " + str(minimum))

        media = np.mean(dom)
        logging.info("Medium's value is: " + str(media))

        desviation = np.std(dom)
        logging.info("Standard deviation's value is: " + str(desviation))

        variance = np.std(dom)
        logging.info("Variance's value is: " + str(variance))

        # El dominio ponderado será el rango de valores entre el valor mínimo y el máximo de nuestro plano ponderado

        logging.info("Real domain generated is: [" + str(minimum) + ", " + str(maximum) + "]")

        # Impresión del plano ponderado y obtención de los valores máximos, mínimos, media, desviación y varianza del plano
        # ponderado para comprobar que se ha hecho bien

        fig, ax = plt.subplots()
        ax.imshow(dom)
        plt.show()

        # Una vez obtenido el plano, se procede a conectar el módulo con el sensor IoT para conocer los valores de irradiancia
        # del plano generado

        # Comando para indicarle al socket en qué puerto escuchar las conexiones
        self.socket.bind((self.host, self.port))

        # Comando para que el socket acepte conexiones, el 1 indica que sólo se aceptará una conexión
        logging.info("Waiting for a new conection...")
        self.socket.listen(1)

        while True:
            # Comando para estar a la espera de conexiones, devolviendo la conexión del cliente
            # (guardada en connect) y la dirección (host y puerto) de dicha conexión

            connect, address = self.socket.accept()

            # Mensaje que informa sobre la dirección del cliente que se ha conectado, de momento solo saca la hora y la fecha
            # Mostramos el puerto de conexión
            logging.info("Conection done succesfully in the specified port.")

            while True:
                # Se comprueba si se recibe información del socket cliente
                if data := connect.recv(1024):
                    self.RESPONSE = data.decode()
                    result = type(self.RESPONSE)
                    logging.info(self.RESPONSE)
                    logging.info(result)
                    
                    # Una vez comprobado se verifica el tipo de peticion del cliente, si es request se extrae el punto solicitado
                    # y se envía el valor de la irradiancia en dicho punto
                    if ((self.RESPONSE['X point'] >= 0) and (self.RESPONSE['X point'] <= 1000)):
                        x = self.RESPONSE['X point']
                        y = self.RESPONSE['Y point']
                            
                        logging.info("Requested item: (" + str(x) + ", " + str(y) + ")")
                            
                        self.REQUEST['X point'] = x
                        self.REQUEST['Y point'] = y
                        self.REQUEST['Value'] = dom[x][y]
                            
                        connect.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))
                           
                        # Si se recibe un punto incorrecto del plano, se envia un "REQUEST" indicando que hay un error
                        # se tiene que repetir el proceso de envío del "REQUEST"                        
                    else:
                        logging.info("Incorrect item requested...")
                        logging.info("Requesting that the process be repeated...")
                        self.REQUEST['type'] = 'ACK'
                        self.REQUEST['message'] = 'repeat'
                        connect.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))
                        
                else:
                    logging.info("Timeout expired, closing conection...")
                    connect.close()
                    logging.info("Client disconected, bye.")
                    self.socket.close()
                    break

                
                    
                   
                   
                   
                   
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
