from autogenstudio import WorkflowManager
# load workflow from exported json workflow file.
workflow_manager = WorkflowManager(workflow="workflow_setup_infra_workflow.json")

# run the workflow on a task
task_query = "What is the height of the Eiffel Tower?. Dont write code, just respond to the question."
workflow_manager.run(message=task_query)