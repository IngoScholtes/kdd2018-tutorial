#%%
import json

def remove_code(ipynb_file, output_file):
    print('Removing code from ipynb file ...')   
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':               
               cell['source'] = []
               cell['outputs'] = []
    with open(output_file, 'w') as f:
        json.dump(notebook, f)  
    print('Done.')

def extract_code(ipynb_file, output_file=None):
    """
    Converts an ipython notebook file to a plain .py file that 
    only contains the code cells. Nice to use as a template for 
    generating the live solution.

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
    output = ''
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
           if cell['cell_type'] == 'code':
                cell_output = '#%% In [' + str(cell['execution_count']) + ']\n'
                for line in cell['source']:
                    # remap relative path data directory from jupyter notebook to VS Code                
                    cell_output += line.replace('../', '')                
                cell_output += '\n\n'
                output += cell_output
    with open(output_file, 'w') as f:
        f.write(output)    
    print('Done.')

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
    print('Converting ipynb file {} to {} ...'.format(ipynb_file, output_file))
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
                if not blank_code or cell['source'][0].startswith('%NOREMOVE'):
                    for line in cell['source']:
                        # remap relative path data directory from jupyter notebook to VS Code                
                        cell_output += line.replace('../', '').replace('from state_lumping_network', 'from solutions.state_lumping_network')
                elif todo_msg is not None:
                    cell_output += todo_msg + '\n'
                cell_output += '\n\n'
                output += cell_output
    with open(output_file, 'w') as f:
        f.write(output)    
    print('Done.')


# To apply the script to the sample solutions, just execute the following cells:
#%% Unit 1.2
convert('solutions/1_2_pathpy.ipynb', 'code/1_2_pathpy.py', blank_code=True, todo_msg=None)
extract_code('solutions/1_2_pathpy.ipynb', 'live_solutions/1_2_pathpy_code.py')
remove_code('solutions/1_2_pathpy.ipynb', 'code/1_2_pathpy.ipynb')
convert('solutions/1_2_pathpy.ipynb', 'solutions/1_2_pathpy.py', blank_code=False, todo_msg=None)

#%% Unit 1.3
convert('solutions/1_3_higher_order.ipynb', 'code/1_3_higher_order.py', blank_code=True, todo_msg=None)
extract_code('solutions/1_3_higher_order.ipynb', 'live_solutions/1_3_higher_order_code.py')
remove_code('solutions/1_3_higher_order.ipynb', 'code/1_3_higher_order.ipynb')
convert('solutions/1_3_higher_order.ipynb', 'solutions/1_3_higher_order.py', blank_code=False, todo_msg=None)

#%% Unit 1.4
convert('solutions/1_4_temporal_networks.ipynb', 'code/1_4_temporal_networks.py', blank_code=True, todo_msg=None)
extract_code('solutions/1_4_temporal_networks.ipynb', 'live_solutions/1_4_temporal_networks_code.py')
remove_code('solutions/1_4_temporal_networks.ipynb', 'code/1_4_temporal_networks.ipynb')
convert('solutions/1_4_temporal_networks.ipynb', 'solutions/1_4_temporal_networks.py', blank_code=False, todo_msg=None)

#%% Unit 1.5
convert('solutions/1_5_exploration.ipynb', 'code/1_5_exploration.py', blank_code=False, todo_msg=None)
convert('solutions/1_5_exploration.ipynb', 'solutions/1_5_exploration.py', blank_code=False, todo_msg=None)

#%% Unit 1.6
convert('solutions/1_6_multi_order.ipynb', 'code/1_6_multi_order.py', blank_code=True, todo_msg=None)
extract_code('solutions/1_6_multi_order.ipynb', 'live_solutions/1_6_multi_order_code.py')
remove_code('solutions/1_6_multi_order.ipynb', 'code/1_6_multi_order.ipynb')
convert('solutions/1_6_multi_order.ipynb', 'solutions/1_6_multi_order.py', blank_code=False, todo_msg=None)

#%% Unit 1.7
convert('solutions/1_7_optimal_analysis.ipynb', 'code/1_7_optimal_analysis.py', blank_code=True, todo_msg=None)
extract_code('solutions/1_7_optimal_analysis.ipynb', 'live_solutions/1_7_optimal_analysis_code.py')
remove_code('solutions/1_7_optimal_analysis.ipynb', 'code/1_7_optimal_analysis.ipynb')
convert('solutions/1_7_optimal_analysis.ipynb', 'solutions/1_7_optimal_analysis.py', blank_code=False, todo_msg=None)

#%% Unit 1.8
convert('solutions/1_8_exploration.ipynb', 'code/1_8_exploration.py', blank_code=False, todo_msg=None)
convert('solutions/1_8_exploration.ipynb', 'solutions/1_8_exploration.py', blank_code=False, todo_msg=None)

#%% Unit 2.1
convert('solutions/2_1_infomap_intro.ipynb', 'code/2_1_infomap_intro.py', blank_code=True)
extract_code('solutions/2_1_infomap_intro.ipynb', 'live_solutions/2_1_infomap_intro_code.py')
remove_code('solutions/2_1_infomap_intro.ipynb', 'code/2_1_infomap_intro.ipynb')
convert('solutions/2_1_infomap_intro.ipynb', 'solutions/2_1_infomap_intro.py', blank_code=False, todo_msg=None)

#%% Unit 2.2
convert('solutions/2_2_explore_flight_data.ipynb', 'code/2_2_explore_flight_data.py', blank_code=True)
extract_code('solutions/2_2_explore_flight_data.ipynb', 'live_solutions/2_2_explore_flight_data_code.py')
remove_code('solutions/2_2_explore_flight_data.ipynb', 'code/2_2_explore_flight_data.ipynb')
convert('solutions/2_2_explore_flight_data.ipynb', 'solutions/2_2_explore_flight_data.py', blank_code=False, todo_msg=None)

#%% Unit 2.3
convert('solutions/2_3_sparse_state_lumping.ipynb', 'code/2_3_sparse_state_lumping.py', blank_code=True)
extract_code('solutions/2_3_sparse_state_lumping.ipynb', 'live_solutions/2_3_sparse_state_lumping_code.py')
remove_code('solutions/2_3_sparse_state_lumping.ipynb', 'code/2_3_sparse_state_lumping.ipynb')
convert('solutions/2_3_sparse_state_lumping.ipynb', 'solutions/2_3_sparse_state_lumping.py', blank_code=False, todo_msg=None)

#%% Unit 2.4
convert('solutions/2_4_sparse_flight_data.ipynb', 'code/2_4_sparse_flight_data.py', blank_code=True)
extract_code('solutions/2_4_sparse_flight_data.ipynb', 'live_solutions/2_4_sparse_flight_data_code.py')
remove_code('solutions/2_4_sparse_flight_data.ipynb', 'code/2_4_sparse_flight_data.ipynb')
convert('solutions/2_4_sparse_flight_data.ipynb', 'solutions/2_4_sparse_flight_data.py', blank_code=False, todo_msg=None)
