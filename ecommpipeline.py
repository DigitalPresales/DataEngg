## Reference for this code is - https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
# Above code is modified to fit demo requirements. 


from datetime import timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['digitalpresales@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    'ecommpipeline',
    default_args=default_args,
    description='E-commerce product feedback data pull pipeline',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['ecomm_usecase'],
) as dag:

    task1 = BashOperator(
        task_id='ingestion_date',
        bash_command='date',
    )

    task2 = BashOperator(
        task_id='prepare',
        depends_on_past=False,
 #       bash_command='prepare.sh',
        bash_command='sleep 5',
        retries=3,
    )

    task1.doc_md = dedent(
    """\
    #### Task Documentation   
    """
    )

    dag.doc_md = __doc__  
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """
    )
# In task below, we can perform scripting. Pl. refer to process.sh for more details. 

    task3 = BashOperator(
        task_id='process',
        depends_on_past=False,
        bash_command='process.sh',
#        params={'product1': 'Washing Machine- Good one, model TNJD is perfect, I bought it 1 year ago and works great'},
    )

# Below we handle dependencies.
    task1 >> [task2, task3]


