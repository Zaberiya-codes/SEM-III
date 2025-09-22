from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkcalendar import DateEntry
import json
import os

#main window
app = Window(themename="minty")
app.title("Cozy Study Planer")
app.geometry("550x650")
app.resizable(False,False)

#variables
subject_var= StringVar()
topic_var= StringVar()
time_var= StringVar()
date_var= StringVar()

#inputs
Label(app, text="Subject:").pack()
Entry(app, textvariable=subject_var, width=40).pack(pady=5)

Label(app, text="topic:").pack()
Entry(app, textvariable=topic_var, width=40).pack(pady=5)

Label(app, text="Time(e.g 4.00 PM):").pack()
Entry(app, textvariable=time_var, width=40).pack(pady=5)

Label(app, text="Enter Date (YYYY-MM-DD):").pack()
Entry(app, textvariable=date_var, width=40).pack(pady=5)

# Label(app, text="Select Date:").pack()
# calendar = DateEntry(app, textvariable= date_var, width= 18)
# calendar.pack(pady=5)

#creating task frame to show tasks
task_frame= Frame(app)
task_frame.pack(pady=20, fill=BOTH, expand=YES)
tasks= []

#defining a function to add tasks 
def add_task():
    subject = subject_var.get().strip()
    topic = topic_var.get().strip()
    time = time_var.get().strip()

    if subject and topic and time:
        task_text = f"📚 {subject} - {topic} at {time}"
        label = ttk.Label(task_frame, text=task_text, font=("Helvetica", 12), bootstyle="info")
        label.pack(pady=2)
        tasks.append(label)

        # Clear input fields after adding
        subject_var.set("")
        topic_var.set("")
        time_var.set("")
    else:
        print("Please fill in all fields.")

#add button
Button(app, text="Add Task", command=add_task, bootstyle="success").pack(pady=10)
app.mainloop()

