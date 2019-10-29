import os
import time
import click
from utils.htmlrunner import HTMLTestRunner
from config import basedir
from suites import get_all_cases, get_app_test_suite, get_web_test_suite

reports_dir = os.path.join(basedir, 'reports')


@click.command()
@click.option("--suite")
def run(suite):
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    if 'app' == suite:
        title, description, test_suite = get_app_test_suite()
    elif 'web' == suite:
        title, description, test_suite = get_web_test_suite()
    else:
        title, description, test_suite = get_all_cases()
    with open("{}_{}.html".format(title, now), 'wb') as f:
        HTMLTestRunner(title=title, description=description, stream=f).run(test_suite)


if __name__ == '__main__':
    run()