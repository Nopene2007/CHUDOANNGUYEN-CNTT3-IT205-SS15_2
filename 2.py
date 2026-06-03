atm_vault_balance = 50000000 
user_account_balance = 10000000
def display_balances():
    global atm_vault_balance,user_account_balance
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance}")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance}")
def deposit_money(amount):
    global atm_vault_balance,user_account_balance
    user_account_balance+=amount
    atm_vault_balance+=amount
    print(f"Giao dich thanh cong! So du tai khoan hien tai: {user_account_balance}")
    return True
def check_withdrawal_rules(amount):
    global atm_vault_balance,user_account_balance
    local_fee = 1100
    total_deduction=local_fee+amount
    if user_account_balance<total_deduction:
        return "INSUFFICIENT_FUNDS"
    elif atm_vault_balance<total_deduction:
        return "ATM_OUT_OF_CASH"
    else: 
        return "OK"
def execute_withdrawal(total_deduction, amount):
    global user_account_balance, atm_vault_balance
    user_account_balance-=total_deduction
    atm_vault_balance-=amount
    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount}")
    print(f"Số dư tài khoản còn lại: {user_account_balance}.")
while True:
    choice=input('''============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
Vui lòng chọn giao dịch (1-4): ''')
    match choice:
        case '1':
            display_balances()
        case '2':
            amount=int(input("Nhap so tien muon nap: "))
            deposit_money(amount)
        case '3':
            print("--- RÚT TIỀN ---")
            amount = int(input("Nhập số tiền cần rút: "))
            status=check_withdrawal_rules(amount)
            if status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Số dư tài khoản không đủ.")
            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
            elif status == "OK":
                fee = 1100
                total_deduction = amount + fee
                execute_withdrawal(total_deduction, amount)
        case '4':
            print("Ket thuc giao dich")
            break
        case _:
            print("Nhap lai di")
        