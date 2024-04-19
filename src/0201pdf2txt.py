# coding=utf-8
__author__ = 'laohuang'

from paddleocr import PaddleOCR
import pdf2image
import os

# 将PDF转换为图片
def convert_pdf_to_images(pdf_path, output_folder):
    pdf2image.convert_to_images(pdf_path, output_folder=output_folder, fmt='png')

# 从图片中提取文本
def extract_text_from_images(image_folder, output_text_file):
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 中文设置lang参数为'ch'
    with open(output_text_file, 'w', encoding='utf-8') as f:
        for image_file in os.listdir(image_folder):
            if image_file.endswith('.png'):
                image_path = os.path.join(image_folder, image_file)
                result = ocr.ocr(image_path, cls=True)
                for line in result:
                    f.write(line[1][0] + '\n')

# 主函数
def main():
    pdf_path = 'E:\\和君书单\\和君推荐阅读书目单V2013.pdf'  # 替换为你的PDF文件路径
    image_folder = 'pdf_images'  # 图片输出文件夹
    output_text_file = '和君推荐阅读书目单V2013.txt'  # 输出文本文件

    convert_pdf_to_images(pdf_path, output_folder=image_folder)
    extract_text_from_images(image_folder, output_text_file)

if __name__ == '__main__':
    main()