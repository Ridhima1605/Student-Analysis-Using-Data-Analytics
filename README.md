# Student Analysis Using Data Analytics

## Overview
This project focuses on performing **Data Preprocessing** and **Exploratory Data Analysis (EDA)** on a student dataset to gain insights into academic performance. The analysis includes cleaning the data, handling missing values, feature engineering, identifying patterns and trends, and visualizing key findings.

---

## Project Objectives
- Clean and preprocess student data (handle missing values, outliers).
- Perform feature selection and engineering.
- Ensure data integrity and consistency.
- Generate summary statistics and identify trends.
- Create visualizations for better understanding of data relationships.

---

## Dataset
- The dataset consists of 100 student records.
- Key attributes include `StudentID`, `Gender`, `GPA`, `Attendance`, and `StudyHours`.
- Missing values and outliers are present and handled during preprocessing.
- Dataset file: [`data/students.csv`](./data/students.csv)

---

## Folder Structure

student-analysis-eda/
│
├── README.md # Project overview and instructions
├── requirements.txt # Python package dependencies
│
├── data/
│ └── students.csv # Dataset CSV file
│
├── scripts/
│ └── student_eda.py # Python script for preprocessing and EDA
│
├── images/
│ ├── gpa_distribution.png # GPA histogram
│ ├── correlation_heatmap.png # Correlation heatmap
│ └── attendance_vs_gpa.png # Scatter plot Attendance vs GPA
│
├── presentation/
│ └── Student_EDA_Presentation.pdf # Summary slides (optional)
│
└── .gitignore # Git ignore file

yaml
Copy
Edit

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd student-analysis-eda
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running the Analysis
Make sure the dataset is available at data/students.csv.

Run the EDA script:

bash
Copy
Edit
python scripts/student_eda.py
The script will:

Clean and preprocess the data.

Handle missing values and outliers.

Engineer new features.

Generate visualizations saved in images/.

Print key insights to the console.

Key Insights from Analysis
Attendance correlates positively with GPA, indicating students with higher attendance tend to perform better academically.

Most students fall into the 'Medium' performance category based on GPA.

Gender distribution is relatively balanced.

Study hours have a positive impact on student GPA.

election of Appropriate Chart Types for Insights
Choosing the right chart type is essential to effectively communicate the insights derived from student data. Each type of insight calls for a specific visualization that best highlights the underlying patterns, comparisons, or relationships.

1. Comparing Categories: Bar Chart
To compare average grades across different subjects, a Bar Chart is used. This chart type clearly displays the performance in each subject side-by-side, making it easy to identify strong and weak areas.

2. Showing Proportions: Pie Chart
The Pie Chart is ideal for visualizing attendance distribution — showing what portion of the total attendance falls under Present, Absent, or Late categories. This gives a quick overview of attendance status proportions.

3. Exploring Relationships: Scatter Plot
To understand the relationship between attendance percentage and student grades, a Scatter Plot is employed. This chart plots individual student data points and reveals trends or correlations, helping to assess if better attendance is associated with higher grades.

4. Other Chart Types (Optional)
Line Charts could be used to visualize trends over time if attendance or grades are tracked across semesters.

Histograms may show the distribution of grades or attendance frequencies to understand data spread.

Summary Table
Insight Type	Chart Type	Purpose
Comparing categories	Bar Chart	Compare average grades across subjects
Showing proportions	Pie Chart	Visualize attendance distribution
Exploring relationships	Scatter Plot	Identify correlation between attendance & grades
Trends over time	Line Chart	Track changes across semesters (optional)
Frequency distribution	Histogram	Show data distribution patterns

Selecting appropriate chart types not only improves the clarity and impact of visualizations but also helps stakeholders derive actionable insights from student data effectively.

If you want, I can also help you integrate this section neatly into your existing README or presentation slides!









Dependencies
This project requires the following Python libraries:

pandas

numpy

matplotlib

seaborn

scikit-learn

Install them using:

bash
Copy
Edit
pip install -r requirements.txt
Contribution
Feel free to fork the repository and submit pull requests for improvements or additional features.

License
This project is licensed under the MIT License.

Contact
For any questions or support, please contact:

Ridhima Goel
Email: ridhimaxb@gmail.com
LinkedIn: https://www.linkedin.com/in/ridhima-goel-33b495299/










