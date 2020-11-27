A quick script to explorer past fee estimates and actually paid fees.

Data is from statoshi.info for the fee estimates and from coingecko.com for
historical BTCUSD price.

Sample output with current data:
```
$ ./history.py
Unit is sat/vB

Fees paid
    Year: total
        average: 79.283
        median: 24.599
    Year: 2016
        average: 52.258
        median: 54.978
    Year: 2017
        average: 193.826
        median: 204.476
    Year: 2018
        average: 51.865
        median: 24.873
    Year: 2019
        average: 41.756
        median: 64.828
    Year: 2020
        average: 54.319
        median: 31.156

Fees estimated:
    Year: total
        averages: 161.733 (1 blocks), 96.279 (2 blocks), 87.639 (3 blocks), 81.71 (4 blocks), 78.87 (5 blocks), 68.844 (10 blocks), 54.237 (20 blocks)
        medians: 11.962 (1 blocks), 11.962 (2 blocks), 8.573 (3 blocks), 5.036 (4 blocks), 2.665 (5 blocks), 1.082 (10 blocks), 1.081 (20 blocks)
    Year: 2016
        averages: 44.508 (1 blocks), 60.677 (2 blocks), 46.087 (3 blocks), 41.527 (4 blocks), 38.66 (5 blocks), 30.039 (10 blocks), 21.643 (20 blocks)
        medians: 0.0 (1 blocks), 134.192 (2 blocks), 51.674 (3 blocks), 47.161 (4 blocks), 39.511 (5 blocks), 23.789 (10 blocks), 15.584 (20 blocks)
    Year: 2017
        averages: 584.524 (1 blocks), 246.598 (2 blocks), 229.498 (3 blocks), 216.489 (4 blocks), 209.787 (5 blocks), 187.265 (10 blocks), 158.155 (20 blocks)
        medians: 1529.129 (1 blocks), 353.335 (2 blocks), 320.657 (3 blocks), 320.657 (4 blocks), 320.657 (5 blocks), 284.144 (10 blocks), 162.648 (20 blocks)
    Year: 2018
        averages: 52.418 (1 blocks), 52.418 (2 blocks), 48.639 (3 blocks), 44.389 (4 blocks), 43.089 (5 blocks), 38.327 (10 blocks), 30.867 (20 blocks)
        medians: 8.79 (1 blocks), 8.79 (2 blocks), 8.225 (3 blocks), 6.171 (4 blocks), 6.043 (5 blocks), 5.49 (10 blocks), 3.597 (20 blocks)
    Year: 2019
        averages: 46.565 (1 blocks), 46.565 (2 blocks), 42.433 (3 blocks), 38.071 (4 blocks), 36.378 (5 blocks), 29.297 (10 blocks), 18.735 (20 blocks)
        medians: 84.039 (1 blocks), 84.039 (2 blocks), 73.554 (3 blocks), 66.538 (4 blocks), 63.788 (5 blocks), 51.924 (10 blocks), 35.747 (20 blocks)
    Year: 2020
        averages: 73.272 (1 blocks), 73.272 (2 blocks), 70.175 (3 blocks), 66.944 (4 blocks), 65.424 (5 blocks), 58.543 (10 blocks), 40.709 (20 blocks)
        medians: 32.03 (1 blocks), 32.03 (2 blocks), 31.083 (3 blocks), 28.756 (4 blocks), 28.695 (5 blocks), 25.263 (10 blocks), 16.788 (20 blocks)
```

```
$ ./history.py --usd
Unit is cents/vB

Fees paid
    Year: total
        average: 4.081
        median: 1.868
    Year: 2016
        average: 0.296
        median: 0.311
    Year: 2017
        average: 7.793
        median: 8.221
    Year: 2018
        average: 3.939
        median: 1.889
    Year: 2019
        average: 3.074
        median: 4.772
    Year: 2020
        average: 5.43
        median: 3.115

Fees estimated:
    Year: total
        averages: 7.699 (1 blocks), 4.953 (2 blocks), 4.618 (3 blocks), 4.316 (4 blocks), 4.184 (5 blocks), 3.683 (10 blocks), 2.831 (20 blocks)
        medians: 0.908 (1 blocks), 0.908 (2 blocks), 0.651 (3 blocks), 0.382 (4 blocks), 0.202 (5 blocks), 0.082 (10 blocks), 0.082 (20 blocks)
    Year: 2016
        averages: 0.252 (1 blocks), 0.344 (2 blocks), 0.261 (3 blocks), 0.235 (4 blocks), 0.219 (5 blocks), 0.17 (10 blocks), 0.122 (20 blocks)
        medians: 0.0 (1 blocks), 0.76 (2 blocks), 0.292 (3 blocks), 0.267 (4 blocks), 0.224 (5 blocks), 0.134 (10 blocks), 0.088 (20 blocks)
    Year: 2017
        averages: 23.503 (1 blocks), 9.915 (2 blocks), 9.228 (3 blocks), 8.705 (4 blocks), 8.435 (5 blocks), 7.529 (10 blocks), 6.359 (20 blocks)
        medians: 61.486 (1 blocks), 14.207 (2 blocks), 12.893 (3 blocks), 12.893 (4 blocks), 12.893 (5 blocks), 11.425 (10 blocks), 6.54 (20 blocks)
    Year: 2018
        averages: 3.981 (1 blocks), 3.981 (2 blocks), 3.694 (3 blocks), 3.371 (4 blocks), 3.273 (5 blocks), 2.911 (10 blocks), 2.344 (20 blocks)
        medians: 0.667 (1 blocks), 0.667 (2 blocks), 0.624 (3 blocks), 0.468 (4 blocks), 0.459 (5 blocks), 0.417 (10 blocks), 0.273 (20 blocks)
    Year: 2019
        averages: 3.428 (1 blocks), 3.428 (2 blocks), 3.123 (3 blocks), 2.802 (4 blocks), 2.678 (5 blocks), 2.156 (10 blocks), 1.379 (20 blocks)
        medians: 6.187 (1 blocks), 6.187 (2 blocks), 5.415 (3 blocks), 4.898 (4 blocks), 4.696 (5 blocks), 3.822 (10 blocks), 2.631 (20 blocks)
    Year: 2020
        averages: 7.325 (1 blocks), 7.325 (2 blocks), 7.016 (3 blocks), 6.693 (4 blocks), 6.541 (5 blocks), 5.853 (10 blocks), 4.07 (20 blocks)
        medians: 3.202 (1 blocks), 3.202 (2 blocks), 3.107 (3 blocks), 2.875 (4 blocks), 2.868 (5 blocks), 2.525 (10 blocks), 1.678 (20 blocks)
```
