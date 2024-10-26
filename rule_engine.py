from typing import Optional, List, Dict
from models import RuleRequest, CombineRulesRequest, EvaluationRequest

class Node:
    def _init_(self, type: str, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left
        self.right = right
        self.value = value

def parse_rule_string(rule_string: str) -> Node:
    # Placeholder function to parse a rule string into an AST
    # Ideally, implement a parser that tokenizes and constructs an AST
    return Node("operator", Node("operand", value="age > 30"), Node("operand", value="department = 'Sales'"))

def combine_rules(rule_asts: List[Node]) -> Node:
    # Combines multiple ASTs into a single AST root node with "AND" operator
    combined = Node("operator", type="AND")
    for ast in rule_asts:
        if combined.left is None:
            combined.left = ast
        else:
            combined.right = ast  # Simple example; in practice, handle nested combinations
    return combined

def evaluate_rule(rule_ast: Node, user_data: Dict) -> bool:
    # Recursive function to evaluate the AST based on user data
    if rule_ast.type == "operand":
        # Evaluate the operand (e.g., age > 30)
        # Here, you'd parse rule_ast.value and evaluate it with user_data
        return True  # Placeholder
    elif rule_ast.type == "operator":
        if rule_ast.value == "AND":
            return evaluate_rule(rule_ast.left, user_data) and evaluate_rule(rule_ast.right, user_data)
        elif rule_ast.value == "OR":
            return evaluate_rule(rule_ast.left, user_data) or evaluate_rule(rule_ast.right, user_data)
    return False

      
