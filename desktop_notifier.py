from plyer import notification
import time
if __name__ == "__main__":
        while True: 
            notification.notify(
                title = "Workout time",
                message = "Time out. Get ready for next exercise.",
                app_icon = "",
                timeout = 5
            )
            time.sleep(10)


# to run this program in background in cmd pythonw file_name
# to stop it go to tsk manager search file and end task