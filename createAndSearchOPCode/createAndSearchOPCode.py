import sqlite3
import sys

# 創建SQLite數據庫連接
conn = sqlite3.connect('opcode_table.db')
c = conn.cursor()

# 創建表格
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS opcode_table
                 (mnemonic TEXT PRIMARY KEY, opcode TEXT)''')

# 初始化數據
def initialize_data():
    initial_data = [
        ('ADD', '18'),
        ('ADDF', '58'),
        ('ADDR', '90'),
        ('AND', '40'),
        ('CLEAR', 'B4'),
        ('COMP', '28'),
        ('COMPF', '88'),
        ('COMPR', 'A0'),
        ('DIV', '24'),
        ('DIVF', '64'),
        ('DIVR', '9C'),
        ('FIX', 'C4'),
        ('FLOAT', 'C0'),
        ('HIO', 'F4'),
        ('J', '3C'),
        ('JEQ', '30'),
        ('JGT', '34'),
        ('JLT', '38'),
        ('JSUB', '48'),
        ('LDA', '00'),
        ('LDB', '68'),
        ('LDCH', '50'),
        ('LDF', '70'),
        ('LDL', '08'),
        ('LDS', '6C'),
        ('LDT', '74'),
        ('LDX', '04'),
        ('LPS', 'D0'),
        ('MUL', '20'),
        ('MULF', '60'),
        ('MULR', '98'),
        ('NORM', 'C8'),
        ('OR', '44'),
        ('RD', 'D8'),
        ('RMO', 'AC'),
        ('RSUB', '4C'),
        ('SHIFTL', 'A4'),
        ('SHIFTR', 'A8'),
        ('SIO', 'F0'),
        ('SSK', 'EC'),
        ('STA', '0C'),
        ('STB', '78'),
        ('STCH', '54'),
        ('STF', '80'),
        ('STI', 'D4'),
        ('STL', '14'),
        ('STS', '7C'),
        ('STSW', 'E8'),
        ('STT', '84'),
        ('STX', '10'),
        ('SUB', '1C'),
        ('SUBF', '5C'),
        ('SUBR', '94'),
        ('SVC', 'B0'),
        ('TD', 'E0'),
        ('TIO', 'F8'),
        ('TIX', '2C'),
        ('TIXR', 'B8'),
        ('WD', 'DC')
    ]

    c.executemany("INSERT OR IGNORE INTO opcode_table VALUES (?, ?)", initial_data)
    conn.commit()

# 手動添加模式
def manual_add_mode():
    while True:
        choice = input("輸入 'a' 添加新的 opCode 和 mnemonic, 輸入 'q' 退出: ").lower()
        if choice == 'q':
            break
        elif choice == 'a':
            mnemonic = input("輸入 mnemonic: ").upper()
            opcode = input("輸入 opCode: ").upper()
            c.execute("INSERT OR IGNORE INTO opcode_table VALUES (?, ?)", (mnemonic, opcode))
            conn.commit()
        else:
            print("無效的選擇,請重試。")

# 查詢opcode
def lookup_opcode(mnemonic):
    c.execute("SELECT opcode FROM opcode_table WHERE mnemonic=?", (mnemonic,))
    result = c.fetchone()
    if result:
        opcode = result[0]
        print(f"mnemonic '{mnemonic}' 對應的 opCode 為: {opcode}")
    else:
        print(f"沒有找到 mnemonic '{mnemonic}' 對應的 opCode")

def main():
    create_table()
    initialize_data()

    # 模式選擇，add: 手動添加模式, lookup: 查詢模式
    if len(sys.argv) > 1:
        if sys.argv[1] == 'add':
            manual_add_mode()
        elif sys.argv[1] == 'lookup':
            while True:
                mnemonic = input("請輸入 mnemonic: ").upper()
                lookup_opcode(mnemonic)
        else:
            print("無效的選擇，請重試。")

    # 關閉數據庫連接
    conn.close()

    # 關閉數據庫連接
    conn.close()

if __name__ == "__main__":
    main()