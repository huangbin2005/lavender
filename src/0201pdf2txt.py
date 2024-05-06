# coding=utf-8
__author__ = 'laohuang'

# from paddleocr import PaddleOCR
import pdf2image
import os
import multiprocessing

# ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 中文设置lang参数为'ch'

# 将PDF转换为图片
def convert_pdf_to_images(pdf_path, output_folder):
    try:
        pdf2image.convert_from_path(pdf_path, output_folder=output_folder, fmt='png')
    except:
        print("******")


def extract_text_from_image(returntxt,image_path,output_text_file):
    from paddleocr import PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 中文设置lang参数为'ch'
    result = ocr.ocr(image_path, cls=True)
    returntxt.put(result)
    with open(output_text_file, 'a+', encoding='utf-8') as f:
        for line in result:
            print(line)
            try:
                for l1 in line:                 
                    try:
                        print(l1[1][0]+'\n')
                        f.write(l1[1][0]+'\n')
                    except e:
                        print("=====",e)
            except:
                print("-----------")



# 从图片中提取文本
def extract_text_from_images(image_folder, output_text_file):
    # with open(output_text_file, 'w', encoding='utf-8') as f:
        for image_file in os.listdir(image_folder):
            if image_file.endswith('.png'):
                image_path = os.path.join(image_folder, image_file)
                print("image_folder======>",image_folder)
                print("image_file======>",image_file)
                print("image_path======>",image_path)
                q = multiprocessing.Queue()
                p = multiprocessing.Process(target=extract_text_from_image, args=(q, image_path,output_text_file))
                p.start()
                p.join()
                if not q.empty():
                    result = q.get()
                    print("Result:", result) 
                else:
                    print("No result found")

                # result = ocr.ocr(image_path, cls=True)
                # for line in result:
                #     print(line)
                #     try:
                #         for l1 in line:                 
                #             try:
                #                 print(l1[1][0]+'\n')
                #                 f.write(l1[1][0]+'\n')
                #             except e:
                #                 print("=====",e)
                #     except:
                #         print("-----------")
# 将文件的目录
def initpicpath(output_folder):
    # 
    try:
        os.makedirs(output_folder)
    except :
        print("=====")
    remove_files(output_folder)

# 删除目录中所有文件
def remove_files(output_folder):
    file_list = os.listdir(output_folder)
    for file in file_list:
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

# 遍历目录
def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)  # 这里可以根据需求对文件路径进行处理
            image_folder = '/mnt/d/information/pdf_images'  # 图片输出文件夹
            initpicpath(image_folder)
            convert_pdf_to_images(file_path, output_folder=image_folder)
            extract_text_from_images(image_folder, file_path+".process.txt")
# 主函数
def main():
# 需要补充相关目的处理
    # initpicpath(image_folder)
    # convert_pdf_to_images(pdf_path, output_folder=image_folder)
    # extract_text_from_images(image_folder, output_text_file)
    pdfs_path = '/mnt/d/information/和君书单'  # 替换为你的PDF文件路径
    traverse_directory(pdfs_path)

if __name__ == '__main__':
    main()


