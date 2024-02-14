import json
import os
from fontTools.ttLib import TTFont
from fontTools.pens.freetypePen import FreeTypePen
import matplotlib.pyplot as plt
import ddddocr


font = TTFont("/usr1/demo/dc027189e0ba4cd.otf")
# font.saveXML("/usr1/demo/dc027189e0ba4cd2.xml")
cmap = font.getBestCmap()

index = 1
for n, v in cmap.items():
    d = v
    glyph = font.getGlyphSet()[d]  # 通过字形名称选择某一字形对象
    pen = FreeTypePen(None)  # 实例化Pen子类
    glyph.draw(pen)  # “画”出字形轮廓
    # pen.show()    # 显示
    b = pen.array()
    print(index, '/', len(cmap), '~~~', glyph)
    plt.figure()
    plt.imshow(b)
    plt.axis('off')  # 禁用坐标轴
    os.makedirs('imgs', exist_ok=True)
    plt.savefig('./imgs/{0}.jpg'.format(d))
    # plt.show()    # 显示
    plt.clf()
    plt.cla()
    plt.close()
    index += 1

ocr = ddddocr.DdddOcr(beta=False, show_ad=False)  # 识别
word_map = {}
for parent, dirnames, filenames in os.walk('imgs'):  # 遍历每一张图片
    for filename in filenames:
        k = filename.split('.')[0]
        currentPath = os.path.join(parent, filename)
        with open(currentPath, 'rb') as f:
            image = f.read()
        res = ocr.classification(image)
        if len(res) == 0:
            res = '未找到'
        if len(res) > 1:
            res = res[0]
        print(k, 'res:', res)
        # os.makedirs('imgs_copy_word', exist_ok=True)
        # d = f'{k}__{res}.jpg'
        # img = Image.open(currentPath)
        # img.save('imgs_copy_word/%s' % d)
        word_map[k] = res
if word_map:
    with open('woff.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(word_map, ensure_ascii=False))