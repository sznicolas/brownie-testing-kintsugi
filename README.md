
# Objectives
This project aims to provide a full configuration to test the Kintsugi network with Brownie.

# Requirements
Brownie: see [installation page](https://eth-brownie.readthedocs.io/en/stable/install.html)

# Conventions
Lines starting with the `# ` prompt are shell commands (zsh or bash, ...)  
Lines starting with the `>>> ` prompt are python/brownie commands

# Testing Kintsugi with Brownie
git clone ...
cd ...

## Configure the network
```
# brownie networks add Ethereum kintsugi  host=https://rpc.kintsugi.themerge.dev/ explorer=https://explorer.kintsugi.themerge.dev/ chainid=1337702
```

## Configure a new account
```
# brownie console

>>> a.add()
mnemonic: 'xxxxxxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx'
<LocalAccount '0x70ca1ADD2E551234567890123456789000000000'>
```
Keep the `LocalAccount` for later ; this is your public address.  
Copy the mnemonic in a new `.env` file in current directory:
```
#  kintsugi echo "export MNEMONIC='xxxxxxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx xxx'" > xenv
#  kintsugi chmod 600 .env
```

## Get some ether
Go to the [faucet](https://faucet.kintsugi.themerge.dev/) to get some test Ether.  
You must provide your public address.
### Display your public key
If needed, here is how to display your public key:

```
# brownie console --network kintsugi
>>> from scripts import conf_utils
>>> conf_utils.get_accounts()[0].address
'0x70ca1ADD2E551234567890123456789000000000'
```

## Deploy a smart contract
```
# brownie run deploy_first_contract.py --network kintsugi
```
You can add `-i` after `run` if you want to stay in the console after the deployment.  
You can also test locally before sending to Kintsugi by changing the `--network` value (development, mainnet-fork accordingly to your configuration)

# TODO
Script sometests (exchange some ether betwwen account[0] and a[1], interact with more advancedsmart contracts, ...)
