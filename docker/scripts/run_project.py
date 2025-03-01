import sys
import os
import workflow_manager
from workflow_manager.project import start_process_monitor

if __name__ == '__main__':
    if len(sys.argv) < 0:
        raise Exception('InputError.')
    path = sys.argv[1]
    project_name = sys.argv[2]

    P = workflow_manager.Project(project_name)
    script = P.script('pretend_import')
    script_input_arguments = {'path': path, 'send_dir': os.getenv('RESULTS')}
    script.run(script_input_arguments)

    start_process_monitor(project_name, 999, 3, 8)