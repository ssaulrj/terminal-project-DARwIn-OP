import time
import numpy as np
import pyrealsense2 as rs
import math

class Avision:
	def __init__(self):
		self.width, self.height, self.framerates = 424, 240, 30
		self.pipeline = rs.pipeline() # Create a pipeline
		self.config = rs.config()
		self.config.enable_stream(rs.stream.depth, self.width, self.height, rs.format.z16, self.framerates)
		self.config.enable_stream(rs.stream.color, self.width, self.height, rs.format.bgr8, self.framerates) #3' framerate
		self.profile = self.pipeline.start(self.config) #Start streaming
		self.depth_sensor = self.profile.get_device().first_depth_sensor() #Getting the depth sensor's depth scale
		self.depth_scale = self.depth_sensor.get_depth_scale() #Getting depth scale 
		print("Depth Scale is: " , self.depth_scale)

		#Remove background of objects more than clipping_distance_in_meters x(1) away
		self.clipping_distance_in_meters = 2 #Metros
		self.clipping_distance = self.clipping_distance_in_meters / self.depth_scale
		self.align_to = rs.stream.color # Create an align object
		self.align = rs.align(self.align_to)
		self.depth_image = 65.7 #Matriz de profundidad
		self.color_intrin = 0
		time.sleep(1.0)

        #Obtener datos--------------------------------------------------------------------------------------------------------------------------------------
	def get_image_depth(self): #Filtrar imagen mayor a ciertas distancias
		frames = self.pipeline.wait_for_frames() # Get frameset of color and depth
		aligned_frames = self.align.process(frames) # Align the depth frame to color frame
		aligned_depth_frame = aligned_frames.get_depth_frame() # Get aligned frames
		color_frame = aligned_frames.get_color_frame()
		self.color_intrin = aligned_depth_frame.profile.as_video_stream_profile().intrinsics #? DUDA DE QUE ES 

		#if not aligned_depth_frame or not color_frame: # Validate that both frames are valid
		    #continue #Error, continue debe estar en loop

		self.depth_image = np.asanyarray(aligned_depth_frame.get_data())
		self.color_image = np.asanyarray(color_frame.get_data())
		color_removed = 1 # Remove background - Set pixels further than clipping_distance to color de fondo, 1 = black
		depth_image_3d = np.dstack((self.depth_image,self.depth_image,self.depth_image)) #depth image is 1 channel, color is 3 channels
		self.bg_removed = np.where((depth_image_3d > self.clipping_distance) | (depth_image_3d <= 0), color_removed, self.color_image)
		return self.bg_removed

	def get_width_objs(self, x, y, w, h, var_limits_inside):  #Obtener ancho de ciertas coordenadas
		ix1, iy1, iz1 = x+var_limits_inside, y+round(h/2), (self.depth_image[y+round(h/2),x+var_limits_inside])/10
		ix2, iy2, iz2 = x+w-var_limits_inside, y+round(h/2), (self.depth_image[y+round(h/2),x+w-var_limits_inside])/10
		point1 = rs.rs2_deproject_pixel_to_point(self.color_intrin, [ix1, iy1], iz1)
		point2 = rs.rs2_deproject_pixel_to_point(self.color_intrin, [ix2, iy2], iz2)
		return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2) + math.pow(point1[2] - point2[2], 2))

	def x(self):
		pass