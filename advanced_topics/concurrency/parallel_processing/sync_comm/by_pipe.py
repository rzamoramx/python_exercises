
import multiprocessing

"""
In multiprocessing, when we want to achieve bidirectional communication between processes, we can use a pipe.
This is a simple example of how to use it.
"""


def child_process(conn):
    conn.send("Hello from the child process!")
    received_data = conn.recv()
    print(f"Child Process Received: {received_data}")
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create a child process
    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    # Send data from the parent to the child
    parent_conn.send("Hello from the parent process!")

    # Receive data from the child
    received_data = parent_conn.recv()
    print(f"Parent Process Received: {received_data}")

    process.join()
