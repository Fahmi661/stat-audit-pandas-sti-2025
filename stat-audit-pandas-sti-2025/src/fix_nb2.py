import nbformat

with open('notebooks/01_eda.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code':
        source = cell.source
        source = source.replace('prs_clean[\\"is_merged\\"]', "prs_clean['is_merged']")
        cell.source = source

with open('notebooks/01_eda.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
