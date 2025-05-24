Prerequisites
Python 3.x installed on your system

Git installed (to clone repo)

Recommended: virtual environment tool (venv)

Steps
1. Clone the repository
bash
Copy
Edit
git clone <your-repo-url>
cd student-analysis-eda
2. Create and activate a virtual environment (optional but recommended)
Linux/macOS:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Verify dataset
Ensure students.csv exists in the data/ directory.

5. Run the analysis script
bash
Copy
Edit
python scripts/student_eda.py
6. Review outputs
Visualizations saved in images/

Insights printed to console

