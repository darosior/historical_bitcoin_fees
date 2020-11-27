if __name__ == "__main__":
    with open("btcusd.csv") as f:
        btcusd = {}
        for line in f.readlines()[1:]:
            [date, price, _, _] = line.split(",")
            year = date[:4]

            if year not in btcusd:
                btcusd[year] = []

            btcusd[year].append(float(price))

        for year, prices in btcusd.items():
            print(f"{year}: {sum(prices) / len(prices)}")
