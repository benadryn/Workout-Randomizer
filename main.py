import json
from tkinter import *
from random import choice, randint

FONT = ("consolas", 14, "bold")


part = ''
new_data = {}
workout_object_list = []
workouts_to_print = ''
workout_amount = 1
count = 0


def reset_workout_items():
    global part, workouts_to_print, workout_object_list, count
    part = ''
    workouts_to_print = ''
    workout_object_list = []
    count = 0


def get_part():
    global new_data
    with open("workout_data.JSON") as data:
        new_data = json.load(data)


def post_data():
    global part, new_data, workouts_to_print, workout_amount
    if not workout_object_list:
        for index in new_data[part]:
            workout_object_list.append(index)
    if workout_amount > 9:
        workout_amount = 9
    while count != workout_amount:
        check_doubles()


def check_doubles():
    global part, new_data, workouts_to_print, workout_amount, count
    rand_choice = choice(workout_object_list)
    last_workout = f"\n{rand_choice}: {new_data[part][rand_choice][randint(0, len(new_data[part][rand_choice]) - 1)]}"
    if last_workout not in workouts_to_print:
        workouts_to_print += last_workout
        count += 1


class WorkoutInterface:
    def __init__(self):
        self.workouts = []
        self.window = Tk()
        self.window.title("Workout randomizer")
        self.window.config(pady=20, padx=20, bg="black")
        # Entries
        self.entry = Entry(width=10)
        self.entry.grid(column=11, row=0)
        self.entry.focus()
        self.entry.insert(END, "Max 9")
        # Entry label
        self.entry_label = Label(text="Number of workouts:", bg="black", fg="white")
        self.entry_label.grid(column=10, row=0)
        # Canvas5
        self.canvas = Canvas(width=400, height=400, bg="black", highlightthickness=0)
        self.c_text = self.canvas.create_text(200, 200, width=380, text="", fill="white", font=FONT)
        self.canvas.grid(column=0, row=0, columnspan=9)
        # Buttons
        self.shoulder_button = Button(text="Shoulders", command=self.press_shoulder)
        self.shoulder_button.grid(column=1, row=1)
        self.back_button = Button(text="Back", command=self.press_back)
        self.back_button.grid(column=2, row=1)
        self.triceps_button = Button(text="Triceps", command=self.press_triceps)
        self.triceps_button.grid(column=3, row=1)
        self.biceps_button = Button(text="Biceps", command=self.press_biceps)
        self.biceps_button.grid(column=4, row=1)
        self.forearms_button = Button(text="Forearms", command=self.press_forearms)
        self.forearms_button.grid(column=5, row=1)
        self.chest_button = Button(text="Chest", command=self.press_chest)
        self.chest_button.grid(column=6, row=1)
        self.legs_button = Button(text="Thighs/Hips", command=self.press_thighs_hips)
        self.legs_button.grid(column=7, row=1)
        self.calves_button = Button(text="Calves", command=self.press_calves)
        self.calves_button.grid(column=8, row=1)
        self.abs_button = Button(text="Abs", command=self.press_abs)
        self.abs_button.grid(column=9, row=1)
        self.window.mainloop()

    def press_button(self, passed_part):
        global part, new_data, workouts_to_print, workout_amount
        try:
            workout_amount = int(self.entry.get())
        except ValueError:
            workout_amount = 0
        part = passed_part
        get_part()
        post_data()
        self.canvas.itemconfig(self.c_text, text=workouts_to_print.title())
        reset_workout_items()

    def press_chest(self):
        self.press_button("chest")

    def press_forearms(self):
        self.press_button("forearms")

    def press_biceps(self):
        self.press_button("biceps")

    def press_triceps(self):
        self.press_button("triceps")

    def press_shoulder(self):
        self.press_button("shoulders")

    def press_back(self):
        self.press_button("back")

    def press_thighs_hips(self):
        self.press_button("thighs/hips")

    def press_calves(self):
        self.press_button("calves")

    def press_abs(self):
        self.press_button("abs")


workout = WorkoutInterface()
