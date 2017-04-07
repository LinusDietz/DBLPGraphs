import os
import time
from django_cron import CronJobBase, Schedule


class DeleteOutputFiles(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'DELETE_UNNEEDED_OUTPUT'  # a unique code

    def do(self):
        print(time.time())
        files = os.listdir('dblpGraphs/static/output')
        for tmp_file in files:

            print(os.path.getmtime(tmp_file))
