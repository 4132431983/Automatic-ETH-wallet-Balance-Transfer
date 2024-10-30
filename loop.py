import threading
from tracemalloc import stop
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjA4NDkzOTRhLWI2ZDEtNGRjMC1iNTg1LTI5ZjgyZjZjOTdhZSIsIm9yZ0lkIjoiNDEzOTAwIiwidXNlcklkIjoiNDI1MzU5IiwidHlwZUlkIjoiMGUwMmZjN2MtYTUyNC00Y2EwLTlmMDAtNzlmNzI4MmEyNTRiIiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE3MzAyNzU0NTYsImV4cCI6NDg4NjAzNTQ1Nn0.ZeCbcrNZy2vnr54Hj9vMZjAsaM5N8yhFr2N-rtlOrgA"))
private_key = "<0xee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258>"
pub_key ="<0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3>"

recipient_pub_key = "<0x551510dFb352bf6C0fCC50bA7Fe94cB1d2182654>"
def loop():
    while True:
        balance = w3.eth.get_balance(pub_key)
        print()
        print(balance)
        gasPrice = w3.toWei('1100', 'gwei')
        gasLimit = 21000
        nonce = w3.eth.getTransactionCount(pub_key)
        tx = {
            'chainId': 1,
            'nonce': nonce,
            'to': recipient_pub_key,
            'value': balance-gasLimit*gasPrice,
            'gas': gasLimit,
            'gasPrice': gasPrice
        }

        try:
         if balance > 0:
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(w3.toHex(tx_hash))
        except:
            print("insufficient funds")

threading.Thread(target=loop, daemon=True).start()
input('Press Enter to exit.')
