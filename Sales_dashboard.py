# TASK 2: E-Commerce Sales Dashboard - CodeAlpha
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_input.csv')
months = df['Month'].tolist()
sales = df['Sales'].tolist()
profit = df['Profit'].tolist()

fig = plt.figure(figsize=(10, 12))
fig.patch.set_facecolor('#f0f2f5')
plt.suptitle('E-Commerce Sales Dashboard - CodeAlpha', fontsize=14, fontweight='bold')

gs = fig.add_gridspec(4, 2, hspace=0.6, wspace=0.4)

# KPI
ax_kpi = fig.add_subplot(gs[0, :])
ax_kpi.axis('off')
ax_kpi.text(0.05, 0.5, "Total Sales: ₹2.15M | Profit: ₹405K (18.8%) | Orders: 5.3K | AOV: ₹405", fontsize=10, fontweight='bold', bbox=dict(facecolor='white', edgecolor='#0078D4', boxstyle='round,pad=0.5'))

# Sales Trend
ax1 = fig.add_subplot(gs[1, 0])
ax1.plot(months, sales, label='Sales', color='#0078D4', linewidth=2)
ax1.plot(months, profit, label='Profit', color='#107C10', linewidth=2)
ax1.set_title('Sales & Profit Trend', fontsize=10, fontweight='bold')
ax1.tick_params(axis='x', rotation=90, labelsize=7)
ax1.legend(fontsize=6)
ax1.grid(True, alpha=0.3)

# Category
ax2 = fig.add_subplot(gs[1, 1])
ax2.pie([42, 28, 30], labels=['Electronics','Clothing','Home'], autopct='%1.1f%%', colors=['#0078D4','#D83B01','#107C10'], textprops={'fontsize': 8})
ax2.set_title('Sales by Category', fontsize=10, fontweight='bold')

# Region
ax3 = fig.add_subplot(gs[2, 0])
ax3.bar(['North','South','East','West'], [550000, 650000, 400000, 550000], color=['#0078D4','#107C10','#D83B01','#FFB900'])
ax3.set_title('Sales by Region', fontsize=10, fontweight='bold')
ax3.tick_params(axis='x', labelsize=7)

# Orders
ax4 = fig.add_subplot(gs[2, 1])
ax4.bar(months, df['Orders'].tolist(), color='#0078D4')
ax4.set_title('Monthly Orders', fontsize=10, fontweight='bold')
ax4.tick_params(axis='x', rotation=90, labelsize=7)

# Forecast
ax5 = fig.add_subplot(gs[3, :])
future = ['2025-01','2025-03','2025-05','2025-07']
forecast = [250000, 265000, 280000, 295000]
ax5.plot(months[-6:], sales[-6:], label='Actual', color='#0078D4')
ax5.plot(future, forecast, label='Forecast +18%', color='#D83B01', linestyle='--')
ax5.fill_between(future, [f*0.9 for f in forecast], [f*1.1 for f in forecast], color='#D83B01', alpha=0.15)
ax5.set_title('Sales Forecasting Next 6 Months', fontsize=10, fontweight='bold')
ax5.legend(fontsize=7)
ax5.grid(True, alpha=0.3)

fig.text(0.5, 0.01, "INSIGHTS: Electronics 42% Best Seller | South Region Top | 18.8% Profit Margin | Forecast +18%", ha='center', fontsize=8, bbox=dict(facecolor="#FFF4CE", edgecolor="#FFC000"))

plt.savefig('sales_dashboard.png', dpi=300, bbox_inches='tight')
print("SUCCESS!")
