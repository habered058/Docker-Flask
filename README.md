# Docker con Flask, HTML y Bootstrap

## Instalación
Primero se debe abrir Docker Desktop

En la terminal correr el comando (Se ha creado con el nombre automatica, pero se puede agregar cualquier nombre)
```sh
docker build -t automatica .  
```

Luego se ejecuta el comando
```sh
docker run -dp 7000:6000 automatica 
```
Para verificar que el servidor se esté ejecutando correctamente 
se puede verifcar en:
```sh
http://localhost:7000/
```
