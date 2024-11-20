from matplotlib import pyplot as plt


def PriorityScheduling(n, pid, at, bt, priority): 
    # Initializing required lists 
    wt = [0] * n  # Waiting times 
    tt = [0] * n  # Turnaround times 
    ct = [0] * n  # Completion times 
    tottt = 0  # Total Turnaround Time 
    totwt = 0  # Total Waiting Time 
    gantt_chart = []  # Store (process_id, start_time, duration) 
     
    # Combine process information into a list of tuples (PID, AT, BT, Priority) 
    processes = [(pid[i], at[i], bt[i], priority[i]) for i in range(n)] 
     
    # Sort processes based on Arrival Time (AT) and if equal, by Priority 
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort first by Arrival Time, then by Priority 
 
    current_time = 0  # Track the current time 
 
    # Process Scheduling 
    for i in range(n): 
        process_id, arrival_time, burst_time, pr = processes[i] 
         
        # If the process arrives after the current time, we need to "wait" 
        if arrival_time > current_time: 
            current_time = arrival_time 
         
        # Calculate Completion Time 
        ct[i] = current_time + burst_time 
         
        # Turnaround Time = Completion Time - Arrival Time 
        tt[i] = ct[i] - arrival_time 
         
        # Waiting Time = Turnaround Time - Burst Time 
        wt[i] = tt[i] - burst_time 
         
        # Add the process details to the Gantt chart 
        gantt_chart.append((process_id, current_time, burst_time)) 
         
        # Update the current time after the process has executed 
        current_time = ct[i] 
         
        # Accumulate total turnaround and waiting times 
        tottt += tt[i] 
        totwt += wt[i] 
 
    # Output Process Information 
    print("\nProcess ID | AT | BT | Priority | CT | TT | WT") 
    for i in range(n): 
        print(f" {pid[i]}       {at[i]}   {bt[i]}    {priority[i]}     {ct[i]}   {tt[i]}   {wt[i]}") 
 
    # Averages 
    print(f"\nAverage Turnaround Time: {tottt / n:.2f}") 
    print(f"Average Waiting Time: {totwt / n:.2f}") 
 
    # Textual Gantt Chart 
    print("\nGantt Chart") 
    print("|", end="") 
    for process, start, duration in gantt_chart: 
        print(f" P{process} {' ' * duration}|", end="") 
    print("\n") 
 
    # Visual Gantt Chart 
    plt.figure(figsize=(10, 3)) 
    for process, start, duration in gantt_chart: 
        plt.barh(y=0, width=duration, left=start, edgecolor='black', label=f"P{process}" if process == 
gantt_chart[0][0] else "") 
        plt.text(start + duration / 2, 0, f"P{process}", ha='center', va='center', color='white', fontsize=10) 
 
    plt.yticks([]) 
    plt.xlabel("Time") 
    plt.title("Gantt Chart - Priority Scheduling (Non-Preemptive)") 
    plt.legend(loc='upper right') 
    plt.grid(axis='x', linestyle='--', alpha=0.7) 
    plt.show() 
 
# Example usage 
n = 3 
pid = [1, 2, 3] 
at = [0, 1, 2]  # Arrival Times 
bt = [10, 5, 8]  # Burst Times 
priority = [3, 1, 2]  # Priority values (lower number = higher priority) 
 
PriorityScheduling(n, pid, at, bt, priority)