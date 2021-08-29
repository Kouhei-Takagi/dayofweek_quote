from tkinter import messagebox
import datetime
import random

weekday = datetime.date.today().weekday()

with open("/Users/takagikouhei/Desktop/Python/20210820/quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

if weekday == 0:
    messagebox.showinfo('Monday', f'Monday.\n{quote}')
elif weekday == 1:
    messagebox.showinfo('Tuesday', f'Tuesday.\n{quote}')
elif weekday == 2:
    messagebox.showinfo('Wednesday', f'Wednesday.\n{quote}')
elif weekday == 3:
    messagebox.showinfo('Thursday', f'Thursday.\n{quote}')
elif weekday == 4:
    messagebox.showinfo('Friday', f'Friday.\n{quote}')
else:
    messagebox.showinfo('Weekend', f'Weekend!.\n{quote}')