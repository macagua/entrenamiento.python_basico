# Importar constantes
import constantes

print ("scp -v -P {0} {1}@{2}:/{3}/{4}/{4}.sql /srv/backup".format(
    str(constantes.PORT_DB_SERVER), constantes.USER_DB_SERVER, 
    constantes.IP_DB_SERVER, constantes.USER_DB_SERVER,
    constantes.DB_NAME))

