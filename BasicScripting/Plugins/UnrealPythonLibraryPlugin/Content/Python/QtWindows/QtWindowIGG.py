import unreal
import sys, os
import re
# sys.path.append('C:/Python27/Lib/site-packages')
# sys.path.append
from PySide import QtGui, QtUiTools
from PySide import QtCore

import WorldFunctions as wf
import AssetFunctions as af
import SequencerFunctions as sf

import IGGUnrealBatchRender as br


WINDOW_NAME = 'IGG Unreal'
UI_FILE_FULLNAME = __file__.replace('.py', '.ui') if '.pyc' not in __file__ else __file__.replace('.pyc', '.ui')

class QtWindowIGG(QtGui.QWidget):
	def __init__(self, parent=None):
		super(QtWindowIGG, self).__init__(parent)
		self.aboutToClose = None # This is used to stop the tick when the window is closed
		self.widget = QtUiTools.QUiLoader().load(UI_FILE_FULLNAME)	
		self.widget.setParent(self)
		self.setWindowTitle(WINDOW_NAME)
		# self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # victor
		self.setFixedSize(self.widget.width(), self.widget.height()) # victor
		self.initialiseWidget()

	def closeEvent(self, event):
		if self.aboutToClose:
			self.aboutToClose(self)
		event.accept()

	def eventTick(self, delta_seconds):
		pass

	##########################################

	def initialiseWidget(self):
		##########################################
		# Make folder
		self.widget.button_MakeFolders.clicked.connect(self.makeFolders)  
		# Import
		self.widget.button_Load.clicked.connect(self.loadAssetDialog)
		self.widget.button_ImportFolder.clicked.connect(self.selectImportFolderDialog)
		self.widget.button_ImportSM.clicked.connect(self.importSM)
		# self.widget.button_ImportSK.clicked.connect(self.importSK)
		# self.widget.button_ImportAnim.clicked.connect(self.importAnim) 
		# BatchRender
		self.level = ''
		self.seq = ''
		self.widget.button_LoadLevel.clicked.connect(self.loadLevel)
		self.widget.button_LoadSeq.clicked.connect(self.loadSeq)
		self.widget.button_BatchRender.clicked.connect(self.batchRender)


	def loadAssetDialog(self):
		# hard coded path to X drive
		drivePath = 'X:/Projects/LME_20190708_LordsMobileEncounter/3d/03_Workflow/'
		ret = self.getShotFolderName(
			self.widget.horizontalLayout_CurrentShotTags, 
			self.widget.lineEdit_CurrentShot)
		shotTag = ret[0]
		shotNo = ret[1]  # self.widget.lineEdit_CurrentShot.text()
		shotPath = shotTag + '-' + shotNo
		# print shotPath
		# if not empty, modify the path to point to the shot folder
		tryPath = drivePath + 'Shots/' + shotPath
		# print tryPath
		if not os.path.isdir(tryPath):
			QtGui.QMessageBox.information(self, self.tr(
								"Warning"), self.tr("Provided folder doesn't exist, loading default folder.        "))
		else:
			drivePath = tryPath
		# print drivePath	
		pathToFile = QtGui.QFileDialog.getOpenFileName(self, "Load Asset", 
										drivePath,
										"FBX (*.fbx)") # return (fileNames, selectedFilter)	
		
		# output loaded file name, if not empty
		if pathToFile[0] != '':
			self.widget.lineEdit_Path.setText(pathToFile[0])
			unreal.log_warning("Loading asset: " + pathToFile[0])
		# else:
		# 	if not self.widget.lineEdit_Path.text() :
		# 		QtGui.QMessageBox.warning(self, self.tr(
        #                     "Warning"), self.tr("Please select your asset!        "))


	def selectImportFolderDialog(self):
		contentPath = unreal.Paths.project_content_dir()  # default startup dialog path
		importPath = QtGui.QFileDialog.getExistingDirectory(self, "Select Import Folder",
                                       contentPath,
                                       QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
		if importPath != '':
			importPath = importPath.replace('\\', '/')
			self.widget.lineEdit_ImportPath.setText(importPath)


	# import mesh
	def importSM(self):
		importPath = self.widget.lineEdit_ImportPath.text()
		
		if importPath == '':
			unreal.log_warning(
				'Please load the asset & select import folder in Unreall!')
			QtGui.QMessageBox.warning(self, self.tr(
                            "Warning"), self.tr("Please load the asset & select import folder in Unreal!        "))
			# importPath = importPath.replace('\\', '/')
		else:	
			filePath = self.widget.lineEdit_Path.text()
			fileName = filePath.split('/')[-1].split('.')[0]
			if filePath == '':
				unreal.log_warning(
					'Please load the asset & select import folder in Unreal!')
				QtGui.QMessageBox.warning(self, self.tr(
                                    "Warning"), self.tr("Please load the asset AND select import folder in Unreal!        "))
			else:	
				try:
					importPath = '/Game' + importPath.split('Content')[1]
				except: 
					dialog = QtGui.QMessageBox.warning(self, self.tr("My Application"),
                                            self.tr("Please select valid import path!\n" +
                                                    "Do you want to import into /Content/IGGImport?"),
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.Ok)
					if dialog == QtGui.QMessageBox.Ok:
						importPath = '/Game/IGGImport' 
					else:
						return

				# prepare to import
				option = af.buildSkeletalMeshImportOptions()
				task = af.buildImportTask(filePath, importPath, option)
				info = af.executeImportTasks([task])
				unreal.log_warning('Asset imported into ' + importPath)
				af.showAssetsInContentBrowser([importPath + '/' + fileName])
			

	

	def makeFolders(self):
		if re.match('^[0-9]{4}$', self.widget.lineEdit_ShotNo.text()):
			name = self.getShotFolderName(
				self.widget.horizontalLayout_ShotTags, 
				self.widget.lineEdit_ShotNo)
			path = '/Game/_shot/' + str(name[0]) + '/' + str(name[0]) + '_' + str(name[1])
			# check if folder exists 
			if not unreal.EditorAssetLibrary.does_directory_exist(path):
				af.createShotFolders(name[0], name[1])
			else:
				unreal.log_warning('Folder at ' + path + ' is already exist!')
				QtGui.QMessageBox.warning(self, self.tr(
					"Warning"), self.tr("Folder already exist!        "))
		else:
			QtGui.QMessageBox.warning(self, self.tr(
                            "Warning"), self.tr("Please provide valid shot No.        "))


	def loadLevel(self):
		loadPath = unreal.Paths.convert_relative_path_to_full(
			unreal.Paths.project_content_dir())
		pathToLevel = QtGui.QFileDialog.getOpenFileName(self, "Load Level",
                                                loadPath,
                                                 "Unreal Level (*.umap)")  # return (fileNames, selectedFilter)
		if '.umap' in pathToLevel[0]:
			level = (pathToLevel[0].split('Content/')[1]).split('.umap')[0]
			self.widget.lineEdit_Level.setText(level)
			self.level = '/Game/' + level
			print self.level
		else:
			QtGui.QMessageBox.warning(self, self.tr(
							"Warning"), self.tr("Please pick valid level.        "))

	def loadSeq(self):
		loadPath = unreal.Paths.convert_relative_path_to_full(
			unreal.Paths.project_content_dir())
		pathToSeq = QtGui.QFileDialog.getOpenFileName(self, "Load Sequencer",
                                                  loadPath,
                                                  "Unreal Asset (*.uasset)")  # return (fileNames, selectedFilter)
		
		if '.uasset' in pathToSeq[0]:
			seq = (pathToSeq[0].split('Content/')[1]).split('.uasset')[0]
			# validation
			seqTemp = '/Game/' + seq
			if unreal.EditorAssetLibrary.find_asset_data(seqTemp).asset_class == 'LevelSequence':
				self.seq = seqTemp
				self.widget.lineEdit_Seq.setText(seq)
				print self.seq
			else:
				QtGui.QMessageBox.warning(self, self.tr(
                                    "Warning"), self.tr("Please pick valid sequence asset.        "))
		else:
			QtGui.QMessageBox.warning(self, self.tr(
                            "Warning"), self.tr("Please pick valid sequence asset.        "))

	def batchRender(self):
		if re.match('^[0-9]{4}$', self.widget.lineEdit_RenderShotNo.text()):
			if self.level and self.seq:
				ret = self.getShotFolderName(
					self.widget.horizontalLayout_RenderShotTag, 
					self.widget.lineEdit_RenderShotNo)
				shotTag = ret[0]
				shotNo = ret[1]
				level = self.level 	# self.widget.lineEdit_Level.text()
				seq = self.seq 		# self.widget.lineEdit_Seq.text()
				resolution_id = self.widget.comboBox_Res.currentIndex()
				render_pass_id = self.widget.comboBox_RenderPass.currentIndex()
				cmd = br.makeCommand(shotTag, shotNo, level, seq, resolution_id, render_pass_id)
				br.batchRender(cmd)
			else:
				QtGui.QMessageBox.warning(self, self.tr(
                                    "Warning"), self.tr("Please load level and sequencer.        "))
		else:
			QtGui.QMessageBox.warning(self, self.tr(
                            "Warning"), self.tr("Please provide valid shot number.        "))



	def getShotFolderName(self, tagGroup, no):
		shotTags = (tagGroup.itemAt(i) for i in range(tagGroup.count()))
		shotTag = [i.widget().text() for i in shotTags if i.widget().isChecked()][0]
		shotNo = no.text()
		return (shotTag, shotNo)


	##########################################




	


