import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)  # Splits the date, time, level, and message
    if len(parts) >= 4:
        date_time = f'{parts[0]} {parts[1]}'
        level = parts[2]
        message = parts[3]
        return {'datetime': date_time, 'level': level, 'message': message}
    return {}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("File not found. Please check the path.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Filter the logs by the given level
    filtered_logs = [log for log in logs if log['level'].lower() == level.lower()]
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        level = log['level'].upper()  # Make sure the level is in uppercase for comparison
        if level in counts:
            counts[level] += 1
    return counts

def display_log_counts(counts: dict, requested_level: str = None):
    # Display the headers for statistics
    print(f"{'Рівень логування':<15} | {'Кількість':<10}")
    print("-" * 30)  # A separator line
    
    # Display the counts only for the requested level, if specified
    if requested_level:
        level_upper = requested_level.upper()
        if level_upper in counts:
            print(f"{level_upper:<15} | {counts[level_upper]:<10}")
    else:
        # Display all levels' counts if no specific level is requested
        for level, count in counts.items():
            print(f"{level:<15} | {count:<10}")
    
def display_filtered_logs(filtered_logs: list):
    # Print detailed logs for the specific level
    print("\nDetailed Logs:")
    print("-" * 30)
    for log in filtered_logs:
        print(f"{log['datetime']} {log['level']} {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the log file path.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2].lower() if len(sys.argv) > 2 else None  # Normalize level to lowercase

    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)

    if log_level:
        # When a log level is provided, filter the logs by the specified level
        filtered_logs = filter_logs_by_level(logs, log_level)
        # Display statistics for the requested log level only
        display_log_counts(counts, requested_level=log_level)
        # Display the filtered detailed logs after the table
        display_filtered_logs(filtered_logs)
    else:
        # If no log level is provided, display counts for all levels
        display_log_counts(counts)


# python log_analyzer.py /Users/sabinina/PythonEx/start/HW8/logs.txt