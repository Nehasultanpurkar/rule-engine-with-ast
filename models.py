from pydantic import BaseModel
from typing import Optional, List

# Request model for rule creation
class RuleRequest(BaseModel):
    rule_string: str

# Request model for combining multiple rules
class CombineRulesRequest(BaseModel):
    rules: List[str]

# Request model for rule evaluation
class EvaluationRequest(BaseModel):
    rule_ast: dict  # AST represented as JSON
    user_data: dict  # User data for evaluation
