# 竹馬/竹兒緊急召回 API

## 安裝

### 安裝 Python

請確保你的系統上已安裝 Python 3.6 以上版本。  
你可以在終端或命令提示符中運行以下命令來檢查 Python 版本：

```bash
python --version
```

### 安裝依賴:

pip install -r requirements.txt

確保 requirements.txt 包含以下依賴項：

```
line-bot-sdk
flask
cx_Oracle
gunicorn
python-dotenv
```

## 加載 .env 文件中的環境變量:

- main.py 加入這兩行才會加載.env
  `from dotenv import load_dotenv`
  `load_dotenv()`

## 修改 requirement.txt:

- 加入以下這行
  `python-dotenv`

## 創建並配置 .env 文件：

### .env 文件範例

DB_HOST=localhost  
DB_PORT=yourport  
DB_SERVICE_NAME=yourservicename  
DB_USER=yourusername  
DB_PASSWORD=yourpassword

## 啟動項目

`python mmh_psn_his_api.py`

## 部署到生產環境

### 安裝 Gunicorn

### 運行以下命令安裝 Gunicorn：

`pip install gunicorn`

## 使用 Gunicorn 運行應用

### 使用以下命令啟動應用，並將端口設置為 5000：

`gunicorn -w 4 -b 0.0.0.0:5000 mmh_psn_his_api:app`

## 配置 Nginx 作為反向代理

### 設置 Nginx 配置文件以轉發請求到 Gunicorn

## 啟動 Nginx

### 確保 Nginx 已安裝並運行

├── mmh_psn_api.py.py # 主應用文件  
├── requirements.txt # 依賴文件  
├── .env.example # 環境變量文件示例  
├── README.md # 項目說明文件
