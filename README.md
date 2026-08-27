## 檔案說明
- train.py : 模型訓練(BERT fine-tune)
- predict.py : 提問預測
- core.py : 模型預測與訓練所需函數
- test1.ipynb : 測試模型調用與分類結果
- main.py 專案主程式

## 資料夾說明
- trained_model : 存放訓練好的模型

## bert 必要檔案
- bert-base-chinese-vocab.txt : bert字典
- nba.txt : 訓練資料集 (檔名變更記得改程式路徑)

## 使用說明
1. 執行train.py 訓練完成後會生成 trained_model 內所需檔案
2. 更改LineBot金鑰 channel_access_token，channel_secret
3. 開啟 ngrok port號為 app.py 程式指定 port 號
4. 執行app.py
5. 回 line developers 改 Webhook settings URL
***
## 環境需求 
- python 
- pytorch 
- falsk 
- line-bot-sdk 
- beautifulsoup4 

pip install 