# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:24:00 2022

@author: hadiqa fatima, 98151043
"""

from tkinter import *

class Ball(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title ("Game")
        self.grid()
        canvas_width=800
        canvas_height=400
        self.canvas= Canvas(self, width = canvas_width, height = canvas_height, bg = "black")
        self.canvas.grid(row=1)
        self.lives = 1
        
        ball_diameter = 20
        top_x = 5
        top_y = 5
        ball = self.canvas.create_oval(top_x, top_y, top_x + ball_diameter,top_y+ball_diameter, fill = "blue", tags = "ball")
        horizontal_direction = "east"  
        vertical_direction = "south"
        dx=dy=3.5
        
        self.paddleTopx = 360
        self.paddleTopy = 380
        self.paddleWidth = 80
        self.paddleHeight = 25

        
        self.paddle = self.canvas.create_rectangle(self.paddleTopx, self.paddleTopy, self.paddleTopx+self.paddleWidth,self.paddleTopy+self.paddleHeight, fill = "red", tags = "rect")
    
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress-Left>',self.moveLeft)
        self.canvas.bind('<KeyPress-Right>',self.moveRight)
        
        while True:
            try:
                if horizontal_direction == "east":
                    top_x += dx
                    
                    if top_x >= (canvas_width - ball_diameter):
                        horizontal_direction = "west"
                    self.canvas.move("ball", dx, 0)
                    
                else:
                    top_x -= dx 
                    
                    if top_x <= 0:
                        horizontal_direction = "east"
                    self.canvas.move("ball", -dx, 0)
                    
                if vertical_direction == "south":
                    top_y += dy
                    
                    if top_y >= (canvas_height - ball_diameter):
                        vertical_direction = "north"
                    self.canvas.move("ball", 0, dy)
                    
                    if top_y >= 350:
                        leftPaddle = self.paddleTopx <= top_x <= (self.paddleTopx + 80)
                        rightPaddle = self.paddleTopx <= top_x + 10 <= (self.paddleTopx + 10)
                        if leftPaddle or rightPaddle:
                            vertical_direction = "north"
                            self.canvas.move("ball", 0, dy)
                        
                    if top_y >= 380:
                        self.lives -= 1
                        
                else:
                    top_y -= dy
                    if top_y <= 0:
                        vertical_direction = "south"
                    self.canvas.move("ball", 0, -dy)
                    
            except:
                break
            
            self._label = Label(self)
#end
            if self.lives == 0:
                #self._label = Label(self)
                self.canvas.delete("ball")
                ball = self.canvas.create_oval(2, 2, 2 + ball_diameter, 2 + ball_diameter, fill = "blue", tags = "ball")
                break
            
            self.canvas.after(15)
            self.canvas.update()
            
    def moveLeft(self, event):
        if self.paddleTopx >= 1:
            self.canvas.delete("rect")
            self.paddleTopx -= 6
            
        self.canvas.create_rectangle(self.paddleTopx, self.paddleTopy, self.paddleTopx+ self.paddleWidth, self.paddleTopy+ self.paddleHeight, fill="red", tags = "rect")
        
    def moveRight(self, event):
        if self.paddleTopx <= 720:
            self.canvas.delete("rect")
            self.paddleTopx += 6
            
        self.canvas.create_rectangle(self.paddleTopx, self.paddleTopy, self.paddleTopx+ self.paddleWidth, self.paddleTopy+ self.paddleHeight, fill="red", tags = "rect")
def main():
    Ball().mainloop()
    
main()