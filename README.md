# Celestia Load Test

A Locust based script to test the *submit_pfb* RPC endpoint.

## Dependencies

* pip
* pipenv (https://pypi.org/project/pipenv/)


## Install

```bash
pipenv install
```

## Run

```bash
pipenv run locust -f locustfile.py --run-time 60s --headless -u 10 --host http://localhost:26659 --csv=/tmp/results.csv
```

This assumes you want to run the test locally to your node with 10 users for a duration of 60 seconds.