#import pyrealsense2 as rs #Camera library
import time

class Arobot:
	def __init__(self):
		self.angle_robot_z = 0
		self.angle_robot_camera = 90 - 30
		self.robot_radius = 10 #Pendiente
		#self.set_angle_robot_z(-250)

	def set_angle_robot_z(self, giroscopio_z): #Giroscopio eje z, va de -500 a 500
		angle_z = ((giroscopio_z)*(-180))/(-500)
		self.angle_robot_z = angle_z

	def set_angle_robot_camera(self, angle):
		self.angle_robot_camera = 90 - angle

	def get_angle_robot_z(self): #Giroscopio eje z, va de -500 a 500
		#input_angle = int(input("Robot angle?: ")) #OBTENER EL VALOR DE POSICION DEL ROBOT 
		input_angle = 0
		return input_angle
		#return self.angle_robot_z #Return el actual valor

	def get_angle_robot_camera(self, angle):
		return self.angle_robot_camerañ #Return el actual valor

	def actions(self):
		pass #No hacer nada

	def net_cpp_python(self):
		pass

"""if __name__ == '__main__':
    obj_robot = Arobot()
    #print(str(obja.clipping_distance_in_meters)) #Obtener un valor de la clase
    obj_robot.main()"""
