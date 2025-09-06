# AIML Projects Repository

## Overview
This repository contains a collection of AI/ML projects focused on solving real-world business problems using data science and machine learning techniques. Each project demonstrates end-to-end implementation from data exploration to model deployment insights.

## Projects

### [Churn Risk Intelligence](./projects/churn-risk-intelligence/)
**Customer Churn Prediction & Retention Analytics**
- **Objective**: Predict customer churn to enable proactive retention strategies
- **Dataset**: Telco Customer Churn (Kaggle)
- **Techniques**: Logistic Regression, KNN, SMOTE for class imbalance
- **Key Results**: 82% accuracy with Logistic Regression, 81% recall with SMOTE-enhanced KNN
- **Business Impact**: Identifies high-risk customers for targeted retention campaigns

### [Bank Term Deposit Prediction](./projects/bank-term-deposit-prediction/)
**Marketing Campaign Effectiveness & Customer Targeting**
- **Objective**: Predict customer subscription to term deposits for optimized marketing campaigns
- **Dataset**: Bank Marketing Campaign Data (UCI Repository)
- **Techniques**: Naive Bayes, Decision Trees (Gini & Entropy), Feature Engineering
- **Key Results**: 88-92% accuracy with Decision Trees, comprehensive EDA insights
- **Business Impact**: Optimizes marketing spend by targeting high-probability prospects

## Technologies Used
- **Languages**: Python
- **Libraries**: 
  - Data Analysis: Pandas, NumPy
  - Visualization: Matplotlib, Seaborn
  - Machine Learning: Scikit-learn, Imblearn
  - Statistical Analysis: SciPy
  - Model Persistence: Joblib
- **Tools**: Jupyter Notebooks, Google Colab, Git

## Repository Structure
```
AIML_projects/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py                    # Portfolio orchestrator
├── projects/
│   ├── churn-risk-intelligence/
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── data/
│   │   ├── models/
│   │   └── results/
│   └── bank-term-deposit-prediction/
│       ├── src/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── data_processing.py
│       │   ├── feature_engineering.py
│       │   ├── model_training.py
│       │   ├── evaluation.py
│       │   └── main.py
│       ├── data/
│       ├── models/
│       ├── results/
│       ├── requirements.txt
│       └── README.md
└── shared_utils/
    └── common_functions.py
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/AIML_projects.git
cd AIML_projects
```

2. Create a virtual environment:
```bash
python -m venv aiml_env
source aiml_env/bin/activate  # On Windows: aiml_env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Portfolio-Wide Execution
Run the main portfolio orchestrator to see all projects:
```bash
python main.py
```

Interactive mode for project selection:
```bash
python main.py --interactive
```

Run a specific project:
```bash
python main.py --project bank-term-deposit-prediction
python main.py --project churn-risk-intelligence
```

### Individual Projects
Navigate to individual project directories for specific setup and usage instructions. Each project contains:
- Detailed README with project overview
- Complete analysis and implementation
- Requirements and setup instructions
- Results and key findings

## Project Highlights

### Churn Risk Intelligence
- Addresses customer retention in telecommunications
- Implements class balancing techniques for imbalanced datasets
- Provides actionable insights for business stakeholders

### Bank Term Deposit Prediction
- Tackles marketing optimization in financial services
- Features comprehensive EDA and feature engineering
- Demonstrates modular, production-ready code architecture

## Contributing
This is a personal learning repository, but feedback and suggestions are welcome! Feel free to:
- Open issues for discussions
- Suggest improvements
- Share similar projects or resources

## Future Projects
- [ ] NLP Sentiment Analysis
- [ ] Computer Vision Image Classification
- [ ] Time Series Forecasting
- [ ] Recommendation System
- [ ] Deep Learning with Neural Networks
- [ ] A/B Testing Framework
- [ ] MLOps Pipeline Implementation

## Contact
Alireza Barzin Zanganeh
- LinkedIn: linkedin.com/in/alireza-barzin-zanganeh-2a9909126
- Email: alireza@zanganehai.com
- Portfolio: https://www.zanganehai.com

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Latest Update**: Added Bank Term Deposit Prediction project with modular architecture and comprehensive evaluation framework.