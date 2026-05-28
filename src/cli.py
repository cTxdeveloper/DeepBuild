from src.task_queue import TaskQueue
from src.worker import WorkerThread

class AgentCLI:
    def __init__(self, queue: TaskQueue):
        self.queue = queue
        self.worker = WorkerThread(queue)

    def start(self):
        print('🤖 Agent OS ready.')
        self.worker.start()

        while True:
            user_input = input('> ').strip()

            if user_input.startswith('/goal '):
                description = user_input[6:]
                goal_id = self.queue.add_goal(description)
                self.queue.add_task(goal_id, f'Plan the project: {description}', 'orchestrator')
                print(f'Goal #{goal_id} created.')

            elif user_input == '/status':
                print(self.queue.get_all_goals())

            elif user_input == '/exit':
                self.worker.stop()
                break
