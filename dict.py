#!/usr/bin/env python3
import sys
import warnings
import requests
from bs4 import BeautifulSoup

# 禁止不必要的警告
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

def lookup_word(word):
    """
    使用 Yahoo 字典查詢單字意思
    """
    try:
        # Yahoo 字典的網址
        url = f"https://tw.dictionary.search.yahoo.com/search?p={word}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 尋找字典單詞卡
        word_card = soup.find('div', class_='sys_dict_word_card')
        
        if not word_card:
            print(f"查詢錯誤：找不到 '{word}' 的結果")
            return False
        
        # 印出英文單字
        title = word_card.find('span', class_='fz-24')
        if title:
            print(f"\n{title.get_text(strip=True)}")
        
        # 尋找音標
        pronunciation_list = word_card.find('ul')
        if pronunciation_list:
            for li in pronunciation_list.find_all('li'):
                pron_text = li.get_text(strip=True)
                if pron_text and ('/' in pron_text or '[' in pron_text or 'K' in pron_text):
                    print(f"  {pron_text}")
                    break
        
        # 尋找詞性和意思 - 尋找所有 compList，第二個應該是詞性區塊
        comp_lists = word_card.find_all('div', class_='compList')
        
        if len(comp_lists) >= 2:
            comp_list = comp_lists[1]  # 取第二個 compList
            items = comp_list.find_all('li')
            
            for item in items:
                # 取得詞性
                pos_elem = item.find('div', class_='pos_button')
                if pos_elem:
                    pos_text = pos_elem.get_text(strip=True)
                    print(f"\n【{pos_text}】")
                
                # 取得中文意思
                explanation = item.find('div', class_='dictionaryExplanation')
                if explanation:
                    exp_text = explanation.get_text(strip=True)
                    print(f"  {exp_text}")
        
        # 尋找詳細例句和說明區塊（在下面的 compArticleList）
        article_list = word_card.find('ul', class_='compArticleList')
        if article_list:
            items = article_list.find_all('li')
            if items:
                print(f"\n【詳細說明】")
                for item in items:
                    text = item.get_text(strip=True)
                    if text:
                        print(f"  {text[:120]}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"網路錯誤：{e}")
        return False
    except Exception as e:
        print(f"查詢錯誤：{e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("使用方法: ./dict.py <單字>")
        print("範例: ./dict.py test")
        sys.exit(1)
    
    word = sys.argv[1]
    
    if not lookup_word(word):
        sys.exit(1)

if __name__ == "__main__":
    main()
