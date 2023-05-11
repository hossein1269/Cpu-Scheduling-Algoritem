def SJF(process: list):
    "process is array [[pname, at, bt]]"
    process_result = []  # is array [tat] result
    all_process_count = len(process)
    done = 0
    total_tat = 0
    total_wt = 0
    # sort process array key = arrival time
    process.sort(key=lambda x: x[0])
    # get minimum of arrival time
    min_arrival = min(process, key=lambda x: x[0])[1]
    current_time = min_arrival

    while done != all_process_count:
        # filter process by logic if at less then current time and cast to list and if we have many
        # process come same time or any of time passed we slect minmum number of burst time
        pname, at, bt = min(
            list(filter(lambda x: x[1] <= current_time, process)), key=lambda x: x[2])
        current_time += bt
        tat = current_time - at
        wt = tat - bt
        process_result.append((pname, tat, wt))
        done += 1
        process.remove([pname, at, bt])
    for result in process_result:
        print(f'{result[0]}:{result[1]}:{result[2]}')
        total_tat += result[1]
        total_wt += result[2]
    print(f'Avg Tat:{ total_tat / all_process_count}\nAvg Wt:{total_wt / all_process_count}')

if __name__ == '__main__':
    proc = [['P1', 1, 6],['P2', 2, 3],['P3', 4, 2],['P4', 1, 3]]
    SJF(proc)