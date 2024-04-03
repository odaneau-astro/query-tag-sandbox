from airflow.decorators import dag
from airflow.utils.dates import days_ago

from include.custom_operators.custom import (
    SnowflakeOperator,
    SQLCheckOperator,
    SQLColumnCheckOperator,
    SQLExecuteQueryOperator,
    SQLTableCheckOperator,
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

    sql_column_check_operator = SQLColumnCheckOperator(
        task_id="sql_column_check_operator_task",
        conn_id=snowflake_conn_id,
        table="INFORMATION_SCHEMA.SCHEMATA",
        column_mapping={"schema_name": {"distinct_check": {"greater_than": 1}}},
        hook_params=hook_params,
    )

    sql_table_check_operator = SQLTableCheckOperator(
        task_id="sql_table_check_operator_task",
        conn_id=snowflake_conn_id,
        table="INFORMATION_SCHEMA.SCHEMATA",
        checks={
            "row_count_check": {
                "check_statement": "COUNT(*) >= 1",
            },
        },
        hook_params=hook_params,
    )

    sql_check_operator = SQLCheckOperator(
        task_id="sql_check_operator_task",
        conn_id=snowflake_conn_id,
        sql="""
            SELECT COUNT(*) 
            FROM INFORMATION_SCHEMA.SCHEMATA
            WHERE schema_name = 'INFORMATION_SCHEMA'
        """,
        hook_params=hook_params,
    )

    snowflake_operator = SnowflakeOperator(
        task_id="snowflake_operator_task",
        snowflake_conn_id=snowflake_conn_id,
        sql="""
            SELECT COUNT(*) 
            FROM INFORMATION_SCHEMA.SCHEMATA
            WHERE schema_name = 'INFORMATION_SCHEMA'
        """,
        hook_params=hook_params,
    )

    sql_execute_query_operator
    sql_column_check_operator
    sql_table_check_operator
    sql_check_operator
    snowflake_operator


test_hook_params_standard_airflow()
