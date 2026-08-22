### 🏢  Network device backups and simple topology (Cisco CML Topology)

Este Laboratorio posee una topologia sencilla simulada en un sandbox de cisco el cual es el laboratorio por
defecto de (CML), este laboratorio tiene configuracioens adicionales en los dispositivos y con un archivo de automatización 
Hecho con python y netmiko para el guardado de la configuracion total de dichos dispositivos.

---


### 🎯 Objetivos del Laboratorio

- ✅ Segmentar la red en VLANs para separar departamentos
- ✅ Implementar enrutamiento OSPF para comunicación entre VLANs
- ✅ Configurar Router-on-a-Stick con subinterfaces
- ✅ Proveer servicios DHCP y NAT para acceso a internet
- ✅ Asegurar los puertos de acceso con Port-Security
- ✅ Implementar IPv6 con DHCPv6 y OSPFv3
- ✅ Automatizar backups con Python y Netmiko

---

### 📊 Topologia de la red 

Esta red esta diseñada con la arquitectura de core colapsado  (Acceso,Distribucion/Core,routers de borde) garantizado tolerancia a fallos.

![Topología Física](Topologia/topologia_fisica.png)

---

## 📂 Estructura del Repositorio

** `Código_Automatización_backups/`: contiene el archivo de python usando netmiko para lanzar el script y el guardado de las configuraciones
    de todos los dispositivos de red de este laboratorio.
* `configs/`: Contiene los scripts de configuración individual listos para cargar vía consola o SSH en los equipos de CML2.
  * `Sw1.txt`, `Sw2.txt`
  * `R1.txt`, `R2.txt`
  *`Host.txt`
* `Notas/`: Explicación mas a detalle de las configruaciones de los dispositivos 
* `Topologia/`:  imágenes de la topología en ejecución.

---

## 🛠️ Requisitos en los Dispositivos de Red

* **SSH Habilitado**: Netmiko utiliza SSH por defecto; Telnet no se recomienda por seguridad.
* **Usuario Local**: Una cuenta con credenciales válidas creadas en el dispositivo o en un servidor .
* **Privilegios de Lectura**: El usuario necesita nivel de privilegio suficiente para ejecutar comandos show (ej. Nivel 1 o superior en Cisco).
* **Contraseña de Enable**: Si el usuario no entra directo al modo privilegiado, necesitas configurar la contraseña de enable.
* **Llaves Criptográficas**: SSH requiere que el dispositivo tenga generado su par de llaves RSA (mínimo 1024 bits).

---

+ ## 🚀 Cómo Ejecutar el Script de Automatización
+ 
+ ```bash
+ # 1. Instalar Netmiko
+ pip install netmiko
+ 
+ # 2. Ejecutar el script
+ python automatizacion_dos.py
+ 
+ # 3. Verificar los backups generados
+ ls ~/Desktop/Backup_Dispositivos_Laboratorio/

--
Todos los equipos de red en este laboratorio cuentan con las siguientes políticas de prácticas implementadas:
* Cifrado de contraseñas globales (`service password-encryption`).
* Secretos de habilitación robustos y autenticación local por SSH  (claves RSA de 2048 bits).
* Banner MOTD de advertencia legal ante accesos no autorizados.