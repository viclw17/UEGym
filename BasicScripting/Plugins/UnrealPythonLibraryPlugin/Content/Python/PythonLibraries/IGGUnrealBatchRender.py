from subprocess import call
import unreal
import os

input_render_pass = \
    [['FinalImage', 'DX12'],
     ['ShadingModel', 'DX12'],
     ['SceneDepthWorldUnits', 'DX12'],
     ['WorldNormal', 'DX12'],
     ['Velocity', 'DX11'],
     ['AmbientOcclusion', 'DX12'],
     ['CustomBuffer2', 'DX12'],
     ['CustomStencil', 'DX12'],
     ['WorldPosition', 'DX11'],
     ['AmbientOcclusion,FinalImage', 'DX12'],
     ['CustomBuffer2,CustomStencil,ShadingModel', 'DX12'],
     ['SceneDepthWorldUnits,WorldNormal', 'DX12'],
     ['Velocity,WorldPosition', 'DX11']] \

input_resolution = [(320, 240), (640, 480), (640, 360),
                    (1280, 720), (1920, 1080), (3840, 2160), (2880, 1620)]
input_frame_range = ['0000', '0010']
input_outputfolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'BatchRenderOutput')

def makeCommand(shotTag, shotNo, input_level, input_seq, res_id, pass_id):
    render_level = input_level + ' -game '
    render_seq = '-LevelSequence="%s" ' % input_seq
    render_dx = '-%s ' % input_render_pass[pass_id][1]
    render_outputfolder = '-MovieFolder="%s" ' % input_outputfolder
    render_res = '-ResX=%d -ResY=%d ' % (input_resolution[res_id][0], input_resolution[res_id][1])
    render_pass = '-CustomRenderPasses="%s" ' % input_render_pass[pass_id][0]
    render_range = '-MovieStartFrame=%s -MovieEndFrame=%s ' % (input_frame_range[0], input_frame_range[1])
    render_frame_name = '-MovieName="%s_%s_{world}_{material}_{frame}" ' % (shotTag, shotNo)
    misc_settings = '-Windowed -NoLoadingScreen -NoScreenMessages -NoTextureStreaming -MovieSceneCaptureType="/Script/MovieSceneCapture.AutomatedLevelSequenceCapture" -MovieFormat=CustomRenderPasses -MovieFrameRate=24 -MovieQuality=100 -MovieCinematicMode=Yes -MovieWarmUpFrames=100 -MovieDelayBeforeWarmUp=3 -CaptureFramesInHDR=1 -HDRCompressionQuality=1 -ForceRes -CaptureGamut="HCGM_Rec709"'

    # TODO:
    # https://wiki.unrealengine.com/Sequencer_Batch_Rendering
    # https://docs.unrealengine.com/en-US/Engine/Sequencer/Workflow/RenderingCmdLine/index.html#
    # -PostProcessingMaterial="MaterialPath"
    # -CaptureGamut = "HCGM_Name"

    # UE4Editor.exe
    engine_path = '"%s" ' % ((unreal.Paths.convert_relative_path_to_full(
        unreal.Paths.engine_dir()) + "Binaries/Win64/UE4Editor.exe").replace("/", '\\'))
    # Uproject
    proj_path = '"%s" ' % (unreal.Paths.convert_relative_path_to_full(
        unreal.Paths.get_project_file_path()).replace("/", '\\'))  

    cmd = [engine_path, proj_path, render_level, render_dx, render_seq, render_outputfolder, render_res, render_pass, render_range, render_frame_name, misc_settings]
    return cmd

def batchRender(cmd):
    # produce batch render bat
    config_path = unreal.Paths.project_config_dir()
    bat_path = unreal.Paths.convert_relative_path_to_full(config_path + 'batch-render-temp.bat')
    bat = open(bat_path, 'w+')
    bat.write(''.join(cmd))
    bat.close()

    # execute bat
    bat_exe_path = unreal.Paths.convert_relative_path_to_full(config_path + 'batch-render-temp-exe-min.bat')
    bat2 = open(bat_exe_path, 'w+')
    bat2.write('start /min ' + bat_path)
    bat2.close()

    # progress bar
    total_frames = 10000
    text_label = "Executing IGG batch render tool..."
    with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
        call(bat_exe_path)                                                                                   
        slow_task.make_dialog(True)
        for i in range(total_frames):
            slow_task.enter_progress_frame(1)

    unreal.log_warning('Batch rendering done successfully!')

