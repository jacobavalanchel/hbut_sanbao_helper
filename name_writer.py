import re
from docx import Document
import os

def replace_text_with_regex(doc, pattern, replacement):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            new_text, count = re.subn(pattern, replacement, run.text)
            run.text = new_text

def generate_new_docx(template_path, output_path, name, student_id, class_name):
    # 打开模板文件
    template_doc = Document(template_path)

    # 使用正则表达式替换模板中的字符串
    replace_text_with_regex(template_doc, r'{{姓名}}', name)
    replace_text_with_regex(template_doc, r'{{学号}}', student_id)
    replace_text_with_regex(template_doc, r'{{班级}}', class_name)

    # 保存生成的新文件
    template_dir = os.path.dirname(template_path)
    output_file = os.path.join(template_dir, output_path)
    template_doc.save(output_file)

if __name__ == "__main__":
    # 获取用户输入
    name = input("请输入名字：")
    student_id = input("请输入学号：")
    class_name = input("请输入班级：")

    # 模板文件路径
    template_path = 'path/to/your/template.docx'

    # 输出文件路径
    output_path = 'path/to/your/output.docx'

    # 生成新的docx文件
    generate_new_docx(template_path, output_path, name, student_id, class_name)

    print(f"新的文档已生成：{output_path}")
