#CSC-11300 Final Project
#DrawPieChart.py
#Description: This code creates GUI and draws the pie chart

from Frequency import *
import tkinter as tk
import turtle

def key_maxval(dic):  # return key of dictionary dic with max value, helper fucntion
    val = list(dic.values())
    key = list(dic.keys())
    return key[val.index(max(val))]

def draw():
    #Reset the canvas
    canvas.delete("all")

    #Set up the turtle
    t = turtle.RawTurtle(canvas)    # create turtle object
    t.hideturtle()  # hide turtle cursor
    t.radians()     #set turtle to radian mode
    n = int(entry_field.get())
    angles = myFrequency.angle_dict.copy()  # copy of letter_angle dictionary we can safely alter
    colors = ["black", "purple", "gray25", "magenta3", "gray45",
              "deep pink", "gray65", "medium purple", "gray85", "royal blue", "slate gray",
              "DeepSkyBlue2", "LightSkyBlue4", "pink", "green", "red", "blue", "orange", "purple",
              "black", "pink", "green", "red", "blue", "orange", "purple",
              "black", "pink", ]  # color list for turtle to cycle through for each pie slice
    color_index = 0  # index of place in colors array
    radius = 150
    total = 0  # sum of radian angles of pie slices looped through so far # FYI I changed the variable sum to tal
    label_radius = radius * 1.25  # radius to write labels too
    t.color(colors[color_index])  # initial color
    t.setpos(0, radius * -1)  # initial position of turtle
    while n >= 0:
        key = key_maxval(angles)  # save key of max value in angles dic

        t.fillcolor(colors[color_index])  # set slice color
        t.color(colors[color_index])  # set pen color
        color_index = color_index + 1
        t.begin_fill()

        if n == 0:  # final iteration uses 2pi - sum as the angle
            # draw final pie slice
            position = t.position()  # save position to draw next arc from
            t.circle(radius, 2 * math.pi - total)  # draw arc
            t.home()  # send turtle back to origin to create pie shape

            # label
            t.setheading(total - math.pi/2 + (2 * math.pi - total)/2)  # set direction of where label needs to be
            t.penup()
            t.forward(label_radius + 25)  # move turtle to label loaction
            t.write("all other\nletters" + "\n" + str(round((2 * math.pi - total) / (2 * math.pi) * 100, 2)) + "%", font=("Calibri", 12, "bold"))  # write label
            t.home()
            t.pendown()

        else:
            # draw pie slice
            t.circle(radius, angles[key])  # draw arc
            position = t.position()  # save position to draw next arc from
            t.home()

            # label
            t.setheading(total - math.pi/2 + (angles[key] / 2))  # set direction of where label needs to be
            t.penup()
            t.forward(label_radius)  # move turtle to label loaction
            t.write(key + "\n" + str(round((myFrequency.prob_dict[key] * 100), 2)) + "%", font=("Calibri", 12, "bold"))  # write label
            t.home()
            t.pendown()

        t.end_fill()  # fill in slice shape with color
        t.setpos(position)  # return turtle to position next arc must start from

        total = total + angles[key]  # add to sum
        t.setheading(total)  # set turtle to correction direction

        angles.pop(key)  # remove key of max value form angle dic
        n = n - 1  # decrement n


####################
#       GUI
####################
root = tk.Tk()
root.title('CSC-11300 Final Project')
root.geometry('600x600')

#Prompt the user to enter n
prompt = tk.Label(text = 'How many most frequent letters to display:', font = ('Calibri', 18))
prompt.grid(column = 0, row = 0)

#Entry field
entry_field = tk.Entry()
entry_field.grid(column = 0, row = 1)

#Button
button = tk.Button(text = 'Submit', command=draw)   #Once button clicked, draw() is called
button.grid(column = 0, row = 2)

#Canvas for turtle to draw on
canvas = tk.Canvas(root, width=600, height=500, background = 'white')
canvas.grid(column = 0, row = 3)

#Read all the info to myFrequency
myFrequency = Frequency()

#n most frequent letters to display
n = 0

root.mainloop
