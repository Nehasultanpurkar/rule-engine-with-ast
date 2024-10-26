from fastapi import FastAPI, HTTPException
from models import RuleRequest, CombineRulesRequest, EvaluationRequest
from rule_engine import parse_rule_string, combine_rules, evaluate_rule

app = FastAPI()

# Endpoint to create a rule
@app.post("/create_rule")
def create_rule(request: RuleRequest):
    try:
        rule_ast = parse_rule_string(request.rule_string)
        return {"ast": rule_ast._dict_}  # Convert Node to dictionary for JSON response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to combine multiple rules
@app.post("/combine_rules")
def combine_rules_endpoint(request: CombineRulesRequest):
    try:
        rule_asts = [parse_rule_string(rule) for rule in request.rules]
        combined_ast = combine_rules(rule_asts)
        return {"combined_ast": combined_ast._dict_}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to evaluate a rule against user data
@app.post("/evaluate_rule")
def evaluate_rule_endpoint(request: EvaluationRequest):
    try:
        result = evaluate_rule(Node(**request.rule_ast), request.user_data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

   
