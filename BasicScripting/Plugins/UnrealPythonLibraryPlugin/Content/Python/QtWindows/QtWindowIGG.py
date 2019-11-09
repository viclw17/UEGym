import unreal
import sys, os
sys.path.append('C:/Python27/Lib/site-packages')
from PySide import QtGui, QtUiTools
from PySide.QtCore import QFile

import WorldFunctions as wf
import AssetFunctions as af

WINDOW_NAME = 'Qt Window IGG'
# UI_FILE_FULLNAME = __file__.replace('.py', '.ui')
UI_FILE_FULLNAME = os.path.dirname(__file__) + '\QtWindowIGG.ui'

class QtWindowIGG(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowIGG, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed

		# print(os.path.dirname(__file__)) 
		# print(UI_FILE_FULLNAME)
		self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)		

		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		self.setGeometry(600, 300, self.widget.width(), self.widget.height())
		self.initialiseWidget()

	def closeEvent(self, event):
		if self.aboutToClose:
			self.aboutToClose(self)
		event.accept()

	def eventTick(self, delta_seconds):
		self.myTick(delta_seconds)


	##########################################


	def initialiseWidget(self):
		self.time_while_this_window_is_open = 0.0
		self.selectedActor = None
		self.isMove = False
		self.isRotate = False
		self.actor_is_going_up = True
		self.widget.button_Move.clicked.connect(self.moveSelectedActorInScene)
		self.widget.button_Rotate.clicked.connect(self.rotateSelectedActorInScene)
		self.widget.button_Import.clicked.connect(self.importAssets)

	def importAssets(self):
		# static_mesh_fbx = 'D:/Git/UEGym/BasicScripting/Assets/bunny_low.FBX'
		# skeletal_mesh_fbx = 'D:/Git/UEGym/BasicScripting/Assets/SK_FBX_Tube.FBX'
		# task = af.buildImportTask(static_mesh_fbx, '/Game/StaticMeshes/test', af.buildStaticMeshImportOptions())
		# af.executeImportTasks([task])
		unreal.AssetToolsHelpers.get_asset_tools().import_assets_with_dialog('D:/Git/UEGym/BasicScripting/Assets/')


	def moveSelectedActorInScene(self):
		# print("clicked!")
		all_actors = wf.getAllActors(True, None, None, None)
		self.selectedActor = all_actors[0]
		self.isMove = not self.isMove
	
	def rotateSelectedActorInScene(self):
		# print("clicked!")
		all_actors = wf.getAllActors(True, None, None, None)
		self.selectedActor = all_actors[0]
		self.isRotate = not self.isRotate


	def myTick(self, delta_seconds):
		self.time_while_this_window_is_open += delta_seconds
		# self.widget.lbl_Seconds.setText("%.1f Seconds" % self.time_while_this_window_is_open)
		
		if self.selectedActor:
			speed = 300.0 * delta_seconds

			if self.isMove:
				actor_location = self.selectedActor.get_actor_location()
				self.selectedActor.add_actor_world_offset(unreal.Vector(0.0, 0.0, unreal.MathLibrary.sin(speed)), False, False)
				if self.actor_is_going_up:
					if actor_location.z > 500.0:
						self.actor_is_going_up = False
				else:
					speed = -speed
					if actor_location.z < 0.0:
						self.actor_is_going_up = True
				self.selectedActor.add_actor_world_offset(unreal.Vector(0.0, 0.0, speed), False, False)

			if self.isRotate:
				self.selectedActor.add_actor_world_rotation(unreal.Rotator(0.0, 0.0, speed), False, False)


