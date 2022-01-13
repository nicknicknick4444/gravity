"""Generates a dictionary to calculate falling speed in m\s, then asks the user for input re. time and speed. Eounds up or down liberally when performing lookups."""

def gravity(sec):
    return round(sec*9.8,2)

def make_dict():
    grav_dict={}
    for i in range(7):
        grav_dict[i] = gravity(i)
    return grav_dict

def time(t,grav_dict):
    t = int(round(t))
    for i in grav_dict:
        if i == t:
            return round(grav_dict[i],2)
        elif t >= len(grav_dict):
            return grav_dict[6]

def speed(s,grav_dict):
    s = int(round(s,0))
    for key in grav_dict:
        if key > 0 and key < 6:
            if s <= grav_dict[key]:
                if s > (grav_dict[key-1]+(grav_dict[key]-grav_dict[key-1])/2) and s <= grav_dict[key]:
                    return grav_dict[key], key
                elif s < grav_dict[1]/2:
                    return 888, key
                else:
                    return grav_dict[key-1], key-1
        elif key == 6 and s > grav_dict[key]:
            return 555, key
        elif key == 0 and s <= 0:
            return 0, key

def time_ask(grav_dict):
    ti = input("How many seconds has the ball been falling for? ")
    try:
        if ti.isdigit() or isinstance(float(ti),float):
            pass
    except ValueError:
        return time_ask(grav_dict)
    else:
        if isinstance(float(ti),float):
            ti = int(round(float(ti),0))
        else:
            ti = int(ti)
    sp = time(ti,grav_dict)
    if sp == 0 or sp == None:
        print("You haven't let go of the ball yet.\n")
    else:
        print("The ball is falling at about {} meters/second.\n".format(sp))

def speed_ask(grav_dict):
    sp = input("How many meters/second is your ball falling at? ")
    try:
        if sp.isdigit() or isinstance(float(sp),float):
            pass
    except ValueError:
        return speed_ask(grav_dict)
    else:
        if isinstance(float(sp),float):
            sp = int(round(float(sp),0))
        else:
            sp = int(sp)
        ti = speed(sp,grav_dict)
        if ti[0] == 555:
            print("Your ball has been falling for at least {} seconds.\n".format(ti[1]))
        elif ti[0] == 888:
            print("Your ball hasn't even fallen for a second yet.\n")
        elif ti[0] == 0 or ti[0] == None:
            print("You haven't let go of the ball yet.\n")
        elif ti[1] == 1:
            print("Your ball has been falling for about {} second.\n".format(ti[1]))
        else:
           print("Your ball has been falling for about {} seconds.\n".format(ti[1]))

def go_again():
    again = input("Go again? (y/n) ")
    if again == "y":
        print()
        return main()
    else:
        print("Bye!")

def main():
    grav_dict = make_dict()
    print(grav_dict)
    print()
    time_ask(grav_dict)
    speed_ask(grav_dict)
    go_again()

if __name__ == "__main__":
    main()
