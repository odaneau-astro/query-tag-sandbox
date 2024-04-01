from airflow.decorators import dag
from airflow.utils.dates import days_ago

from include.custom_operators.custom import (
    SQLExecuteQueryOperator,
)
from include.utils import hook_params

snowflake_conn_id = "snowflake_admin"

@dag(schedule=None, start_date=days_ago(1))
def test_hook_params_standard_airflow():
    sql_execute_query_operator = SQLExecuteQueryOperator(
        task_id="sql_execute_query_operator_task",
        conn_id=snowflake_conn_id,
        sql="SELECT '1';",
        hook_params=hook_params,
    )

test_hook_params_standard_airflow()