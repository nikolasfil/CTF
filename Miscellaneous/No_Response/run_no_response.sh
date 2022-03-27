#!/bin/bash
ip a | grep 'inet'

sudo nc -lnvp 500 -e ./no_response.py