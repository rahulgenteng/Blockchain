from blockchain import Blockchain
from block import Block
from pow import proof_of_work
from pos import proof_of_stake

blockchain = Blockchain()


blockchain.add_block({
    "transaction_id": "TRX-001",
    "customer": "Customer-001",
    "merchant": "Toko ABC",
    "actor": "customer",
    "points": 100,
    "action": "Earn Point"
})


blockchain.add_block({
    "transaction_id": "TRX-001",
    "customer": "Customer-001",
    "merchant": "Toko ABC",
    "actor": "Merchant",
    "points": 100,
    "action": "Verify Point"
})


blockchain.add_block({
    "transaction_id": "TRX-001",
    "customer": "Customer-001",
    "merchant": "Toko ABC",
    "actor": "Admin",
    "points": 100,
    "action": "Approve Point"
})


blockchain.add_block({
    "transaction_id": "TRX-001",
    "customer": "Customer-001",
    "merchant": "Toko ABC",
    "actor": "Payment Gateway",
    "points": 100,
    "action": "Transaction Verification"
})


for block in blockchain.chain:

    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)


print("\nBlockchain valid:", blockchain.is_valid())


print("PROOF OF WORK")

block = Block(
    index=1,
    data="Poin Loyalty",
    previous_hash="0"
)

difficulty = 2

print("\nData Block       :", block.data)
print("Difficulty       :", difficulty)

proof_of_work(block, difficulty)

print("Nonce            :", block.nonce)
print("Hash             :", block.hash)

print("PROOF OF STAKE")

validators = {
    "Merchant": 10,
    "Customer": 20,
    "Admin": 30,
    "Payment Gateway": 40
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"- {validator}: {stake} stake")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)