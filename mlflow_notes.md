## Setting up ML Flow

#### First: Set up experiment
- "This run uses mlflow.set_experiment() to specify an experiment in the workspace where runs should be logged. 
- If the experiment specified by experiment_name does not exist in the workspace, MLflow creates it."
  ```
  experiment_name = "/Shared/diabetes_experiment/"
  mlflow.set_experiment(experiment_name)
  ```
- In Databricks the pathway ```/Shared``` must be used
- Locally you can set it to your users folder or use Docker
- Regardless of how you are using it, you need to specify some pathway. Some examples say ```experiment_name = "diabetes_experiment/"```, but this will fail.
- Once you run this cell, you will see what looks like an error, but is actually just letting you know this experiment does not exist and it creates it.
- 
