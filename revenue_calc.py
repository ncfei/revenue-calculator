import matplotlib.pyplot as plt
import numpy as np
print("Please enter the following variables:")
setup_fee = input("Setup fee($500):")
monthly_fee = input("Monthly fee($150):")
new_customer = input("New customer per month(5):")
churn_rate = input("Number of customer leaving per month(1):")

if setup_fee == "":
    setup_fee = 500
if monthly_fee == "":
    monthly_fee = 150
if new_customer == "":
    new_customer = 5
if churn_rate == "":
    churn_rate = 1
total_customer = 0
cumulative_revenue = 0
year = 10

for n in range(1,12*year+1):
    total_customer = int(new_customer) + total_customer
    if(n == 1) :
        j = 0
    else:
        j = 1
    monthly_revenue = (int(setup_fee) * int(new_customer)) + (int(monthly_fee)*(int(total_customer)-int(churn_rate)*j))
    #print("Setup fee: " + setup_fee)
    #print("New customer: " + new_customer)
    #print("Monthly fee: " + monthly_fee)
    #print("Total customer: " + str(total_customer))
    #print("Churn rate: " + churn_rate)
    #if(n < 13):
        #print("Month " + str(n) + " revenue is :" + str(monthly_revenue))
    cumulative_revenue = monthly_revenue + cumulative_revenue

    if(n == 1):
       cum_revenue = [monthly_revenue]
       mon_revenue = [monthly_revenue]
    else:
        cum_revenue.append(cumulative_revenue)
        mon_revenue.append(monthly_revenue)
print("**********************************************************************")
print("Monthly revenue for the first 12 months is:")
for k in range(0,12):
    print("Month " + str(k+1) +": " + str(mon_revenue[k]))
print("**********************************************************************")
#print("Cumulative revenue for first 12 months is: " + str(cum_revenue[0:12]))
#print(len(cum_revenue))
cum_yearly_revenue = [cum_revenue[11],cum_revenue[23],cum_revenue[35],cum_revenue[47],cum_revenue[59],cum_revenue[71],cum_revenue[83],cum_revenue[95],cum_revenue[107],cum_revenue[119]]
#print("Cumulative yearly revenue for 10 years is: " + str(yearly_revenue))
yearly_revenue = [0,0,0,0,0,0,0,0,0,0]
sum_yearly_revenue = 0
for p in range(0,10):
    yearly_revenue[p] = cum_revenue[12*(p+1)-1] - sum_yearly_revenue
    sum_yearly_revenue = yearly_revenue[p] + sum_yearly_revenue

print("Yearly revenue for the first 10 years is:")
for s in range(0,10):
    print("Year " + str(s+1) +": " + str(yearly_revenue[s]))
print("**********************************************************************")
#print(mon_revenue)
#print(yearly_revenue)
#print(cum_yearly_revenue)
#fig, ax = plt.subplots()
#fruits = ['apple', 'blueberry', 'cherry', 'orange']
#counts = [40, 100, 30, 55]
#ax.bar(fruits,counts)
#plt.show()
# Plot graph for Monthly revenue for the first 12 months
fig, ax = plt.subplots(2,1,figsize=(15,9))
xpoints = (1,2,3,4,5,6,7,8,9,10,11,12)
#print(np.shape(xpoints))
#print(np.shape(cum_revenue[0:12]))

ax[0].bar(xpoints,mon_revenue[0:12], label=xpoints)
ax[0].set_ylabel('Revenue ($) ')
ax[0].set_xlabel('Month')
ax[0].set_title('Monthly Revenue ($)')
txt = 'Setup fee: '+ str(setup_fee) + '\nMonthly fee:' + str(monthly_fee) + '\nNew Customer: ' + str(new_customer) + '\nchurn rate:' + str(churn_rate)
ax[0].text(1,9000,txt,color='red')
rects = ax[0].patches
labels = mon_revenue
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax[0].text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )
#plt.plot(xpoints,cum_revenue[0:12])
#plt.show()

#fig, ax = plt.subplots(2,2,figsize=(12,4))
xpoints = (1,2,3,4,5,6,7,8,9,10)
ax[1].bar(xpoints,yearly_revenue[0:11], label=xpoints)
ax[1].set_ylabel('Revenue ($) ')
ax[1].set_xlabel('Year')
ax[1].set_title('Yearly Revenue ($)')
rects = ax[1].patches
labels = yearly_revenue
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax[1].text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )
#plt.plot(xpoints,cum_revenue[0:12])
plt.show()
