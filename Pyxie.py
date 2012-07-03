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
	    alturaMaxima = alturaMaxima > img.size[1] if alturaMaxima else img.size[1]
	    
    Pyxie = Image.new('RGBA', (anchoTotal, alturaMaxima), (255,255,255,0))

    offsetX = offsetY = 0
    
    for img, path in imagenes:
        Pyxie.paste(img, (offsetX,0)) # Pegar cada imagen en el sprite.
	print '[{0}] background-position: {1}px 0px !important;'.format(path, offsetX,) 
        offsetX += img.size[0] # Moverse al final de la imagen.
    Pyxie.save('Pyxie.png', 'PNG')
    
if __name__ == '__main__':
    main()
