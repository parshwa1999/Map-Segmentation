import codecs
import PIL.Image
import numpy as np
import io

def encodeImageForJson(image):
    img_pil = PIL.Image.fromarray(image, mode='RGB')
    f = io.BytesIO()
    img_pil.save(f, format='PNG')
    data = f.getvalue()
    encData = codecs.encode(data, 'base64').decode()
    encData = encData.replace('\n', '')
    return encData


print(encodeImageForJson(np.array(PIL.Image.open('Img51.png')) ))