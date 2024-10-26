# Este repositorio se basa en realizar la práctica de como integrar GitHub (en este caso GitHub Action) con Sphinx (generador de documentación para Python)
# Para ello hay varios pasos a realizar pero son sencillos:
# 1. Crear un repositorio en GitHub para alojar el proyecto y su documentación
# 2. Crear la carpeta .github/.workflows/archivo.yml (el cual hará la automatización/integración) en la rama 'main'
# 3. Hacer uso de Sphinx antes de nada para generar la documentación del proyecto en python (parte de Nerea)
# 4. Subir el proyecto con su documentación a la rama 'main'
# 5. Crear la rama 'gh-pages' donde mostraremos la documentación creada con Sphinx
# 6. Subir la carpeta 'html' generada con Sphinx a dicha rama (opcional)
# 7. Desde GitHub Pages (configuración) elegir la rama 'gh-pages' (y en caso de que hayáis creado una carpeta '/docs' también lo elegís, sino '/root')
# 8. ¡No hay que hacer nada más en dicha rama! Ahora simplemente configuramos el fichero '.yml' (archivo.yml):
#   8.1 Esta parte se explica en el mismo fichero mediante comentarios* (#)
#   8.2 Cambiar los permisos de los 'workflows' desde la configuración de GitHub Action para que los "scripts" (archivo.yml) puedan leer y escribir
# 9. Probar el fichero haciendo un 'push' a la rama elegida en este
# 10. Comprobar la rama 'gh-pages'. Si todo ha ido bien estará toda la documentación subida y se podrá ver desde GitHub Pages
