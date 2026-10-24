# mkpa-tools

MKPA 所有放喺 Netlify 嘅工具／網站，集中喺呢一個 repo。每個子 folder 係一個獨立工具，各自部署做一個 Netlify site（Base directory = 該 folder 名）。

## 工具一覽

| Folder | 工具 | 類型 | Netlify 設定 |
|---|---|---|---|
| `bankrate/` | 定存息口通：香港銀行定期息口比較 | 純前端 + 爬蟲（自動更新） | Base `bankrate`，其餘由 `netlify.toml` 處理（publish `public`） |
| `ci-promotion/` | 危疾定義更新計劃（顧問自用，noindex） | 純前端 | Base `ci-promotion`，其餘由 `netlify.toml` 處理 |
| `claimsreport/` | 七年理賠數據解讀 2019–2025 | 純前端 | Base `claimsreport`，Build command、Publish 留空 |
| `hk-medical-insurance-compare/` | 醫保對照：自願醫保、危疾及癌症保障比較 | 純前端（單一 `index.html`） | Base `hk-medical-insurance-compare`，其餘留空 |
| `mpf-compass/` | 積金羅盤：強積金成分基金分析 | React + Vite（要 build，有 SSR functions） | Base `mpf-compass`，其餘由 `netlify.toml` 處理 |
| `public-rental-housing/` | 公屋全程指南 | 純前端（單一 `index.html`） | Base `public-rental-housing`，其餘留空 |
| `vhis-rate/` | 自願醫保保費規劃 | 純前端 | Base `vhis-rate`，其餘留空 |

## 自動更新（GitHub Actions）

Workflow 一定要放喺 repo 根目錄 `.github/workflows/`，用 `working-directory` 指去對應 folder：

- `bankrate-scrape.yml`：每 2 小時抓各銀行息口同匯價，commit 落 `bankrate/public/data/` 同 `bankrate/debug/`。Commit message 帶 `[skip netlify]`，因為網站直接由 GitHub raw 讀數據，唔使重新部署。
- `mpf-compass-refresh.yml`：星期一至六更新 MPFA 基金資料，commit 落 `mpf-compass/src/`，會觸發 `mpf-compass` 重新部署。

呢啲由 bot commit 嘅數據檔，除非我明確要求，否則唔好手動改。

## 修改工具時必須遵守

1. **只改指定嘅 folder**：改 `bankrate` 時唔好掂其他工具，除非我明確要求。
2. **保留每個 folder 嘅 `netlify.toml` 入面 `ignore` 嗰行**：佢令 Netlify 只喺該 folder 有改動時先重新部署，否則改一個工具會令全部工具重建。
3. **檔案路徑唔好超出自己個 folder**：Netlify 只會發佈該 folder 入面嘅檔案，所以唔可以用 `../` 引用其他 folder 嘅檔案。共用資源要用完整網址。
4. **語言**：介面文字用繁體中文（香港用語），`<html lang="zh-HK">`（或 `zh-Hant-HK`）。
5. **手機優先**：必須喺手機闊度（約 375px）正常顯示，唔可以出現橫向捲動。
6. **純前端工具保持純前端**：唔好為純前端工具加入 build 步驟或 npm 依賴。
7. **唔好放任何密碼、API key 落 repo**（呢個 repo 係公開嘅）。
8. **Commit message** 開頭寫 folder 名，例如 `vhis-rate: 修正保費計算`。

## 設計規格（MKPA 統一標準）

所有工具必須跟以下標準。每個工具可以保留自己嘅 CSS 變數名，但數值要對應呢套。

**標準檔案喺 `_standard/`**（唔會部署，只係範本）：
- `_standard/mkpa.css`：配色變數、電子名片、列印按鈕、列印頁頭嘅樣式。複製入工具嘅 CSS。
- `_standard/snippets.html`：字體連結、列印頁頭、列印按鈕、電子名片（連二維碼）、版權行、年份／列印日期 script。
- 改標準時先改 `_standard/`，再同步到每個工具。React 工具（mpf-compass）用 `src/components/layout/mk-standard.tsx`。

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

1. 開新 folder（英文細楷加連字號，例如 `price-calculator`）。
2. 寫 `index.html`，跟上面規則同設計規格（配色、字體、頁尾、列印）。
3. 複製任何一個純前端工具嘅 `netlify.toml`（只有 `ignore` 嗰行）放入新 folder。
4. 喺上面「工具一覽」加一行。
5. 喺 Netlify 新增 site，揀呢個 repo，Base directory 填該 folder 名。
