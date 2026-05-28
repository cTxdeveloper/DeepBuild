import os
from dotenv import load_dotenv
from src.task_queue import TaskQueue
from src.cli import AgentCLI

load_dotenv()

if __name__ == '__main__':
    queue = TaskQueue()
    cli = AgentCLI(queue)
    cli.start()
