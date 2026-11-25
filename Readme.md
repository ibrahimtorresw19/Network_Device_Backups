### 🌐 Dual-Stack Enterprise Network (IPv4/IPv6) & Netmiko Automation (Cisco CML)

Este laboratorio implementa una infraestructura empresarial Dual-Stack (IPv4 e IPv6) simulada en Cisco Modeling Labs (CML). Incluye segmentación por VLANs, enrutamiento dinámico OSPFv2/OSPFv3, servicios DHCP/DHCPv6 Stateful, NAT/PAT con Port Forwarding, seguridad en Capa 2/Capa 3 y scripts en Python con Netmiko y TextFSM para el aprovisionamiento de configuraciones y la generación automática de reportes de inventario.

---

### 🎯 Objetivos del Laboratorio

- ✅ Segmentar la red en VLANs (10, 20, 30, 40 y Nativa 90) con Router-on-a-Stick.
- ✅ Implementar direccionamiento Dual-Stack con DHCPv4, DHCPv6 Stateful y OSPFv2/OSPFv3 en Área 0.
- ✅ Configurar NAT Overload (PAT) para salida a Internet y NAT estático (Port Forwarding) hacia servidores internos.
- ✅ Asegurar los puertos de acceso con Port-Security, BPDU Guard y DHCP Snooping.
- ✅ Filtrar tráfico inter-VLAN mediante ACLs extendidas en IPv4 e IPv6.
- ✅ Automatizar el despliegue de configuraciones y la extracción de inventario (`.txt` y `.csv`) con Python, Netmiko y TextFSM.

---

### 📊 Topología de la Red

La topología separa el tráfico de producción (Dual-Stack IPv4/IPv6 entre switches, routers y hosts) de la red de administración dedicada Out-of-Band (OOB).

![Topología Lógica](Topologia/topologia_logica.png)

---

### 🌐 Arquitectura de Red (Plano de Datos y Plano de Gestión)

Esta topología utiliza un **Unmanaged Switch** exclusivamente para la **red de gestión (Out-of-Band Management)**. Las interfaces de administración de los equipos de red (`R1`, `R2`, `SW1` y `SW2`) están conectadas a este switch dentro del segmento `10.10.20.0/24` (`10.10.20.171` a `.174`), permitiendo el acceso remoto seguro exclusivamente vía **SSHv2** (credenciales `cisco`/`cisco`).

El tráfico de datos de usuarios y servidores viaja de forma totalmente independiente a través de las interfaces dedicadas (segmentos `192.168.x.x`, `2001:db8:acad::/48` y el enlace WAN `10.0.12.0/30`), garantizando que las tareas de administración y automatización no interfieran con la red de producción.

---

## 📂 Estructura del Repositorio

* `Automatizacion/`: Scripts desarrollados en Python con Netmiko:
  * `read_file.py`: Automatiza la lectura y el envío de bloques de configuración desde archivos `.txt` hacia los dispositivos.
  * `device_information.py`: Extrae versión de IOS y estado de interfaces mediante TextFSM y exporta reportes estructurados.
* `Configuraciones/`: Archivos de configuración individual listos para cargar en los nodos de CML:
  * `R1.txt`, `R2.txt`
  * `Sw1.txt`, `Sw2.txt`
  * `Host.txt` (Scripts de configuración IPv4/IPv6 para clientes `udhcpc`/`udhcpc6` y servidores).
* `Notas/`: Documentación técnica detallada de direccionamiento, políticas y configuraciones (`Notas.md`).
* `Reportes/`: Archivos generados automáticamente por el script de inventario (`reporte_inventario.txt` y `reporte_inventario.csv`).
* `Topologia/`: Diagrama lógico de la infraestructura (`topologia_logica.png`).

---

## 🛠️ Requisitos en los Dispositivos de Red

* **SSHv2 Habilitado**: Telnet está deshabilitado (`transport input ssh`) por seguridad; Netmiko se conecta mediante SSH en el puerto 22.
* **Usuario Local**: Cuenta con credenciales válidas (`cisco`) y nivel de privilegio 15.
* **Contraseña de Enable**: Configurada (`enable secret cisco`) para ejecutar comandos de configuración y diagnóstico.
* **Llaves Criptográficas**: Par de llaves RSA de 2048 bits generado en cada equipo.

---

## 🚀 Cómo Ejecutar los Scripts de Automatización

```bash
# 1. Instalar las dependencias necesarias
pip install netmiko tabulate

# 2. Aprovisionar configuración en un dispositivo (ej. R1)
python read_file.py

# 3. Recolectar inventario de todos los equipos (R1, R2, SW1, SW2)
python device_information.py

# 4. Verificar los reportes generados
ls ../Reportes/
