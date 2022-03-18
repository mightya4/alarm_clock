class AlarmClock:
    def __init__(self):
        self.is_on = False
        self.time = ""
    #Toggle the alarm clocks's on off switch    
    def toggle_alarm(self):
        self.is_on = not self.is_on

    #Print the current status of the alarm
    def get_alarm_status(self):
        if self.is_on == False:
            print(f"The alarm is currently set to alarm.")
        else:
            print(f"The alarm is currently not set to alarm.")

    #Change the current time
    def set_current_time(self , time):
        self.time = time

    def get_current_time(self):
        print(f"current time : {self.time}")

