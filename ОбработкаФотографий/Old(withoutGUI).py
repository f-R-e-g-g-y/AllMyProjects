from PIL import Image
import os


#import watermark
watermark = Image.open('C:\\Users\\Sergey\\Desktop\\reactor.png')
watermark = watermark.resize((280, 109)) #resize image


#import all images
for filename in os.listdir('C:\\Users\\Sergey\\Desktop\\fotki'):
        if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                fullkartorig = Image.open(f'C:\\Users\\Sergey\\Desktop\\fotki\\{filename}')
                fullkart=fullkartorig
                fullkart =fullkart.convert('RGB')
                position = (fullkart.width - watermark.width-20, fullkart.height - watermark.height-20)
                fullkart.paste(watermark, position, watermark)
                fullkart.save(f'C:\\Users\\Sergey\\Desktop\\izmen\\{filename}')
                fullkartorig.close()
watermark.close()
