class Queue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, elem):
        self.queue.insert(0, elem)

    def from_queue(self):
        try:
            return self.queue.pop()
        except Exception as err:
            print(err)

    def list_queue(self):
        print(self.queue)
        return self.queue

    def size_of_queue(self):
        print(len(self.queue))
        return self.queue

#добавить задачу(-и) в очередь
def add_task(task:list, queue: Queue):
    for i in task:
        queue.add_to_queue(i)

#переместить очередную задачу из одной очереди в другую
def move_task(out_uqeue: Queue, to_queue: Queue):
    to_queue.add_to_queue(out_uqeue.from_queue())

base_tasks = Queue()
rework_tasks = Queue()
solved_tasks = Queue()

add_task(['task_1', 'task_2', 'task_3'], base_tasks)
add_task(['task_4'], base_tasks)

move_task(base_tasks, rework_tasks)
move_task(base_tasks, solved_tasks)
move_task(rework_tasks, solved_tasks)
pass
