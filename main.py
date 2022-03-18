from types import new_class
from alarm_clock import AlarmClock

new_alarm_clock = AlarmClock()
new_alarm_clock.get_current_time()
new_alarm_clock.set_current_time("12:00")
new_alarm_clock.get_current_time()
new_alarm_clock.get_alarm_status()
new_alarm_clock.toggle_alarm()
new_alarm_clock.get_alarm_status()