import unreal
import sys, os
sys.path.append('C:/Python27/Lib/site-packages')
from PySide import QtGui, QtUiTools
from PySide import QtCore

import WorldFunctions as wf
import AssetFunctions as af
import SequencerFunctions as sf


WINDOW_NAME = 'IGG Unreal'
# UI_FILE_FULLNAME = __file__.replace('.py', '.ui')
UI_FILE_FULLNAME = os.path.dirname(__file__) + '\QtWindowIGG.ui'

class QtWindowIGG(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowIGG, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed
		self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)	
		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # victor
		self.setFixedSize(self.widget.width(), self.widget.height()) # victor
		self.setGeometry(100, 100, self.widget.width(), self.widget.height())
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
		
		# self.widget.button_Move.clicked.connect(self.moveSelectedActorInScene)
		# self.widget.button_Rotate.clicked.connect(self.rotateSelectedActorInScene)
		self.widget.button_MakeFolders.clicked.connect(self.makeFolders)  
		self.widget.button_Load.clicked.connect(self.loadAssetDialog)
		self.widget.button_ImportFolder.clicked.connect(self.selectImportFolderDialog)
		# import mesh
		self.widget.button_ImportSM.clicked.connect(self.importSM)
		# self.widget.button_ImportSK.clicked.connect(self.importSK) addSkeletalAnimationTrackOnActor_EXAMPLE
		# self.widget.button_ImportAnim.clicked.connect(self.importAnim) 

	# TODO
	# def importAnim(self):
		# sf.addSkeletalAnimationTrackOnActor_EXAMPLE()
		# print 'importAnim'
	
	# dialog - select asset
	def loadAssetDialog(self):
		# hard coded path to X drive
		drivePath = 'X:/Projects/LME_20190708_LordsMobileEncounter/3d/03_Workflow/'
		# get current shot folder name
		shotPath = self.widget.lineEdit_CurrentShot.text()
		# if not empty, modify the path to point to the shot folder
		if shotPath != '':
			drivePath = drivePath + 'Shots/' + shotPath
		# open file dialog to load fbx
		pathToFile = QtGui.QFileDialog.getOpenFileName(self, "Load Asset", 
										drivePath,
										"FBX (*.fbx)") # return (fileNames, selectedFilter)	
		# output loaded file name, if not empty
		if pathToFile[0] != '':
			self.widget.lineEdit_Path.setText(pathToFile[0])
			unreal.log_warning("Loading asset: " + pathToFile[0])
	
	# dialog - select import folder
	def selectImportFolderDialog(self):
		# open file dialog to select import folder
		# startup dialog path
		contentPath = unreal.Paths.project_content_dir()
		importPath = QtGui.QFileDialog.getExistingDirectory(self, "Select Import Folder",
                                       contentPath,
                                       QtGui.QFileDialog.ShowDirsOnly
                                       | QtGui.QFileDialog.DontResolveSymlinks)
		if importPath != '':
			importPath = importPath.replace('\\', '/')
			self.widget.lineEdit_ImportPath.setText(importPath)

	# import mesh
	def importSM(self):
		importPath = self.widget.lineEdit_ImportPath.text()
		
		if importPath != '':
			importPath = importPath.replace('\\', '/')
			
			try:
				importPath = '/Game' + importPath.split('Content')[1]
			except:
				unreal.log_warning('Please select valid import path!')
				unreal.log_warning('Asset imported into default pass: /Game/IGGImport')
				importPath = '/Game/IGGImport'
			# finally:
				# this runs anyway!
			filePath = self.widget.lineEdit_Path.text()
			fileName = filePath.split('/')[-1].split('.')[0]

			# prepare to import
			# option = af.buildStaticMeshImportOptions()
			
			option = af.buildSkeletalMeshImportOptions()
			if filePath != '':
				task = af.buildImportTask(filePath, importPath, option)
				info = af.executeImportTasks([task])
				unreal.log_warning('Asset imported into ' + importPath)
				af.showAssetsInContentBrowser([importPath + '/' + fileName])
			else:
				unreal.log_warning('Please load the asset AND select import folder!')
		else:
			unreal.log_warning('Please load the asset AND select import folder!')

	# def importSK(self):
	# 	filePath = self.widget.lineEdit_Path.text()
	# 	option = af.buildSkeletalMeshImportOptions()
	# 	task = af.buildImportTask(filePath, '/Game/_shot/', option)
	# 	info = af.executeImportTasks([task])

	def getShotFolderName(self):
		shotTags = []
		shotTags.append(self.widget.shotTag_BT)
		shotTags.append(self.widget.shotTag_JG)
		shotTags.append(self.widget.shotTag_DEV)
		shotTags.append(self.widget.shotTag_PJG)
		shotTag  = None
		for item in shotTags:
			if item.isChecked():
				shotTag = item.text()
		shotNo = self.widget.lineEdit_ShotNo.text()
		return [shotTag, shotNo]

	def makeFolders(self):
		name = self.getShotFolderName()
		if name[0] and name[1]:
			path = '/Game/_shot/' + str(name[0]) + '/' + str(name[0]) + '_' + str(name[1])
			if not unreal.EditorAssetLibrary.does_directory_exist(path):
				af.createShotFolders(name[0], name[1])
			else:
				unreal.log_warning('Folder at ' + path + ' is already exist!')
	

	##########################################

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


