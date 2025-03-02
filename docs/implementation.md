# Implementation Steps

## Step 1: Data Collection (One-time Fetch)
- Fetch the latest USCIS public data on H1B applications.
- Store the raw dataset in the data/raw/ directory.

## Step 2: Data Cleaning & Transformation
- Load the dataset (Employer Information 2024.xlsx).
- Perform missing value imputation.
- Standardize column names for consistency.
- Convert categorical columns to appropriate formats.
- Store cleaned data in data/processed/.

## Step 3: Exploratory Data Analysis (EDA)
### Analyze:
- Top companies applying for H1B visas.
- Approval vs. denial rates by employer and state.
- Industry distribution of H1B petitions.
- Trends in initial vs. continuing approvals.
- Geographic distribution of applications.
- Visualize trends using matplotlib, seaborn, or plotly.

## Step 4: AWS Data Pipeline Setup
- AWS S3: Store cleaned datasets for analysis.
- AWS Glue: Automate ETL (Extract, Transform, Load) process.
- AWS Athena: Query data directly from S3 using SQL.

## Step 5: Dashboard Development
- Create a Streamlit/Flask dashboard to visualize:
- Approval and denial trends.
- Top employers filing H1B applications.
- Industry-wise approval rates.
- State-wise H1B petition trends.
- Deploy the dashboard on AWS Lambda & API Gateway.

## Step 6: Deployment
- Use Docker to containerize the project.
- Deploy on AWS ECS/Fargate for scalability.
- Automate deployment using AWS CodePipeline.

