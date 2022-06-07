#!/usr/bin/python3

import tweepy

def main():
    twitter_auth_keys = {
        "consumer_key": "PA1cClHXtfCZuNVbNSdCPhchO",
        "consumer_secret": "m2PiLSeXgEfkHQ4GlqH3I8KRazTotOohnFFWy7WLp3bkZkYjfx",
        "access_token": "1408723104742973441-pLi37z7SNKc46q7y9yEzTMFmMlu4S1",
        "access_token_secret": "iNQr00SHjJD9NV3U4ywcI25LbUAKdGMiCe8ijh5ng7GwP"
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
    
    #Busqueda de usuario y recuento de tweets
    timeline = api.user_timeline(screen_name= 'aestheticpi', count=1)
 
    #Consigue la source de la foto del registro o log registrado por el archivo testing.py
    with open('pylogs.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        
    #Cada tweet que encuentra lo cita con el caption sacado de los logs publicados en el archivo pylogs.txt con la id conseguida   
    for tweet in timeline:
        #el parametro f hace que pueda pasar variables por cadena de caracteres                        
        api.update_status(status = f'{last_line}', in_reply_to_status_id = tweet.id, auto_populate_reply_metadata=True)

        
    
    
    
    

if __name__ == "__main__":
    main()