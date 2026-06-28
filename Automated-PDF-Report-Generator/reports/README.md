# Automated PDF Report Generator

A Python automation project that transforms raw CSV sales data into a professional PDF business report. The application performs automated data analysis using Pandas, generates visualizations with Matplotlib, and compiles a polished multi-page PDF using ReportLab.

This project demonstrates how repetitive business reporting can be automated with Python, reducing manual effort while producing consistent, presentation-ready reports.

---

## Features

* Reads sales data from a CSV file
* Cleans and prepares data using Pandas
* Calculates key business metrics

  * Total Sales
  * Total Profit
  * Average Sale
  * Highest Sale
  * Lowest Sale
* Groups sales by product and region
* Generates professional charts using Matplotlib
* Creates a formatted PDF report with ReportLab
* Fully automated report generation from a single Python script

---

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* ReportLab

---

## Project Structure

```text
Automated-PDF-Report-Generator/
│
├── data/
│   └── sales_data.csv
│
├── charts/
│   ├── product_sales.png
│   ├── region_sales.png
│   └── daily_sales.png
│
├── reports/
│   └── Sales_Report.pdf
│
├── report_generator.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/Automated-PDF-Report-Generator.git
```

Move into the project folder.

```bash
cd Automated-PDF-Report-Generator
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the report generator.

```bash
python report_generator.py
```

After execution, the script will:

* Load the CSV dataset
* Analyze sales data
* Generate charts
* Create a formatted PDF report
* Save all outputs automatically

---

## Generated Outputs

### Charts

* Product Sales Bar Chart
* Regional Sales Pie Chart
* Daily Sales Trend Line Chart

### PDF Report

The generated report contains:

* Executive summary
* Sales statistics
* Profit analysis
* Business visualizations
* Professional formatting suitable for sharing or printing

---

## Sample Dataset

The project uses a CSV dataset containing:

* Date
* Product
* Region
* Sales
* Profit

The dataset can easily be replaced with any similarly structured sales data.

---

## Screenshots

Add screenshots to the `screenshots/` folder and display them here.

### Application

```
screenshots/application.png
```

### Generated Charts

```
screenshots/charts.png
```

### Generated PDF

```
screenshots/pdf_report.png
```

### Terminal Output

```
screenshots/terminal.png
```

---

## Skills Demonstrated

* Python scripting
* Data analysis
* Data aggregation
* File automation
* CSV processing
* Business reporting
* Data visualization
* PDF document generation
* Report automation
* Workflow optimization

---

## Business Value

This project automates a reporting process that would traditionally require manually analyzing spreadsheets, creating charts, and formatting reports. By integrating data analysis, visualization, and document generation into a single workflow, the application produces consistent reports in seconds and significantly reduces repetitive manual work.

---

## Future Improvements

* Company branding and logos
* Interactive charts
* Excel input support
* Automatic email delivery
* Scheduled report generation
* Multiple report templates
* Dashboard integration
* Command-line arguments
* Database connectivity
* Cloud deployment

---

## Author

Developed as a portfolio project demonstrating Python automation, data analysis, reporting, and business process automation.
