import threading
from copy import deepcopy
import time
import random

class Process:
    def __init__(self, id, max_resources, allocated_resources):
        self.id = id
        self.max_resources = max_resources
        self.allocated_resources = allocated_resources

    @property
    def need(self):
        return [max_r - alloc_r for max_r, alloc_r in zip(self.max_resources, self.allocated_resources)]


class Resource:
    def __init__(self, total_resources):
        self.total_resources = total_resources
        self.available_resources = deepcopy(total_resources)


class DynamicResource(Resource):
    def __init__(self, total_resources):
        super().__init__(total_resources)

    def add_resources(self, additional_resources):
        self.total_resources = [total + add for total, add in zip(self.total_resources, additional_resources)]
        self.available_resources = [avail + add for avail, add in zip(self.available_resources, additional_resources)]
        print(f"Resources added: {additional_resources}")
        print(f"New total resources: {self.total_resources}")
        print(f"New available resources: {self.available_resources}")


def is_safe_state(processes, available_resources):
    work = deepcopy(available_resources)
    finish = [False] * len(processes)
    safe_sequence = []

    while len(safe_sequence) < len(processes):
        allocated_in_this_loop = False

        for i, process in enumerate(processes):
            if not finish[i] and all(n <= w for n, w in zip(process.need, work)):
                work = [w + alloc for w, alloc in zip(work, process.allocated_resources)]
                safe_sequence.append(process.id)
                finish[i] = True
                allocated_in_this_loop = True

        if not allocated_in_this_loop:
            return False, []

    return True, safe_sequence


def request_resources(process, request, processes, resources):
    available_resources = resources.available_resources
    if all(req <= avail for req, avail in zip(request, available_resources)):
        process.allocated_resources = [alloc + req for alloc, req in zip(process.allocated_resources, request)]
        resources.available_resources = [avail - req for avail, req in zip(available_resources, request)]

        is_safe, safe_sequence = is_safe_state(processes, resources.available_resources)
        if is_safe:
            return True, safe_sequence
        else:
            process.allocated_resources = [alloc - req for alloc, req in zip(process.allocated_resources, request)]
            resources.available_resources = deepcopy(available_resources)
    return False, []


def process_thread(process, request, processes, resources):
    granted, sequence = request_resources(process, request, processes, resources)
    if granted:
        print(f"Process {process.id} request granted. Safe sequence: {sequence}")
    else:
        print(f"Process {process.id} request denied. System would be in an unsafe state.")


def race_condition_monitor(processes, resources):
    pass  

def display_state(processes, available_resources):
    print(f"Available Resources: {available_resources}")
    for process in processes:
        print(f"Process {process.id}: Max: {process.max_resources}, Allocated: {process.allocated_resources}, Need: {process.need}")


def dynamic_resource_changer(resource, interval):
    while True:
        time.sleep(interval)
        additional_resources = [random.randint(0, 3) for _ in resource.total_resources]
        resource.add_resources(additional_resources)


if __name__ == "__main__":
    total_resources = [10, 5, 7]
    resources = DynamicResource(total_resources)

    processes = [
        Process(0, [7, 5, 3], [0, 1, 0]),
        Process(1, [3, 2, 2], [2, 0, 0]),
        Process(2, [9, 0, 2], [3, 0, 2]),
        Process(3, [2, 2, 2], [2, 1, 1]),
        Process(4, [4, 3, 3], [0, 0, 2])
    ]

    display_state(processes, resources.available_resources)

    # Start the dynamic resource changer thread
    dynamic_resource_thread = threading.Thread(target=dynamic_resource_changer, args=(resources, 10))
    dynamic_resource_thread.daemon = True
    dynamic_resource_thread.start()

    # Simulate process requests in separate threads
    requests = [
        (processes[0], [0, 2, 0]),
        (processes[4], [0, 3, 0]),
        (processes[1], [1, 0, 2]),
        (processes[3], [0, 1, 0])
    ]

    for process, request in requests:
        t = threading.Thread(target=process_thread, args=(process, request, processes, resources))
        t.start()
        t.join()

    display_state(processes, resources.available_resources)
