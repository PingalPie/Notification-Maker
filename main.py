'''
This reminder is for drinking water
==================================================
In this program we are using plyer module
So, make sure you have installed plyer module
--------------------------------------------------
For windows process to install plyer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Step 1 -> Open command prompt
Step 2 -> Type pip install plyer
Done!
==================================================
For Mac/Unix process to install plyer
Step 1 -> Open terminal
Step 2 -> type pip install plyer
Done!
'''
from plyer import notification
# modules required


if __name__ == '__main__':
    notification.notify(
        title= "Please drink water",
        # Here is title you can change it
        message= "Drink water or I'll call your mom",
        # Here is the message for you
        app_icon="C:\\PycharmProjects\\reminder\\Iconsmind-Outline-Glass-Water.ico",
        # Here icon path will come
        timeout=0
        # Here is the timer to cancel the notification, In 0 you will have to close it manually
    )
