import tkinter as tk
import os
import pyautogui
import time

class ScreenRecorder:
    window = tk.Tk()
    fps = tk.IntVar(window)
    frame = 0
    pause = tk.BooleanVar(window)
    stop = tk.BooleanVar(window)

    def __init__(self):
        self.window.title("Screen Recorder")
        self.window.geometry("300x50")
        self.window.resizable(False,False)
        self.createDirectories()
        self.createUI()
        self.window.mainloop()

    def createDirectories(self):
        if not(os.path.exists("screenshots")):
            os.makedirs("screenshots")
        os.chdir("screenshots")

    def createUI(self):
        tk.Label(self.window, text="FPS:").pack(side=tk.LEFT, padx=(10,5))
        self.snbxFps = tk.Spinbox(self.window, from_=1, to=60, width=10, textvariable=self.fps)
        self.btnStop = tk.Button(self.window, text="Stop", state="disabled", command=self.stopButton)
        self.btnPause = tk.Button(self.window, text="Pause", state="disabled", command=self.pauseButton)
        self.btnRecord = tk.Button(self.window, text="Record", command=self.recordButton)
        self.packUI()
    
    def packUI(self):
        self.snbxFps.pack(side=tk.LEFT)
        self.btnStop.pack(side=tk.RIGHT, padx=(5,10))
        self.btnPause.pack(side=tk.RIGHT, padx=5)
        self.btnRecord.pack(side=tk.RIGHT, padx=5)

    def stopButton(self):
        self.snbxFps["state"] = "normal"
        self.btnRecord["state"] = "active"
        self.btnStop["state"] = "disabled"
        self.btnPause["state"] = "disabled"
        if self.pause.get():
            self.pauseButton()
        self.stop.set(not(self.stop.get()))
        #Compile pictures into video

    def pauseButton(self):
        self.pause.set(not(self.pause.get()))
        if not(self.pause.get()):
            self.btnPause["text"] = "Pause"
            self.recordLoop()
        else:
            self.btnPause["text"] = "Unpause"
            self.btnRecord["state"] = "disabled"

    def recordButton(self):
        self.snbxFps["state"] = "disabled"
        self.btnPause["state"] = "active"
        self.btnStop["state"] = "active"
        self.btnRecord["state"] = "disabled"
        self.frame = 0
        self.recordLoop()

    def recordLoop(self):
        self.window.update()
        if not(self.pause.get()):
            pyautogui.screenshot().save(str(self.frame) + ".png")
            self.frame += 1
            if not(self.stop.get()):
                self.window.after(int((1/self.fps.get())*1000), self.recordLoop)
        self.stop.set(False)

ScreenRecorder()