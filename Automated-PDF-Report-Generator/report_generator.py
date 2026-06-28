
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image
)
from reportlab.lib.styles import getSampleStyleSheet

# Load data
df = pd.read_csv("data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()
highest_sale = df["Sales"].max()
lowest_sale = df["Sales"].min()

sales_product = df.groupby("Product")["Sales"].sum()
sales_region = df.groupby("Region")["Sales"].sum()
daily = df.groupby("Date")["Sales"].sum()

top_product = sales_product.idxmax()
top_product_sales = sales_product.max()
top_region = sales_region.idxmax()
top_region_sales = sales_region.max()

# Charts
plt.figure(figsize=(7,5))
sales_product.plot(kind="bar")
plt.title("Sales by Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/product_sales.png")
plt.close()

plt.figure(figsize=(7,5))
sales_region.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.savefig("charts/region_sales.png")
plt.close()

plt.figure(figsize=(8,5))
daily.plot(marker="o")
plt.title("Daily Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/daily_sales.png")
plt.close()

styles = getSampleStyleSheet()
pdf = SimpleDocTemplate("reports/Sales_Report.pdf")
story = []

story.append(Paragraph("Sales Performance Report", styles["Title"]))
story.append(Spacer(1,18))

story.append(Paragraph("Executive Summary", styles["Heading1"]))
story.append(Paragraph(
    "This report analyses sales transactions from 1 January 2025 to 20 January 2025. "
    "It summarizes revenue, profit, product performance, regional performance and daily sales trends.",
    styles["BodyText"]))
story.append(Spacer(1,12))

story.append(Paragraph("Key Performance Indicators", styles["Heading1"]))
summary = f"""
<b>Total Sales:</b> ${total_sales:,}<br/>
<b>Total Profit:</b> ${total_profit:,}<br/>
<b>Average Sale:</b> ${average_sales:.2f}<br/>
<b>Highest Sale:</b> ${highest_sale:,}<br/>
<b>Lowest Sale:</b> ${lowest_sale:,}
"""
story.append(Paragraph(summary, styles["BodyText"]))
story.append(Spacer(1,18))

story.append(Paragraph("Sales by Product", styles["Heading1"]))
story.append(Image("charts/product_sales.png", width=420, height=260))
story.append(Paragraph(
    f"The bar chart compares total sales for each product. "
    f"{top_product} generated the highest revenue (${top_product_sales:,}), making it the best-performing product. "
    "Monitors recorded the lowest sales, suggesting opportunities to improve demand through pricing or marketing.",
    styles["BodyText"]))
story.append(Spacer(1,18))

story.append(Paragraph("Sales by Region", styles["Heading1"]))
story.append(Image("charts/region_sales.png", width=420, height=260))
story.append(Paragraph(
    f"The regional distribution shows that the {top_region} region contributed the largest share of sales "
    f"(${top_region_sales:,}). Other regions contributed smaller but relatively balanced portions of revenue, "
    "indicating that sales are spread across multiple markets.",
    styles["BodyText"]))
story.append(Spacer(1,18))

story.append(Paragraph("Daily Sales Trend", styles["Heading1"]))
story.append(Image("charts/daily_sales.png", width=420, height=260))
story.append(Paragraph(
    "Daily sales generally trend upward across the reporting period, despite small day-to-day fluctuations. "
    "The final days record the highest sales values, suggesting improving business performance over time.",
    styles["BodyText"]))
story.append(Spacer(1,18))

story.append(Paragraph("Business Insights", styles["Heading1"]))
story.append(Paragraph(
    f"""
    • Focus inventory on <b>{top_product}</b>, the strongest-selling product.<br/>
    • Maintain investment in the <b>{top_region}</b> region while exploring growth opportunities elsewhere.<br/>
    • Monitor lower-performing products to identify pricing or promotional improvements.<br/>
    • Continue tracking daily sales to identify seasonal patterns and support forecasting.
    """, styles["BodyText"]))
story.append(Spacer(1,18))

story.append(Paragraph("Conclusion", styles["Heading1"]))
story.append(Paragraph(
    "Overall, the business demonstrated healthy sales and profitability during the reporting period. "
    "The charts and KPIs indicate strong product performance, balanced regional contributions, "
    "and an encouraging upward sales trend that can support future strategic planning.",
    styles["BodyText"]))

pdf.build(story)
print("Report Generated Successfully!")
