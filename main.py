from blockchain import Blockchain


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