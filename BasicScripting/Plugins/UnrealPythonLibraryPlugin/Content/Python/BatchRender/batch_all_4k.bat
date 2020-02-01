@ECHO ON
cd "\D:\p4\2019.1_galaxy\render\gm_s0000"
call ambientocclusion_dx12.bat
call custombuffer2_dx12.bat
call customstencil_dx12.bat
call finalimage_dx12.bat
call scenedepth_dx12.bat
call shadingmodel_dx12.bat
call velocity_dx11.bat
call worldnormal_dx12.bat
call worldposition_dx11.bat
::
::
::"D:\p4\2019.1_galaxy\UnrealEngine\Engine\Binaries\Win64\UE4Editor.exe" "D:\p4\2019.1_galaxy\UnrealEngine\galaxymobile_01\galaxymobile_01.uproject" /Game/_shots/gm_0000/ue4master/map/s0000_loadermap -DX12 -game -MovieSceneCaptureType="/Script/MovieSceneCapture.AutomatedLevelSequenceCapture" -LevelSequence="/Game/_shots/gm_0000/ue4master/sequence/s0000_seq" -NoLoadingScreen -Windowed -ResX=3840 -ResY=2160 -ForceRes -MovieFrameRate=24 -NoTextureStreaming -MovieFolder="D:\Renders\GalaxyMobile\__s0000_PROVIDE_DESCRIPTION_RENAME" -MovieFormat=CustomRenderPasses -MovieQuality=100 -MovieName="gm_s0000_{material}_{frame}" -MovieCinematicMode=Yes -MovieWarmUpFrames=100 -MovieDelayBeforeWarmUp=3 -MovieStartFrame=0990 -MovieEndFrame=1001 -NoScreenMessages -CustomRenderPasses="AmbientOcclusion,CustomBuffer2,CustomStencil,FinalImage,SceneDepthWorldUnits,ShadingModel,Velocity,WorldNormal,WorldPosition" -CaptureFramesInHDR=1 -HDRCompressionQuality=1 -CaptureGamut="HCGM_Rec709"