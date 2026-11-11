# YahooDictionary

使用 Python 從命令行查詢 Yahoo 字典

## ⚠️ 重要免責聲明

**本工具僅供個人學習與學術研究使用。**

- ✓ 允許：個人學習、教育用途、學術研究
- ✗ **禁止**：大規模商業爬蟲、數據販售、競爭對手情報蒐集
- ✗ **禁止**：違反 Yahoo 字典的服務條款

使用本工具即表示您已理解並同意上述限制。**作者不對使用者的任何違法行為、服務條款違反或伺服器損害承擔責任。**

詳見 [LICENSE](LICENSE) 文件的免責聲明部分。

## 功能

- 🔍 快速查詢英文單字意思
- 📝 顯示音標、詞性和中文意思
- 📚 展示詳細的語法說明（時態、複數等）
- 🚀 簡單易用的命令行界面
- 🔄 內建自動更新機制 - 無需 git，只需 Python
- ⏱️ **內建請求間隔控制** - 自動避免過度爬蟲
- 🔐 **標準化 User-Agent** - 明確標識工具身份

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
✓ 已是最新版本 (1.0.2)
```

### 自動更新
```bash
$ ./dict.py --check-update
正在檢查更新...
✓ 發現新版本！
  本地版本: 1.0.0
  遠端版本: 1.0.2

執行以下命令進行更新:
  /path/to/dict.py --update

$ ./dict.py --update
正在下載最新版本...
正在備份舊版本到 /path/to/dict.py.backup...
正在寫入新版本...

✅ 更新成功！
   舊版本已備份: /path/to/dict.py.backup
   新版本: 1.0.2
```

## 技術特性

### 1. 請求速率限制 (Rate Limiting)
- 每次查詢至少間隔 **1 秒**
- 自動避免短時間內發送過多請求
- 減少對 Yahoo 伺服器的壓力

### 2. User-Agent 標識
```
User-Agent: YahooDictionary/1.0 (Personal Learning Tool)
```
- 明確標識此工具的身份
- 尊重網站的爬蟲管理機制

### 3. 更新機制
- ✅ 無需 git - 只需要 Python 和網路連接
- ✅ 自動備份 - 更新前自動備份舊版本為 `.backup`
- ✅ 版本控制 - 內建版本號，自動檢查與下載
- ✅ CDN 快取繞過 - 使用時間戳記參數確保獲得最新版本

### 4. 無內建字典資料庫
- 程式碼只包含解析邏輯（Parser）
- 所有字典內容來自 Yahoo 字典線上查詢
- **不附帶任何預先爬蟲的字典文件**
- 減少 Repository 大小

## 開源授權

本專案採用 **MIT License** 授權。詳見 [LICENSE](LICENSE) 文件。

### MIT License 摘要
- ✓ 可以自由使用、修改、分發
- ✗ 作者不提供任何保證
- ✗ 作者不對使用結果負責

## 原始專案說明

本專案結合 Python 和 Yahoo 字典  
原本想使用 Google 翻譯，但 Google 翻譯 API 開始收費，所以改用 Yahoo 字典

## 技術細節

- **主要檔案**: `dict.py` - 命令行版本，內建更新機制
- **舊版本**: `yahooDictionary.py` - 原始互動式版本
- **爬蟲工具**: 
  - `requests` - HTTP 請求
  - `BeautifulSoup4` - HTML 解析
- **版本**: v1.0.2
- **授權**: MIT License

## 常見問題

### Q: 我可以用這個工具進行商業爬蟲嗎？
A: **不可以。** 本工具明確禁止用於商業目的。

### Q: 為什麼查詢之間有延遲？
A: 這是故意設計的請求速率限制，避免對 Yahoo 伺服器造成壓力。

### Q: 為什麼不內建字典資料庫？
A: 遵守著作權和服務條款，字典內容應該由官方提供，而非本地打包。

### Q: 如果 Yahoo 字典改版怎麼辦？
A: 歡迎提交 Issue 或 PR 幫助更新解析邏輯。

## 貢獻

歡迎提交 Issue 和 Pull Request！但請注意：
- 所有改動必須保持學習目的的初衷
- 不接受商業爬蟲相關的改動
- 必須遵守 MIT License

## 聯絡

如有問題或建議，歡迎開立 Issue。

---

**再次提醒：本工具僅供個人學習使用。請負責任地使用它。** ⚖️



