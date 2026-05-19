### Frequently used DBT commands

- ```uv run dbt init dbt_project``` Create a dbt project within your repository
- ```uv run dbt run```	Executes all models (tables, views, incremental models)	After updating models; rebuilds your data pipeline
    - ```uv run dbt run -s tag:drift``` Run model with specific tag. Ex. A model named with name of drift
- ```uv run dbt test```	Runs all data tests (built-in + custom)	After dbt run to validate data quality
    - ```uv run dbt test -s stg_transactions``` Test specific models
- ```uv run dbt compile```	Compiles SQL without executing	Debug SQL before running; check for syntax errors
- ```uv run dbt docs``` generate	Generates documentation from your project	Before sharing docs; documents models, tests, lineage
- ```uv run dbt docs serve```	Serves generated docs locally on a web UI	Browse documentation in browser (http://localhost:8000)
- ```uv run dbt freshness```	Checks if source data is stale	Monitor if raw data pipeline is still feeding dbt
- ```uv run dbt snapshot```	Creates point-in-time snapshots of data	Track slowly changing dimensions
- ```uv run dbt seed```	Loads CSV files from seeds/ directory	Load reference tables (currencies, country codes, etc.)
- ```uv run dbt clean```Removes compiled artifacts and target directory	Clean up before fresh runs; debugging
- ```uv run dbt debug```	Verifies dbt/database connection.Troubleshoot connection issues.
- ```uv run dbt deps``` After adding dbt_project/packages.yml. This will install custom DBT utils
    - ```packages:package: dbt-labs/dbt_utils version: 1.1.1```

### Typical workflow
1. Set-up DBT projects using ```uv run dbt init dbt_project```
   - Update profiles with DBT info
   - Update pyproject.toml with DBT info
2. Run models ```uv run dbt run```
3. Run tests ```uv run dbt test```
4. View results in browser
    - ```uv run dbt docs generate```
    - ```uv run dbt docs serve```
  
### Debug Errors
- Compilation
    - SQL syntax errors, undefined macros, missing refs
    - ```dbt compile -s model_name```
- Execution
    - Runtime errors from the database (DuckDB, Postgres, etc.)
    - ```dbt run -v``` check SQL ```target/compiled/```
- Validation
    - Test failures, data quality issues
    - ```dbt test -v``` then inspect ```run_results.json```
 
- Test only your custom drift tests
```uv run dbt test -s tag:drift```
- Test only a single test
```uv run dbt test -s test_distribution_shift```
- Test a specific model's tests
```uv run dbt test -s stg_transactions```
- Quick tips for validation, verify first: 
1. Does stg_transactions actually exist?
```uv run dbt list -s stg_transactions```
2. What tests are actually defined?
```uv run dbt list -s tag:drift --resource-type test```
3. Are your models materialized correctly?
```uv run dbt list -s stg_transactions,fct_drift_metrics --output json | python -m json.tool```
