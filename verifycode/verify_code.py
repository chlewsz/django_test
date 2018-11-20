from django.http import HttpResponse
from PIL import Image, ImageFont, ImageFilter, ImageDraw
from random import randint
from io import BytesIO


def verify_code(request):
    bg_color = (randint(30, 155), randint(30, 155), randint(30, 155))

    width = 100
    height = 25

    # 创建画布
    image = Image.new('RGB', (width, height), bg_color)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 文本内容
    text = '1234ABCD'

    font = ImageFont.truetype('PlantagenetCherokee.ttf', 19)

    code = ''
    for i in range(4):
        temp_code = text[randint(0, len(text) - 1)]
        draw.text((25 * i, 3), temp_code, (255, 255, 255), font=font)
        code.join(temp_code)

    request.session['code'] = code  # 通过session保存的code来与客户端提交的验证码进行比较即可

    buf = BytesIO()
    image.save(buf, 'png')

    # 将内存流中的内容输出
    return HttpResponse(buf.getvalue(), 'image/png')
