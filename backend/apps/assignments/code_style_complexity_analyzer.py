"""
EduCore Framework - Automated Code Style & Complexity Analyzer

A helper module for grading programming assignments by verifying code complexity metrics:
- Indentation depth analysis
- Line counts and method length capping
- Cyclomatic complexity estimates
- Simple static token metrics
"""

import re
from typing import Dict, List, Any

class CodeStyleComplexityAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lines: List[str] = []
        self.load_file()

    def load_file(self) -> None:
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.lines = f.readlines()
        except IOError:
            self.lines = []

    def compute_indentation_metrics(self) -> Dict[str, Any]:
        """
        Analyzes indentation depth to estimate nested loop and condition density.
        """
        max_depth = 0
        excessive_nested_count = 0
        
        for line in self.lines:
            stripped = line.lstrip()
            if not stripped:
                continue
                
            leading_spaces = len(line) - len(stripped)
            depth = leading_spaces // 4  # Assuming standard 4-space indent
            
            if depth > max_depth:
                max_depth = depth
            if depth >= 4:
                excessive_nested_count += 1
                
        return {
            "max_indentation_depth": max_depth,
            "excessive_nesting_lines_count": excessive_nested_count,
            "has_indentation_issues": max_depth > 6
        }

    def find_functions_or_classes(self) -> List[Dict[str, Any]]:
        """
        Identifies class and function/method declarations and calculates their line spans.
        """
        declarations: List[Dict[str, Any]] = []
        
        current_name = None
        current_type = None
        start_line = 0
        
        for i, line in enumerate(self.lines):
            class_match = re.match(r"^\s*class\s+(\w+)", line)
            def_match = re.match(r"^\s*def\s+(\w+)", line)
            
            if class_match:
                if current_name:
                    declarations.append({
                        "name": current_name,
                        "type": current_type,
                        "start_line": start_line,
                        "end_line": i
                    })
                current_name = class_match.group(1)
                current_type = "CLASS"
                start_line = i + 1
            elif def_match:
                if current_name:
                    declarations.append({
                        "name": current_name,
                        "type": current_type,
                        "start_line": start_line,
                        "end_line": i
                    })
                current_name = def_match.group(1)
                current_type = "FUNCTION"
                start_line = i + 1
                
        if current_name:
            declarations.append({
                "name": current_name,
                "type": current_type,
                "start_line": start_line,
                "end_line": len(self.lines)
            })
            
        return declarations

    def analyze_cyclomatic_complexity_approximation(self) -> Dict[str, Any]:
        """
        Approximates cyclomatic complexity based on conditional branch tokens:
        if, elif, for, while, and, or, except.
        """
        complexity = 1  # Base complexity
        branch_tokens = ["if ", "elif ", "for ", "while ", " except ", " and ", " or "]
        
        for line in self.lines:
            stripped = line.strip()
            # Ignore comments
            if stripped.startswith("#"):
                continue
                
            for token in branch_tokens:
                complexity += len(re.findall(re.escape(token), line))
                
        return {
            "estimated_cyclomatic_complexity": complexity,
            "complexity_level": "HIGH" if complexity > 10 else ("MEDIUM" if complexity > 5 else "LOW")
        }
