#!/bin/sh
if [ ! -f ./orders.json ]; then
	wget https://gist.githubusercontent.com/udnay/20603ff9956064c8d1f1abf7a5e6f5b2/raw/9e841b973a3d9d51940bdffe162c1400a9bac022/orders.json
elif [ ! -f ./customers.json ]; then
	wget https://gist.githubusercontent.com/udnay/d8e2ea75f2cfd7d75482f42549c31c59/raw/60da021e9f083f0c4bf0910f690baf5f38410bc6/customers.json
fi

python inner_join.py customers.json orders.json cid customer_id
