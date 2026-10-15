# 🎓 Learner Demographics and Course Enrollment Behavior Analysis on EduPro

## 📌 Project Overview

This project analyzes learner demographics and course enrollment behavior on the EduPro online learning platform to understand participation patterns, course preferences, and enrollment activity.

The analysis focuses on age and gender distributions, course category popularity, course type and level preferences, and differences in enrollment behavior across learner groups.

An interactive **Streamlit dashboard** was developed to help users explore learner demographics and course enrollment patterns through dynamic filters, charts, and summary metrics.

The project aims to provide descriptive insights that can support educational planning and data-driven decision-making.

---

## 🎯 Project Objectives

The project aims to answer the following questions:

- What is the demographic distribution of learners by age and gender?
- Which age groups contribute the most course enrollments?
- Which course categories are most popular?
- Do course category preferences differ by gender?
- How do course type and course level preferences vary across learner groups?
- How do enrollment patterns differ across age groups?
- How many courses does a learner typically enroll in?
- How does enrollment activity vary across learners?

---

## 📊 Key Analyses

### 1. Learner Demographic Analysis

Examines learner participation by age and gender to understand the demographic composition of the platform.

### 2. Age-Wise Enrollment Analysis

Analyzes enrollment counts and percentages across age groups to identify groups contributing the largest share of enrollments.

### 3. Course Category Popularity

Identifies popular course categories based on enrollment activity and compares their relative participation.

### 4. Course Type and Level Preferences

Examines enrollment patterns across course types, including Free and Paid, and course levels, including Beginner, Intermediate, and Advanced.

### 5. Gender-Based Course Preferences

Compares course category and course level enrollment patterns across gender groups to identify differences in observed participation.

### 6. Age Group and Course Preferences

Uses cross-tabulation and heatmap visualizations to examine relationships between age groups, course categories, and course levels.

### 7. Learner Enrollment Behavior

Analyzes the number of course enrollments associated with each learner and groups learners into enrollment activity segments.

---

## 📈 Interactive Streamlit Dashboard

The dashboard was developed using **Streamlit** to present the analysis through interactive visualizations, summary metrics, and data filters.

### Dashboard Filters

- Age group
- Gender
- Course category
- Course level

These filters allow users to explore enrollment patterns for selected learner groups and course characteristics.

---

## 📊 Dashboard Modules

### 👥 Learner Demographic Overview

Displays key metrics, including unique learners, total enrollments, average enrollments per learner, and gender participation.

### 📅 Age-Wise Enrollment Analysis

Visualizes enrollment counts and percentages across age groups.

### 📚 Course Category Popularity

Highlights popular course categories based on enrollment records.

### 🎯 Course Type and Level Preferences

Compares enrollment patterns across course types and course difficulty levels.

### ⚖️ Gender-Based Course Preferences

Explores course category and course level participation across gender groups.

### 🔥 Age Group and Course Preferences

Uses heatmaps and related visualizations to compare course preferences across age groups.

### 📈 Learner Enrollment Behavior

Examines the distribution of enrollments per learner and groups learners by enrollment activity.

### 🔎 Interactive Filters and Filtered Data

Enables users to filter the dataset and inspect the corresponding records and visualizations.

---

## 🛠️ Technologies Used

- **Python** – Data analysis and processing
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Streamlit** – Interactive dashboard development
- **Jupyter Notebook** – Exploratory data analysis
- **Visual Studio Code** – Development environment
- **Git** – Version control
- **GitHub** – Source code hosting

---

## 📁 Project Structure

```text
EduPro-Learner-Analysis/
│
├── Data/
│   ├── EduPro Online Platform.xlsx - Users.csv
│   ├── EduPro Online Platform.xlsx - Courses.csv
│   ├── EduPro Online Platform.xlsx - Transactions.csv
│   └── edupro_dashboard_data.csv
│
├── Notebooks/
│   └── EduPro_Learner_Demographics_Analysis.ipynb
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

## 📂 Dataset Description

The project uses three source datasets representing learners, courses, and enrollment transactions.

### Users Dataset

Contains learner demographic information:

- `UserID` – Unique learner identifier
- `UserName` – Learner name
- `Age` – Learner age
- `Gender` – Learner gender

### Courses Dataset

Contains course information:

- `CourseID` – Unique course identifier
- `CourseName` – Course name
- `CourseCategory` – Course category
- `CourseType` – Course type, such as Free or Paid
- `CourseLevel` – Course difficulty level

### Transactions Dataset

Contains enrollment transaction information:

- `TransactionID` – Unique transaction identifier
- `UserID` – Learner associated with the transaction
- `CourseID` – Course associated with the transaction
- `TransactionDate` – Enrollment transaction date

### Processed Dashboard Dataset

The `edupro_dashboard_data.csv` file contains processed data used by the dashboard, where applicable.

---

## 🧹 Data Preparation

The analytical workflow includes:

- Loading the source CSV files using Pandas
- Inspecting dataset structure and data types
- Preparing learner demographic information
- Combining transaction data with learner and course information
- Categorizing learners into age groups
- Calculating enrollment counts and percentages
- Comparing enrollment patterns across gender groups
- Analyzing course category, type, and level preferences
- Calculating enrollment activity per learner
- Preparing data for dashboard visualizations

The Jupyter notebook contains the exploratory analysis, while the Streamlit application presents the interactive dashboard.

---

## 📐 Key Analytical Metrics

### Unique Learners

The number of distinct learners represented in the dataset.

### Total Enrollments

The total number of enrollment transaction records included in the analysis.

### Average Enrollments per Learner

Calculated by dividing the total enrollment records by the number of unique learners.

### Age-Wise Enrollment Share

Measures the percentage of total enrollments associated with each age group.

### Course Category Popularity

Measures enrollment activity across different course categories.

### Gender-Based Course Participation

Compares enrollment patterns across gender groups and course characteristics.

### Learner Enrollment Activity

Measures the number of enrollments associated with each learner and supports grouping learners by enrollment frequency.

---

## 🚀 Running the Dashboard Locally

### 1. Open the Project Directory

Open the `EduPro-Learner-Analysis` folder in Visual Studio Code.

### 2. Install Required Packages

Open the terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit Application

Run the following command:

```bash
streamlit run app.py
```

### 4. Open the Dashboard

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

The dashboard should open in your web browser.

---

## 📓 Analysis Notebook

The Jupyter notebook is located in the `Notebooks/` directory.

It contains the exploratory data analysis and supporting calculations used to understand learner demographics and course enrollment behavior.

The notebook and Streamlit application serve complementary purposes: the notebook documents the analysis workflow, while the dashboard makes the findings easier to explore interactively.

---

## 📦 Dashboard Data Files

The `Data/` directory contains the source and processed CSV files used by the project.

- **Users CSV:** Learner demographic information.
- **Courses CSV:** Course details and classifications.
- **Transactions CSV:** Enrollment transaction records.
- **Dashboard CSV:** Processed data used by the dashboard, where applicable.

---

## 💡 Practical Applications

The findings may help educational stakeholders:

- Understand which learner groups contribute most to enrollment activity.
- Identify popular course categories.
- Compare participation patterns across demographic groups.
- Review enrollment patterns across course types and levels.
- Support course planning and learner engagement discussions.
- Make informed decisions using descriptive data analysis.

These applications are intended to support planning. Observed associations do not necessarily establish causation.

---

## 🌐 Dashboard Deployment

The interactive dashboard is built using **Streamlit** and can be published through Streamlit Community Cloud.

**Live Dashboard:** https://edupro-learner-analysis-gk.streamlit.app/

---

## 🔗 GitHub Repository

The GitHub repository will contain the project source code, analysis notebook, dataset files where appropriate, dependencies, and documentation.

**Repository URL:** https://github.com/ModiGurpreetkaurJaykumar/EduPro-Learner-Analysis

---

## 📝 Conclusion

The EduPro project provides a structured analysis of learner demographics and course enrollment behavior using Python, Pandas, and interactive visualization.

By combining demographic analysis, course category popularity, course preferences, and learner enrollment activity, the project makes it easier to explore participation patterns across different learner groups.

The Streamlit dashboard provides an interactive interface for examining these patterns and supports evidence-based discussions about educational planning and learner engagement.

---

## 👤 Project Type

**Data Analytics / Exploratory Data Analysis Project**

**Project Title:** Learner Demographics and Course Enrollment Behavior Analysis on EduPro