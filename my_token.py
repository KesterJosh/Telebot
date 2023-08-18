import requests
from web3 import Web3

# Etherscan API key
ETHERSCAN_API_KEY = "P1T6WRTYS8RHXDXUAC6FKX1BIZ5TX9E8M2"

# Ethereum node URL
infura_url = "https://mainnet.infura.io/v3/05e37ed816b34dc9bb71c8e0719aa081"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Contract address
contract_address = "0xbD1b10DA53f82bA46b27Ac498BcaaB4d96591FBD"

# Construct the Etherscan API URL
etherscan_api_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={ETHERSCAN_API_KEY}"

# Fetch the ABI using the Etherscan API
response = requests.get(etherscan_api_url)
data = response.json()

if data.get("status") == "1":
    token_abi = data.get("result")

    # Create contract instance
    token_contract = web3.eth.contract(address=contract_address, abi=token_abi)

    address_to_check = "0xF166c66D276EF58aF0Df4BB6977B5F2aF2889BB8"
    token_balance = token_contract.functions.balanceOf(address_to_check).call()

    print(f"Tokens burned from {address_to_check}: {token_balance}") 
else:
    print("Failed to fetch ABI.")
