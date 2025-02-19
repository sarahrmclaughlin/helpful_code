
### Create a login for Airflow
- Within your terminal in VSCode enter the following.
- Note: anything that follow words with -- can be customized. (eg. --firstname SHREK)
  
```airflow users create --username admin --firstname FIRST_NAME --lastname LAST_NAME --role Admin --email admin@example.org --password YOUR_PASSWORD```
- After running this, you will see ```User 'admin' created```


#### - If you want to check whether you've already created a user
```airflow users list```

#### - If you forgot your password or you just want to delete a user
- You may encounter an error when trying to log into http://localhost:8080, the Airflow UI, within your browser that says "Invalid login. Please try again."
- As a result, you may need to delete that username in order to create a new login
```airflow users delete -u admin```

- Typically, ```admin``` is username
- After running this, you will see ```User 'admin' deleted```
  
