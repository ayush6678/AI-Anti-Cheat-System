import psutil

def list_unique_active_processes_with_network_interface():
    # Retrieve a list of all running processes
    processes = psutil.process_iter(['pid', 'name'])
    
    unique_process_names = set()
    
    for process in processes:
        try:
            connections = process.net_connections()
            if connections:
                unique_process_names.add(process.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that cannot be accessed
            continue
    
    return unique_process_names