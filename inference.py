# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com

from rapidocr import RapidOCR

# 初始化OCR引擎
engine = RapidOCR()

# 待识别的图片路径
img_url = "Input_Img/img.png"

# 执行OCR识别，获取详细结果
result = engine(img_url, return_word_box=True, return_single_char_box=True)

# 可视化识别结果并保存为图片
result.vis("Output/img/result.jpg")

markdown_content = result.to_markdown()
# 将markdown内容写入到result.txt文件
with open("Output/txt/result.txt", "w", encoding="utf-8") as f:
    f.write(markdown_content)

