from logging import WARNING
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass  # older Pythons / unusual terminals: safe to ignore

CASHOUT_REQUESTS = [
    {"customer": "Chinedu Okafor", "phone": "08031234567", "amount": 5000,  "account_balance": 20000},
    {"customer": "Aisha Bello",    "phone": "07061234567", "amount": "five thousand", "account_balance": 15000},
    {"customer": "Emeka Nwosu",    "phone": "08101234567", "amount": 40000, "account_balance": 2000},
    {"customer": "Fatima Sani",    "phone": "09021234567", "amount": 2550,  "account_balance": 30000},
    {"customer": "Tunde Adeyemi",  "phone": "08051234567", "amount": 75000, "account_balance": 90000},
    {"customer": "Blessing Eze",   "phone": "07031234567", "amount": 10000, "account_balance": 50000},
    {"customer": "Unknown Customer","phone": "08099887766", "amount": 3000},  # <-- missing "account_balance"!
    {"customer": "Ibrahim Musa",   "phone": "08122334455", "amount": -3000, "account_balance": 10000},
    {"customer": "Ngozi Uche",     "phone": "09033445566", "amount": 0,     "account_balance": 8000},
]

NOTE_UNIT = 100
OPENING_FLOAT = 50000

class TransactionError(Exception):
    pass

class InsufficientFundsError(TransactionError):
    pass  # TODO: keep this class; it should inherit from TransactionError.

class DailyLimitError(TransactionError):
    pass

def validate_amount(amount):
    
    try:
        amount = int(amount)
    except:
        raise TransactionError("Amount must be a number")
    
    if amount <= 0:
        raise TransactionError("Amount must be greater than zero")
    if amount % NOTE_UNIT != 0:
        raise TransactionError("Amount must be a multiple of zero")
    if amount > 100000:
        raise DailyLimitError("Cash-Out cannot be more than ₦100,000")
    
    return amount

def check_balance(amount, account_balance):
    if amount > account_balance:
        raise InsufficientFundsError(
            "Customer doesnt have enough money"
        )

def check_agent_float(amount, agent_float):
    
    if amount > agent_float:
        raise TransactionError("Agent doesnt have enough money")
    
def charge_fee(amount):
    
    return (amount // 5000) * 100  # (this is the only line you need).

def process_cashout(request, agent_float):
    
    new_float = agent_float
    
    try:
        customer = request["customer"]
        amount = validate_amount(request["amount"])
        balance = request["balance"]
        
        check_balance(amount, balance)
        check_agent_float(amount, agent_float)
        
    except TransactionError as e:
        print("Rejected:", e)
        
    except KeyError as f:
        print("Rejected: request was missing information", f)
        
    except Exception as g:
        print("Rejected: unexpected issue", g)
        
    else:
        fee = charge_fee(amount)
        new_float = agent_float - amount
        print("Approved! Paid out, fee charged, new float:", new_float)
        
        if new_float < 10000:
            print( "WARNING: Float is below ₦10,000!")
        
    finally:
        print("---Transction ended---")
        
    return new_float

def main():
    agent_float = OPENING_FLOAT
    
    successes = 0
    failures = 0
    
    print("====== MAMA NGOZI POS TERMINAL ======")
    print(f"Opening float: ₦{agent_float:,}")
    print()
    
    for request in CASHOUT_REQUESTS:
        name = request.get("customer", "Unknown")
        phone = request.get("phone", "")
        print(f"Processing cash-out for {name} ({phone})...")

        old_float = agent_float
        
        agent_float = process_cashout(request, agent_float)
        
        if agent_float != old_float:
            successes += 1
        else:
            failures += 1
            
        print()
        print("============ END OF DAY ============")
        print(f"Successful cash-outs: {successes}")
        print(f"Failed cash-outs:     {failures}")
        print(f"Final float: ₦{agent_float:,}")


if __name__ == "__main__":
    main()