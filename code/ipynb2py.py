#%%
import json

def convert(ipynb_file, output_file=None, blank_code = False, todo_msg = '# TODO: Fill code here'):
    """
    Converts an ipython notebook file to a plain .py file that 
    can be used with the jupyter extension in Visual Studio Code. 
    Markdown cells in the notebook will be output properly formatted 
    in the VS Code Results panel.

    Parameters:
    -----------
    ipynb_file: str
        filename of ipynb jupyter notebook file
    output_file: str
        where to store the .py output file
    blank_code: bool
        if True, this will generate blank code cells, resulting in 
        files that can be used as exercise skeletons. If False (default), 
        all code cells will be populated with actual code.
    todo_msg: str
        A string text by which code cells will be replaced if blank_code 
        is set to True. If set to None, no todo message will be created.
    """
    print('Converting ipynb file ...')
    output = '#%%\nimport markdown\n' \
             'from IPython.core.display import display, HTML\n'\
             'def md(str):\n'\
             '    display(HTML(markdown.markdown(str + "<br />")))\n\n'
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                cell_output = '#%%\nmd("""\n'
                for line in cell['source']:
                    cell_output += line                    
                cell_output += '\n""")\n\n'
                output += cell_output
            elif cell['cell_type'] == 'code':
                cell_output = '#%% In [' + str(cell['execution_count']) + ']\n'
                if not blank_code:
                    for line in cell['source']:
                        cell_output += line
                elif todo_msg is not None:
                    cell_output += todo_msg + '\n'
                cell_output += '\n\n'
                output += cell_output
    with open(output_file, 'w') as f:
        f.write(output)    
    print('Done.')


# To use the script just execute the following cell:
#%% 
convert('code/1_2_pathpy.ipynb', 'code/1_2_pathpy.py', blank_code=True, todo_msg=None)
