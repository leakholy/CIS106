#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:02:09 2026

@author: omar
"""

# Calculate amount invested in a stock

ticker_symbol = input("Enter the stock ticker symbol: ")
shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print(f"Stock ticker symbol: {ticker_symbol}")
print(f"Amount invested: ${amount_invested:.2f}")