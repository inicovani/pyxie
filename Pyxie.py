#!/usr/bin/env python

import glob
import Image

def main(args=None):
    listaImgCarpeta = glob.glob('input/*.png') # TODO: Cualquier formato de imagen...
    imagenes = []
    anchoTotal = 0
    alturaMaxima = 0
    
    # Se abre cada imagen de la carpeta (que haya pasado el filtro) y se copia
    # a una lista.
    for imgPath in listaImgCarpeta:
        img = Image.open(imgPath)
        imagenes.append([img.copy(), imgPath])

        # Se usara para determinar el ancho total del sprite final
        anchoTotal += img.size[0]

        # Las imagenes se iran agrupando horizontalmente. Se determina la altura
        # maxima para usar en el sprite final.
        # TODO: Aprovechar al maximo el espacio.
        if img.size[1] > alturaMaxima:
            alturaMaxima = img.size[1]
	    
    Pyxie = Image.new('RGBA', (anchoTotal, alturaMaxima), (255,255,255,0))

    offsetX = offsetY = 0
    agregados = 0 # cantidad de archivos agregados al sprite final

    with open('Pyxie.css', 'w') as css:
        css.write('.Pyxie { background: #fff url(\'Pyxie.png\') no-repeat;}\n\n')
        for img, path in imagenes:
            ancho,alto = img.size
            Pyxie.paste(img, (offsetX,0)) # Pegar cada imagen en el sprite.
            print '[{0} agregado] w:{1} h:{2} x:{3} y:{4};'.format(path, img.size[0], img.size[1], offsetX, offsetY)
            css.write('.Pyxie_{0} {{ background-position: -{1}px 0px !important; padding-left: {2}px; }}\n'.format(path[6:-4], offsetX,ancho))
            offsetX += img.size[0] # Moverse al final de la imagen.
            agregados += 1
        Pyxie.save('Pyxie.png', 'PNG')
        print '{0} imagenes agregadas a Pyxie.png ({1}x{2}px)'.format(agregados, anchoTotal, alturaMaxima)
    
if __name__ == '__main__':
    main()
