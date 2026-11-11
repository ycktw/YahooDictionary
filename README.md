# YahooDictionary

使用 Python 從命令行查詢 Yahoo 字典

## 功能

- 🔍 快速查詢英文單字意思
- 📝 顯示音標、詞性和中文意思
- 📚 展示詳細的語法說明（時態、複數等）
- 🚀 簡單易用的命令行界面

## 安裝

### 必要套件

```bash
pip install requests beautifulsoup4
```

### 使用方式

```bash
# 基本用法
./dict.py <單字>

# 範例
./dict.py test
./dict.py hello
./dict.py beautiful
```

## 範例輸出

```
=== 查詢: test ===

test
  KK[/tɛst/]

【n.[C]】
  測驗；考試；檢驗

【v.】
  測試；檢驗；考核

【詳細說明】
  過去式：tested 過去分詞：tested 現在分詞：testing
  名詞複數：tests
```

## 原始專案說明

本專案結合 Python 和 Yahoo 字典  
原本想使用 Google 翻譯，但 Google 翻譯 API 開始收費，所以改用 Yahoo 字典

## 技術細節

- **主要檔案**: `dict.py` - 新的命令行版本
- **舊版本**: `yahooDictionary.py` - 原始互動式版本
- **爬蟲工具**: 
  - `requests` - HTTP 請求
  - `BeautifulSoup4` - HTML 解析

