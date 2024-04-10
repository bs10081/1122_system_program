import sqlite3
import sys

# 創建SQLite數據庫連接
conn = sqlite3.connect('symbol_table.db')
c = conn.cursor()

# 創建表格
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS symbol_table
                 (label TEXT PRIMARY KEY, address TEXT)''')

# 手動添加模式
def manual_add_mode():
    while True:
        label = input("輸入 label (或輸入 'exit()' 退出): ").upper()
        if label == 'EXIT()':
            break
        address = input("輸入 address: ").upper()
        c.execute("INSERT OR IGNORE INTO symbol_table VALUES (?, ?)", (label, address))
        conn.commit()

# 查詢address
def lookup_address(label):
    c.execute("SELECT address FROM symbol_table WHERE label=?", (label,))
    result = c.fetchone()
    if result:
        address = result[0]
        print(f"label '{label}' 對應的address為: {address}")
    else:
        print(f"沒有找到 label '{label}' 對應的address")

def main():
    create_table()
    
    # 模式選擇,add: 手動添加模式, lookup: 查詢模式    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'add':
            manual_add_mode()
        elif sys.argv[1] == 'lookup':
            while True:
                label = input("請輸入 label (或輸入 'exit()' 退出): ").upper()
                if label == 'EXIT()':
                    break
                lookup_address(label)
        else:
            print("無效的選擇,請重試。")
            
    # 關閉數據庫連接        
    conn.close()

if __name__ == "__main__":
    main()