# mkpa-tools：MKPA 設計標準

呢個 repo **只放設計標準**，唔放任何工具代碼，亦唔會部署。每個工具有自己嘅 GitHub repo，各自部署去 Netlify。

**改工具要去該工具自己嘅 repo 改，唔好喺呢度加工具代碼。**（2026 年 10 月曾經將所有工具放喺呢度，已經搬走；舊版本仍然喺 git 歷史入面。）

## 工具 repo 一覽

| Repo | 工具 | 類型 |
|---|---|---|
| `mickoo129/bankrate` | 定存息口通：香港銀行定期息口比較 | 純前端（`public/`）＋ 爬蟲，GitHub Actions 每 2 小時更新 |
| `mickoo129/ci-promotion` | 危疾定義更新計劃（顧問自用，noindex） | 純前端 |
| `mickoo129/claimsreport` | 七年理賠數據解讀 2019–2025 | 純前端 |
| `mickoo129/hk-medical-insurance-compare` | 醫保對照：自願醫保、危疾及癌症保障比較 | 純前端 |
| `mickoo129/mpf-compass` | 積金羅盤：強積金成分基金分析 | React + Vite（要 build），GitHub Actions 更新 MPFA 資料 |
| `mickoo129/public-rental-housing` | 公屋全程指南 | 純前端 |
| `mickoo129/vhis-rate` | 自願醫保保費規劃 | 純前端 |

每個工具 repo 都有自己嘅 CLAUDE.md，指返嚟呢份標準。

## 所有工具都要遵守

1. 介面文字用繁體中文（香港用語），`<html lang="zh-HK">`（或 `zh-Hant-HK`）。
2. 手機優先：手機闊度（約 375px）正常顯示，唔可以出現橫向捲動。
3. 純前端工具保持純前端，唔好加 build 步驟或 npm 依賴。
4. 唔好放任何密碼、API key 落 repo。
5. 改嘢之前一定用 repo 最新版本做底，唔好用對話記憶入面嘅舊代碼覆蓋。
6. 某個工具刻意同標準唔同，要寫喺該工具 CLAUDE.md 嘅「呢個工具嘅特別嘢」。同步標準時先讀嗰度，寫明係例外嘅唔好改返做標準；冇寫明嘅就當係未跟標準。

## 設計規格（MKPA 統一標準）

所有工具必須跟以下標準。每個工具可以保留自己嘅 CSS 變數名，但數值要對應呢套。

**標準檔案喺 `_standard/`**（唔會部署，只係範本）：
- `_standard/mkpa.css`：配色變數、電子名片、列印按鈕、列印頁頭嘅樣式。複製入工具嘅 CSS。
- `_standard/snippets.html`：icon 連結、字體連結、列印頁頭、列印按鈕、電子名片（連二維碼）、版權行、年份／列印日期 script。
- `_standard/make-icons.py` 同 `_standard/icons/`：產生工具 icon（見下面「Icon」）。
- 改標準時先改呢度，再逐個工具 repo 同步。React 工具（mpf-compass）用佢 repo 入面嘅 `src/components/layout/mk-standard.tsx`。

### 配色

| 用途 | 變數（建議名） | 色碼 |
|---|---|---|
| 主色：主要按鈕、重點、色帶、圖表主系列 | `--mk-brand` | `#00A758`（宏利綠） |
| 綠色文字、連結、按鈕 hover | `--mk-brand-ink` | `#00753E` |
| 淺綠底（提示框、選中狀態） | `--mk-brand-soft` | `#E6F6EE` |
| 深色：頁頭底色、大標題 | `--mk-deep` | `#0E5E57`（深青綠） |
| 內文文字 | `--mk-ink` | `#1D2B2A` |
| 次要文字 | `--mk-muted` | `#5B6B6A` |
| 頁面背景 | `--mk-bg` | `#F6F9F8` |
| 卡片／面板 | `--mk-surface` | `#FFFFFF` |
| 分隔線、邊框 | `--mk-line` | `#E3E9E7` |
| 警示（琥珀） | `--mk-warn` / `--mk-warn-soft` | `#8A5B00` / `#FFF5DC` |
| 錯誤、下跌（紅） | `--mk-danger` / `--mk-danger-soft` | `#C62828` / `#FDECEC` |

- 白底上嘅綠色**文字**一律用 `#00753E`（`#00A758` 喺白底對比度唔夠）。
- 主要按鈕：`#00A758` 底、白色粗體字；hover 轉 `#00753E`。
- 圖表需要多個分類顏色時可以加其他顏色，但主系列用宏利綠。
- **唔做深色模式**，唔好加 `prefers-color-scheme: dark` 或主題切換掣。
- 例外：mpf-compass 整體用深青綠 `#0E5E57` 做頁面底色（白色卡片放上面），列印時自動轉白底黑字。

### 版面闊度

- 內容最闊 **1320px**，兩邊留白 `clamp(16px, 3vw, 32px)`（手機約 16px、平板約 24px、桌面 32px）。
- 用 `_standard/mkpa.css` 嘅 `--mk-max`、`--mk-gutter` 或 `.mk-wrap`；工具自己嘅外框 class 都要用同樣數值。
- 例外：一大段文字可以自己限闊（約 720px）方便閱讀；簡報式頁面（例如 ci-promotion 嘅講解簡報）按簡報比例縮放。
- 手機（375px）、平板（768–1024px）都唔可以橫向捲動。

### Icon（每個工具都要有）

- 每個工具有一個簡單單色 icon：**宏利綠 `#00A758` 圓角方塊 + 白色線條圖形**（32×32 網格、線粗 2.5、圓角端）。
- 用 `_standard/make-icons.py` 產生全套檔案，唔好自己畫唔同風格：
  ```
  python3 _standard/make-icons.py <圖形> <工具網頁 folder> --name "工具全名" --short "短名"
  ```
  現成圖形喺 `_standard/icons/`；新工具可以照格式加一個新圖形。
- 產生嘅檔案同用途：
  - `favicon.svg`、`favicon.ico`：瀏覽器分頁
  - `apple-touch-icon.png`：iPhone／iPad「加至主畫面」
  - `icon-192.png`、`icon-512.png`、`site.webmanifest`：Android／Chrome「加至主畫面」或「安裝」
- `<head>` 要有 `_standard/snippets.html` 第 1 段嘅 icon 連結；標題旁邊用 `<img class="mk-logo" src="favicon.svg">` 顯示同一個 icon。
- 標題旁 icon 大細跟頁頭標題高度調整，大約 **24–40px**（`.mk-logo` 預設 32px）：頁頭窄就細啲，標題加副標題兩行字就大啲。唔使硬性統一做 32px。

| 工具 | 圖形 |
|---|---|
| bankrate | `trend-up` |
| ci-promotion | `pulse` |
| claimsreport | `shield-check` |
| hk-medical-insurance-compare | `shield-plus` |
| mpf-compass | `compass` |
| public-rental-housing | `house` |
| vhis-rate | `medical-cross` |

### 字體

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@500;600;700&family=Noto+Sans+HK:wght@400;500;700;900&display=swap" rel="stylesheet">
```

- 內文、標題：`"Noto Sans HK", "PingFang HK", "Microsoft JhengHei", system-ui, sans-serif`
- 大數字、金額、百分比：`"Barlow", "Noto Sans HK", system-ui, sans-serif`
- 唔用襯線字體（Serif）。

### 頁尾（每個工具一樣）

由上至下：工具專屬免責聲明 → 資料來源（如有）→ 電子名片 → 版權。

```html
<footer class="mk-footer">
  <!-- 工具專屬免責聲明、資料來源放呢度 -->
  <p class="mk-contact">想進一步了解或有疑問？
    <a href="https://api.portfoplus.com/api/v1/adviser/5e41564ab3b1bc00153394db?m=link&amp;r=adviser" target="_blank" rel="noopener">查看電子名片 →</a>
    <span>可直接 WhatsApp、加 IG 或儲存聯絡資料</span>
  </p>
  <p class="mk-copy">© <span class="mk-year">2026</span> Michael Koo Protection Alliance (MKPA). 版權所有。</p>
</footer>
<script>document.querySelectorAll('.mk-year').forEach(e=>e.textContent=new Date().getFullYear());</script>
```

- **聯絡資料只用電子名片連結**，唔好喺工具顯示電話、WhatsApp 號碼、電郵、牌照號碼，亦唔好加顧問資料輸入欄。
- 「分享去 WhatsApp」呢類分享功能可以保留，佢唔係聯絡資料。

### 列印／存 PDF（每個工具都要有）

- 按鈕文字統一：**「列印 / 存 PDF」**，用 `window.print()`。
- 紙張 A4；直向或橫向按內容決定（闊表格用橫向）。
- 列印時：隱藏導覽、按鈕、輸入提示等互動元素；保留顏色（`print-color-adjust: exact`）；卡片、表格行唔好斷頁（`break-inside: avoid`）。
- 列印版頂部顯示工具名稱同列印日期，底部顯示電子名片連結同版權行（PDF 入面條連結撳得到）。

## 新增工具

1. 喺 GitHub 開一個新 repo（英文細楷加連字號，例如 `price-calculator`）。
2. 寫 `index.html`，跟上面設計規格（版面闊度、icon、配色、字體、頁尾、列印），由 `_standard/` 複製樣式同片段。
3. 揀或者畫一個圖形，用 `_standard/make-icons.py` 產生 icon，並喺上面 icon 表加一行。
4. 喺新 repo 加一份 CLAUDE.md，格式參考其他工具 repo（指返呢份標準 ＋ 該工具嘅特別嘢）。
5. 喺上面「工具 repo 一覽」加一行。
6. 喺 Netlify 新增 site，連去新 repo。
