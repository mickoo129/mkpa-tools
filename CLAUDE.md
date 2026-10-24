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

## 設計規格

**統一標準：未定。** 而家每個工具各有自己嘅配色同字體，喺決定統一標準之前，改工具時跟返該工具現有嘅風格，唔好自行引入新配色。

現有配色參考：

| 工具 | 主色 | 背景 | 文字 |
|---|---|---|---|
| bankrate | `#1565c0` | `#f2f5f8` | `#0f1d2c` |
| claimsreport | `#b5502a` | `#f6f4ef` | `#14213d` |
| mpf-compass | `#1a7a96` | — | — |
| public-rental-housing | `#00a758` | `#f7f9f8` | `#1d1d1f` |
| vhis-rate | `#0e5e57` | `#f4f2ec` | `#16213a` |
| ci-promotion | — | — | `#1D2B2A` |
| hk-medical-insurance-compare | — | — | `#16262B` |

## 新增工具

1. 開新 folder（英文細楷加連字號，例如 `price-calculator`）。
2. 寫 `index.html`，跟上面規則。
3. 複製任何一個純前端工具嘅 `netlify.toml`（只有 `ignore` 嗰行）放入新 folder。
4. 喺上面「工具一覽」加一行。
5. 喺 Netlify 新增 site，揀呢個 repo，Base directory 填該 folder 名。
