def FCFS(process: list):
    """ process is array [[pname, at, bt]] """
    all_process_count = len(process)
    total_tat = 0
    total_wt = 0
    process.sort(key=lambda x: x[1])
    current_time = min(process, key=lambda x: x[1])[1]
    for p in process:
        pname, at, bt = p
        current_time += bt
        tat = current_time - at
        wt = tat - bt
        total_tat += tat
        total_wt += wt
        print(f"{pname}:{tat}:{wt}")
    print(f'Avg Tat:{ total_tat / all_process_count}\nAvg Wt:{total_wt / all_process_count}')

if __name__ == '__main__':
    proc = [['P1', 1, 4],['P2', 0, 6],['P3', 3, 8],['P4', 5, 5]]
    FCFS(proc)
