# Christian R
# 5/22/24 Period: 2 
# Take home exam
def print_menu():
    # write something here to welcome user
    print("Welcome to the droid menu")



def create_droid(name, skill, battery_level):
    print(f"Congratulations! You have created the following droid:")
    print(f"Name: {name}")
    print(f"Skill: {skill}")
    print(f"Battery Level: {battery_level}")



def droid_info(name, battery_level):
    print(f"Name: {name}")
    print(f"Current battery level: {battery_level}")



def quick_charge(battery_level):
    print(f"Your battery level was {battery_level}")
    print(f"Your batter level is now {battery_level+5}")
    return battery_level + 5



def long_charge(num_hours, battery_level):
    print(f"Your battery level was {battery_level}")
    if 5 * num_hours + battery_level < 100:
        battery_level = 5 * num_hours + battery_level
        print(f"Your battery level is now {battery_level}")
        return  5 * num_hours + battery_level
    elif 5 * num_hours + battery_level >= 100:
        battery_level = 100
        print(f"Your battery level is now {battery_level}")
        return 100 



def perform_task(task, duration, battery_level):
    print(f"{duration} minutes of {task} is being performed. {battery_level}% battery remains")
    if -(2 * duration) + battery_level >= 0:
        battery_level = -(2 * duration) + battery_level
        print(f"{duration} minutes of {task} is complete. {battery_level}% battery remains")
    elif -(2 * duration) + battery_level < 0:
        print(f"{duration} minutes of {task} failed to be completed, battery was depleted.")



def main():
    print_menu()
    name = "Roomba"
    skill = "Cleaning"
    battery_level = 30
    create_droid(name,skill,battery_level)
    print("\nQuick charge...")
    battery_level = quick_charge(battery_level)
    print("\nStaus check...")
    droid_info(name,battery_level)
    print("\nLong charge...")
    num_hours = int(input("How many hours will you charge?: "))
    battery_level = long_charge(num_hours,battery_level)
    task = "cleaning"
    duration = int(input("\nHow many minutes will you clean?: "))
    perform_task(task,duration,battery_level)
if __name__ == "__main__":
    main()