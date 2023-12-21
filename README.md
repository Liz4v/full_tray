Full Tray
=========

Windows 11 will always hide new icons in the system tray.
This is a problem for some self-updating packages like Discord and Google Drive.

I used a registry diff tool and found out this registry value:

    HKEY_CURRENT_USER\Control Panel\NotifyIconSettings\<uint64>\IsPromoted

The value is absent until set in Control Panel. We can automate this!


First Run
---------

* Install the latest Python from the Microsoft Store. As of writing, it's 3.12
  ([link](https://www.microsoft.com/store/productId/9NCVDN91XZQP)).
* Get `full-tray.pyw` and put it anywhere it makes sense for you. Remember where it is.
* Double-click `full-tray.pyw`.
  * You may be asked to choose Python to open it with.
  * Choose the one you installed and click `Always`.
* The script runs silently. Any hidden icons should now be visible and nothing else will happen.

This change is not permanent yet.

Scheduled Task
--------------

The script needs to run repeatedly to catch those pesky self-updating packages.

* Press the Windows key and type `Scheduler`. Select `Task Scheduler`.
* Click `Create Task...` on the right.
* In `General`, name it `Full Tray` or whatever you want. Leave the rest as default.
* Go to the `Triggers` tab, click `New...`.
  * Set it to what makes sense to you. I chose `At log on` and `Repeat task every: 1 hour`.
* Go to the `Actions` tab, click `New...`.
  * Set the program/script to wherever you put `full-tray.pyw`.
* Click `OK` and you're done! You can see your task at `Task Scheduler Library`.
