# 竹馬/竹兒緊急召回 API

## 安裝

### 安裝 Python

請確保你的系統上已安裝 Python 3.6 以上版本。你可以在終端或命令提示符中運行以下命令來檢查 Python 版本：

```bash
python --version
```

### 安裝依賴:

pip install -r requirements.txt

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

### 啟動項目

python mmh_psn_his_api.py.py

├── mmh_psn_api.py.py # 主應用文件
├── requirements.txt # 依賴文件
├── .env.example # 環境變量文件示例
├── README.md # 項目說明文件
