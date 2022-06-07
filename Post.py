#!/usr/bin/python3

import tweepy
import shutil, os
import testing

# Definimos una variable para que almacene el resultado del modulo que hemos creado anterior.
var = testing.result
# Damos las credenciales para el login en la API de Twitter
def main():
    twitter_auth_keys = {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": ""
    }
# Autentificamos y relizamos el proceso de log-in en Twitter
    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)


    # Realizamos un proceso de cambio de directorio de trabajo
    back = os.getcwd()
    os.chdir("pics/")

    # Definimos la variable de subida de la imagen que vamos a utilizar
    media = api.media_upload(var)

    # Definimos cual es el texto que va a utilzar el tweet como status
    tweet = testing.TweetCaption

    # Comienzo de bucle
    while True:
        #Comienza con el intento del bucle
        try:
            #Se postea el tweet si el tipo de archivo no devuelve error 
            post_result = api.update_status(media_ids=[media.media_id])
            #El archivo se elimina
            shutil.rmtree(r"/home/pi/Pictures/pics/")
            os.mkdir(r"/home/pi/Pictures/pics/")
            #Termina la ejecución y sale del bucle         
            break
        
        #Crea una excepción en caso de recibir un error
        except:
            #Se elimina aunque de fallo
            shutil.rmtree(r"/home/pi/Pictures/pics/")
            os.mkdir(r"/home/pi/Pictures/pics/")
            #Vuelve al principio del bucle
            continue
        



    # Vuelta al directorio padre
    os.chdir(back)
    
    

if __name__ == "__main__":
    main()
