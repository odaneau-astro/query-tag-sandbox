from typing import Sequence

from airflow.providers.common.sql.operators import sql
from airflow.providers.snowflake.operators import snowflake


class SQLExecuteQueryOperator(sql.SQLExecuteQueryOperator):
    template_fields: Sequence[str] = ("sql", "parameters", "hook_params")


class SQLColumnCheckOperator(sql.SQLColumnCheckOperator):
    template_fields: Sequence[str] = ("partition_clause", "table", "sql", "hook_params")


class SQLTableCheckOperator(sql.SQLTableCheckOperator):
    template_fields: Sequence[str] = (
        "partition_clause",
        "table",
        "sql",
        "conn_id",
        "hook_params",
    )


class SQLCheckOperator(sql.SQLCheckOperator):
    template_fields: Sequence[str] = ("sql", "hook_params")


class SQLValueCheckOperator(sql.SQLValueCheckOperator):
    template_fields: Sequence[str] = ("sql", "pass_value", "hook_params")


class SQLIntervalCheckOperator(sql.SQLIntervalCheckOperator):
    template_fields: Sequence[str] = ("sql1", "sql2", "hook_params")


class SQLThresholdCheckOperator(sql.SQLThresholdCheckOperator):
    template_fields: Sequence[str] = (
        "sql",
        "min_threshold",
        "max_threshold",
        "hook_params",
    )


class BranchSQLOperator(sql.BranchSQLOperator):
    template_fields: Sequence[str] = ("sql", "hook_params")


class SnowflakeOperator(snowflake.SnowflakeOperator):
    template_fields: Sequence[str] = ("sql", "hook_params")

    template_fields_renderers = {"sql": "sql", "hook_params": "json"}
