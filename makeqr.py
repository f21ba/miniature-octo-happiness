import qrcode

img = qrcode.make('test text')
file_name='000'+'.png'
print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

img.save(file_name)
