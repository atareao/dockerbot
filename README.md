
# Dockerbot

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  

Un Bot en **Python** para interactuar con Docker.

## Indice

- [Dockerbot](#dockerbot)
  - [Indice](#indice)
  - [Pasos iniciales](#pasos-iniciales)
    - [Añadimos dependencias](#añadimos-dependencias)
  - [Capturas de pantalla](#capturas-de-pantalla)
  - [Módulos de Python](#módulos-de-python)
  - [Funcionando localmente](#funcionando-localmente)
  - [Variables de entorno](#variables-de-entorno)
  - [Mas información](#mas-información)
  - [Feedback](#feedback)
  - [Licencia](#licencia)

## Pasos iniciales

- Crea el archivo `.gitignore`
- Crea el archivo `LICENSE`
- Crea el archivo `README.md`
- Ejecutar `poetry init` desde la terminal incorporada de *Visual Studio Code*. Esto te guiará por la creación del archivo `pyproject.toml`. No añadas ninguna dependencia, esto lo haremos directamente desde la extensión que hemos configurado para ello.
- Crea los directorios `src` y `test`, donde estará tu código y los tests respectivamente.
- Inicializa el repositorio git con un `git init`.
- Crea el archivo `.env` donde guardarás las variables de entorno y añade este archivo a `.gitignore`, para que no se haga control de versiones de este archivo.

### Añadimos dependencias

Uno de las extensiones que hemos instalado en *Visual Studio Code* se encarga de añadir dependencias a *Poetry*. Desde la paleta de comandos añade la primera de las dependencias que vamos a utilizar, que no es, ni mas ni menos, que `aiohttp`, que es un módulo que nos permite realizar llamadas de forma asíncrona.

Inicialmente había indicado `httpx` sin embargo, dado que el módulo de Python para Docker también utiliza `aiohttp`, voy a decantarme por este. Pero, elige tu el que consideres


## Funcionando localmente

## Variables de entorno

Para hacer funcionar este proyecto encastarás añadir al menos la siguiente variable de entorno a tu archivo `.env`,

* `TELEGRAM_BOT_TOKEN`

## Mas información

* [Pyldoras Pythonicas](https://atareao.es/pyldoras)
* [Historias de un Pythonico](https://atareao.es/python)

## Feedback

Sabes que amo el feedback, si tienes cualquier idea o sugerencia, por favor, hazmela saber directamente en [atareao.es](https://atareao.es)

## Licencia  

[MIT](https://choosealicense.com/licenses/mit/)
