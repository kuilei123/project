import os
import random
from io import BytesIO

from PIL import Image,ImageFont,ImageDraw  # 导入画笔、字体、画布


class VerifyCode:
    def __init__(self,width=100,height=40,size=4):
        """
        :param width: 验证码宽度
        :param height: 验证码高度
        :param size: 验证码字符个数
        """
        self.width = width
        self.height = height
        self.size = size
        self.__code = ''

    @property
    def code(self):
        return self.__code
    def generate(self):
        # 1.创建画布
        # 参数：颜色模式，大小（宽，高）、颜色：red (r,g,b)
        self.im = Image.new('RGB',(self.width,self.height),self.__rand_color(200,250))

        # 2.创建画笔
        self.pen = ImageDraw.Draw(self.im)

        # 3.生成验证码字符串
        self.rand_string()

        # 4.画验证码字符串
        self.draw_code()

        # 5.画干扰点、干扰线
        self.__draw_point()
        self.__draw_line()

        # 6.返回验证码
        # self.im.save('vc.png')
        buf = BytesIO()  # 创建缓冲区
        self.im.save(buf,'png')
        binary = buf.getvalue()  # 获取图片二进制
        buf.close()  # 关闭缓冲区

        return binary
    # 生成随机字符串
    def rand_string(self):
        s1 = "234589qweyupasdfghjklzxcvbnmQWERTYUPASDFGHJKLZXCVBNM"
        for i in range(self.size):
            self.__code += random.choice(s1)

    # 画验证码
    def draw_code(self):
        # 获取字体
        font1 = ImageFont.truetype(font='App/static/index/fonts/SIMLI.TTF',size=18,encoding='utf-8')

        width = (self.width - 10)/self.size  # 每个字符的宽度
        for i in range(self.size):
            x = 14 + i*width
            y = 12
            self.pen.text((x,y), self.__code[i], font=font1,fill='black')

    def __draw_point(self):
        for i in range(200):
            x = random.randint(1,self.width-1)
            y = random.randint(1,self.height-1)
            self.pen.point((x,y),fill=self.__rand_color(20,100))
    def __draw_line(self):
        for i in range(5):
            x1 =random.randint(1,self.width-1)
            x2 =random.randint(1,self.width-1)
            y1 = random.randint(1,self.height-1)
            y2 = random.randint(1,self.height-1)
            self.pen.line([(x1,y1),(x2,y2)],fill=self.__rand_color(50,80),width=1)
    def __rand_color(self,low,high):
        return random.randint(low,high),random.randint(low,high),random.randint(low,high)


if __name__ == '__main__':
    vc = VerifyCode()
    print(vc.code)