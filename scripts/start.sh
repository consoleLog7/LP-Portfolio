#!/bin/bash

cd /home/ec2-user/LP-Portfolio

nohup python3 -m streamlit run main.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  > streamlit.log 2>&1 &