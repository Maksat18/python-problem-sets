# -*- coding: utf-8 -*-
"""Problem set 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fX6umuAJo9S0pIyCp2p28LBM7Szwd_Ba

Problem 1
"""

n = 11
k = 10
for i in range(0,n+0):
    for j in range(k-i,0,-1):
        print(j,end= ' ')
    print(0)

"""Problem 2"""

savings = 2000
goal = 120_000
savings_contribution = 500
interest_contribution = 0
rate = 0.05
boost = 0.04
month = 1
while savings < goal:
  earned =  savings * (1+rate)
  interest_contribution += earned
  savings= earned
  savings_contribution += savings
  month= month + 1
print (f"It took {month} months to meet your goal.")
print (f"Your savings goal is met with amount {savings}")
print (f"Of which {savings_contribution} came from cash.")
print (f"and {interest_contribution} was earned in interest")
# followed your directions on the announcement. I am not sure the outcome is correct or not.