import requests
from web3 import Web3

# First Work 
# Etherscan API URL
api_url = "https://api.etherscan.io/api"

# Your Etherscan API key (sign up on Etherscan to get one)
api_key = "P1T6WRTYS8RHXDXUAC6FKX1BIZ5TX9E8M2"

# Smart contract address
contract_address = "0x7D6af46d6789652D811435d36B716fCc824F4f46"

# Initialize a set to store unique addresses
unique_addresses = set()

# Define parameters for the API request
params = {
    "module": "account",
    "action": "txlist",
    "address": contract_address,
    "apikey": api_key,
}

# Make the API request
responseX = requests.get(api_url, params=params)

# Parse the JSON responseX
if responseX.status_code == 200:
    data = responseX.json()
    if data["status"] == "1":
        for tx in data["result"]:
            # Check if the 'from' and 'to' fields are not empty before adding them to the set
            if tx["from"]:
                unique_addresses.add(tx["from"])
            if tx["to"]:
                unique_addresses.add(tx["to"])
    else:
        print("API response status is not 1 (error).")
else:
    print("API request failed.")

# Convert the set of unique addresses to a list
unique_addresses_list = list(unique_addresses)

# Print the list of unique addresses
# print(unique_addresses_list)

# End First work 

# Etherscan API key
ETHERSCAN_API_KEY = "P1T6WRTYS8RHXDXUAC6FKX1BIZ5TX9E8M2"

# Ethereum node URL
infura_url = "https://mainnet.infura.io/v3/05e37ed816b34dc9bb71c8e0719aa081"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Contract address

# Construct the Etherscan API URL
etherscan_api_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={ETHERSCAN_API_KEY}"

# Fetch the ABI using the Etherscan API
response = requests.get(etherscan_api_url)
data = response.json()

if data.get("status") == "1":
    token_abi = data.get("result")

    try:
        # Create contract instance
        token_contract = web3.eth.contract(address=contract_address, abi=token_abi)

        # List of unique addresses to check
        # unique_addresses_list = ["0x6d3fd2dba53c072d272b4f9ab319b63de62618fe", "0x6d3fd2dba53c072d272b4f9ab319b63de62618fe", "0xbd9715d59dc280bd84746670c3a21c4e88962e72", "0x776a4d4533624374b0866ae17136222c75b5e367", "0x6357cc70d0d955f6038153c23f84e2436d3c1810", "0x8051273a46cabef40493070e829cb8ee499bf549", "0x3ba331b7026b60e5f92f5a039cdded8e52c90cd3", "0x28004d7977a63f67006c3769c6680635c5b50e01", "0xa3efed4b1359e3c0c58ea511fa55387a15002597", "0x7e96f1852fe94348de2177aeeba5909cb601b3e5", "0xa25773218e7698b3cdf5867ec555d99e09f88c3e", "0x2966c972df5de4d78e0623b12a38088bdf5e862e"]
        token_total = 0
        for address_to_check in unique_addresses_list:
            # Convert the address to checksum format
            checksum_address = Web3.to_checksum_address(address_to_check)

            token_balance = token_contract.functions.balanceOf(checksum_address).call()

            # Add the token_balance to token_total
            token_total += token_balance

            print(f"Tokens burned from {checksum_address}: {token_balance} - Total {token_total}")
    except Exception as e:
        print(f"An error occurred while checking balance: {e}")
    print(f"Total Token Burnt: {token_total}")
else:
    print("Failed to fetch ABI.")
