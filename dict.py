#!/usr/bin/env python3
"""
YahooDictionary - Command line interface for Yahoo Dictionary
Version: 1.0.2
GitHub: https://raw.githubusercontent.com/ycktw/YahooDictionary/refs/heads/master/dict.py

DISCLAIMER:
This tool is for personal learning and academic research only.
Do NOT use for commercial crawling or large-scale data collection.
The author is not responsible for misuse or violations of service terms.
"""

__version__ = "1.0.2"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/ycktw/YahooDictionary/refs/heads/master/dict.py"
MIN_REQUEST_INTERVAL = 1.0  # 最少請求間隔（秒），避免伺服器壓力

import sys
import warnings
import requests
from bs4 import BeautifulSoup
import os
import shutil
from pathlib import Path
import time

# 禁止不必要的警告
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

# 記錄最後一次請求的時間
_last_request_time = 0

def get_script_path():
    """取得當前 script 的完整路徑"""
    return os.path.abspath(__file__)

def rate_limit():
    """實現請求速率限制，避免短時間內發送過多請求"""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        sleep_time = MIN_REQUEST_INTERVAL - elapsed
        time.sleep(sleep_time)
    _last_request_time = time.time()

def check_update():
    """檢查是否有新版本"""
    try:
        print("正在檢查更新...")
        rate_limit()
        
        # 加上時間戳記參數以繞過 CDN 緩存
        url = f"{GITHUB_RAW_URL}?t={int(time.time())}"
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'YahooDictionary/1.0 (Personal Learning Tool)'
        })
        response.encoding = 'utf-8'
        
        # 從遠端版本提取版本號
        for line in response.text.split('\n')[:20]:
            if '__version__ = ' in line:
                # 解析版本號 (例如: __version__ = "1.0.2")
                remote_version = line.split('"')[1]
                
                if remote_version != __version__:
                    print(f"✓ 發現新版本！")
                    print(f"  本地版本: {__version__}")
                    print(f"  遠端版本: {remote_version}")
                    print(f"\n執行以下命令進行更新:")
                    print(f"  {get_script_path()} --update")
                    return True
                else:
                    print(f"✓ 已是最新版本 ({__version__})")
                    return False
        
        print("⚠️ 無法解析遠端版本")
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 網路錯誤，無法檢查更新：{e}")
        return False
    except Exception as e:
        print(f"❌ 檢查更新失敗：{e}")
        return False

def update_script():
    """自動更新 script"""
    try:
        script_path = get_script_path()
        
        print("正在下載最新版本...")
        rate_limit()
        
        # 加上時間戳記參數以繞過 CDN 緩存
        url = f"{GITHUB_RAW_URL}?t={int(time.time())}"
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'YahooDictionary/1.0 (Personal Learning Tool)'
        })
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"❌ 下載失敗 (HTTP {response.status_code})")
            return False
        
        new_content = response.text
        
        # 驗證新內容是否為有效的 Python 檔案
        if '#!/usr/bin/env python3' not in new_content:
            print("❌ 下載的內容不是有效的 Python script")
            return False
        
        # 備份舊版本
        backup_path = f"{script_path}.backup"
        print(f"正在備份舊版本到 {backup_path}...")
        shutil.copy2(script_path, backup_path)
        
        # 寫入新版本
        print("正在寫入新版本...")
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # 保持可執行權限
        os.chmod(script_path, 0o755)
        
        # 提取新版本號
        new_version = None
        for line in new_content.split('\n')[:20]:
            if '__version__ = ' in line:
                new_version = line.split('"')[1]
                break
        
        if new_version:
            print(f"\n✅ 更新成功！")
            print(f"   舊版本已備份: {backup_path}")
            print(f"   新版本: {new_version}")
        else:
            print(f"\n✅ 更新成功！")
        
        return True
        
    except Exception as e:
        print(f"❌ 更新失敗：{e}")
        print(f"   請手動恢復：cp {backup_path} {script_path}")
        return False

def lookup_word(word):
    """
    使用 Yahoo 字典查詢單字意思
    """
    try:
        # Yahoo 字典的網址
        url = f"https://tw.dictionary.search.yahoo.com/search?p={word}"
        
        # 設定 User-Agent 以標識此工具
        headers = {
            'User-Agent': 'YahooDictionary/1.0 (Personal Learning Tool)'
        }
        
        rate_limit()
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

def show_help():
    """顯示使用說明"""
    print(f"""YahooDictionary v{__version__}

使用方法:
  ./dict.py <單字>              查詢單字
  ./dict.py --check-update      檢查是否有新版本
  ./dict.py --update            自動更新 script
  ./dict.py --version           顯示版本
  ./dict.py --help              顯示此幫助

範例:
  ./dict.py test
  ./dict.py hello
  ./dict.py --check-update

⚠️  免責聲明：本工具僅供個人學習與學術研究使用。
   請勿用於大規模商業爬蟲。
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == '--help':
        show_help()
    elif command == '--version':
        print(f"YahooDictionary v{__version__}")
    elif command == '--check-update':
        check_update()
    elif command == '--update':
        if update_script():
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        # 視為要查詢的單字
        if not lookup_word(command):
            sys.exit(1)

if __name__ == "__main__":
    main()
