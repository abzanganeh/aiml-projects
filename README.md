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

## Technologies Used
- **Languages**: Python
- **Libraries**: 
  - Data Analysis: Pandas, NumPy
  - Visualization: Matplotlib, Seaborn
  - Machine Learning: Scikit-learn, Imblearn
  - Statistical Analysis: SciPy
- **Tools**: Jupyter Notebooks, Google Colab, Git

## Repository Structure
```
AIML_projects/
├── README.md
├── requirements.txt
├── .gitignore
├── projects/
│   └── churn-risk-intelligence/
│       ├── notebook.ipynb
│       ├── README.md
│       ├── data/
│       ├── models/
│       └── results/
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
Navigate to individual project directories for specific setup and usage instructions. Each project contains:
- Detailed README with project overview
- Jupyter notebook with complete analysis
- Requirements and setup instructions
- Results and key findings

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

## Contact
Alireza Barzin Zanganeh
- LinkedIn: linkedin.com/in/alireza-barzin-zanganeh-2a9909126
- Email: alireza@zanganehai.com
- Portfolio: https://www.zanganehai.com

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

