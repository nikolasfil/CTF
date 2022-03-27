#!/bin/bash

# sudo nc -lnvp 500 -e ./no_response.py
# ncat --broker -lnvp 500 -e ./no_response.py
ncat -lnvkp 500 -e ./no_response.py

