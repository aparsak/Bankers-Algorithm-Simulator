## 🚧 Work in Progress

Please note that this README is a work in progress and may not include all the information related to the Banker's Algorithm Simulator. We are actively updating and improving the documentation. If you have any questions or need further details, feel free to reach out or check back later for updates.

Thank you for your understanding!


# 🖥️ Banker's Algorithm Simulator

This repository contains a Python implementation of the Banker's Algorithm, a deadlock avoidance algorithm used in operating systems for resource allocation. The simulator includes two parts: one for static resource allocation and another for dynamic resource allocation scenarios.

## Overview

The Banker's Algorithm ensures that processes request resources in a way that avoids deadlock by dynamically checking if the system's state is safe before granting requests. This repository demonstrates the algorithm's application in both static and dynamic resource allocation environments.

## Static Resource Allocation

Simulates a scenario where processes request and release resources, with safety checks using the Banker's Algorithm.

### Features

- **Safe State Checking:** Evaluates if a resource request can be granted without entering an unsafe state.
- **Resource Request Handling:** Processes request resources; the system decides whether to grant or deny based on the current state.
- **System State Display:** Shows current allocation, maximum resources per process, and resource needs.

### 📄 Example Output with Static Resource Allocation

Displays the initial system state and processes for resource allocation:

| Process | Max Resources | Allocated Resources | Needed Resources |
|---------|---------------|---------------------|------------------|
|   P0    |    [7, 5, 3]  |       [0, 1, 0]     |     [7, 4, 3]    |
|   P1    |    [3, 2, 2]  |       [2, 0, 0]     |     [1, 2, 2]    |
|   P2    |    [9, 0, 2]  |       [3, 0, 2]     |     [6, 0, 0]    |
|   P3    |    [2, 2, 2]  |       [2, 1, 1]     |     [0, 1, 1]    |
|   P4    |    [4, 3, 3]  |       [0, 0, 2]     |     [4, 3, 1]    |

Available Resources: [3, 3, 5]

### 📥 Input

To interact with the simulation, input the following:

- **Process ID:** The ID of the process requesting resources.
- **Resource Request:** Specify resources requested by the process as a list of integers.

### 📤 Output

The system outputs whether the request is granted or denied based on the Banker's Algorithm evaluation, along with the updated system state.

## Dynamic Resource Allocation

Extends the simulation by allowing resources to be dynamically added to the system over time.

### Features

- **Dynamic Resource Addition:** Simulates the addition of resources at random intervals.
- **Real-time Safe State Evaluation:** Continuously checks the system's safety state as resources are added and processes request more resources.
- **Threaded Execution:** Uses separate threads to handle resource requests and dynamic changes concurrently.

### 📄 Example Output with Dynamic Resources

Displays the initial system state with dynamic resources added:

| Process | Max Resources | Allocated Resources | Needed Resources |
|---------|---------------|---------------------|------------------|
|   P0    |    [7, 5, 3]  |       [0, 1, 0]     |     [7, 4, 3]    |
|   P1    |    [3, 2, 2]  |       [2, 0, 0]     |     [1, 2, 2]    |
|   P2    |    [9, 0, 2]  |       [3, 0, 2]     |     [6, 0, 0]    |
|   P3    |    [2, 2, 2]  |       [2, 1, 1]     |     [0, 1, 1]    |
|   P4    |    [4, 3, 3]  |       [0, 0, 2]     |     [4, 3, 1]    |

Available Resources: [3, 3, 5]

#### Dynamic Resource Addition

- **Resources added:** [2, 1, 3]
- **New total resources:** [5, 4, 8]
- **New available resources:** [1, 2, 5]

This section demonstrates how the simulator handles changes in resource availability and continues to manage process requests using the Banker's Algorithm.

## 📞 Contact

For any inquiries or issues, please open an issue on this repository or reach out to aparsa.khadem@gmail.com.
