
def ROUND_ROBIN(process: list, quantum: int):
    """
    process is array [pname, at, bt]
    quantum is number set each process have execute time limit
    """
    all_process_count = len(process)
    total_tat = 0
    total_wt = 0
    done = 0
    process.sort(key=lambda x: x[1])
    current_time = min(process, key=lambda x: x[1])[1]
    while done != all_process_count:
        calc_all_process = False
        queue = []
        while not calc_all_process:
            for cp in process:
                if cp not in queue and cp[1] <= current_time:
                    cp.insert(3, cp[2])
                    queue.append(cp)
            if len(queue) > 1:
                queue.append(queue.pop(0))

            pname, at, bt, orginal_bt = queue[0]
            if bt == 0 :
                continue
            if bt <= quantum:
                current_time += bt
                queue[0][2] -= bt
                done += 1
                tat = current_time - at
                wt = tat - orginal_bt
                total_tat += tat
                total_wt += wt
                print(f"{pname}:{tat}:{wt}")
            else:
                current_time += quantum
                queue[0][2] -= quantum
            if done == all_process_count:
                calc_all_process = True
    print(f"Avg Tat:{total_tat / all_process_count}\nAvg Wt:{total_wt / all_process_count}")

if __name__ == '__main__':
    proc = [['P1', 2, 3], ['P2', 0, 8], ['P3', 3, 7], ['P4', 6, 5]]
    ROUND_ROBIN(proc, 2)