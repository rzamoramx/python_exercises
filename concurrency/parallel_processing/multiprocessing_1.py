
import multiprocessing as mp
import numpy as np

results = []


def prepare_data() -> list:
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[200000, 5])
    data = arr.tolist()
    return data[:5]


def howmany_within_range(i, row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return i, count


def collect_result(result):
    global results
    results.append(result)


def test_mp_pool_async_apply():
    pool = mp.Pool(mp.cpu_count())
    data = prepare_data()
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range, args=(i, row, 4, 8), callback=collect_result)

    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

    # Step 5: Sort results [OPTIONAL]
    #results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]

    print(results_final[:10])


def check_num_cpus():
    cnt = mp.cpu_count()
    print(f"Num of CPUs: {cnt}")


if __name__ == "__main__":
    check_num_cpus()
    test_mp_pool_async_apply()
