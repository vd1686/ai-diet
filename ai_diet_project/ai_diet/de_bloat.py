import ast
from pathlib import Path
from collections import defaultdict

def scan_for_ai_bloat(directory_path: str):
    """Scans a folder of Python files to find structural logic duplicated by AI tools."""
    dir_path = Path(directory_path)
    if not dir_path.exists():
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Dictionary format: {unparsed_body_string: [(file_name, function_name)]}
    function_registry = defaultdict(list)
    
    # Locate all python scripts in target folder
    for file_path in dir_path.glob("*.py"):
        try:
            file_content = file_path.read_text(encoding="utf-8")
            tree = ast.parse(file_content)
            
            # Walk down the logical structure tree of the file
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Unparse converts structural blocks back to plain text strings 
                    # to reliably evaluate matching shapes
                    function_body = ast.unparse(node.body)
                    function_registry[function_body].append((file_path.name, node.name))
        except Exception:
            continue # Quietly skip files with syntax breaks
            
    print("\nAI-DIET DE-BLOAT REPORT")
    print("-" * 25)
    
    bloat_counter = 0
    
    for body, locations in function_registry.items():
        if len(locations) > 1:
            bloat_counter += 1
            print(f"\nDuplicate Logic Pattern #{bloat_counter}:")
            for file_name, func_name in locations:
                print(f"  File: {file_name} -> def {func_name}()")
                
    if bloat_counter == 0:
        print("\nNo repeating code bloat discovered.")
    print("-" * 25 + "\n")
