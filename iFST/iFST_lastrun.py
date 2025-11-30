#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.0),
    on November 30, 2025, at 16:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2025.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.0'
expName = 'iFST'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'language': ["English", "Spanish", "French"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1280, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\morenoverdu\\OneDrive - UCL\\BAS-Lab\\Github_repos\\iFST\\iFST_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('inst_adv') is None:
        # initialise inst_adv
        inst_adv = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst_adv',
        )
    if deviceManager.getDevice('block_adv_resp') is None:
        # initialise block_adv_resp
        block_adv_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='block_adv_resp',
        )
    if deviceManager.getDevice('adv_trial') is None:
        # initialise adv_trial
        adv_trial = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='adv_trial',
        )
    if deviceManager.getDevice('seq_resp') is None:
        # initialise seq_resp
        seq_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='seq_resp',
        )
    # create speaker 'sound_corr'
    deviceManager.addDevice(
        deviceName='sound_corr',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index='-1',
        resample='True',
        latencyClass=1,
    )
    # create speaker 'sound_incorr'
    deviceManager.addDevice(
        deviceName='sound_incorr',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index='-1',
        resample='True',
        latencyClass=1,
    )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    expShelf = data.shelf.Shelf(scope='experiment', expPath=_thisDir)
    # create uniform conditions for counterbalance
    counterbalanceConditions = []
    for n in range(2):
        counterbalanceConditions.append({
            'group': n,
            'probability': 1/2,
            'cap': 1
        })
    
    # create counterbalance object for counterbalance 
    counterbalance = data.Counterbalancer(
        shelf=expShelf,
        entry='counterbalance',
        conditions=counterbalanceConditions,
        nReps=100
    )
    
    # --- Initialize components for Routine "exp_settings" ---
    # Run 'Begin Experiment' code from exp_settings_code
    # block settings
    n_stimuli = 4 # exe-ima and simple-complex sequences
    # n_stimuli is not really used
    practice_blocks = 1 # number of practice blocks
    feedback = True # variable for settings in practice/test blocks
    # parameters for criterion in practice block
    stim_counters = {1: 0, 2: 0, 3: 0, 4: 0} # counters
    # the number of counter should match with the number of stimuli
    target_per_stim = 2 # whatever criterion
    task_blocks = 2 # number of task blocks
    total_blocks = practice_blocks + task_blocks
    ##### IMPORTANT VARIABLE #######
    n_reps = 1  # repetitions per task block
    ################################
    # placeholder variables:
    reps_per_block = 1 # variable to control reps in a block
    block_number = 0 # initialize variable for output
    color_text = "" # initialize variable
    self_assess_show = 0 # variable to show self-assessment loop
    sequence = "simple" # placeholder, it's updated later
    # settings for max/min time of breaks between blocks
    reg_max_pause = 60 # maximum time in seconds
    min_pause = 0 # minimum time in seconds
    
    
    # --- Initialize components for Routine "load_lg" ---
    # Run 'Begin Experiment' code from update_language_code
    # we define "lang_code" which is our variable to
    # be used for the language localisation dynamically
    # we set it to English as default language
    lang_code = "EN"
    thisExp.addData("language_code", lang_code)
    
    # --- Initialize components for Routine "update_msg" ---
    
    # --- Initialize components for Routine "welcome" ---
    title_text = visual.TextStim(win=win, name='title_text',
        text='',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    handedness_text = visual.TextStim(win=win, name='handedness_text',
        text='',
        font='Arial',
        pos=(0, -0.1), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    left_poly = visual.Rect(
        win=win, name='left_poly',
        width=(0.3, 0.15)[0], height=(0.3, 0.15)[1],
        ori=0.0, pos=(-0.2, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[0.6549, 0.6549, 0.6549], fillColor=[0.6549, 0.6549, 0.6549],
        opacity=None, depth=-4.0, interpolate=True)
    right_poly = visual.Rect(
        win=win, name='right_poly',
        width=(0.3, 0.15)[0], height=(0.3, 0.15)[1],
        ori=0.0, pos=(0.2, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[0.6549, 0.6549, 0.6549], fillColor=[0.6549, 0.6549, 0.6549],
        opacity=None, depth=-5.0, interpolate=True)
    left_text = visual.TextStim(win=win, name='left_text',
        text='',
        font='Arial',
        pos=(-0.2, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    right_text = visual.TextStim(win=win, name='right_text',
        text='',
        font='Arial',
        pos=(0.2, -0.3), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from inst_code
    inst_msg = ""
    task_title = visual.TextStim(win=win, name='task_title',
        text='',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    inst_text = visual.TextStim(win=win, name='inst_text',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    advance_text = visual.TextStim(win=win, name='advance_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    inst_image = visual.ImageStim(
        win=win,
        name='inst_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=1.0,
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    inst_adv = keyboard.Keyboard(deviceName='inst_adv')
    
    # --- Initialize components for Routine "block_start" ---
    block_main_text = visual.TextStim(win=win, name='block_main_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    block_number_text = visual.TextStim(win=win, name='block_number_text',
        text='',
        font='Arial',
        pos=(0, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 0.4980, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    block_adv_resp = keyboard.Keyboard(deviceName='block_adv_resp')
    block_start_adv_text = visual.TextStim(win=win, name='block_start_adv_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    timer = visual.TextStim(win=win, name='timer',
        text='',
        font='Arial',
        pos=(-0.8, -0.45), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "pre_trial" ---
    # Run 'Begin Experiment' code from pre_trial_code
    prompt_before = ""
    prompt_before_text = visual.TextStim(win=win, name='prompt_before_text',
        text='',
        font='Arial',
        pos=(0, 0.1), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    adv_trial = keyboard.Keyboard(deviceName='adv_trial')
    press_space_text = visual.TextStim(win=win, name='press_space_text',
        text='',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "seq_trial" ---
    # Run 'Begin Experiment' code from seq_trial_code
    key_count = 0
    prompt = ""
    fill1 = ""
    fill2 = ""
    fill3 = ""
    fill4 = ""
    prompt_text = visual.TextStim(win=win, name='prompt_text',
        text='',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    fix_cross = visual.ShapeStim(
        win=win, name='fix_cross', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    seq_image = visual.ImageStim(
        win=win,
        name='seq_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    box_F = visual.Rect(
        win=win, name='box_F',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.15, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    box_G = visual.Rect(
        win=win, name='box_G',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.05, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    box_H = visual.Rect(
        win=win, name='box_H',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.05, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    box_J = visual.Rect(
        win=win, name='box_J',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.15, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    seq_resp = keyboard.Keyboard(deviceName='seq_resp')
    
    # --- Initialize components for Routine "seq_fb" ---
    # Run 'Begin Experiment' code from seq_fb_code
    fb_dur = 3
    seq_fb_text = visual.TextStim(win=win, name='seq_fb_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    sound_corr = sound.Sound(
        'A', 
        secs=1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_corr',    name='sound_corr'
    )
    sound_corr.setVolume(1.0)
    sound_incorr = sound.Sound(
        'A', 
        secs=1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_incorr',    name='sound_incorr'
    )
    sound_incorr.setVolume(1.0)
    
    # --- Initialize components for Routine "self_assess" ---
    # Run 'Begin Experiment' code from self_assess_code
    self_assess_question = ""
    label_min = ""
    label_middle = ""
    label_max = ""
    self_assess_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.18), draggable=False,      letterHeight=0.03,
         size=(0.9, 0.4), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='self_assess_text',
         depth=-1, autoLog=True,
    )
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.05), pos=(0, -0.05), units=win.units,
        labels=(0,'','','','','|','','','','',10), ticks=(0,1,2,3,4,5,6,7,8,9,10), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor=[-1.0000, 0.4980, 1.0000], lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Arial', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    label_0 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.5, -0.35), draggable=False,      letterHeight=0.03,
         size=(0.4, 0.3), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_0',
         depth=-3, autoLog=True,
    )
    label_5 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.03,
         size=(0.4, 0.3), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_5',
         depth=-4, autoLog=True,
    )
    label_10 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.5, -0.35), draggable=False,      letterHeight=0.03,
         size=(0.4, 0.3), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=0.8, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='bottom-center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='label_10',
         depth=-5, autoLog=True,
    )
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    next_poly = visual.Rect(
        win=win, name='next_poly',
        width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
        ori=0.0, pos=(0.45, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 1.0000, 1.0000], fillColor=[0.6549, 0.6549, 0.6549],
        opacity=None, depth=-7.0, interpolate=True)
    next_text = visual.TextStim(win=win, name='next_text',
        text='',
        font='Arial',
        pos=(0.45, -0.4), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "bye" ---
    bye_text = visual.TextStim(win=win, name='bye_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    # get group from shelf
    counterbalance.allocateGroup()
    # if slots and repeats are fully depleted, end the experiment now
    if counterbalance.finished:
        # first print and log a message to make it clear why the experiment ended
        print('Slots for Counterbalancer counterbalance have been fully depleted, ending experiment.')
        logging.exp('Slots for Counterbalancer counterbalance have been fully depleted, ending experiment.')
        endExperiment(thisExp, win=win)
    thisExp.addData('counterbalance.group', counterbalance.group)
    for _key, _val in counterbalance.params.items():
        thisExp.addData(f'counterbalance.{_key}', _val)
    thisExp.addData('counterbalance.remaining', counterbalance.remaining)
    thisExp.nextEntry()
    # the Routine "counterbalance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp_settings" ---
    # create an object to store info about Routine exp_settings
    exp_settings = data.Routine(
        name='exp_settings',
        components=[],
    )
    exp_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exp_settings_code
    group = int(counterbalance.group)
    # we use this variable to counterbalance the conditions
    # see code in the block_start routine.
    # The orders are:
    # group == 0: simple-complex
    # group == 1: complex-simple
    # store start times for exp_settings
    exp_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_settings.tStart = globalClock.getTime(format='float')
    exp_settings.status = STARTED
    exp_settings.maxDuration = None
    # keep track of which components have finished
    exp_settingsComponents = exp_settings.components
    for thisComponent in exp_settings.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_settings" ---
    exp_settings.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=exp_settings,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_settings" ---
    for thisComponent in exp_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_settings
    exp_settings.tStop = globalClock.getTime(format='float')
    exp_settings.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "exp_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    lang_loop = data.TrialHandler2(
        name='lang_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('language_localiser.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(lang_loop)  # add the loop to the experiment
    thisLang_loop = lang_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLang_loop.rgb)
    if thisLang_loop != None:
        for paramName in thisLang_loop:
            globals()[paramName] = thisLang_loop[paramName]
    
    for thisLang_loop in lang_loop:
        lang_loop.status = STARTED
        if hasattr(thisLang_loop, 'status'):
            thisLang_loop.status = STARTED
        currentLoop = lang_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisLang_loop.rgb)
        if thisLang_loop != None:
            for paramName in thisLang_loop:
                globals()[paramName] = thisLang_loop[paramName]
        
        # --- Prepare to start Routine "load_lg" ---
        # create an object to store info about Routine load_lg
        load_lg = data.Routine(
            name='load_lg',
            components=[],
        )
        load_lg.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from update_language_code
        # we put this code at the beginning of the routine.
        # at this point the language has already been selected
        # in the dialogue box by the participant
        
        # now we update the language code based on the
        # language localiser variable ISO_code
        if language == expInfo['language']:
            lang_code = ISO_code  
        
        thisExp.addData("language_code", lang_code)  # add it to output
        
        # this way now lang_code has the value of ISO_code
        # where language in our Excel sheet matches with the
        # language selected by the participant
        # store start times for load_lg
        load_lg.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        load_lg.tStart = globalClock.getTime(format='float')
        load_lg.status = STARTED
        thisExp.addData('load_lg.started', load_lg.tStart)
        load_lg.maxDuration = None
        # keep track of which components have finished
        load_lgComponents = load_lg.components
        for thisComponent in load_lg.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "load_lg" ---
        load_lg.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLang_loop, 'status') and thisLang_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=load_lg,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                load_lg.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in load_lg.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "load_lg" ---
        for thisComponent in load_lg.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for load_lg
        load_lg.tStop = globalClock.getTime(format='float')
        load_lg.tStopRefresh = tThisFlipGlobal
        thisExp.addData('load_lg.stopped', load_lg.tStop)
        # the Routine "load_lg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLang_loop as finished
        if hasattr(thisLang_loop, 'status'):
            thisLang_loop.status = FINISHED
        # if awaiting a pause, pause now
        if lang_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            lang_loop.status = STARTED
    # completed 1.0 repeats of 'lang_loop'
    lang_loop.status = FINISHED
    
    
    # set up handler to look after randomisation of conditions etc
    messages_loop = data.TrialHandler2(
        name='messages_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('messages.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(messages_loop)  # add the loop to the experiment
    thisMessages_loop = messages_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMessages_loop.rgb)
    if thisMessages_loop != None:
        for paramName in thisMessages_loop:
            globals()[paramName] = thisMessages_loop[paramName]
    
    for thisMessages_loop in messages_loop:
        messages_loop.status = STARTED
        if hasattr(thisMessages_loop, 'status'):
            thisMessages_loop.status = STARTED
        currentLoop = messages_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisMessages_loop.rgb)
        if thisMessages_loop != None:
            for paramName in thisMessages_loop:
                globals()[paramName] = thisMessages_loop[paramName]
        
        # --- Prepare to start Routine "update_msg" ---
        # create an object to store info about Routine update_msg
        update_msg = data.Routine(
            name='update_msg',
            components=[],
        )
        update_msg.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from update_messages_code
        ## THIS CODE DOES NOT AUTO-TRANSLATE!!!!
        
        # now that we have selected our new language (lang_code)
        # we can use a loop to iterate over the messages
        # every iteration, we're gonna update the value of our
        # global variables with the value corresponding to the
        # lang_code (ISO_code from the language localiser)
        # this way we don't need to manually specify the text
        
        # this iteration, select the message
        msg_name = message  # e.g. variable "welcome_msg"
        # for this iteration, assign the value based on code
        msg_value = eval(lang_code) # e.g. "Bienvenido" if lang_code = "ES"
        # update message based on code
        globals()[msg_name] = msg_value  # e.g. should update the value of welcome_msg by "Bienvenido"
        # finally we add the values to output just to check
        thisExp.addData("msg_name", msg_name)
        thisExp.addData("msg_value", msg_value)
        # store start times for update_msg
        update_msg.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        update_msg.tStart = globalClock.getTime(format='float')
        update_msg.status = STARTED
        update_msg.maxDuration = None
        # keep track of which components have finished
        update_msgComponents = update_msg.components
        for thisComponent in update_msg.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "update_msg" ---
        update_msg.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMessages_loop, 'status') and thisMessages_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=update_msg,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                update_msg.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in update_msg.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "update_msg" ---
        for thisComponent in update_msg.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for update_msg
        update_msg.tStop = globalClock.getTime(format='float')
        update_msg.tStopRefresh = tThisFlipGlobal
        # the Routine "update_msg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisMessages_loop as finished
        if hasattr(thisMessages_loop, 'status'):
            thisMessages_loop.status = FINISHED
        # if awaiting a pause, pause now
        if messages_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            messages_loop.status = STARTED
    # completed 1.0 repeats of 'messages_loop'
    messages_loop.status = FINISHED
    
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[title_text, welcome_text, handedness_text, left_poly, right_poly, left_text, right_text, mouse],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from welcome_code
    handedness = ""
    title_text.setText(title_msg)
    welcome_text.setText(welcome_msg)
    handedness_text.setText(handedness_msg)
    left_text.setText(left_handed_msg)
    right_text.setText(right_handed_msg)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from welcome_code
        clicked = mouse.getPressed()[0]
        
        if clicked:
            if mouse.isPressedIn(left_poly):
                handedness = "left"
                continueRoutine = False
            elif mouse.isPressedIn(right_poly):
                handedness = "right"
                continueRoutine = False
        
        # *title_text* updates
        
        # if title_text is starting this frame...
        if title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            title_text.frameNStart = frameN  # exact frame index
            title_text.tStart = t  # local t and not account for scr refresh
            title_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(title_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'title_text.started')
            # update status
            title_text.status = STARTED
            title_text.setAutoDraw(True)
        
        # if title_text is active this frame...
        if title_text.status == STARTED:
            # update params
            pass
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *handedness_text* updates
        
        # if handedness_text is starting this frame...
        if handedness_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            handedness_text.frameNStart = frameN  # exact frame index
            handedness_text.tStart = t  # local t and not account for scr refresh
            handedness_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(handedness_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            handedness_text.status = STARTED
            handedness_text.setAutoDraw(True)
        
        # if handedness_text is active this frame...
        if handedness_text.status == STARTED:
            # update params
            pass
        
        # *left_poly* updates
        
        # if left_poly is starting this frame...
        if left_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_poly.frameNStart = frameN  # exact frame index
            left_poly.tStart = t  # local t and not account for scr refresh
            left_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_poly, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_poly.started')
            # update status
            left_poly.status = STARTED
            left_poly.setAutoDraw(True)
        
        # if left_poly is active this frame...
        if left_poly.status == STARTED:
            # update params
            pass
        
        # *right_poly* updates
        
        # if right_poly is starting this frame...
        if right_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_poly.frameNStart = frameN  # exact frame index
            right_poly.tStart = t  # local t and not account for scr refresh
            right_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_poly, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_poly.started')
            # update status
            right_poly.status = STARTED
            right_poly.setAutoDraw(True)
        
        # if right_poly is active this frame...
        if right_poly.status == STARTED:
            # update params
            pass
        
        # *left_text* updates
        
        # if left_text is starting this frame...
        if left_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_text.frameNStart = frameN  # exact frame index
            left_text.tStart = t  # local t and not account for scr refresh
            left_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_text.started')
            # update status
            left_text.status = STARTED
            left_text.setAutoDraw(True)
        
        # if left_text is active this frame...
        if left_text.status == STARTED:
            # update params
            pass
        
        # *right_text* updates
        
        # if right_text is starting this frame...
        if right_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_text.frameNStart = frameN  # exact frame index
            right_text.tStart = t  # local t and not account for scr refresh
            right_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_text.started')
            # update status
            right_text.status = STARTED
            right_text.setAutoDraw(True)
        
        # if right_text is active this frame...
        if right_text.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([left_poly, right_poly], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcome,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    # Run 'End Routine' code from welcome_code
    thisExp.addData("handedness", handedness)
    
    if handedness == "left":
        conditions_file = "conditions_left.xlsx"
    else:
        conditions_file = "conditions_right.xlsx"
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse.x', mouse.x)
    thisExp.addData('mouse.y', mouse.y)
    thisExp.addData('mouse.leftButton', mouse.leftButton)
    thisExp.addData('mouse.midButton', mouse.midButton)
    thisExp.addData('mouse.rightButton', mouse.rightButton)
    thisExp.addData('mouse.time', mouse.time)
    thisExp.addData('mouse.clicked_name', mouse.clicked_name)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    instructions_loop = data.TrialHandler2(
        name='instructions_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('instructions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(instructions_loop)  # add the loop to the experiment
    thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop:
            globals()[paramName] = thisInstructions_loop[paramName]
    
    for thisInstructions_loop in instructions_loop:
        instructions_loop.status = STARTED
        if hasattr(thisInstructions_loop, 'status'):
            thisInstructions_loop.status = STARTED
        currentLoop = instructions_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
        if thisInstructions_loop != None:
            for paramName in thisInstructions_loop:
                globals()[paramName] = thisInstructions_loop[paramName]
        
        # --- Prepare to start Routine "instructions" ---
        # create an object to store info about Routine instructions
        instructions = data.Routine(
            name='instructions',
            components=[task_title, inst_text, advance_text, inst_image, inst_adv],
        )
        instructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from inst_code
        thisExp.addData("handedness", handedness)
        if hand == handedness:
            continueRoutine = True
        else:
            continueRoutine = False
        
        # hide mouse for the rest of the experiment
        win.mouseVisible = False
        # get column from excel sheet based on language code
        try:
            inst_msg = eval(f"inst_msg_{lang_code}")
        # default to english if this fails
        except ReferenceError:
            inst_msg = inst_msg_EN
        
        task_title.setText(title_msg)
        inst_text.setPos((text_x, 0))
        inst_text.setText(inst_msg)
        advance_text.setText(adv_msg)
        inst_image.setSize((image_w, image_h))
        inst_image.setImage(inst_pic)
        # create starting attributes for inst_adv
        inst_adv.keys = []
        inst_adv.rt = []
        _inst_adv_allKeys = []
        # store start times for instructions
        instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        instructions.tStart = globalClock.getTime(format='float')
        instructions.status = STARTED
        instructions.maxDuration = None
        # keep track of which components have finished
        instructionsComponents = instructions.components
        for thisComponent in instructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructions" ---
        instructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisInstructions_loop, 'status') and thisInstructions_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *task_title* updates
            
            # if task_title is starting this frame...
            if task_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_title.frameNStart = frameN  # exact frame index
                task_title.tStart = t  # local t and not account for scr refresh
                task_title.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_title, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_title.started')
                # update status
                task_title.status = STARTED
                task_title.setAutoDraw(True)
            
            # if task_title is active this frame...
            if task_title.status == STARTED:
                # update params
                pass
            
            # *inst_text* updates
            
            # if inst_text is starting this frame...
            if inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_text.frameNStart = frameN  # exact frame index
                inst_text.tStart = t  # local t and not account for scr refresh
                inst_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_text.status = STARTED
                inst_text.setAutoDraw(True)
            
            # if inst_text is active this frame...
            if inst_text.status == STARTED:
                # update params
                pass
            
            # *advance_text* updates
            
            # if advance_text is starting this frame...
            if advance_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                advance_text.frameNStart = frameN  # exact frame index
                advance_text.tStart = t  # local t and not account for scr refresh
                advance_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(advance_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                advance_text.status = STARTED
                advance_text.setAutoDraw(True)
            
            # if advance_text is active this frame...
            if advance_text.status == STARTED:
                # update params
                pass
            
            # *inst_image* updates
            
            # if inst_image is starting this frame...
            if inst_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_image.frameNStart = frameN  # exact frame index
                inst_image.tStart = t  # local t and not account for scr refresh
                inst_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_image.status = STARTED
                inst_image.setAutoDraw(True)
            
            # if inst_image is active this frame...
            if inst_image.status == STARTED:
                # update params
                pass
            
            # *inst_adv* updates
            waitOnFlip = False
            
            # if inst_adv is starting this frame...
            if inst_adv.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inst_adv.frameNStart = frameN  # exact frame index
                inst_adv.tStart = t  # local t and not account for scr refresh
                inst_adv.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inst_adv, 'tStartRefresh')  # time at next scr refresh
                # update status
                inst_adv.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(inst_adv.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(inst_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if inst_adv.status == STARTED and not waitOnFlip:
                theseKeys = inst_adv.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _inst_adv_allKeys.extend(theseKeys)
                if len(_inst_adv_allKeys):
                    inst_adv.keys = _inst_adv_allKeys[-1].name  # just the last key pressed
                    inst_adv.rt = _inst_adv_allKeys[-1].rt
                    inst_adv.duration = _inst_adv_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=instructions,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                instructions.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions" ---
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for instructions
        instructions.tStop = globalClock.getTime(format='float')
        instructions.tStopRefresh = tThisFlipGlobal
        # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisInstructions_loop as finished
        if hasattr(thisInstructions_loop, 'status'):
            thisInstructions_loop.status = FINISHED
        # if awaiting a pause, pause now
        if instructions_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            instructions_loop.status = STARTED
    # completed 1.0 repeats of 'instructions_loop'
    instructions_loop.status = FINISHED
    
    
    # set up handler to look after randomisation of conditions etc
    blocks_loop = data.TrialHandler2(
        name='blocks_loop',
        nReps=total_blocks, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(blocks_loop)  # add the loop to the experiment
    thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
    if thisBlocks_loop != None:
        for paramName in thisBlocks_loop:
            globals()[paramName] = thisBlocks_loop[paramName]
    
    for thisBlocks_loop in blocks_loop:
        blocks_loop.status = STARTED
        if hasattr(thisBlocks_loop, 'status'):
            thisBlocks_loop.status = STARTED
        currentLoop = blocks_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
        if thisBlocks_loop != None:
            for paramName in thisBlocks_loop:
                globals()[paramName] = thisBlocks_loop[paramName]
        
        # --- Prepare to start Routine "block_start" ---
        # create an object to store info about Routine block_start
        block_start = data.Routine(
            name='block_start',
            components=[block_main_text, block_number_text, block_adv_resp, block_start_adv_text, timer],
        )
        block_start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from block_code
        # DOES NOT AUTO-TRANSLATE!!!
        
        win.mouseVisible = False
        # start block at 1 and increase every iteration
        block_number += 1
        # initialize timer
        screen_timer = core.Clock()
        # set up block messages according to task progress
        # and minimum time for pauses
        if block_number == 1:
            # practice block
            block_message = block_first_msg
        elif block_number == practice_blocks + 1:
            # first task block
            block_message = block_intro_task_msg
        else:
            # after block
            block_message = block_msg_standard
        block_main_text.setText(block_message)
        block_number_text.setText(block_msg + ' ' + str(block_number) + ' ' + out_of_msg + ' ' + str(total_blocks) )
        # create starting attributes for block_adv_resp
        block_adv_resp.keys = []
        block_adv_resp.rt = []
        _block_adv_resp_allKeys = []
        block_start_adv_text.setText(adv_msg)
        # store start times for block_start
        block_start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        block_start.tStart = globalClock.getTime(format='float')
        block_start.status = STARTED
        thisExp.addData('block_start.started', block_start.tStart)
        block_start.maxDuration = None
        # keep track of which components have finished
        block_startComponents = block_start.components
        for thisComponent in block_start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_start" ---
        block_start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlocks_loop, 'status') and thisBlocks_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from block_code
            # show timer
            elapsed = screen_timer.getTime()
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            timer_text = f"{minutes:02d}:{seconds:02d}"
            
            # stop routine when we reach the maximum time
            if seconds >= reg_max_pause:
                continueRoutine = False
            
            # *block_main_text* updates
            
            # if block_main_text is starting this frame...
            if block_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_main_text.frameNStart = frameN  # exact frame index
                block_main_text.tStart = t  # local t and not account for scr refresh
                block_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_main_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_main_text.started')
                # update status
                block_main_text.status = STARTED
                block_main_text.setAutoDraw(True)
            
            # if block_main_text is active this frame...
            if block_main_text.status == STARTED:
                # update params
                pass
            
            # *block_number_text* updates
            
            # if block_number_text is starting this frame...
            if block_number_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block_number_text.frameNStart = frameN  # exact frame index
                block_number_text.tStart = t  # local t and not account for scr refresh
                block_number_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_number_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_number_text.started')
                # update status
                block_number_text.status = STARTED
                block_number_text.setAutoDraw(True)
            
            # if block_number_text is active this frame...
            if block_number_text.status == STARTED:
                # update params
                pass
            
            # *block_adv_resp* updates
            waitOnFlip = False
            
            # if block_adv_resp is starting this frame...
            if block_adv_resp.status == NOT_STARTED and tThisFlip >= min_pause-frameTolerance:
                # keep track of start time/frame for later
                block_adv_resp.frameNStart = frameN  # exact frame index
                block_adv_resp.tStart = t  # local t and not account for scr refresh
                block_adv_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_adv_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_adv_resp.started')
                # update status
                block_adv_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(block_adv_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(block_adv_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if block_adv_resp.status == STARTED and not waitOnFlip:
                theseKeys = block_adv_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _block_adv_resp_allKeys.extend(theseKeys)
                if len(_block_adv_resp_allKeys):
                    block_adv_resp.keys = _block_adv_resp_allKeys[-1].name  # just the last key pressed
                    block_adv_resp.rt = _block_adv_resp_allKeys[-1].rt
                    block_adv_resp.duration = _block_adv_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *block_start_adv_text* updates
            
            # if block_start_adv_text is starting this frame...
            if block_start_adv_text.status == NOT_STARTED and tThisFlip >= min_pause-frameTolerance:
                # keep track of start time/frame for later
                block_start_adv_text.frameNStart = frameN  # exact frame index
                block_start_adv_text.tStart = t  # local t and not account for scr refresh
                block_start_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block_start_adv_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                block_start_adv_text.status = STARTED
                block_start_adv_text.setAutoDraw(True)
            
            # if block_start_adv_text is active this frame...
            if block_start_adv_text.status == STARTED:
                # update params
                pass
            
            # *timer* updates
            
            # if timer is starting this frame...
            if timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer.frameNStart = frameN  # exact frame index
                timer.tStart = t  # local t and not account for scr refresh
                timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timer.started')
                # update status
                timer.status = STARTED
                timer.setAutoDraw(True)
            
            # if timer is active this frame...
            if timer.status == STARTED:
                # update params
                timer.setText(timer_text, log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=block_start,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                block_start.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_start" ---
        for thisComponent in block_start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for block_start
        block_start.tStop = globalClock.getTime(format='float')
        block_start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('block_start.stopped', block_start.tStop)
        # Run 'End Routine' code from block_code
        thisExp.addData("block_number", block_number)
        thisExp.addData("block_pause", seconds)
        # check responses
        if block_adv_resp.keys in ['', [], None]:  # No response was made
            block_adv_resp.keys = None
        blocks_loop.addData('block_adv_resp.keys',block_adv_resp.keys)
        if block_adv_resp.keys != None:  # we had a response
            blocks_loop.addData('block_adv_resp.rt', block_adv_resp.rt)
            blocks_loop.addData('block_adv_resp.duration', block_adv_resp.duration)
        # Run 'End Routine' code from block_settings_code
        # change conditions based on block
        if block_number <= practice_blocks:
            feedback = True
            reps_per_block = 999
            self_assess_show = 0
            sequence = sequence
        elif block_number == practice_blocks + 1:
            feedback = False
            reps_per_block = n_reps
            self_assess_show = 1
            if group == 0:
                sequence = "simple"
            elif group == 1:
                sequence = "complex"
        elif block_number == practice_blocks + 2:
            feedback = False
            reps_per_block = n_reps
            self_assess_show = 1
            if group == 0:
                sequence = "complex"
            elif group == 1:
                sequence = "simple"
        thisExp.addData("reps_per_block", reps_per_block)
        thisExp.addData("sequence_selected", sequence)
        # the Routine "block_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        seq_loop = data.TrialHandler2(
            name='seq_loop',
            nReps=reps_per_block, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(conditions_file), 
            seed=None, 
        )
        thisExp.addLoop(seq_loop)  # add the loop to the experiment
        thisSeq_loop = seq_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSeq_loop.rgb)
        if thisSeq_loop != None:
            for paramName in thisSeq_loop:
                globals()[paramName] = thisSeq_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSeq_loop in seq_loop:
            seq_loop.status = STARTED
            if hasattr(thisSeq_loop, 'status'):
                thisSeq_loop.status = STARTED
            currentLoop = seq_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSeq_loop.rgb)
            if thisSeq_loop != None:
                for paramName in thisSeq_loop:
                    globals()[paramName] = thisSeq_loop[paramName]
            
            # --- Prepare to start Routine "pre_trial" ---
            # create an object to store info about Routine pre_trial
            pre_trial = data.Routine(
                name='pre_trial',
                components=[prompt_before_text, adv_trial, press_space_text],
            )
            pre_trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from pre_trial_code
            # in test blocks, skip routine based on counterbalancing
            if block_number > practice_blocks:
                if sequence_type == sequence:
                    continueRoutine = True
                else:
                    continueRoutine = False
            current_stim = int(stim)
            # in practice blocks, show only if counter is not complete
            if block_number <= practice_blocks:
                if stim_counters[current_stim] == target_per_stim:
                    stim_counters[current_stim] = 100
                if stim_counters[current_stim] >= target_per_stim:
                    continueRoutine = False
            print(stim_counters[current_stim])
            win.mouseVisible = False
            
            # Set color for text and update prompts
            if trial_type == "imagery":
                prompt_before = pre_prompt_ima_msg
                color_text = "purple"
            elif trial_type == "execution":
                prompt_before = pre_prompt_exe_msg
                color_text = "blue"
            
            prompt_before_text.setColor(color_text, colorSpace='rgb')
            prompt_before_text.setText(prompt_before)
            # create starting attributes for adv_trial
            adv_trial.keys = []
            adv_trial.rt = []
            _adv_trial_allKeys = []
            press_space_text.setColor(color_text, colorSpace='rgb')
            press_space_text.setText(adv_msg)
            # store start times for pre_trial
            pre_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            pre_trial.tStart = globalClock.getTime(format='float')
            pre_trial.status = STARTED
            thisExp.addData('pre_trial.started', pre_trial.tStart)
            pre_trial.maxDuration = None
            # keep track of which components have finished
            pre_trialComponents = pre_trial.components
            for thisComponent in pre_trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "pre_trial" ---
            pre_trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisSeq_loop, 'status') and thisSeq_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *prompt_before_text* updates
                
                # if prompt_before_text is starting this frame...
                if prompt_before_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    prompt_before_text.frameNStart = frameN  # exact frame index
                    prompt_before_text.tStart = t  # local t and not account for scr refresh
                    prompt_before_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prompt_before_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prompt_before_text.started')
                    # update status
                    prompt_before_text.status = STARTED
                    prompt_before_text.setAutoDraw(True)
                
                # if prompt_before_text is active this frame...
                if prompt_before_text.status == STARTED:
                    # update params
                    pass
                
                # *adv_trial* updates
                waitOnFlip = False
                
                # if adv_trial is starting this frame...
                if adv_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    adv_trial.frameNStart = frameN  # exact frame index
                    adv_trial.tStart = t  # local t and not account for scr refresh
                    adv_trial.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(adv_trial, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'adv_trial.started')
                    # update status
                    adv_trial.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(adv_trial.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(adv_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if adv_trial.status == STARTED and not waitOnFlip:
                    theseKeys = adv_trial.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _adv_trial_allKeys.extend(theseKeys)
                    if len(_adv_trial_allKeys):
                        adv_trial.keys = _adv_trial_allKeys[-1].name  # just the last key pressed
                        adv_trial.rt = _adv_trial_allKeys[-1].rt
                        adv_trial.duration = _adv_trial_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *press_space_text* updates
                
                # if press_space_text is starting this frame...
                if press_space_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    press_space_text.frameNStart = frameN  # exact frame index
                    press_space_text.tStart = t  # local t and not account for scr refresh
                    press_space_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(press_space_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'press_space_text.started')
                    # update status
                    press_space_text.status = STARTED
                    press_space_text.setAutoDraw(True)
                
                # if press_space_text is active this frame...
                if press_space_text.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=pre_trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    pre_trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pre_trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pre_trial" ---
            for thisComponent in pre_trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for pre_trial
            pre_trial.tStop = globalClock.getTime(format='float')
            pre_trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('pre_trial.stopped', pre_trial.tStop)
            # check responses
            if adv_trial.keys in ['', [], None]:  # No response was made
                adv_trial.keys = None
            seq_loop.addData('adv_trial.keys',adv_trial.keys)
            if adv_trial.keys != None:  # we had a response
                seq_loop.addData('adv_trial.rt', adv_trial.rt)
                seq_loop.addData('adv_trial.duration', adv_trial.duration)
            # the Routine "pre_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "seq_trial" ---
            # create an object to store info about Routine seq_trial
            seq_trial = data.Routine(
                name='seq_trial',
                components=[prompt_text, fix_cross, seq_image, box_F, box_G, box_H, box_J, seq_resp],
            )
            seq_trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from seq_trial_code
            # Trial settings depending on condition
            current_stim = int(stim)
            # in test blocks, skip routine based on counterbalancing
            if block_number > practice_blocks:
                if sequence_type == sequence:
                    continueRoutine = True
                else:
                    continueRoutine = False
            # in practice blocks, show only if counter is not complete
            if block_number <= practice_blocks:
                if stim_counters[current_stim] >= target_per_stim:
                    continueRoutine = False
            
            # Initialize variables
            fill1, fill2, fill3, fill4 = 'black', 'black', 'black', 'black'  # Default color
            seq_timer = core.Clock() # create timer
            seq_timer.reset() # start timer at 0
            # Initialize variables to count keys and end routine
            # based on number of key presses
            previous_key_count = 0
            current_key_count = 0
            last_key = ""
            win.mouseVisible = False
            seq_resp.keys = []
            key_count = 0
            seq_resp.rt = []
            # change color and prompt based on condition (old)
            if trial_type == "imagery":
                prompt = prompt_ima_msg
                color_text = "purple"
            elif trial_type == "execution":
                prompt = prompt_exe_msg
                color_text = "blue"
            
            
            prompt_text.setColor(color_text, colorSpace='rgb')
            prompt_text.setText(prompt)
            seq_image.setImage(sequence_picture)
            # create starting attributes for seq_resp
            seq_resp.keys = []
            seq_resp.rt = []
            _seq_resp_allKeys = []
            # store start times for seq_trial
            seq_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            seq_trial.tStart = globalClock.getTime(format='float')
            seq_trial.status = STARTED
            thisExp.addData('seq_trial.started', seq_trial.tStart)
            seq_trial.maxDuration = None
            # keep track of which components have finished
            seq_trialComponents = seq_trial.components
            for thisComponent in seq_trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "seq_trial" ---
            seq_trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisSeq_loop, 'status') and thisSeq_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from seq_trial_code
                
                # At the beginning, no key has been pressed
                # We initialize the list of key presses
                if seq_resp.keys is None:
                    seq_resp.keys = []
                
                # set variable to count the number of keys
                current_key_count = len(seq_resp.keys) # use the native variable from component
                
                # Check if a key has been pressed
                if current_key_count > previous_key_count:
                    key_count += 1
                    last_key = seq_resp.keys[-1]  # Get the latest key pressed
                    seq_timer.reset()  # Reset the timer to 0 whenever a new key is pressed
                    if feedback == True:
                        if last_key == "f":
                            fill1, fill2, fill3, fill4 = 'white', 'black', 'black', 'black'
                        elif last_key == "g":
                            fill1, fill2, fill3, fill4 = 'black', 'white', 'black', 'black'
                        elif last_key == "h":
                            fill1, fill2, fill3, fill4 = 'black', 'black', 'white', 'black'
                        elif last_key == "j":
                            fill1, fill2, fill3, fill4 = 'black', 'black', 'black', 'white'
                    elif feedback == False:
                        fill1 = fill2 = fill3 = fill4 = 'black'
                else:
                    key_count = key_count
                
                # Update the previous key count for the next frame
                previous_key_count = current_key_count
                
                # Check timer and get back to black after a couple of ms
                if seq_timer.getTime() >= 0.1:
                    fill1, fill2, fill3, fill4 = 'black', 'black', 'black', 'black'
                
                # End trial when reaching expected number of keys
                if key_count == key_presses:
                    continueRoutine = False
                
                
                # *prompt_text* updates
                
                # if prompt_text is starting this frame...
                if prompt_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    prompt_text.frameNStart = frameN  # exact frame index
                    prompt_text.tStart = t  # local t and not account for scr refresh
                    prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prompt_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prompt_text.started')
                    # update status
                    prompt_text.status = STARTED
                    prompt_text.setAutoDraw(True)
                
                # if prompt_text is active this frame...
                if prompt_text.status == STARTED:
                    # update params
                    pass
                
                # *fix_cross* updates
                
                # if fix_cross is starting this frame...
                if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_cross.frameNStart = frameN  # exact frame index
                    fix_cross.tStart = t  # local t and not account for scr refresh
                    fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross.started')
                    # update status
                    fix_cross.status = STARTED
                    fix_cross.setAutoDraw(True)
                
                # if fix_cross is active this frame...
                if fix_cross.status == STARTED:
                    # update params
                    pass
                
                # *seq_image* updates
                
                # if seq_image is starting this frame...
                if seq_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    seq_image.frameNStart = frameN  # exact frame index
                    seq_image.tStart = t  # local t and not account for scr refresh
                    seq_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(seq_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'seq_image.started')
                    # update status
                    seq_image.status = STARTED
                    seq_image.setAutoDraw(True)
                
                # if seq_image is active this frame...
                if seq_image.status == STARTED:
                    # update params
                    pass
                
                # *box_F* updates
                
                # if box_F is starting this frame...
                if box_F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_F.frameNStart = frameN  # exact frame index
                    box_F.tStart = t  # local t and not account for scr refresh
                    box_F.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_F, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'box_F.started')
                    # update status
                    box_F.status = STARTED
                    box_F.setAutoDraw(True)
                
                # if box_F is active this frame...
                if box_F.status == STARTED:
                    # update params
                    box_F.setFillColor(fill1, log=False)
                    box_F.setLineColor(fill1, log=False)
                
                # *box_G* updates
                
                # if box_G is starting this frame...
                if box_G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_G.frameNStart = frameN  # exact frame index
                    box_G.tStart = t  # local t and not account for scr refresh
                    box_G.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_G, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'box_G.started')
                    # update status
                    box_G.status = STARTED
                    box_G.setAutoDraw(True)
                
                # if box_G is active this frame...
                if box_G.status == STARTED:
                    # update params
                    box_G.setFillColor(fill2, log=False)
                    box_G.setLineColor(fill2, log=False)
                
                # *box_H* updates
                
                # if box_H is starting this frame...
                if box_H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_H.frameNStart = frameN  # exact frame index
                    box_H.tStart = t  # local t and not account for scr refresh
                    box_H.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_H, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'box_H.started')
                    # update status
                    box_H.status = STARTED
                    box_H.setAutoDraw(True)
                
                # if box_H is active this frame...
                if box_H.status == STARTED:
                    # update params
                    box_H.setFillColor(fill3, log=False)
                    box_H.setLineColor(fill3, log=False)
                
                # *box_J* updates
                
                # if box_J is starting this frame...
                if box_J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    box_J.frameNStart = frameN  # exact frame index
                    box_J.tStart = t  # local t and not account for scr refresh
                    box_J.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(box_J, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'box_J.started')
                    # update status
                    box_J.status = STARTED
                    box_J.setAutoDraw(True)
                
                # if box_J is active this frame...
                if box_J.status == STARTED:
                    # update params
                    box_J.setFillColor(fill4, log=False)
                    box_J.setLineColor(fill4, log=False)
                
                # *seq_resp* updates
                waitOnFlip = False
                
                # if seq_resp is starting this frame...
                if seq_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    seq_resp.frameNStart = frameN  # exact frame index
                    seq_resp.tStart = t  # local t and not account for scr refresh
                    seq_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(seq_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'seq_resp.started')
                    # update status
                    seq_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(seq_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(seq_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if seq_resp.status == STARTED and not waitOnFlip:
                    theseKeys = seq_resp.getKeys(keyList=['f','g','h','j'], ignoreKeys=["escape"], waitRelease=False)
                    _seq_resp_allKeys.extend(theseKeys)
                    if len(_seq_resp_allKeys):
                        seq_resp.keys = [key.name for key in _seq_resp_allKeys]  # storing all keys
                        seq_resp.rt = [key.rt for key in _seq_resp_allKeys]
                        seq_resp.duration = [key.duration for key in _seq_resp_allKeys]
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=seq_trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    seq_trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in seq_trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "seq_trial" ---
            for thisComponent in seq_trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for seq_trial
            seq_trial.tStop = globalClock.getTime(format='float')
            seq_trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('seq_trial.stopped', seq_trial.tStop)
            # Run 'End Routine' code from seq_trial_code
            # create a string with the key presses
            seq_typed = "".join(seq_resp.keys)
            # the output will be "fghjjhgf"
            
            # compare with variable hosting correct response
            seq_acc = 1 if seq_typed == sequence_code else 0
            
            # calculate time to finish the sequence
            # as the trial does not finish until a given N of key presses
            # we can calculate the time as the last minus the first items
            # regardless of the type of trial
            # we use key_presses as this variable may change every trial depending
            # on trial type (e.g. execution vs imagery)
            if seq_resp.rt and len(seq_resp.rt) >= key_presses:
                last_press = key_presses - 1  # Index of last expected press
                seq_time = seq_resp.rt[last_press] - seq_resp.rt[0]
                seq_time = round(seq_time, 2)
            else:
                seq_time = 999  # Fallback in case of missing responses
            # save to output
            thisExp.addData("seq_typed", seq_typed)
            thisExp.addData("seq_acc", seq_acc)
            thisExp.addData("seq_time", seq_time)
            # check responses
            if seq_resp.keys in ['', [], None]:  # No response was made
                seq_resp.keys = None
            seq_loop.addData('seq_resp.keys',seq_resp.keys)
            if seq_resp.keys != None:  # we had a response
                seq_loop.addData('seq_resp.rt', seq_resp.rt)
                seq_loop.addData('seq_resp.duration', seq_resp.duration)
            # the Routine "seq_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "seq_fb" ---
            # create an object to store info about Routine seq_fb
            seq_fb = data.Routine(
                name='seq_fb',
                components=[seq_fb_text, sound_corr, sound_incorr],
            )
            seq_fb.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from seq_fb_code
            win.mouseVisible = False
            current_stim = int(stim)
            if block_number <= practice_blocks:
                if seq_acc == 1:
                    fb_dur = 3
                    corr_vol = 1
                    incorr_vol = 0
                    stim_counters[current_stim] += 1
                elif seq_acc == 0:
                    fb_dur = 5
                    corr_vol = 0
                    incorr_vol = 1
                    # practice block, show always if counter is not reached
                if stim_counters[current_stim] <= target_per_stim:
                    continueRoutine = True
                if stim_counters[current_stim] == 100:
                    continueRoutine = False
                    stim_counters[current_stim] = 100 # keep it
                thisExp.addData("crit_counter", stim_counters[current_stim])
            else:
                continueRoutine = False
            
            if trial_type == "imagery":
                color_text = "purple"
                if seq_acc == 1:
                    fb_message = correct_ima_msg
                elif seq_acc == 0:
                    fb_message = incorrect_ima_msg
            elif trial_type == "execution":
                color_text = "blue"
                if seq_acc == 1:
                    fb_message = correct_exe_msg
                elif seq_acc == 0:
                    fb_message = incorrect_exe_msg
            seq_fb_text.setColor(color_text, colorSpace='rgb')
            seq_fb_text.setText(fb_message + '\n\n' + time_msg + ': ' + str(seq_time) + ' ' + seconds_msg +  '\n\n' + correct_trials_msg + '\n\n' + str(stim_counters[current_stim]) + ' ' + out_of_msg + ' ' + str(target_per_stim))
            sound_corr.setSound('stimuli/correct_sound.wav', secs=1, hamming=True)
            sound_corr.setVolume(corr_vol, log=False)
            sound_corr.seek(0)
            sound_incorr.setSound('stimuli/incorrect_sound.wav', secs=1, hamming=True)
            sound_incorr.setVolume(incorr_vol, log=False)
            sound_incorr.seek(0)
            # store start times for seq_fb
            seq_fb.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            seq_fb.tStart = globalClock.getTime(format='float')
            seq_fb.status = STARTED
            thisExp.addData('seq_fb.started', seq_fb.tStart)
            seq_fb.maxDuration = fb_dur
            # keep track of which components have finished
            seq_fbComponents = seq_fb.components
            for thisComponent in seq_fb.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "seq_fb" ---
            seq_fb.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisSeq_loop, 'status') and thisSeq_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > seq_fb.maxDuration-frameTolerance:
                    seq_fb.maxDurationReached = True
                    continueRoutine = False
                
                # *seq_fb_text* updates
                
                # if seq_fb_text is starting this frame...
                if seq_fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    seq_fb_text.frameNStart = frameN  # exact frame index
                    seq_fb_text.tStart = t  # local t and not account for scr refresh
                    seq_fb_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(seq_fb_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'seq_fb_text.started')
                    # update status
                    seq_fb_text.status = STARTED
                    seq_fb_text.setAutoDraw(True)
                
                # if seq_fb_text is active this frame...
                if seq_fb_text.status == STARTED:
                    # update params
                    pass
                
                # *sound_corr* updates
                
                # if sound_corr is starting this frame...
                if sound_corr.status == NOT_STARTED and tThisFlip >= 0.01-frameTolerance:
                    # keep track of start time/frame for later
                    sound_corr.frameNStart = frameN  # exact frame index
                    sound_corr.tStart = t  # local t and not account for scr refresh
                    sound_corr.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('sound_corr.started', tThisFlipGlobal)
                    # update status
                    sound_corr.status = STARTED
                    sound_corr.play(when=win)  # sync with win flip
                
                # if sound_corr is stopping this frame...
                if sound_corr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_corr.tStartRefresh + 1-frameTolerance or sound_corr.isFinished:
                        # keep track of stop time/frame for later
                        sound_corr.tStop = t  # not accounting for scr refresh
                        sound_corr.tStopRefresh = tThisFlipGlobal  # on global time
                        sound_corr.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sound_corr.stopped')
                        # update status
                        sound_corr.status = FINISHED
                        sound_corr.stop()
                
                # *sound_incorr* updates
                
                # if sound_incorr is starting this frame...
                if sound_incorr.status == NOT_STARTED and tThisFlip >= 0.01-frameTolerance:
                    # keep track of start time/frame for later
                    sound_incorr.frameNStart = frameN  # exact frame index
                    sound_incorr.tStart = t  # local t and not account for scr refresh
                    sound_incorr.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('sound_incorr.started', tThisFlipGlobal)
                    # update status
                    sound_incorr.status = STARTED
                    sound_incorr.play(when=win)  # sync with win flip
                
                # if sound_incorr is stopping this frame...
                if sound_incorr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > sound_incorr.tStartRefresh + 1-frameTolerance or sound_incorr.isFinished:
                        # keep track of stop time/frame for later
                        sound_incorr.tStop = t  # not accounting for scr refresh
                        sound_incorr.tStopRefresh = tThisFlipGlobal  # on global time
                        sound_incorr.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'sound_incorr.stopped')
                        # update status
                        sound_incorr.status = FINISHED
                        sound_incorr.stop()
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=seq_fb,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    seq_fb.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in seq_fb.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "seq_fb" ---
            for thisComponent in seq_fb.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for seq_fb
            seq_fb.tStop = globalClock.getTime(format='float')
            seq_fb.tStopRefresh = tThisFlipGlobal
            thisExp.addData('seq_fb.stopped', seq_fb.tStop)
            # Run 'End Routine' code from end_routine_code
            ## DOES NOT AUTO-TRANSLATE!!!!
            
            # check if the counters are complete
            if block_number <= practice_blocks:
                if all(value >= target_per_stim for value in stim_counters.values()):
                    seq_loop.finished = True
                    reps_per_block = 0
            sound_corr.pause()  # ensure sound has stopped at end of Routine
            sound_incorr.pause()  # ensure sound has stopped at end of Routine
            # the Routine "seq_fb" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisSeq_loop as finished
            if hasattr(thisSeq_loop, 'status'):
                thisSeq_loop.status = FINISHED
            # if awaiting a pause, pause now
            if seq_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                seq_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed reps_per_block repeats of 'seq_loop'
        seq_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        self_assess_loop = data.TrialHandler2(
            name='self_assess_loop',
            nReps=self_assess_show, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('self_assess_questions.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(self_assess_loop)  # add the loop to the experiment
        thisSelf_assess_loop = self_assess_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSelf_assess_loop.rgb)
        if thisSelf_assess_loop != None:
            for paramName in thisSelf_assess_loop:
                globals()[paramName] = thisSelf_assess_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSelf_assess_loop in self_assess_loop:
            self_assess_loop.status = STARTED
            if hasattr(thisSelf_assess_loop, 'status'):
                thisSelf_assess_loop.status = STARTED
            currentLoop = self_assess_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSelf_assess_loop.rgb)
            if thisSelf_assess_loop != None:
                for paramName in thisSelf_assess_loop:
                    globals()[paramName] = thisSelf_assess_loop[paramName]
            
            # --- Prepare to start Routine "self_assess" ---
            # create an object to store info about Routine self_assess
            self_assess = data.Routine(
                name='self_assess',
                components=[self_assess_text, slider, label_0, label_5, label_10, mouse_2, next_poly, next_text],
            )
            self_assess.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from self_assess_code
            win.mouseVisible = True
            # fetch language localisation from excel sheet
            try:
                self_assess_question = eval(f"self_assess_question_{lang_code}")
                label_min = eval(f"label_min_{lang_code}")
                label_middle = eval(f"label_middle_{lang_code}")
                label_max = eval(f"label_max_{lang_code}")
            except ReferenceError:
                self_assess_question = self_assess_question_EN
                label_min = label_min_EN
                label_middle = label_middle_EN
                label_max = label_max_EN
            self_assess_text.reset()
            self_assess_text.setText(self_assess_question)
            slider.reset()
            label_0.reset()
            label_0.setText(label_min)
            label_5.reset()
            label_5.setText(label_middle)
            label_10.reset()
            label_10.setText(label_max)
            # setup some python lists for storing info about the mouse_2
            mouse_2.x = []
            mouse_2.y = []
            mouse_2.leftButton = []
            mouse_2.midButton = []
            mouse_2.rightButton = []
            mouse_2.time = []
            mouse_2.clicked_name = []
            gotValidClick = False  # until a click is received
            next_text.setText(next_msg)
            # store start times for self_assess
            self_assess.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            self_assess.tStart = globalClock.getTime(format='float')
            self_assess.status = STARTED
            thisExp.addData('self_assess.started', self_assess.tStart)
            self_assess.maxDuration = None
            # keep track of which components have finished
            self_assessComponents = self_assess.components
            for thisComponent in self_assess.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "self_assess" ---
            self_assess.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisSelf_assess_loop, 'status') and thisSelf_assess_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *self_assess_text* updates
                
                # if self_assess_text is starting this frame...
                if self_assess_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    self_assess_text.frameNStart = frameN  # exact frame index
                    self_assess_text.tStart = t  # local t and not account for scr refresh
                    self_assess_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(self_assess_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'self_assess_text.started')
                    # update status
                    self_assess_text.status = STARTED
                    self_assess_text.setAutoDraw(True)
                
                # if self_assess_text is active this frame...
                if self_assess_text.status == STARTED:
                    # update params
                    pass
                
                # *slider* updates
                
                # if slider is starting this frame...
                if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider.frameNStart = frameN  # exact frame index
                    slider.tStart = t  # local t and not account for scr refresh
                    slider.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slider.started')
                    # update status
                    slider.status = STARTED
                    slider.setAutoDraw(True)
                
                # if slider is active this frame...
                if slider.status == STARTED:
                    # update params
                    pass
                
                # *label_0* updates
                
                # if label_0 is starting this frame...
                if label_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    label_0.frameNStart = frameN  # exact frame index
                    label_0.tStart = t  # local t and not account for scr refresh
                    label_0.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(label_0, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'label_0.started')
                    # update status
                    label_0.status = STARTED
                    label_0.setAutoDraw(True)
                
                # if label_0 is active this frame...
                if label_0.status == STARTED:
                    # update params
                    pass
                
                # *label_5* updates
                
                # if label_5 is starting this frame...
                if label_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    label_5.frameNStart = frameN  # exact frame index
                    label_5.tStart = t  # local t and not account for scr refresh
                    label_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(label_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'label_5.started')
                    # update status
                    label_5.status = STARTED
                    label_5.setAutoDraw(True)
                
                # if label_5 is active this frame...
                if label_5.status == STARTED:
                    # update params
                    pass
                
                # *label_10* updates
                
                # if label_10 is starting this frame...
                if label_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    label_10.frameNStart = frameN  # exact frame index
                    label_10.tStart = t  # local t and not account for scr refresh
                    label_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(label_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'label_10.started')
                    # update status
                    label_10.status = STARTED
                    label_10.setAutoDraw(True)
                
                # if label_10 is active this frame...
                if label_10.status == STARTED:
                    # update params
                    pass
                # *mouse_2* updates
                
                # if mouse_2 is starting this frame...
                if mouse_2.status == NOT_STARTED and slider.rating:
                    # keep track of start time/frame for later
                    mouse_2.frameNStart = frameN  # exact frame index
                    mouse_2.tStart = t  # local t and not account for scr refresh
                    mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_2.started', t)
                    # update status
                    mouse_2.status = STARTED
                    mouse_2.mouseClock.reset()
                    prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
                if mouse_2.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_2.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames(next_poly, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse_2):
                                    gotValidClick = True
                                    mouse_2.clicked_name.append(obj.name)
                                    mouse_2.clicked_name.append(obj.name)
                            if gotValidClick:
                                x, y = mouse_2.getPos()
                                mouse_2.x.append(x)
                                mouse_2.y.append(y)
                                buttons = mouse_2.getPressed()
                                mouse_2.leftButton.append(buttons[0])
                                mouse_2.midButton.append(buttons[1])
                                mouse_2.rightButton.append(buttons[2])
                                mouse_2.time.append(mouse_2.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
                # *next_poly* updates
                
                # if next_poly is starting this frame...
                if next_poly.status == NOT_STARTED and slider.rating:
                    # keep track of start time/frame for later
                    next_poly.frameNStart = frameN  # exact frame index
                    next_poly.tStart = t  # local t and not account for scr refresh
                    next_poly.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(next_poly, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'next_poly.started')
                    # update status
                    next_poly.status = STARTED
                    next_poly.setAutoDraw(True)
                
                # if next_poly is active this frame...
                if next_poly.status == STARTED:
                    # update params
                    pass
                
                # *next_text* updates
                
                # if next_text is starting this frame...
                if next_text.status == NOT_STARTED and slider.rating:
                    # keep track of start time/frame for later
                    next_text.frameNStart = frameN  # exact frame index
                    next_text.tStart = t  # local t and not account for scr refresh
                    next_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'next_text.started')
                    # update status
                    next_text.status = STARTED
                    next_text.setAutoDraw(True)
                
                # if next_text is active this frame...
                if next_text.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=self_assess,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    self_assess.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in self_assess.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "self_assess" ---
            for thisComponent in self_assess.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for self_assess
            self_assess.tStop = globalClock.getTime(format='float')
            self_assess.tStopRefresh = tThisFlipGlobal
            thisExp.addData('self_assess.stopped', self_assess.tStop)
            self_assess_loop.addData('slider.response', slider.getRating())
            self_assess_loop.addData('slider.rt', slider.getRT())
            # store data for self_assess_loop (TrialHandler)
            self_assess_loop.addData('mouse_2.x', mouse_2.x)
            self_assess_loop.addData('mouse_2.y', mouse_2.y)
            self_assess_loop.addData('mouse_2.leftButton', mouse_2.leftButton)
            self_assess_loop.addData('mouse_2.midButton', mouse_2.midButton)
            self_assess_loop.addData('mouse_2.rightButton', mouse_2.rightButton)
            self_assess_loop.addData('mouse_2.time', mouse_2.time)
            self_assess_loop.addData('mouse_2.clicked_name', mouse_2.clicked_name)
            # the Routine "self_assess" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisSelf_assess_loop as finished
            if hasattr(thisSelf_assess_loop, 'status'):
                thisSelf_assess_loop.status = FINISHED
            # if awaiting a pause, pause now
            if self_assess_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                self_assess_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed self_assess_show repeats of 'self_assess_loop'
        self_assess_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisBlocks_loop as finished
        if hasattr(thisBlocks_loop, 'status'):
            thisBlocks_loop.status = FINISHED
        # if awaiting a pause, pause now
        if blocks_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            blocks_loop.status = STARTED
    # completed total_blocks repeats of 'blocks_loop'
    blocks_loop.status = FINISHED
    
    
    # --- Prepare to start Routine "bye" ---
    # create an object to store info about Routine bye
    bye = data.Routine(
        name='bye',
        components=[bye_text],
    )
    bye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    bye_text.setText(bye_msg)
    # store start times for bye
    bye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bye.tStart = globalClock.getTime(format='float')
    bye.status = STARTED
    thisExp.addData('bye.started', bye.tStart)
    bye.maxDuration = 3
    # keep track of which components have finished
    byeComponents = bye.components
    for thisComponent in bye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bye" ---
    bye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > bye.maxDuration-frameTolerance:
            bye.maxDurationReached = True
            continueRoutine = False
        
        # *bye_text* updates
        
        # if bye_text is starting this frame...
        if bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bye_text.frameNStart = frameN  # exact frame index
            bye_text.tStart = t  # local t and not account for scr refresh
            bye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bye_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bye_text.started')
            # update status
            bye_text.status = STARTED
            bye_text.setAutoDraw(True)
        
        # if bye_text is active this frame...
        if bye_text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=bye,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bye" ---
    for thisComponent in bye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bye
    bye.tStop = globalClock.getTime(format='float')
    bye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bye.stopped', bye.tStop)
    thisExp.nextEntry()
    # the Routine "bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
