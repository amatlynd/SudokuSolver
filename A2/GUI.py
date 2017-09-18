import Tkinter
import time

next = 0
button_text = ''

#prints matrix
def printMatrix(s):
    newS = ''
    count = 0
    for i in s:
        count += 1
        newS = newS + i + ' '
        if (count%3 == 0 and count%9 != 0):
            newS += '| '
        if (count%9 == 0):
            if (count%27 == 0 and count != 81):
                newS += '\n------+--------+------'
            newS += '\n'
    return newS

#GUI pops up
def display_GUI(states):
    global next
    global button_text
    def close_window():
        root.destroy()
    def update2(states):
        update(states)
        w.after(400, lambda: update2(states))
        
            
    def update(states):
        global next
        global button_text
        if next < len(states) - 1:
            next += 1
            button_text = 'Next Step'
        else:
            button_text = 'Done'
            b.configure(command = close_window)
        b.configure(text = button_text)
        updated_text = printMatrix(states[next])

        w.configure(text = updated_text)
    root = Tkinter.Tk()
    w = Tkinter.Label(root, text = 'Sudoku Solver')

    button_text = 'Click to step'
    b = Tkinter.Button(root, text = button_text, command =lambda: update(states))
    c = Tkinter.Button(root, text = 'Dynamic Generation', command =lambda: update2(states))
    w.pack()
    b.pack()
    c.pack()

    root.mainloop()

