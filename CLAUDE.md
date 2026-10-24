# my-tools 統一規則

呢個 repo 集合咗我所有放喺 Netlify 嘅小工具。每個子 folder 係一個獨立工具，各自部署做一個 Netlify site（Base directory = 該 folder 名）。

## Repo 結構

```
my-tools/
├── CLAUDE.md
├── shared/          ← 共用樣式，獨立部署做一個 Netlify site
│   └── style.css
├── tool-a/
│   └── index.html
└── tool-b/
    └── index.html
```

## 修改工具時必須遵守

1. **樣式**：一律引用共用 CSS，唔好喺個別工具重新定義顏色、字體、按鈕樣式：
   ```html
   <link rel="stylesheet" href="https://【你的共用樣式網址】.netlify.app/style.css">
   ```
   工具專屬嘅排版可以加喺該工具自己嘅 `<style>`，但只限 layout，唔好改顏色同字體。
2. **語言**：介面文字用繁體中文（香港用語）。
3. **頁面結構**：每個工具都要有：
   - 頂部 header：工具名稱 + 一句簡介
   - 中間主要內容
   - 底部 footer：【例如：© 你的名字／品牌、返回工具總覽連結】
4. **手機優先**：必須喺手機闊度（約 375px）正常顯示，唔可以出現橫向捲動。
5. **純前端**：每個工具係純 HTML/CSS/JS，唔使 build 步驟。盡量一個 `index.html` 搞掂。
6. **唔好改其他 folder**：改 `tool-a` 時唔好掂 `tool-b` 等其他工具，除非我明確要求。

## 設計規格（同 shared/style.css 一致）

- 主色：【例如 #2563EB】
- 輔助色：【例如 #F59E0B】
- 背景色：【例如 #FFFFFF】
- 文字色：【例如 #1F2937】
- 字體：【例如 "Noto Sans TC", sans-serif】
- 圓角：【例如 8px】
- 按鈕：主色背景、白色字、圓角

## 新增工具

1. 開新 folder（英文細楷加連字號，例如 `price-calculator`）
2. 跟上面規則寫 `index.html`
3. 喺 Netlify 新增 site，Base directory 填該 folder 名
