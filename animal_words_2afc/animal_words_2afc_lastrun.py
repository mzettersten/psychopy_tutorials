#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.1),
    on Thu Aug  5 14:07:51 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.1'
expName = 'psychopy_tutorial_test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/martinzettersten/GitHub/psychopy_tutorials/animal_words_2afc/animal_words_2afc_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
star = visual.ShapeStim(
    win=win, name='star', vertices='star7',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='yellow', fillColor='yellow',
    opacity=None, depth=0.0, interpolate=True)
right_rectangle = visual.Rect(
    win=win, name='right_rectangle',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0.5, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
left_rectangle = visual.Rect(
    win=win, name='left_rectangle',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(-0.5, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
right_image = visual.ImageStim(
    win=win,
    name='right_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
left_image = visual.ImageStim(
    win=win,
    name='left_image', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.6,0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
left_rectangle_trial = visual.Rect(
    win=win, name='left_rectangle_trial',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(-0.5, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
right_rectangle_trial = visual.Rect(
    win=win, name='right_rectangle_trial',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0.5, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
left_image_trial = visual.ImageStim(
    win=win,
    name='left_image_trial', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
right_image_trial = visual.ImageStim(
    win=win,
    name='right_image_trial', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
trial_mouse = event.Mouse(win=win)
x, y = [None, None]
trial_mouse.mouseClock = core.Clock()
trial_sound = sound.Sound('A', secs=1.5, stereo=True, hamming=True,
    name='trial_sound')
trial_sound.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('psychopy_tutorial_trials.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "start"-------
    continueRoutine = True
    # update component parameters for each repeat
    right_image.setImage(r_image)
    left_image.setImage(l_image)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    startComponents = [star, right_rectangle, left_rectangle, right_image, left_image, mouse]
    for thisComponent in startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start"-------
    while continueRoutine:
        # get current time
        t = startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *star* updates
        if star.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            star.frameNStart = frameN  # exact frame index
            star.tStart = t  # local t and not account for scr refresh
            star.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(star, 'tStartRefresh')  # time at next scr refresh
            star.setAutoDraw(True)
        
        # *right_rectangle* updates
        if right_rectangle.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            right_rectangle.frameNStart = frameN  # exact frame index
            right_rectangle.tStart = t  # local t and not account for scr refresh
            right_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_rectangle, 'tStartRefresh')  # time at next scr refresh
            right_rectangle.setAutoDraw(True)
        
        # *left_rectangle* updates
        if left_rectangle.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            left_rectangle.frameNStart = frameN  # exact frame index
            left_rectangle.tStart = t  # local t and not account for scr refresh
            left_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_rectangle, 'tStartRefresh')  # time at next scr refresh
            left_rectangle.setAutoDraw(True)
        
        # *right_image* updates
        if right_image.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            right_image.frameNStart = frameN  # exact frame index
            right_image.tStart = t  # local t and not account for scr refresh
            right_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_image, 'tStartRefresh')  # time at next scr refresh
            right_image.setAutoDraw(True)
        
        # *left_image* updates
        if left_image.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            left_image.frameNStart = frameN  # exact frame index
            left_image.tStart = t  # local t and not account for scr refresh
            left_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_image, 'tStartRefresh')  # time at next scr refresh
            left_image.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(star)
                        clickableList = star
                    except:
                        clickableList = [star]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start"-------
    for thisComponent in startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('star.started', star.tStartRefresh)
    trials.addData('star.stopped', star.tStopRefresh)
    trials.addData('right_rectangle.started', right_rectangle.tStartRefresh)
    trials.addData('right_rectangle.stopped', right_rectangle.tStopRefresh)
    trials.addData('left_rectangle.started', left_rectangle.tStartRefresh)
    trials.addData('left_rectangle.stopped', left_rectangle.tStopRefresh)
    trials.addData('right_image.started', right_image.tStartRefresh)
    trials.addData('right_image.stopped', right_image.tStopRefresh)
    trials.addData('left_image.started', left_image.tStartRefresh)
    trials.addData('left_image.stopped', left_image.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(mouse.x): trials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    left_image_trial.setImage(l_image)
    right_image_trial.setImage(r_image)
    # setup some python lists for storing info about the trial_mouse
    trial_mouse.x = []
    trial_mouse.y = []
    trial_mouse.leftButton = []
    trial_mouse.midButton = []
    trial_mouse.rightButton = []
    trial_mouse.time = []
    trial_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    trial_sound.setSound(target_sound, secs=1.5, hamming=True)
    trial_sound.setVolume(1.0, log=False)
    # keep track of which components have finished
    trialComponents = [left_rectangle_trial, right_rectangle_trial, left_image_trial, right_image_trial, trial_mouse, trial_sound]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *left_rectangle_trial* updates
        if left_rectangle_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_rectangle_trial.frameNStart = frameN  # exact frame index
            left_rectangle_trial.tStart = t  # local t and not account for scr refresh
            left_rectangle_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_rectangle_trial, 'tStartRefresh')  # time at next scr refresh
            left_rectangle_trial.setAutoDraw(True)
        
        # *right_rectangle_trial* updates
        if right_rectangle_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_rectangle_trial.frameNStart = frameN  # exact frame index
            right_rectangle_trial.tStart = t  # local t and not account for scr refresh
            right_rectangle_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_rectangle_trial, 'tStartRefresh')  # time at next scr refresh
            right_rectangle_trial.setAutoDraw(True)
        
        # *left_image_trial* updates
        if left_image_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_image_trial.frameNStart = frameN  # exact frame index
            left_image_trial.tStart = t  # local t and not account for scr refresh
            left_image_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_image_trial, 'tStartRefresh')  # time at next scr refresh
            left_image_trial.setAutoDraw(True)
        
        # *right_image_trial* updates
        if right_image_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_image_trial.frameNStart = frameN  # exact frame index
            right_image_trial.tStart = t  # local t and not account for scr refresh
            right_image_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_image_trial, 'tStartRefresh')  # time at next scr refresh
            right_image_trial.setAutoDraw(True)
        # *trial_mouse* updates
        if trial_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_mouse.frameNStart = frameN  # exact frame index
            trial_mouse.tStart = t  # local t and not account for scr refresh
            trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_mouse, 'tStartRefresh')  # time at next scr refresh
            trial_mouse.status = STARTED
            trial_mouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if trial_mouse.status == STARTED:  # only update if started and not finished!
            x, y = trial_mouse.getPos()
            trial_mouse.x.append(x)
            trial_mouse.y.append(y)
            buttons = trial_mouse.getPressed()
            trial_mouse.leftButton.append(buttons[0])
            trial_mouse.midButton.append(buttons[1])
            trial_mouse.rightButton.append(buttons[2])
            trial_mouse.time.append(trial_mouse.mouseClock.getTime())
            buttons = trial_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([left_image_trial,right_image_trial,left_rectangle_trial,right_rectangle_trial])
                        clickableList = [left_image_trial,right_image_trial,left_rectangle_trial,right_rectangle_trial]
                    except:
                        clickableList = [[left_image_trial,right_image_trial,left_rectangle_trial,right_rectangle_trial]]
                    for obj in clickableList:
                        if obj.contains(trial_mouse):
                            gotValidClick = True
                            trial_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # start/stop trial_sound
        if trial_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_sound.frameNStart = frameN  # exact frame index
            trial_sound.tStart = t  # local t and not account for scr refresh
            trial_sound.tStartRefresh = tThisFlipGlobal  # on global time
            trial_sound.play(when=win)  # sync with win flip
        if trial_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_sound.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                trial_sound.tStop = t  # not accounting for scr refresh
                trial_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_sound, 'tStopRefresh')  # time at next scr refresh
                trial_sound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('left_rectangle_trial.started', left_rectangle_trial.tStartRefresh)
    trials.addData('left_rectangle_trial.stopped', left_rectangle_trial.tStopRefresh)
    trials.addData('right_rectangle_trial.started', right_rectangle_trial.tStartRefresh)
    trials.addData('right_rectangle_trial.stopped', right_rectangle_trial.tStopRefresh)
    trials.addData('left_image_trial.started', left_image_trial.tStartRefresh)
    trials.addData('left_image_trial.stopped', left_image_trial.tStopRefresh)
    trials.addData('right_image_trial.started', right_image_trial.tStartRefresh)
    trials.addData('right_image_trial.stopped', right_image_trial.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('trial_mouse.x', trial_mouse.x)
    trials.addData('trial_mouse.y', trial_mouse.y)
    trials.addData('trial_mouse.leftButton', trial_mouse.leftButton)
    trials.addData('trial_mouse.midButton', trial_mouse.midButton)
    trials.addData('trial_mouse.rightButton', trial_mouse.rightButton)
    trials.addData('trial_mouse.time', trial_mouse.time)
    trials.addData('trial_mouse.clicked_name', trial_mouse.clicked_name)
    trials.addData('trial_mouse.started', trial_mouse.tStart)
    trials.addData('trial_mouse.stopped', trial_mouse.tStop)
    trial_sound.stop()  # ensure sound has stopped at end of routine
    trials.addData('trial_sound.started', trial_sound.tStartRefresh)
    trials.addData('trial_sound.stopped', trial_sound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
