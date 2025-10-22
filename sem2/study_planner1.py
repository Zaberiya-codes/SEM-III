import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime
import json
import os

# Setup the window
app = ttk.Window(themename="minty", title="🌿 Cozy Study Planner", size=(550, 650))
app.resizable(False, False)

# Title
ttk.Label(app, text="🌿 My Cozy Study Planner", font=("Comic Sans MS", 20, "bold")).pack(pady=15)

# Input frame
input_frame = ttk.Frame(app, padding=10)
input_frame.pack(pady=10)

subject_var = ttk.StringVar()
topic_var = ttk.StringVar()
time_var = ttk.StringVar()

ttk.Entry(input_frame, textvariable=subject_var, width=30, placeholder="Subject").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=topic_var, width=30, placeholder="Topic").grid(row=1, column=0, padx=5, pady=5)
ttk.Entry(input_frame, textvariable=time_var, width=30, placeholder="Time (e.g. 5 PM)").grid(row=2, column=0, padx=5, pady=5)

# Task list frame with scrollable canvas
task_canvas = ttk.Canvas(app, height=300)
scroll_y = ttk.Scrollbar(app, orient="vertical", command=task_canvas.yview)
task_list_frame = ttk.Frame(task_canvas)

task_list_frame.bind(
    "<Configure>",
    lambda e: task_canvas.configure(
        scrollregion=task_canvas.bbox("all")
    )
)

task_canvas.create_window((0, 0), window=task_list_frame, anchor="nw")
task_canvas.configure(yscrollcommand=scroll_y.set)

task_canvas.pack(side="left", fill="both", expand=True, padx=(20, 0))
scroll_y.pack(side="right", fill="y", padx=(0, 20))

tasks = []

# Add task function
def add_task():
    subject = subject_var.get().strip()
    topic = topic_var.get().strip()
    time = time_var.get().strip()

    if subject and topic and time:
        task_text = f"📚 {subject} — {topic} @ {time}"
        label = ttk.Label(task_list_frame, text=task_text, font=("Helvetica", 12), bootstyle="info", padding=5)
        label.pack(pady=5, fill="x", padx=10)
        tasks.append(label)

        subject_var.set("")
        topic_var.set("")
        time_var.set("")

# Save/load functions
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump([t.cget("text") for t in tasks], f)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            for text in json.load(f):
                label = ttk.Label(task_list_frame, text=text, font=("Helvetica", 12), bootstyle="info", padding=5)
                label.pack(pady=5, fill="x", padx=10)
                tasks.append(label)

# Buttons
button_frame = ttk.Frame(app)
button_frame.pack(pady=15)

ttk.Button(button_frame, text="➕ Add Task", command=add_task, bootstyle="success-outline").pack(side="left", padx=10)
ttk.Button(button_frame, text="💾 Save", command=save_tasks, bootstyle="secondary-outline").pack(side="left", padx=10)
ttk.Button(button_frame, text="📂 Load", command=load_tasks, bootstyle="secondary-outline").pack(side="left", padx=10)

# Load saved tasks on startup
load_tasks()

# Run the app
app.mainloop()
