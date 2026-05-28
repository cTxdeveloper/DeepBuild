import threading
import time
from src.crew import KickoffCrew

class WorkerThread(threading.Thread):
    def __init__(self, queue):
        super().__init__(daemon=True)
        self.queue = queue
        self.running = True

    def run(self):
        while self.running:
            task = self.queue.get_next_pending_task()
            if not task:
                time.sleep(5)
                continue

            print(f'Running task: {task}')

            try:
                crew = KickoffCrew(self.queue).crew()
                crew.kickoff(inputs={'user_request': task[2]})
            except Exception as e:
                print(f'Worker error: {e}')

    def stop(self):
        self.running = False
