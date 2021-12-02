from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    print(f"Account: {account}")
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    print(updated_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
