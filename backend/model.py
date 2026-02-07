import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv('../data/LoanApprovalPrediction.csv')

# Drop ID column
df.drop('Loan_ID', axis=1, inplace=True)

# Encode categorical columns
cat_cols = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
encoder = LabelEncoder()

for col in cat_cols:
    df[col] = encoder.fit_transform(df[col].astype(str))

# Convert Dependents (3+ → 3)
df['Dependents'] = df['Dependents'].replace('3+', 3).astype(float)

# Target encoding
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# Handle missing values
imputer = SimpleImputer(strategy='median')
df[:] = imputer.fit_transform(df)

# Split features & target
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# Train model in memory
loan_model = RandomForestClassifier(random_state=42)
loan_model.fit(X, y)

feature_columns = X.columns.tolist()
