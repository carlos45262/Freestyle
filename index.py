# -*- coding: utf-8 -*-
from flask import Flask, render_template,send_from_directory

import random
from PIL import Image
import os

    
def imagenes():
    
    num=0
    
    global imagen

    # Ruta a la carpeta que contiene las imágenes
    carpeta_imagenes ="static\img2017"
    
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(carpeta_imagenes)
    
    numero_limite = random.randint(1, 100)
    
    for archivo in archivos:
        
        num+=1
        
        if num==numero_limite:
            
            break
        
    ruta_imagen= os.path.join(carpeta_imagenes, archivo)
            
    #imagen = Image.open(ruta_imagen)
            
   # imagen = imagen.resize((250,250))
    
    return ruta_imagen
    
def ran(lista):
    
    aleatorio=random.randint(0,len(lista)-1)
    
    return aleatorio
    
    
    

def palabras(archivo):
        
        num=0
        numero_lim = random.randint(1, 105000)
        archivo = open('archivo.txt', 'r', encoding='utf-8', errors='ignore')
        
        for linea in archivo:
            
            num+=1
            if num==numero_lim:
                
                #print(linea)
                return linea
                archivo.close()
                
                break
            
def preguntas(archivo):
        
        num=0
        numero_lim = random.randint(1, 50)
        archivo = open('archivo.txt', 'r', encoding='utf-8', errors='ignore')
        
        for linea in archivo:
            
            num+=1
            if num==numero_lim:
                
                #print(linea)
                return linea
                archivo.close()
                
                break
            
def term():
        
        
        terminacion=['aa','ab','ba', 'ac','ca','ad','da','ae','ea','af','fa','ga','ag','ha','ah','ia','ai','ja','aj','ak','ka','la','al','ma','am','na','an','oa','ao','ap','pa','ar','ra','as','sa','at','at','ua','au','va','av', 'wa','aw','ax','xa','az','za','ay','ya',
                 'eb','be', 'ec','ce','ed','de','ee','ef','fe','ge','eg','he','eh','ie','ei','je','ej','ek','ke','le','el','me','em','ne','en','oe','eo','ep','pe','er','re','es','se','et','et','ue','eu','ve','ev', 'we','ew','ex','xe','ez','ze','ey','ye',
                 'ib','bi', 'ic','ci','id','di','if','fi','gi','ig','hi','ih','ii','ji','ij','ik','ki','li','il','mi','im','ni','in','oi','io','ip','pi','ir','ri','is','si','it','ti','ui','iu','vi','iv', 'wi','iw','ix','xi','iz','zi','iy','yi',
                 'ob','bo', 'oc','co','od','do','of','fo','go','og','ho','oh','jo','oj','ok','ko','lo','ol','mo','om','no','on','oo','op','po','or','ro','os','so','ot','to','uo','ou','vo','ov', 'wo','ow','ox','xo','oz','zo','oy','yo',
                 'ub','bu', 'uc','cu','ud','du','uf','fu','gu','ug','hu','uh','ju','uj','uk','ku','lu','ul','mu','um','nu','un','up','pu','ur','ru','us','su','ut','tu','uu','vu','uv', 'wu','uw','ux','xu','uz','zu','uy','yu']
        
        aleatorio=random.randint(0,len(terminacion)-1)

        
        text= terminacion[aleatorio]
        
        return text
                
            
            


app=Flask(__name__)

"""

@app.route('/')
def principal():
    
    return "Bienvenido al sitio web"

@app.route('/palabras')

"""

@app.route('/')
def principal():
    
    return render_template('index.html')

@app.route('/historias')
def historias():
    
    palabra=palabras('palabras.txt')
    
    return render_template('historias.html',word=palabra,word1=palabras('palabras.txt'),word2=palabras('palabras.txt'),word3=palabras('palabras.txt') )

@app.route('/objetos')
def objetos():

    
    return render_template('objetos.html',img=imagenes(),img1=imagenes(),img2=imagenes(),img3=imagenes())

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory('static/audios', filename)

@app.route('/batalla/audio/<filename>')
def serve_audio1(filename):
    return send_from_directory('static/audios/mecha', filename)

@app.route('/terminaciones')
def terminaciones():
    
    return render_template('terminaciones.html', text=term(),text1=term(),text2=term(),text3=term(),text4=term(),text5=term())
    
@app.route('/batalla')
def Batalla():
        
    return render_template('batalla.html')

    
@app.route('/batalla/chuty')
def chuty():
    
     audioschuty=['batallachuty1.mp3','batallachuty2.mp3','batallachuty3.mp3','batallachuty4.mp3',
                  'batallachuty5.mp3','batallachuty6.mp3','batallachuty7.mp3','batallachuty8.mp3','batallachuty9.mp3'
                  'batallachuty10.mp3']
     
     #aleatorio=random.randint(0,len(audioschuty)-1)
        
     return render_template('chuty.html',audio1=audioschuty[ran(audioschuty)],audio2=audioschuty[ran(audioschuty)],audio3=audioschuty[ran(audioschuty)],audio4=audioschuty[ran(audioschuty)],audio5=audioschuty[ran(audioschuty)],audio6=audioschuty[ran(audioschuty)])
    
@app.route('/batalla/mecha')
def mecha():
    
     audiosmecha=['mecha1.mp3','mecha2.mp3','mecha3.mp3','mecha4.mp3',
                  'mecha5.mp3','mecha6.mp3','mecha7.mp3','mecha8.mp3',
                  ]
     #aleatorio=random.randint(0,len(audiosmecha)-1)
        
     return render_template('mecha.html',audio1=audiosmecha[ran(audiosmecha)],audio2=audiosmecha[ran(audiosmecha)],audio3=audiosmecha[ran(audiosmecha)],audio4=audiosmecha[ran(audiosmecha)],audio5=audiosmecha[ran(audiosmecha)],audio6=audiosmecha[ran(audiosmecha)])
    
@app.route('/batalla/sweetpain')
def sweetpain():
        
    return render_template('sweetpain.html')

@app.route('/incremental')
def incremental():
    
    palabra=palabras('palabras.txt')
            
    return render_template('incremental.html',word=palabra,word1=palabras('palabras.txt'),word2=palabras('palabras.txt'),word3=palabras('palabras.txt'),word4=palabras('palabras.txt'),word5=palabras('palabras.txt'),word6=palabras('palabras.txt'),word7=palabras('palabras.txt'),word8=palabras('palabras.txt'))

@app.route('/kickback')
def kickback():
    
    palabra=preguntas('kickback.txt')
    return render_template('kickback.html',pregunta=palabra,p1=preguntas('kickback.txt'),p2=preguntas('kickback.txt'),p3=preguntas('kickback.txt'),p4=preguntas('kickback.txt'),p5=preguntas('kickback.txt'),p6=preguntas('kickback.txt'),p7=preguntas('kickback.txt'),p8=preguntas('kickback.txt'))


if __name__=='__main__':
    
    app.run(debug=True)
    

    

    

    


