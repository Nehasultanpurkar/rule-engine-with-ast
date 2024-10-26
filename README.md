This project is a rule engine application that evaluates user eligibility based on customizable conditions such as age, department, income, and experience. 
It represents rules using an Abstract Syntax Tree (AST), allowing for dynamic rule creation, combination, and evaluation.

Features:
Dynamic Rule Creation: Parse rule strings into ASTs for flexible rule representation.
Rule Combination: Combine multiple rules efficiently into a single AST.
Rule Evaluation: Evaluate rules against user data to determine eligibility.
Error Handling: Validates rule structures and provides informative error messages.\

Tech Stack
Backend: Python, FastAPI
Database: PostgreSQL (or MongoDB if preferred for flexibility)
Deployment: Uvicorn for ASGI server
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
2. Create a Virtual Environment
Set up a virtual environment to manage dependencies:
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install Dependencies
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
astapi
uvicorn
psycopg2  # For PostgreSQL connection
4. Database Setup
PostgreSQL
Install PostgreSQL if you haven’t already:

bash
Copy code
sudo apt update
sudo apt install postgresql
Create a Database:

sql
Copy code
CREATE DATABASE rule_engine;
CREATE USER rule_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE rule_engine TO rule_user;
Define Database Schema:

sql
Copy code
CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_name VARCHAR(255) NOT NULL,
    rule_string TEXT NOT NULL,
    ast JSONB NOT NULL
);
CREATE TABLE attributes (
    id SERIAL PRIMARY KEY,
    attribute_name VARCHAR(255) UNIQUE NOT NULL,
    attribute_type VARCHAR(50) NOT NULL  -- e.g., 'string', 'number'
);
Configure Database Connection: Update database.py to connect to PostgreSQL with the created user and database.

5. Running the Application
Start the FastAPI application using Uvicorn
FastAPI Docs: Access interactive documentation at http://127.0.0.1:8000/docs.
API Root: http://127.0.0.1:8000.
API Endpoints
1. Create Rule (POST /create_rule)
Parses a rule string and generates the corresponding AST.

Request Body
json
Copy code
{
  "rule_string": "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')"
}
response:
{
  "ast": {
    "type": "operator",
    "value": "OR",
    "left": {
      "type": "operator",
      "value": "AND",
      "left": {"type": "operand", "value": "age > 30"},
      "right": {"type": "operand", "value": "department = 'Sales'"}
    },
    "right": {
      "type": "operator",
      "value": "AND",
      "left": {"type": "operand", "value": "age < 25"},
      "right": {"type": "operand", "value": "department = 'Marketing'"}
    }
  }
}
Combine Rules (POST /combine_rules)
Combines multiple ASTs into a single rule, typically with an "AND" operator.

Request Body
json
Copy code
{
  "rules": [
    "(age > 30 AND department = 'Sales')",
    "(salary > 50000 OR experience > 5)"
  ]
}
response:
{
  "combined_ast": {
    "type": "operator",
    "value": "AND",
    "left": { ... },
    "right": { ... }
  }
}
3. Evaluate Rule (POST /evaluate_rule)
Evaluates the provided rule AST against user data.

Request Body
{
  "rule_ast": {
    "type": "operator",
    "value": "AND",
    "left": {"type": "operand", "value": "age > 30"},
    "right": {"type": "operand", "value": "department = 'Sales'"}
  },
  "user_data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
  }
}
response:
{
"result": true
}
Testing
Use pytest for testing. Run tests with:

bash
Copy code
pytest
Sample Tests (test_rules.py)

Test AST Creation: Verify if create_rule parses rule strings accurately.
Test Rule Combination: Check if combine_rules merges ASTs correctly.
Test Rule Evaluation: Evaluate sample data against rules to confirm functionality.
Additional Notes
Error Handling: The API validates input rules, catches syntax errors, and returns descriptive error messages.
Attribute Validation: Extend the system to validate attributes used in rules against a catalog to prevent invalid entries.
Future Enhancements

User-Defined Functions: Allow functions like isSenior(age) for advanced conditions.
AST Modification: Enable rule modification by updating the AST structure dynamically.
Caching: Implement caching for frequently used rules to improve performance
