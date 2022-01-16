
# Goals
This project aims to provide a complete Brownie configuration to test the Kintsugi network.

# Requirements
Brownie: see [installation page](https://eth-brownie.readthedocs.io/en/stable/install.html)

# Conventions
Lines starting with the `# ` prompt are shell commands (zsh or bash, ...)  
Lines starting with the `>>> ` prompt are python/brownie commands  
Verbose output is omited.

# Testing Kintsugi with Brownie
```
# git clone https://github.com/sznicolas/brownie-testing-kintsugi
# cd brownie-testing-kintsugi
```

## Configure the network
This command must be run only once, and the network will be available for all your Brownie projects.
```
# brownie networks add Ethereum kintsugi \
    host=https://rpc.kintsugi.themerge.dev/ \
    explorer=https://explorer.kintsugi.themerge.dev/ \
    chainid=1337702
```

## Configure a new account
```
# brownie console

>>> a.add()
mnemonic: 'xxxxxxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx'
<LocalAccount '0x10ca1ADD2E550000000000123456789000000000'>
```
`LocalAccount` is your public address for the first account. You'll need it later.  
Copy the mnemonic in a new `.env` file in current directory:
```
# echo "export MNEMONIC='xxxxxxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx'" >> .env
# chmod 600 .env
```
This mnemonic will allow us to create several addresses, we'll generate two of them.

## Get some ether
Go to the [faucet](https://faucet.kintsugi.themerge.dev/) to get some test Ether.  
You must provide your public address, then wait few seconds to receive founds.

### Display your public key and your balance
```
# brownie console --network kintsugi
>>> from scripts import conf_utils
>>> mypubaccount = conf_utils.get_accounts()[0]
>>> mypubaccount.address
'0x10ca1ADD2E550000000000123456789000000000'
>>> mypubaccount.balance()
10710000000000000000
```

## Deploy a smart contract
The sample smart contract deployed is [`./contracts/FirstContract.sol`](./contracts/FirstContract.sol) .
```
# brownie run deploy_first_contract.py --network kintsugi
Brownie v1.17.2 - Python development framework for Ethereum

BrownieTestingKintsugiProject is the active project.

Running 'scripts/deploy_first_contract.py::main'...
Transaction sent: 0xd8e0018f0dea5f04a3dc71d72da914d468c552eb13e741c7bdad4fa24a3bff72
  Gas price: 1.0 gwei   Gas limit: 328027   Nonce: 0
  FirstContract.constructor confirmed   Block: 174665   Gas used: 298207 (90.91%)
  FirstContract deployed at: 0x79754e9680F0f04C51e8a131002c7DABdb6Bd470

My new contract
Transaction sent: 0xd380c5d75dc94cd34c02de9ccac2936da2f7cc76c44d8a3643103dc28198682e
  Gas price: 1.0 gwei   Gas limit: 32907   Nonce: 1
  FirstContract.updateMessage confirmed   Block: 174666   Gas used: 29900 (90.86%)

My contract updated!
```
You can add `-i` after `run` if you want to stay in the console after the deployment.  
You can also test locally before sending to Kintsugi by changing the `--network` value (development, mainnet-fork depending on your configuration)

# TODO
Script some tests (exchange some ether between account[0] and a[1], interact with more advanced smart contracts, ...)
