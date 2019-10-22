from datetime import time
import time

def frame(title):
    print(200 * '*')
    print(75 * '*' + title + 100 * '*')
    print(200 * '*')


def create_timer(minutes):
    var_start = input("Type 'START' to Start the Timer for 25 minutes :-")

    if var_start == "start":
        print("Timer Will Start for {} minutes".format(minutes))
        timer_loop = True
        min = minutes
        sec = 60

        while timer_loop:
            print(str(round(min)) + ":" + str(round(sec)).zfill(2))
            sec = sec-1
            time.sleep(1)
            if sec < 0:
                min = min-1
                sec=60
                if min==0:
                    print("Buzzzzzzz End of time")
                    break
frame("Pomodoro")
create_timer(25)
