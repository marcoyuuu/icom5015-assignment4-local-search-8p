import nbformat as nbf
import json

# Load the original notebook
notebook_path = 'AI_LocalSearch_Final_Report.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = nbf.read(f, as_version=4)

# Load the improvement content
with open('notebook_improvements.md', 'r', encoding='utf-8') as f:
    improvements = f.read()

# Process sections to add explanations
sections = {
    'Setup and Data Loading': "",
    'Results Analysis - Success Rates': "",
    'Performance Metrics': "",
    'Algorithm Performance Profiles': "",
    'Implementation Details': "",
    'Key Findings': "",
    'Conclusions': "",
    'Figure Display': ""
}

# Parse improvements to get content for each section
current_section = None
content = ""
for line in improvements.split('\n'):
    if line.startswith('## '):
        if current_section:
            sections[current_section] = content.strip()
        current_section = line[3:].strip()
        content = ""
    else:
        content += line + "\n"

if current_section:
    sections[current_section] = content.strip()

# Update notebook cells with explanations
updated_cells = []
for cell in notebook.cells:
    updated_cells.append(cell)
    
    # Add Setup and Data Loading explanation
    if cell.get('source', '').strip() == '## Setup and Data Loading':
        updated_cells.append(nbf.v4.new_markdown_cell(sections['Setup and Data Loading']))
    
    # Add Results Analysis explanation
    elif cell.get('source', '').strip() == '## Results Analysis\n\n### 1. Success Rates':
        updated_cells.append(nbf.v4.new_markdown_cell(sections['Results Analysis - Success Rates']))
    
    # Add Performance Metrics explanation
    elif cell.get('source', '').strip() == '### 2. Performance Metrics':
        updated_cells.append(nbf.v4.new_markdown_cell(sections['Performance Metrics']))
    
    # Add Algorithm Performance Profiles explanation
    elif cell.get('source', '').strip() == '### 3. Algorithm Performance Profiles':
        updated_cells.append(nbf.v4.new_markdown_cell(sections['Algorithm Performance Profiles']))

# Add Implementation Details section with key algorithm code
implementation_cell = nbf.v4.new_markdown_cell("## Implementation Details\n\nThis section presents the key algorithms and functions used in our experiments.")
updated_cells.append(implementation_cell)
updated_cells.append(nbf.v4.new_markdown_cell(sections['Implementation Details']))

# Add Figure Display section at the end
figure_display_cell = nbf.v4.new_markdown_cell("## Figure Display\n\nThe following section displays the key result figures generated from our experiments.")
updated_cells.append(figure_display_cell)

# Extract python code from Figure Display section
figure_code = sections['Figure Display'].strip()
if '```python' in figure_code and '```' in figure_code:
    code_content = figure_code.split('```python')[1].split('```')[0].strip()
    updated_cells.append(nbf.v4.new_code_cell(code_content))

# Create the updated notebook with new cells
notebook.cells = updated_cells

# Save the updated notebook
with open('AI_LocalSearch_Final_Report_Improved.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(notebook, f)

print("Notebook updated successfully. New file: AI_LocalSearch_Final_Report_Improved.ipynb") 