import time

def current_time():
    print(time.strftime('%H:%M:%S'))
    return

def current_date():
    print(time.strftime('%D'))
    return

def current_moment():
    print(time.strftime('%H:%M:%S %D'))
    return

def sleep(n=0):
    time.sleep(n)
    return

def main(log):
    command = log['command']

    if command == 'time':
        return current_time()

    elif command == 'date':
        return current_date()

    elif command == 'full_time' or command == 'ftime':
        return current_moment()

    elif command == 'sleep':
        args = log['args']
        return sleep(int(args[0]))
    else:
        return "#### Undefined Function ####"