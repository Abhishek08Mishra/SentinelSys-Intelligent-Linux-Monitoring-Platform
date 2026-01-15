import psutil
from datetime import datetime
import csv
import os
from config import CSV_FILE, LOG_DIR

def system_metrics():
    try :
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent

        return [{
            "timestamp" : timestamp,
            "cpu_usage" : cpu_usage,
            "memory_usage" : memory_usage,
            "disk_usage": disk_usage
        }]
    
    except Exception as e :
        print(str(e))
        return []

file_exists = os.path.isfile("sys_data.csv")


def save_metrics_with_logging(sys_info, headers, csv_file=CSV_FILE, log_dir=LOG_DIR):
    
    """
    Saves system metrics to CSV and logs success/failure with timestamp.

    Args:
        sys_info (list of dict): List of system metric dictionaries
        headers (list of str): CSV column headers
        csv_file (str): Path to CSV file
        log_dir (str): Directory to store logs

    Returns:
        bool: True if CSV write was successful, False otherwise
    """

    # Ensure log directory exists
    """
    Creates the log directory if it does not exist and returns paths for
    success and error log files along with a current timestamp.
    """
    os.makedirs(log_dir, exist_ok=True)
    success_log = os.path.join(log_dir, "success.log")
    error_log = os.path.join(log_dir, "error.log")
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    try:
        # Check if CSV exists
        file_exists = os.path.isfile(csv_file)

        # Write to CSV
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            if not file_exists:
                writer.writeheader()

            writer.writerows(sys_info)

        # Log success
        with open(success_log, "a") as f:
            f.write(f"{time_stamp} - File updated successfully\n")

        return True

    except Exception as e:
        # Log error
        with open(error_log, "a") as f:
            f.write(f"{time_stamp} - Failed to update file. Error: {str(e)}\n")

        return False
    
headers = ["timestamp", "cpu_usage", "memory_usage", "disk_usage"]

sys_info = system_metrics()

# Called combined function
save_metrics_with_logging(sys_info, headers)