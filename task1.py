def fcfs(requests, initial_pos):
    hm = 0
    current_pos = initial_pos

    for reqs in requests:
        hm += abs(reqs - current_pos)
        current_pos = reqs

    return hm

def scan(requests, initial_pos, total_cyls):
    hm = 0
    current_pos = initial_pos

    for reqs in requests:
        if reqs >= current_pos:
            hm += reqs - current_pos
            current_pos = reqs
    
    hm += total_cyls - 1 - current_pos
    hm += total_cyls - 1

    return hm

def c_scan(requests, initial_pos, total_cyls):
    hm = 0 
    current_pos = initial_pos

    index = requests.index(initial_pos)

    reqs_after_current = requests[index:]
    reqs_before_current = requests[:index]

    for reqs in reqs_after_current:
        hm += reqs - current_pos
        current_pos = reqs

    hm += total_cyls - 1 - current_pos
    hm += total_cyls - 1
    hm += reqs_before_current[-1] + 1

    return hm

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python task1_disk_scheduling.py <initial_position> <requests_file>")
        sys.exit(1)
    
    initial_position = int(sys.argv[1])
    requests_file = sys.argv[2]
    total_cylinders = 5000
    
    requests = read_requests(requests_file)
    
    print("Task 1:")
    print("FCFS Total Head Movements:", fcfs(requests, initial_position))
    print("SCAN Total Head Movements:", scan(requests, initial_position, total_cylinders))
    print("C-SCAN Total Head Movements:", c_scan(requests, initial_position, total_cylinders))
