# YahooDictionary

使用 Python 從命令行查詢 Yahoo 字典

## 功能

- 🔍 快速查詢英文單字意思
- 📝 顯示音標、詞性和中文意思
- 📚 展示詳細的語法說明（時態、複數等）
- 🚀 簡單易用的命令行界面
- 🔄 **內建自動更新機制** - 無需 git，只需 Python

## 安裝

### 必要套件

```bash
pip install requests beautifulsoup4
```

### 使用方式

#### 基本查詢
```bash
./dict.py <單字>
```

#### 自動更新
```bash
# 檢查是否有新版本
./dict.py --check-update

# 自動下載並安裝新版本
./dict.py --update
```

#### 其他命令
```bash
./dict.py --version              # 顯示當前版本
./dict.py --help                 # 顯示幫助
```

## 使用範例

### 查詢單字
```bash
$ ./dict.py test

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

### 檢查更新
```bash
$ ./dict.py --check-update
正在檢查更新...
✓ 已是最新版本 (1.0.1)
```

### 自動更新
```bash
$ ./dict.py --check-update
正在檢查更新...
✓ 發現新版本！
  本地版本: 1.0.0
  遠端版本: 1.0.1

執行以下命令進行更新:
  /path/to/dict.py --update

$ ./dict.py --update
正在下載最新版本...
正在備份舊版本到 /path/to/dict.py.backup...
正在寫入新版本...

✅ 更新成功！
   舊版本已備份: /path/to/dict.py.backup
   新版本: 1.0.1
```

## 更新機制

- ✅ **無需 git** - 只需要 Python 和網路連接
- ✅ **自動備份** - 更新前自動備份舊版本為 `.backup`
- ✅ **版本控制** - 內建版本號，自動檢查與下載
- ✅ **CDN 快取繞過** - 使用時間戳記參數確保獲得最新版本

## 原始專案說明

本專案結合 Python 和 Yahoo 字典  
原本想使用 Google 翻譯，但 Google 翻譯 API 開始收費，所以改用 Yahoo 字典

## 技術細節

- **主要檔案**: `dict.py` - 命令行版本，內建更新機制
- **舊版本**: `yahooDictionary.py` - 原始互動式版本
- **爬蟲工具**: 
  - `requests` - HTTP 請求
  - `BeautifulSoup4` - HTML 解析
- **版本**: v1.0.1


