import cx_Oracle
import os
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# 加載 .env 文件中的環境變量
load_dotenv()

# 從環境變量中獲取數據庫連接信息
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_service_name = os.getenv("DB_SERVICE_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# 確保所有必要的環境變量都已設置
if not all([db_host, db_port, db_service_name, db_user, db_password]):
    raise ValueError("One or more environment variables are not set.")

# 創建 DSN 字符串
dsn_tns = cx_Oracle.makedsn(db_host, db_port, service_name=db_service_name)

# 創建 Flask 應用
app = Flask(__name__)

# 設置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        connection = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn_tns)
        return connection
    except cx_Oracle.DatabaseError as e:
        logger.error(f"Failed to connect to the database: {str(e)}")
        raise ValueError("Failed to connect to the database.")

def query_psn_table(hospid, empno):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # 執行查詢
        cursor.execute("SELECT HOSPID, NAMEC, QDATE, DDATE, DIVISION FROM PSN_HIS WHERE HOSPID = :hospid AND EMPNO = :empno AND QDATE IS NULL AND DDATE IS NOT NULL", hospid=hospid, empno=empno)
        rows = cursor.fetchall()
        
        # 將查詢結果轉換為字典列表
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        return result
    
    except cx_Oracle.DatabaseError as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise ValueError("An error occurred while querying the database.")
    
    finally:
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass  # cursor 未定義
        try:
            if connection:
                connection.close()
        except NameError:
            pass  # connection 未定義

@app.route('/psn', methods=['GET'])
def get_psn():
    hospid = request.args.get('HOSPID')
    empno = request.args.get('EMPNO')
    if not hospid or not empno:
        return jsonify({"error": "Missing HOSPID or EMPNO"}), 400
    try:
        result = query_psn_table(hospid, empno)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
