hook_params = {
    "session_parameters": {
        "query_tag": (
            "{"
            "'dag_id': '{{ dag.dag_id }}', "
            "'task_id': '{{ task.task_id }}', "
            "'run_id': '{{ run_id }}', "
            "'logical_date': '{{ logical_date }}', "
            "'started': '{{ ti.start_date }}', "
            "'operator': '{{ ti.operator }}'"
            "}"
        )
    }
}
