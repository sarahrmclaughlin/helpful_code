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
