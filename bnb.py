from web3 import Web3
import config
import time

bsc = "https://bsc-dataseed.binance.org/"
# bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

account1 = "0xA183CAC199f229e127986fe6aeE29d271e758B6A"
receiver = ["0x22e4aFF96b5200F2789033d85fCa9F58f163E9Ea", "0xa03e190c8249292a32cbf6ea04f394af44ce8f74"]

balance = web3.eth.get_balance(account1)
humanReadable = web3.fromWei(balance, 'ether')
print(humanReadable)

for i in receiver:
    print(i)
    nonce = web3.eth.getTransactionCount(account1)
    
    tx = {
        'nonce': nonce,
        'to': web3.toChecksumAddress(i),
        'value': web3.toWei(0.0001, 'ether'),
        'gas': 21000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    
    signedTx = web3.eth.account.signTransaction(tx, config.private)
    tx_hash = web3.eth.sendRawTransaction(signedTx.rawTransaction)
    trans = web3.toHex(tx_hash)
    print(trans)
    time.sleep(10)