#!/usr/bin/env python3
import sys

def rounded(n: float) -> float:
    return n * 1000 // 1 / 1000

if __name__ == "__main__":
    USE_USD = len(sys.argv) == 2 and sys.argv[1] == "--usd"
    # This data is from Coingecko. See https://www.coingecko.com/en/coins/bitcoin/historical_data/usd?end_date=2020-11-27&start_date=2016-01-01#panel
    # and the btcusd.py script.
    BTCUSD = {
        "2016": 567,
        "2017": 4021,
        "2018": 7596,
        "2019": 7362,
        "2020": 9998,
    }

    if USE_USD:
        print("Unit is cents/vB", end="\n\n")
    else:
        print("Unit is sat/vB", end="\n\n")

    # This data is from Statoshi (by Jameson Lopp). See https://www.statoshi.info/dashboard/db/fee-estimates
    with open("fees_paid.csv", "r") as f:
        fees_paid = {
            "total": [],
        }
        for line in f.readlines()[1:]:
            [_, date, sat_vb] = line.split(";")
            year = date[:4]

            if year not in fees_paid:
                fees_paid[year] = []
            sat_vb = float(sat_vb.strip("\n"))
            if USE_USD:
                if year not in BTCUSD:
                    raise ValueError("Need fresh numbergoup sir")
                sat_vb = sat_vb * BTCUSD[year] * 10**-5  # Cents of USDs
            fees_paid[year].append(sat_vb)
            fees_paid["total"].append(sat_vb)

        print("Fees paid")
        for year, fees in fees_paid.items():
            n = len(fees)
            avg = sum(fees) / n
            median = fees[n // 2] if n % 2 == 0 else \
                        (fees[n // 2] + fees[n // 2 + 1]) / 2
            print(f"    Year: {year}")
            print(f"        average: {rounded(avg)}")
            print(f"        median: {rounded(median)}")

    with open("fees_estimated.csv", "r") as f:
        estimates = {
            "total": {},
        }
        for line in f.readlines()[1:]:
            [target_id, date, sat_vb] = line.split(";")
            target = int(target_id.strip("block"))
            year = date[:4]

            if target > 20:
                # They are 'null' in the dataset, and we don't really care
                continue

            if year not in estimates:
                estimates[year] = {}
            if target not in estimates[year]:
                estimates[year][target] = []
            if target not in estimates["total"]:
                estimates["total"][target] = []

            sat_vb = float(sat_vb.strip("\n"))
            if USE_USD:
                if year not in BTCUSD:
                    raise ValueError("Need fresh numbergoup sir")
                sat_vb = sat_vb * BTCUSD[year] * 10**-5  # Cents of USDs
            estimates[year][target].append(sat_vb)
            estimates["total"][target].append(sat_vb)

        print("\nFees estimated:")
        for year in estimates:
            avgs = {}
            medians = {}
            for target in estimates[year]:
                n = len(estimates[year][target])
                avgs[target] = sum(estimates[year][target]) / n
                if n % 2 == 0:
                    medians[target] = estimates[year][target][n // 2]
                else:
                    medians[target] = (estimates[year][target][n // 2] +
                                       estimates[year][target][n // 2 + 1]) / 2

            print(f"    Year: {year}")
            print("        averages: {}".format(
                ", ".join(f"{rounded(avgs[target])} ({target} blocks)"
                          for target in avgs)
            ))
            print("        medians: {}".format(
                ", ".join(f"{rounded(medians[target])} ({target} blocks)"
                          for target in medians)
            ))
