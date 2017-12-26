[![Build Status](https://travis-ci.org/MagicJHC10/Proyecto-IV.svg?branch=master)](https://travis-ci.org/MagicJHC10/Proyecto-IV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Repositorio para el proyecto de IV

Directorio para entrega del proyecto de la asignatura de IV.

He leido algo sobre Scraping de paginas web y he decidido realizar el proyecto de la asignatura basandome en esta tecnica y apoyandome en la creación de un bot de telegram en Python.

El bot de telegram, irá sobre Clash Royale, el juego de estrategia,multijugador en tiempo real que esta batiendo todos los records.Nos permitirá conocer estadisticas de personajes, puntos fuertes, counters etc...

A día de hoy tiene dos funcionalidades:

-Mostrar un mensaje de saludo al usuario.

-Mostrar las cartas disponibles del juego.
# Integración continua

En este proyecto vamos a utilizar un sistema de integración continua para facilitar el trabajo en equipo. En dicho sistema habra que pasar una serie de tests, para asegurar que nuestro codigo es el correcto y no arrastrar errores a lo largo de nuestro proyecto

# Despliegue en Heroku

Para nuestro proyecto , el PAAS elegido es Heroku, debido a que es gratuito y nos permite hacer todo lo que necesitamos para nuestra aplicación. Para su uso , hemos tenido que instalarlo con el siguiente comando:

```bash
$ wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

Una vez hacemos esto, nos registramos con nuestros datos personales y creamos nuestra aplicacion, pulsando en "Create New App" y poniendo el nombre de nuestra aplicación, en mi caso "clashroyaleivbot".

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/1.png)

A continuación , tenemos que configurar github y heroku para que se enlacen y cada vez que modifiquemos algo de nuestro proyecto , si pasan los tests pertinentes, se despliega automaticamente en heroku.

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/2.png)

Además, para el correcto funcionamiento, de un archivo para el json, me he creado un archivo Procfile, cuyo contenido es el [siguiente](https://github.com/MagicJHC10/ProyectoIV/blob/master/Procfile).

Despliegue https://clashroyaleivbot.herokuapp.com/

# Despliegue en Docker
 
Para realizar el despliegue nos tenemos que dar de alta en la pagina de [docker](https://hub.docker.com/) y pulsar "create automated build". Tras esto autorizamos a github y nos saldra algo asi:

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/githubenlazadoadocker.png)

Tras esto vamos a crear nuestro repositorio aportando nuestros datos, como vemos a continuación:

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/creandorepositoriodocker.png)

Para que todo funcione debemos crear un archivo Dockerfile, el cual ya esta en este mismo repositorio. De esta forma cuando hagamos push de nuestro archivo Dockerfile , la construcción del proyecto se realizará automaticamente en docker:

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/traspushdedockerfile.png)

Una vez hecho esto, se puede hacer pull del repositorio con: docker pull magicjhc10/proyecto-iv y ejecutarlo con sudo docker run -e "TOKEN=MI_TOKEN" -i -t magicjhc10/proyecto-iv y si todo va bien aparecerá algo así:

![img](https://github.com/MagicJHC10/Proyecto-IV/blob/master/capturas/rundocker.png)

Enlace del repositorio en Docker Hub: https://hub.docker.com/r/magicjhc10/proyecto-iv/

Para desplegar el contenedor en zeit simplemente nos instalamos now y ejecutamos: now -e "TOKEN=MI_TOKEN" -e , en el directorio donde tenemos el Dockerfile y automaticamente se desplegará:

URL: https://proyecto-iv-dezvoxwmjh.now.sh/

# Diseño del soporte virtual para el despliegue de una aplicación

En este apartado, donde debemos desplegar la aplicacion en un laaS, he usado Vagrant, que se encargará de desplegar una máquina virtual creada en Azure, con los pases que el profesor proporcionó al inicio de la asignatura.

Lo primero que tenemos que hacer es instalar Vagrant y Ansible

```bash
$  sudo dpkg -i vagrant_2.0.1_x86_64.deb 
```

```bash
$  vagrant plugin install vagrant-azure
```

```bash
$ sudo apt-get install ansible

```

Luego debemos configurar el archivo var.yml que se quedaría [así](https://github.com/MagicJHC10/Proyecto-IV/blob/master/var.yml).
A continuación, configurar el archivo ansible.yml , que clonará nuestro repositorio, instalará dependencias etc, [ansible.yml](https://github.com/MagicJHC10/Proyecto-IV/blob/master/ansible.yml).

Para evitar algunos errores durante el provisionamiento he configurado [ansible.cfg](https://github.com/MagicJHC10/Proyecto-IV/blob/master/ansible.cfg).

Luego debemos configurar azure para conseguir que nos proporcione un fichero (.cer), el cual será nuestro certificado y que subiremos a la cuenta de Azure para poder registrar nuestra aplicación en Azure.

Una vez creada, necesitamos cierta información que nos proporciona Azure, para poder configurar nuestro archivo Vagrantfile, como:

- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SUBSCRIPTION_ID

Quedando el fichero [así](https://github.com/MagicJHC10/Proyecto-IV/blob/master/Vagranfile).

Por último creamos la maquina virtual con:

```bash
$ vagrant up --provider=azure

```

Instalamos Fabric y configuramos el fichero fabfile.py, quedando [así](https://github.com/MagicJHC10/Proyecto-IV/blob/master/despliegue/fabfile.py).

Y ya debería funcionar, todo correctamente.


URL: http://clashbot.westus.cloudapp.azure.com/

