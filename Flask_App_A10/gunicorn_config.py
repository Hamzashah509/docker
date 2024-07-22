import multiprocessing

bind = '0.0.0.0:5010'  
workers = multiprocessing.cpu_count() * 2 + 1
#worker_class = 'gthread'  
threads = 2
timeout = 30

#errorlog = '/home/ubuntu/web_app/logs/gunicorn_error.log'
#accesslog = '/home/ubuntu/web_app/logs/gunicorn_access.log'

loglevel = 'info'

