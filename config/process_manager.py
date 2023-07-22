import psutil

class ProcessManager:
    def __init__(self):
        pass

    @staticmethod
    def is_process_running(pid: int) -> bool:
        """Check if a process with the given PID is running."""
        return psutil.pid_exists(pid)

    @staticmethod
    def get_process_by_pid(pid: int) -> psutil.Process:
        """Get a psutil.Process object for the given PID."""
        try:
            process = psutil.Process(pid)
            return process
        except psutil.NoSuchProcess:
            return None

    @staticmethod
    def suspend_process(pid: int) -> bool:
        """Suspend (pause) a process with the given PID."""
        process = ProcessManager.get_process_by_pid(pid)
        if process:
            process.suspend()
            return True
        return False

    @staticmethod
    def resume_process(pid: int) -> bool:
        """Resume a suspended process with the given PID."""
        process = ProcessManager.get_process_by_pid(pid)
        if process:
            process.resume()
            return True
        return False

    @staticmethod
    def kill_process(pid: int) -> bool:
        """Terminate (kill) a process with the given PID."""
        process = ProcessManager.get_process_by_pid(pid)
        if process:
            process.terminate()
            return True
        return False
