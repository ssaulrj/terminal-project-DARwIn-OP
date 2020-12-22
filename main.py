
import cv2 as cv
from matplotlib import pyplot as plt
import time
from time import sleep
import math

from vision import Avision
from procesamiento import Aprocesamiento #Clase de vision
from mapeo import Amapeo, AStarPlanner #Import class from a_star
from robot import Arobot #Clase de robot 

class Amain:
    def __init__(self):
        self.event = 0 #1 Penalty kick / 2 Obstacle run
        self.scaled = 1
        self.width_field = 350//self.scaled #90 width x
        self.height_field = 180//self.scaled #45 height y
        self.grid_size = 5.0

    def set_event(self, number_event):
        self.event = number_event

    def get_event(self):
        return self.event
           
    def main(self):
        print(__file__ + " start!!")

        obj_vision = Avision()
        obj_robot = Arobot() #Inicializar variables en Adarwinop de a_robot.py #print(Adarwinop_obj.angle_robot_camera)
        obj_mapeo = Amapeo(self.width_field, self.height_field, self.scaled, self.grid_size) #Inicializar variables en A_field de a_star.py       
        obj_procesamiento = Aprocesamiento(obj_mapeo, obj_robot, obj_vision) #Inicializar variables en A_vision -> clase Acamera

        #self.set_robot_obstacles_pos(Afield_obj, Adarwinop_obj,150, 50, 50)
        
        obj_mapeo.Aplot_obstacle(40, 60, 25) #Objeto identificado, ejemplo
        obj_mapeo.Aplot_obstacle(100, 80, 50) #Objeto identificado, ejemplo

        #while True: #Ubicacion de robot(x,y) y de pelota(x,y)
            #self.set_robot_ball_pos(Afield_obj, Adarwinop_obj)
        obj_procesamiento.main()
        obj_mapeo.Aplot_ball_robot()

if __name__ == '__main__':
    obj_main = Amain()
    #Inicio de programa
    obj_main.main()