import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_and_extract_papers(course_name, num_papers):
    # 构建搜索URL
    search_query = f"site:scholar.google.com {course_name} research papers"
    search_url = f"https://www.google.com/search?q={search_query}"

    # 发送搜索请求并获取页面内容
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(search_url)
    # 提取搜索结果中的论文信息
    papers = []
    for result in soup.find_all('div', class_='BVG0Nb'):
        title = result.find('h3').get_text()
        authors = result.find('div', class_='sB6Vze').get_text()
        date_source = result.find('span', class_='f').get_text()
        abstract = result.find('div', class_='BNeawe s3v9rd AP7Wnd').get_text()

        papers.append({
            'Title': title,
            'Authors': authors,
            'Date_Source': date_source,
            'Abstract': abstract
        })

    # 创建 DataFrame
    papers_df = pd.DataFrame(papers)

    # 保存 DataFrame 到 CSV 文件
    papers_df.head(num_papers).to_csv('papers_data.csv', index=False)

if __name__ == "__main__":
    course_name = input("请输入课程名称：")
    num_papers = int(input("请输入要获取的论文数量："))

    search_and_extract_papers(course_name, num_papers)
