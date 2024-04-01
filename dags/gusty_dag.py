import os
from typing import Any

from gusty import create_dag

from include import utils as c

dag_dir = os.path.join(os.environ["AIRFLOW_HOME"],"dags","gusty_dag")


def constant(x: str) -> Any:
    return getattr(c, x)

macro_dict = {
    "constant": constant
}

my_dag = create_dag(dag_dir, latest_only=False, user_defined_macros=macro_dict)