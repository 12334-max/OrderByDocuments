import os
import shutil
#diccionario de extencioes
extension = {
    "Fotos": ['.jpg', '.png', '.jpeg'],
    "Videos": ['.mp4', '.avi', '.wav'],
    "Musica": ['.mp3'],
    "Documentos": ['.pdf', '.docx', '.dotx', '.pptx']
}

#ruta de la carpeta descarga
ruta_descarga = "D:\Spartha"

#rutas de desitino
rutas = {
    "Fotos": "D:\Pictures",
    "Videos": "D:\Videos",
    "Musica": "D:\Music",
    "Documentos": "D:\Documents"

}

#funcion ordenar
def order_by_ext(file, ext):
    for i in extension.keys():
        if ext in extension[i]:
            for ruta in rutas.keys():
                if ruta == i:
                    r = rutas[ruta]
                    try:
                        shutil.move(ruta_descarga+"/"+file, r)
                    except:
                        print("Ocurrio un error al mover el archivo")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for archivo in os.listdir(ruta_descarga):
        ext = os.path.splitext(archivo)
        order_by_ext(archivo, ext[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
