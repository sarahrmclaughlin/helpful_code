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
- Here is an example that is a combo of chatGPT and my own notes/additions
  
 ```
    with mlflow.start_run() as run:
    # Log model parameters to MLflow
    mlflow.log_params(params)

    # Train the XGBoost model
    model = xgb.train(params, dtrain, num_boost_round=100, evals=[(dtest, "test")], early_stopping_rounds=10)

    # Predict probabilities on the test set
    y_pred_prob = model.predict(dtest)

    # Calculate AUC score
    auc = roc_auc_score(y_test, y_pred_prob)
    print(f"AUC: {auc}")

    # Log the AUC metric to MLflow
    mlflow.log_metric("AUC", auc)

    # The signature contains info about the expected schema, which will be used again when the model is called again and is especially important during model deployment
    signature = infer_signature(X_test_df, y_pred_prob)

    # Log the model to MLflow with signature
    mlflow.xgboost.log_model(model, artifact_path="xgboost_model", signature=signature)

    # Save the model_uri info, with run_id, this can be used when you are ready to register the model.
    model_uri = f"runs:/{run.info.run_id}/xgboost_model"

    # Print model_uri to see what it looks like:
    print(model_uri) # --> runs:/b4e18a5f37ep01234513f2ed/xgboost_model

    # When you have decided on which experiment run you think is the best, you can register the model.
    # It will assign Version 1. 
    mlflow.register_model(model_uri=model_uri, name="Sarah_XGBoost_BC_Model")

    # Print the MLflow run URL for reference
    print(f"MLflow run URL: {mlflow.get_artifact_uri()}")
```
- There are a few ways to load a model. (This works in Databricks)
```
# There are two ways to load a model
# 1. Use model run ID and name directly from experiment
# model_uri_by_run_id = 'runs:/5a1f7eaf011249379eaad42e584e5eab/xgboost_model'
# loaded_model_by_run_id = mlflow.pyfunc.load_model(model_uri_by_run_id)

# 2. Use the model name that was registered and make sure to include the version number
registered_model_uri = "models:/Sarah_XGBoost_BC_Model/1"
loaded_model_by_model_name = mlflow.pyfunc.load_model(model_uri=registered_model_uri)
loaded_model_by_model_name

# See methods and attributes of a model
dir(loaded_model_by_model_name._model_impl_sklearn_model)
# --> Things like n_features_in_ , feature_name_
# Get list of features in the model
loaded_model_by_model_name._model_impl_sklearn_model.feature_name_
# Get number of features in the model
loaded_model_by_model_name._model_impl_sklearn_model.n_features_in_

# Load artifacts from the registered model
artifacts = mlflow.artifacts.download_artifacts(artifact_uri=registered_model_uri)

# Load artifacts from a run_id
artifact_uri = mf_flow.get_run(run_id).info,artifact_uri
# -- If run_id = 123,and experiment_id = 701, in Databricks it is stored in DBFS, the artifact_uri will be something like:
# --> dbfs:/databricks/mlflow-tracking/{experiment_id}/{run_id}/artifacts
# ---> dbfs:/databricks/mlflow-tracking/701/123/artifacts

```

#### General notes about ML Flow log_params, log_metrics, log_artifacts
- ```log_params``` Stores info about parameters and hyperparameters
- ```log_metrics``` Stores info about metrics like AUC, accuracy, etc
-  ```log_artifacts``` Stores the model and also files like plots, jsons, csvs etc. Metrics can be stored this way, but you need to do additional processing.
-  Otherwise, in order to view the metrics, you need to get to it in a round about way
  ```
# Load the model using the registered model URI (see above)
loaded_model = mlflow.pyfunc.load_model(model_uri=registered_model_uri)

# Retrieve the run ID from the model URI
client = MlflowClient()
model_details = client.get_registered_model(name="Sarah_XGBoost_BC_Model")
latest_version = model_details.latest_versions[0]
run_id = latest_version.run_id

# Load the metrics logged during the run
metrics = mlflow.get_run(run_id).data.metrics

# Display the metrics
metrics
```
