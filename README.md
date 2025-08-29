# AI 股市分析助理

## 專案概述

本專案旨在建構一個個人化的 AI 股市分析助理，利用大型語言模型（LLM）的能力，為使用者關注的特定股票（例如：緯創、陽明、長榮航）提供綜合性分析與買賣決策建議。有別於傳統程式交易的死板規則，本系統將模擬人類交易員的「思考」過程，綜合技術指標、市場趨勢與財經新聞等多元資訊，提供更具洞察力的決策輔助。

本專案的技術選型考量開發效率與彈性，將採用 Python Flask 作為後端，並以 Streamlit 快速建構前端介面。

## 核心價值

- 綜合分析：結合量化數據（價格、技術指標）與質化資訊（財經新聞）。

- 決策透明：AI 的分析過程與建議理由清晰可見，使用者能理解其背後邏輯。

- 個人化：專注於使用者感興趣的特定股票，避免資訊超載。

- 快速原型：選擇的技術棧（Flask + Streamlit）能有效縮短開發週期，迅速驗證想法。

## 系統架構與技術棧

本專案將分為三大核心模組，各司其職，協同運作。

1. 資料層（Data Layer）

|   模組   |   用途   |      執行方式|
|---------|-----------|----------------------|
|yfinance|	獲取歷史股票價格數據（日線、開盤、收盤價等）|使用 yfinance.download('股票代碼') 獲取數據，作為技術分析的輸入|
|pandas  |數據處理與組織|將原始數據轉換成易於處理的 DataFrame 格式|
|Pandas-ta|	計算技術分析指標|使用 talib.MACD(), talib.RSI() 等函數計算所需的指標數值|
|requests & BeautifulSoup4|	財經新聞爬蟲|爬取財經網站，並用關鍵字過濾出與關注股票相關的新聞標題與內容|

2. 後端層（Backend Layer）

|   模組   |   用途   |      執行方式|
|---------|-----------|----------------------|
|Flask|輕量級後端伺服器|建立 API 路由，接收前端請求，並調用其他模組進行處理。|
|openai|與 OpenAI API 互動|將市場數據與新聞整合成 Prompt，發送給 OpenAI 並接收分析結果|
|prompt engineering|提示詞工程|設計精準的 Prompt，引導 AI 扮演專業分析師，並要求提供決策理由|

3. 前端層（Frontend Layer）

|   模組   |   用途   |      執行方式|
|---------|-----------|----------------------|
|Streamlit| 快速建構網頁應用程式|創建使用者介面，如股票選擇下拉選單、圖表展示區與分析結果文字框|
|matplotlib|繪製互動式圖表|繪製 K 線圖、技術指標線，並在圖上標註 AI 建議的買賣點|

## 執行流程

1. 使用者在 Streamlit 介面選擇感興趣的股票。

2. 前端透過 Flask 向後端發送請求。

3. 後端調用 yfinance 和爬蟲模組獲取最新的市場數據和新聞。

4. 數據經過 pandas 和 talib 處理，生成技術指標。

5. 所有資訊被彙整成一份結構化的「市場報告」。

6. 後端將「市場報告」組裝成一個精準的 Prompt，並透過 openai 模組發送給 OpenAI API。

7. LLM 回傳分析結果，包含買賣建議、理由與信心度。

8. 後端將結果傳回前端 Streamlit。

9. Streamlit 將分析內容與圖表呈現在網頁上，供使用者參考。

## 建構步驟

1. 架設虛擬環境

  ```sh
  python -m venv venv
  ```

2. 安裝相關套件

  ```sh
  pip install flask streamlit openai

  pip install yfinance pandas pandas-ta

  pip install requests beautifulsoup4

  pip install matplotlib plotly

  pip install pytest pytest-cov
  ```