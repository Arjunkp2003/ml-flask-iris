cat > README.md <<EOL
# ML Flask Iris Project

A full-stack **Machine Learning Flask project** using the **Iris dataset**, featuring:  

- User **login/register** system with SQLite  
- ML **prediction of Iris flower type**  
- **Preprocessing, training, evaluation** scripts  
- **Flask web interface** for predictions  
- **GitHub Actions CI/CD** to automate preprocessing, training, evaluation, and testing  

---

## Project Structure
\`\`\`
ml-flask-iris/
├── src/
│   ├── app.py                  # Flask app entry point
│   ├── ml/
│   │   ├── preprocess.py       # Dataset preprocessing
│   │   ├── train.py            # Train ML model
│   │   ├── evaluate.py         # Evaluate model
│   │   ├── predict.py          # Prediction logic
│   │   └── model.pkl           # Trained model
│   ├── routes/
│   │   ├── auth_routes.py      # Login/register routes
│   │   └── predict_routes.py   # Prediction routes
│   ├── db/
│   │   ├── database.py         # SQLite DB connection
│   │   └── users.db            # Users database
│   └── config.py               # App configuration
├── templates/                  # HTML templates
├── static/                     # CSS/JS
├── tests/                      # Test scripts for CI
├── requirements.txt            # Python dependencies
└── .github/workflows/ci.yml    # GitHub Actions CI/CD pipeline
\`\`\`

---

## Features
- **User Authentication:** Login, register, logout using SQLite  
- **ML Pipeline:** Preprocessing, training, evaluation, and prediction of Iris flower classes  
- **Web Interface:**  
  - \`/register\` → Create an account  
  - \`/login\` → Login  
  - \`/predict\` → Make predictions after login  
- **CI/CD with GitHub Actions:**  
  - Runs preprocessing, training, evaluation, and tests automatically  
  - Checks model file exists (\`model.pkl\`)  
  - Validates Flask routes  

---

## Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/<username>/ml-flask-iris.git
cd ml-flask-iris
\`\`\`

2. Create a virtual environment:
\`\`\`bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Usage

1. **Preprocess data**
\`\`\`bash
python src/ml/preprocess.py
\`\`\`

2. **Train the ML model**
\`\`\`bash
python src/ml/train.py
\`\`\`

3. **Evaluate the ML model**
\`\`\`bash
python src/ml/evaluate.py
\`\`\`

4. **Run the Flask app**
\`\`\`bash
python src/app.py
\`\`\`

5. Open browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)  
   - Register a new account → Login → Go to \`/predict\` → Enter features → Get Iris class  

---

## Iris Dataset Features
- Sepal Length (cm)  
- Sepal Width (cm)  
- Petal Length (cm)  
- Petal Width (cm)  

**Target Classes:**
- \`0\` → setosa  
- \`1\` → versicolor  
- \`2\` → virginica  

---

## Testing

- Tests for ML pipeline and Flask routes are in \`tests/\`.  
- Run tests locally:
\`\`\`bash
pytest tests/
\`\`\`

- Tests are also automatically run via GitHub Actions CI/CD.

---

## GitHub Actions CI/CD

- Workflow file: \`.github/workflows/ci.yml\`  
- Automatically runs on every push or pull request to \`main\`:  
  1. Installs dependencies  
  2. Initializes SQLite DB  
  3. Preprocesses data  
  4. Trains and evaluates the ML model  
  5. Runs tests  
  6. Checks \`model.pkl\` exists  

---

## Dependencies
- Python 3.10+  
- Flask  
- Pandas  
- scikit-learn  
- joblib  
- pytest (for testing)  

---

## Author
Arjun K P
EOL
