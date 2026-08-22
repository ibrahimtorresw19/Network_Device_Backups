#================================================================================
#SCRIPT DE BACKUP AUTOMATIZADO PARA DISPOSITIVOS DE RED
#================================================================================

#NOTA DE SEGURIDAD:
#    Este script utiliza credenciales en texto plano (cisco/cisco) por ser
#    un entorno de laboratorio. En entornos de PRODUCCIÓN, se recomienda
#    usar variables de entorno o un archivo de configuración externo.

#    Para implementar variables de entorno:
#    1. Crear archivo .env con:
#        DEVICE_USERNAME=cisco
#        DEVICE_PASSWORD=cisco
#        DEVICE_SECRET=cisco

#    2. Instalar: pip install python-dotenv

#    3. Agregar al script:
#        from dotenv import load_dotenv
 #       load_dotenv()
#        USERNAME = os.getenv('DEVICE_USERNAME', 'cisco')
#================================================================================
#

import os
from datetime import datetime, timezone

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException

# 1. Configuración de fechas y rutas optimizada
fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
ruta_home = os.path.expanduser("~")
ruta_carpeta = os.path.join(
    ruta_home, "Desktop", "Backup_Dispositivos_Laboratorio", fecha
)

# exist_ok=True evita errores si ejecutas el script más de una vez el mismo día
os.makedirs(ruta_carpeta, exist_ok=True)

lista_ips = ["10.10.20.171", "10.10.20.172","10.10.20.173", "10.10.20.174"]

dispositivo = {
    "device_type": "cisco_ios",
    "host": "",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "port": 22,
}

# 2. Ciclo de conexión y respaldo
for ip in lista_ips:
    dispositivo["host"] = ip
   

    try:
        with ConnectHandler(**dispositivo) as connect:
            connect.enable()
            prompt = connect.find_prompt()
            hostname = prompt.replace("#", "")

            
            nombre_archivo = f"{hostname}__{ip}_config.txt"
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            backup_configuration=connect.send_command("sh run")
            with open (ruta_archivo ,"w" ,encoding="utf-8") as f:
                f.write(backup_configuration) 
             
        
            print(f"Respaldo completado para {hostname}")
            print(f"    [!] ¡Éxito! Copia de seguridad guardada en: {ruta_archivo}")

    except NetmikoAuthenticationException as e:
        print(f"Error de autenticación en la IP {ip}: {e}")
  