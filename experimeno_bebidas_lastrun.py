#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on abril 30, 2022, at 19:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from psychopy import core, visual, event
from pylsl import StreamInfo, StreamOutlet

info = StreamInfo(name='example_streme', type='Markers', channel_count=1,
                    channel_format='int32', source_id='example_stream_001')
outlet = StreamOutlet(info)

markers = {
    'jugo': [1],
    'refresco': [2],
    'leche': [3],
    'energetica': [4],
    'alcoholica': [5],
    'jugo2': [6],
    'yogurt': [7],
    'cafe': [8],
    'malteada': [9],
    'agua': [11],
    'cocacola': [22],
    'hersheys': [33],
    'atole': [44],
    'valle': [66],
    'danone': [77],
    'michoacana': [88],
    'prueba': [98],
    'malteadafresa': [99],
}

for _ in range(5):
    outlet.push_sample(markers['prueba'])
    print("marcador prueba")
    core.wait(0.5)

path= r'C:\Users\Invitad@\Desktop\bebidas_azucaradas-master\bebidas'
path2= r'C:\Users\Invitad@\Desktop\bebidas_azucaradas-master\bebidas\bebidas_preguntas'
list_of_images = []
testcosaimg=[]
list_of_images2 = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_images.append(os.path.join(root,file))
shuffle(list_of_images)

for root, dirs, files in os.walk(path):
    for file in files:
        testcosaimg.append(os.path.join(root,file))
shuffle(testcosaimg)
list_of_images.extend(testcosaimg)
testcosaimg=[]

for root, dirs, files in os.walk(path):
    for file in files:
        testcosaimg.append(os.path.join(root,file))
shuffle(testcosaimg)
list_of_images.extend(testcosaimg)

for root, dirs, files in os.walk(path2):
    for file in files:
        list_of_images2.append(os.path.join(root,file))

#shuffle(list_of_images)
veces_rep=len(list_of_images)
veces_rep2=len(list_of_images2)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'experimeno_bebidas'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Invitad@\\Desktop\\bebidas_azucaradas-master\\experimeno_bebidas_lastrun.py',
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
    size=[1200, 700], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "inicio_instruccion"
inicio_instruccionClock = core.Clock()
win.setColor('white')
Instrucciones = visual.TextStim(win=win, name='Instrucciones',
    text='Aquí van las instrucciones del experimento',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='grey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "mostrar_imagen"
mostrar_imagenClock = core.Clock()
img_num = 0


cruz = visual.ShapeStim(
    win=win, name='cruz', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
b_siguiente = keyboard.Keyboard()
imagen = visual.ImageStim(
    win=win,
    name='imagen', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Instrucciones_2"
Instrucciones_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='instrucciones de la visualización',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "respuesta_imagen1"
respuesta_imagen1Clock = core.Clock()
img_num1 = 0
cruz_img_resp1 = visual.ShapeStim(
    win=win, name='cruz_img_resp1', vertices='cross',
    size=(0.2, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
image_resp1 = visual.ImageStim(
    win=win,
    name='image_resp1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image_triste_alegre = visual.ImageStim(
    win=win,
    name='image_triste_alegre', 
    image='escala/triste_alegre.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1,0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
tr1 = visual.ShapeStim(
    win=win, name='tr1',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(-0.29, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-4.0, interpolate=True)
tr2 = visual.ShapeStim(
    win=win, name='tr2',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(-0.22, -0.05 ), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-5.0, interpolate=True)
tr3 = visual.ShapeStim(
    win=win, name='tr3',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(-0.15, -0.05 ), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-6.0, interpolate=True)
tr4 = visual.ShapeStim(
    win=win, name='tr4',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(-0.07, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-7.0, interpolate=True)
tr5 = visual.ShapeStim(
    win=win, name='tr5',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(0.01, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-8.0, interpolate=True)
tr6 = visual.ShapeStim(
    win=win, name='tr6',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(0.09, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-9.0, interpolate=True)
tr7 = visual.ShapeStim(
    win=win, name='tr7',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(0.16, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-10.0, interpolate=True)
tr8 = visual.ShapeStim(
    win=win, name='tr8',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(0.23, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-11.0, interpolate=True)
tr9 = visual.ShapeStim(
    win=win, name='tr9',
    size=(0.04, 0.05), vertices='circle',
    ori=0.0, pos=(0.31, -0.05), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-12.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "respuesta_imagen2"
respuesta_imagen2Clock = core.Clock()
image_dependiente_independiente = visual.ImageStim(
    win=win,
    name='image_dependiente_independiente', 
    image='escala/dependiente_independiente.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
td1 = visual.ShapeStim(
    win=win, name='td1',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.285, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-1.0, interpolate=True)
td2 = visual.ShapeStim(
    win=win, name='td2',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.212, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-2.0, interpolate=True)
td3 = visual.ShapeStim(
    win=win, name='td3',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.145, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-3.0, interpolate=True)
td4 = visual.ShapeStim(
    win=win, name='td4',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.065, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-4.0, interpolate=True)
td5 = visual.ShapeStim(
    win=win, name='td5',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.010, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-5.0, interpolate=True)
td6 = visual.ShapeStim(
    win=win, name='td6',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.090, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-6.0, interpolate=True)
td7 = visual.ShapeStim(
    win=win, name='td7',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.160, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-7.0, interpolate=True)
td8 = visual.ShapeStim(
    win=win, name='td8',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.239, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-8.0, interpolate=True)
td9 = visual.ShapeStim(
    win=win, name='td9',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.313, -0.08), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-9.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "respuesta_imagen3"
respuesta_imagen3Clock = core.Clock()
image_tranquilo_activo = visual.ImageStim(
    win=win,
    name='image_tranquilo_activo', 
    image='escala/tranquilo_activo.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ta1 = visual.ShapeStim(
    win=win, name='ta1',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.288, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-1.0, interpolate=True)
ta2 = visual.ShapeStim(
    win=win, name='ta2',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.216, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-2.0, interpolate=True)
ta3 = visual.ShapeStim(
    win=win, name='ta3',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.149, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-3.0, interpolate=True)
ta4 = visual.ShapeStim(
    win=win, name='ta4',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(-0.068, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-4.0, interpolate=True)
ta5 = visual.ShapeStim(
    win=win, name='ta5',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.007, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-5.0, interpolate=True)
ta6 = visual.ShapeStim(
    win=win, name='ta6',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.087, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-6.0, interpolate=True)
ta7 = visual.ShapeStim(
    win=win, name='ta7',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.157, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-7.0, interpolate=True)
ta8 = visual.ShapeStim(
    win=win, name='ta8',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.233, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-8.0, interpolate=True)
ta9 = visual.ShapeStim(
    win=win, name='ta9',
    size=(0.03, 0.03), vertices='circle',
    ori=0.0, pos=(0.306, -0.07), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='aqua', fillColor='aqua',
    opacity=None, depth=-9.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "fin"
finClock = core.Clock()
fin_text = visual.TextStim(win=win, name='fin_text',
    text='Este es el final del experimento.\n\nPresiona la tecla espacio para finalizar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='grey', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inicio_instruccion"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
inicio_instruccionComponents = [Instrucciones, key_resp_2]
for thisComponent in inicio_instruccionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inicio_instruccionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inicio_instruccion"-------
while continueRoutine:
    # get current time
    t = inicio_instruccionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inicio_instruccionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrucciones* updates
    if Instrucciones.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instrucciones.frameNStart = frameN  # exact frame index
        Instrucciones.tStart = t  # local t and not account for scr refresh
        Instrucciones.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instrucciones, 'tStartRefresh')  # time at next scr refresh
        Instrucciones.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inicio_instruccionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inicio_instruccion"-------
for thisComponent in inicio_instruccionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instrucciones.started', Instrucciones.tStartRefresh)
thisExp.addData('Instrucciones.stopped', Instrucciones.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "inicio_instruccion" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
imgse = data.TrialHandler(nReps=veces_rep, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='imgse')
thisExp.addLoop(imgse)  # add the loop to the experiment
thisImgse = imgse.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImgse.rgb)
if thisImgse != None:
    for paramName in thisImgse:
        exec('{} = thisImgse[paramName]'.format(paramName))

for thisImgse in imgse:
    currentLoop = imgse
    # abbreviate parameter names if possible (e.g. rgb = thisImgse.rgb)
    if thisImgse != None:
        for paramName in thisImgse:
            exec('{} = thisImgse[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "mostrar_imagen"-------
    continueRoutine = True
    # update component parameters for each repeat
    imgg = list_of_images[img_num]
    img_num+=1
    if "1.-" in imgg:
        print("encontrado")
    b_siguiente.keys = []
    b_siguiente.rt = []
    _b_siguiente_allKeys = []
    imagen.setImage(imgg)
    # keep track of which components have finished
    mostrar_imagenComponents = [cruz, b_siguiente, imagen]
    for thisComponent in mostrar_imagenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mostrar_imagenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "mostrar_imagen"-------
    while continueRoutine:
        # get current time
        t = mostrar_imagenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mostrar_imagenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz* updates
        if cruz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cruz.frameNStart = frameN  # exact frame index
            cruz.tStart = t  # local t and not account for scr refresh
            cruz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz, 'tStartRefresh')  # time at next scr refresh
            cruz.setAutoDraw(True)
        
        # *b_siguiente* updates
        waitOnFlip = False
        if b_siguiente.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            b_siguiente.frameNStart = frameN  # exact frame index
            b_siguiente.tStart = t  # local t and not account for scr refresh
            b_siguiente.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_siguiente, 'tStartRefresh')  # time at next scr refresh
            b_siguiente.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(b_siguiente.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(b_siguiente.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if b_siguiente.status == STARTED and not waitOnFlip:
            theseKeys = b_siguiente.getKeys(keyList=['space'], waitRelease=False)
            _b_siguiente_allKeys.extend(theseKeys)
            if len(_b_siguiente_allKeys):
                b_siguiente.keys = _b_siguiente_allKeys[-1].name  # just the last key pressed
                b_siguiente.rt = _b_siguiente_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *imagen* updates
        if imagen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            imagen.frameNStart = frameN  # exact frame index
            imagen.tStart = t  # local t and not account for scr refresh
            imagen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagen, 'tStartRefresh')  # time at next scr refresh
            imagen.setAutoDraw(True)
        if imagen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imagen.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imagen.tStop = t  # not accounting for scr refresh
                imagen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imagen, 'tStopRefresh')  # time at next scr refresh
                imagen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mostrar_imagenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "mostrar_imagen"-------
    for thisComponent in mostrar_imagenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    imgse.addData('cruz.started', cruz.tStartRefresh)
    imgse.addData('cruz.stopped', cruz.tStopRefresh)
    # check responses
    if b_siguiente.keys in ['', [], None]:  # No response was made
        b_siguiente.keys = None
    imgse.addData('b_siguiente.keys',b_siguiente.keys)
    if b_siguiente.keys != None:  # we had a response
        imgse.addData('b_siguiente.rt', b_siguiente.rt)
    imgse.addData('b_siguiente.started', b_siguiente.tStartRefresh)
    imgse.addData('b_siguiente.stopped', b_siguiente.tStopRefresh)
    imgse.addData('imagen.started', imagen.tStartRefresh)
    imgse.addData('imagen.stopped', imagen.tStopRefresh)
    # the Routine "mostrar_imagen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed veces_rep repeats of 'imgse'


# ------Prepare to start Routine "Instrucciones_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Instrucciones_2Components = [text, key_resp]
for thisComponent in Instrucciones_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instrucciones_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instrucciones_2"-------
while continueRoutine:
    # get current time
    t = Instrucciones_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instrucciones_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instrucciones_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrucciones_2"-------
for thisComponent in Instrucciones_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instrucciones_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
respuestas = data.TrialHandler(nReps=veces_rep2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='respuestas')
thisExp.addLoop(respuestas)  # add the loop to the experiment
thisRespuesta = respuestas.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRespuesta.rgb)
if thisRespuesta != None:
    for paramName in thisRespuesta:
        exec('{} = thisRespuesta[paramName]'.format(paramName))

for thisRespuesta in respuestas:
    currentLoop = respuestas
    # abbreviate parameter names if possible (e.g. rgb = thisRespuesta.rgb)
    if thisRespuesta != None:
        for paramName in thisRespuesta:
            exec('{} = thisRespuesta[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "respuesta_imagen1"-------
    continueRoutine = True
    # update component parameters for each repeat
    imggg = list_of_images2[img_num1]
    img_num1+=1
    image_resp1.setImage(imggg)
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respuesta_imagen1Components = [cruz_img_resp1, image_resp1, image_triste_alegre, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, mouse]
    for thisComponent in respuesta_imagen1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    respuesta_imagen1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "respuesta_imagen1"-------
    while continueRoutine:
        # get current time
        t = respuesta_imagen1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=respuesta_imagen1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cruz_img_resp1* updates
        if cruz_img_resp1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cruz_img_resp1.frameNStart = frameN  # exact frame index
            cruz_img_resp1.tStart = t  # local t and not account for scr refresh
            cruz_img_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cruz_img_resp1, 'tStartRefresh')  # time at next scr refresh
            cruz_img_resp1.setAutoDraw(True)
        if cruz_img_resp1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cruz_img_resp1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                cruz_img_resp1.tStop = t  # not accounting for scr refresh
                cruz_img_resp1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cruz_img_resp1, 'tStopRefresh')  # time at next scr refresh
                cruz_img_resp1.setAutoDraw(False)
        
        # *image_resp1* updates
        if image_resp1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            image_resp1.frameNStart = frameN  # exact frame index
            image_resp1.tStart = t  # local t and not account for scr refresh
            image_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_resp1, 'tStartRefresh')  # time at next scr refresh
            image_resp1.setAutoDraw(True)
        if image_resp1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_resp1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                image_resp1.tStop = t  # not accounting for scr refresh
                image_resp1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_resp1, 'tStopRefresh')  # time at next scr refresh
                image_resp1.setAutoDraw(False)
        
        # *image_triste_alegre* updates
        if image_triste_alegre.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            image_triste_alegre.frameNStart = frameN  # exact frame index
            image_triste_alegre.tStart = t  # local t and not account for scr refresh
            image_triste_alegre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_triste_alegre, 'tStartRefresh')  # time at next scr refresh
            image_triste_alegre.setAutoDraw(True)
        
        # *tr1* updates
        if tr1.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            tr1.frameNStart = frameN  # exact frame index
            tr1.tStart = t  # local t and not account for scr refresh
            tr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr1, 'tStartRefresh')  # time at next scr refresh
            tr1.setAutoDraw(True)
        
        # *tr2* updates
        if tr2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr2.frameNStart = frameN  # exact frame index
            tr2.tStart = t  # local t and not account for scr refresh
            tr2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr2, 'tStartRefresh')  # time at next scr refresh
            tr2.setAutoDraw(True)
        
        # *tr3* updates
        if tr3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr3.frameNStart = frameN  # exact frame index
            tr3.tStart = t  # local t and not account for scr refresh
            tr3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr3, 'tStartRefresh')  # time at next scr refresh
            tr3.setAutoDraw(True)
        
        # *tr4* updates
        if tr4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr4.frameNStart = frameN  # exact frame index
            tr4.tStart = t  # local t and not account for scr refresh
            tr4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr4, 'tStartRefresh')  # time at next scr refresh
            tr4.setAutoDraw(True)
        
        # *tr5* updates
        if tr5.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr5.frameNStart = frameN  # exact frame index
            tr5.tStart = t  # local t and not account for scr refresh
            tr5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr5, 'tStartRefresh')  # time at next scr refresh
            tr5.setAutoDraw(True)
        
        # *tr6* updates
        if tr6.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr6.frameNStart = frameN  # exact frame index
            tr6.tStart = t  # local t and not account for scr refresh
            tr6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr6, 'tStartRefresh')  # time at next scr refresh
            tr6.setAutoDraw(True)
        
        # *tr7* updates
        if tr7.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr7.frameNStart = frameN  # exact frame index
            tr7.tStart = t  # local t and not account for scr refresh
            tr7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr7, 'tStartRefresh')  # time at next scr refresh
            tr7.setAutoDraw(True)
        
        # *tr8* updates
        if tr8.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr8.frameNStart = frameN  # exact frame index
            tr8.tStart = t  # local t and not account for scr refresh
            tr8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr8, 'tStartRefresh')  # time at next scr refresh
            tr8.setAutoDraw(True)
        
        # *tr9* updates
        if tr9.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            tr9.frameNStart = frameN  # exact frame index
            tr9.tStart = t  # local t and not account for scr refresh
            tr9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tr9, 'tStartRefresh')  # time at next scr refresh
            tr9.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 4-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
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
                    try:
                        iter([tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9])
                        clickableList = [tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9]
                    except:
                        clickableList = [[tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respuesta_imagen1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "respuesta_imagen1"-------
    for thisComponent in respuesta_imagen1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    respuestas.addData('cruz_img_resp1.started', cruz_img_resp1.tStartRefresh)
    respuestas.addData('cruz_img_resp1.stopped', cruz_img_resp1.tStopRefresh)
    respuestas.addData('image_resp1.started', image_resp1.tStartRefresh)
    respuestas.addData('image_resp1.stopped', image_resp1.tStopRefresh)
    respuestas.addData('image_triste_alegre.started', image_triste_alegre.tStartRefresh)
    respuestas.addData('image_triste_alegre.stopped', image_triste_alegre.tStopRefresh)
    respuestas.addData('tr1.started', tr1.tStartRefresh)
    respuestas.addData('tr1.stopped', tr1.tStopRefresh)
    respuestas.addData('tr2.started', tr2.tStartRefresh)
    respuestas.addData('tr2.stopped', tr2.tStopRefresh)
    respuestas.addData('tr3.started', tr3.tStartRefresh)
    respuestas.addData('tr3.stopped', tr3.tStopRefresh)
    respuestas.addData('tr4.started', tr4.tStartRefresh)
    respuestas.addData('tr4.stopped', tr4.tStopRefresh)
    respuestas.addData('tr5.started', tr5.tStartRefresh)
    respuestas.addData('tr5.stopped', tr5.tStopRefresh)
    respuestas.addData('tr6.started', tr6.tStartRefresh)
    respuestas.addData('tr6.stopped', tr6.tStopRefresh)
    respuestas.addData('tr7.started', tr7.tStartRefresh)
    respuestas.addData('tr7.stopped', tr7.tStopRefresh)
    respuestas.addData('tr8.started', tr8.tStartRefresh)
    respuestas.addData('tr8.stopped', tr8.tStopRefresh)
    respuestas.addData('tr9.started', tr9.tStartRefresh)
    respuestas.addData('tr9.stopped', tr9.tStopRefresh)
    # store data for respuestas (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9])
            clickableList = [tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9]
        except:
            clickableList = [[tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8,tr9]]
        for obj in clickableList:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    respuestas.addData('mouse.x', x)
    respuestas.addData('mouse.y', y)
    respuestas.addData('mouse.leftButton', buttons[0])
    respuestas.addData('mouse.midButton', buttons[1])
    respuestas.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        respuestas.addData('mouse.clicked_name', mouse.clicked_name[0])
    respuestas.addData('mouse.started', mouse.tStart)
    respuestas.addData('mouse.stopped', mouse.tStop)
    # the Routine "respuesta_imagen1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "respuesta_imagen2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respuesta_imagen2Components = [image_dependiente_independiente, td1, td2, td3, td4, td5, td6, td7, td8, td9, mouse_2]
    for thisComponent in respuesta_imagen2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    respuesta_imagen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "respuesta_imagen2"-------
    while continueRoutine:
        # get current time
        t = respuesta_imagen2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=respuesta_imagen2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_dependiente_independiente* updates
        if image_dependiente_independiente.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_dependiente_independiente.frameNStart = frameN  # exact frame index
            image_dependiente_independiente.tStart = t  # local t and not account for scr refresh
            image_dependiente_independiente.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_dependiente_independiente, 'tStartRefresh')  # time at next scr refresh
            image_dependiente_independiente.setAutoDraw(True)
        
        # *td1* updates
        if td1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td1.frameNStart = frameN  # exact frame index
            td1.tStart = t  # local t and not account for scr refresh
            td1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td1, 'tStartRefresh')  # time at next scr refresh
            td1.setAutoDraw(True)
        
        # *td2* updates
        if td2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td2.frameNStart = frameN  # exact frame index
            td2.tStart = t  # local t and not account for scr refresh
            td2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td2, 'tStartRefresh')  # time at next scr refresh
            td2.setAutoDraw(True)
        
        # *td3* updates
        if td3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td3.frameNStart = frameN  # exact frame index
            td3.tStart = t  # local t and not account for scr refresh
            td3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td3, 'tStartRefresh')  # time at next scr refresh
            td3.setAutoDraw(True)
        
        # *td4* updates
        if td4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td4.frameNStart = frameN  # exact frame index
            td4.tStart = t  # local t and not account for scr refresh
            td4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td4, 'tStartRefresh')  # time at next scr refresh
            td4.setAutoDraw(True)
        
        # *td5* updates
        if td5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td5.frameNStart = frameN  # exact frame index
            td5.tStart = t  # local t and not account for scr refresh
            td5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td5, 'tStartRefresh')  # time at next scr refresh
            td5.setAutoDraw(True)
        
        # *td6* updates
        if td6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td6.frameNStart = frameN  # exact frame index
            td6.tStart = t  # local t and not account for scr refresh
            td6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td6, 'tStartRefresh')  # time at next scr refresh
            td6.setAutoDraw(True)
        
        # *td7* updates
        if td7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td7.frameNStart = frameN  # exact frame index
            td7.tStart = t  # local t and not account for scr refresh
            td7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td7, 'tStartRefresh')  # time at next scr refresh
            td7.setAutoDraw(True)
        
        # *td8* updates
        if td8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td8.frameNStart = frameN  # exact frame index
            td8.tStart = t  # local t and not account for scr refresh
            td8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td8, 'tStartRefresh')  # time at next scr refresh
            td8.setAutoDraw(True)
        
        # *td9* updates
        if td9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            td9.frameNStart = frameN  # exact frame index
            td9.tStart = t  # local t and not account for scr refresh
            td9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(td9, 'tStartRefresh')  # time at next scr refresh
            td9.setAutoDraw(True)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
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
                    try:
                        iter([td1,td2,td3,td4,td5,td6,td7,td8,td9])
                        clickableList = [td1,td2,td3,td4,td5,td6,td7,td8,td9]
                    except:
                        clickableList = [[td1,td2,td3,td4,td5,td6,td7,td8,td9]]
                    for obj in clickableList:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respuesta_imagen2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "respuesta_imagen2"-------
    for thisComponent in respuesta_imagen2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    respuestas.addData('image_dependiente_independiente.started', image_dependiente_independiente.tStartRefresh)
    respuestas.addData('image_dependiente_independiente.stopped', image_dependiente_independiente.tStopRefresh)
    respuestas.addData('td1.started', td1.tStartRefresh)
    respuestas.addData('td1.stopped', td1.tStopRefresh)
    respuestas.addData('td2.started', td2.tStartRefresh)
    respuestas.addData('td2.stopped', td2.tStopRefresh)
    respuestas.addData('td3.started', td3.tStartRefresh)
    respuestas.addData('td3.stopped', td3.tStopRefresh)
    respuestas.addData('td4.started', td4.tStartRefresh)
    respuestas.addData('td4.stopped', td4.tStopRefresh)
    respuestas.addData('td5.started', td5.tStartRefresh)
    respuestas.addData('td5.stopped', td5.tStopRefresh)
    respuestas.addData('td6.started', td6.tStartRefresh)
    respuestas.addData('td6.stopped', td6.tStopRefresh)
    respuestas.addData('td7.started', td7.tStartRefresh)
    respuestas.addData('td7.stopped', td7.tStopRefresh)
    respuestas.addData('td8.started', td8.tStartRefresh)
    respuestas.addData('td8.stopped', td8.tStopRefresh)
    respuestas.addData('td9.started', td9.tStartRefresh)
    respuestas.addData('td9.stopped', td9.tStopRefresh)
    # store data for respuestas (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([td1,td2,td3,td4,td5,td6,td7,td8,td9])
            clickableList = [td1,td2,td3,td4,td5,td6,td7,td8,td9]
        except:
            clickableList = [[td1,td2,td3,td4,td5,td6,td7,td8,td9]]
        for obj in clickableList:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    respuestas.addData('mouse_2.x', x)
    respuestas.addData('mouse_2.y', y)
    respuestas.addData('mouse_2.leftButton', buttons[0])
    respuestas.addData('mouse_2.midButton', buttons[1])
    respuestas.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        respuestas.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    respuestas.addData('mouse_2.started', mouse_2.tStart)
    respuestas.addData('mouse_2.stopped', mouse_2.tStop)
    # the Routine "respuesta_imagen2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "respuesta_imagen3"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    respuesta_imagen3Components = [image_tranquilo_activo, ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, mouse_3]
    for thisComponent in respuesta_imagen3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    respuesta_imagen3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "respuesta_imagen3"-------
    while continueRoutine:
        # get current time
        t = respuesta_imagen3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=respuesta_imagen3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_tranquilo_activo* updates
        if image_tranquilo_activo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_tranquilo_activo.frameNStart = frameN  # exact frame index
            image_tranquilo_activo.tStart = t  # local t and not account for scr refresh
            image_tranquilo_activo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_tranquilo_activo, 'tStartRefresh')  # time at next scr refresh
            image_tranquilo_activo.setAutoDraw(True)
        
        # *ta1* updates
        if ta1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta1.frameNStart = frameN  # exact frame index
            ta1.tStart = t  # local t and not account for scr refresh
            ta1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta1, 'tStartRefresh')  # time at next scr refresh
            ta1.setAutoDraw(True)
        
        # *ta2* updates
        if ta2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta2.frameNStart = frameN  # exact frame index
            ta2.tStart = t  # local t and not account for scr refresh
            ta2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta2, 'tStartRefresh')  # time at next scr refresh
            ta2.setAutoDraw(True)
        
        # *ta3* updates
        if ta3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta3.frameNStart = frameN  # exact frame index
            ta3.tStart = t  # local t and not account for scr refresh
            ta3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta3, 'tStartRefresh')  # time at next scr refresh
            ta3.setAutoDraw(True)
        
        # *ta4* updates
        if ta4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta4.frameNStart = frameN  # exact frame index
            ta4.tStart = t  # local t and not account for scr refresh
            ta4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta4, 'tStartRefresh')  # time at next scr refresh
            ta4.setAutoDraw(True)
        
        # *ta5* updates
        if ta5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta5.frameNStart = frameN  # exact frame index
            ta5.tStart = t  # local t and not account for scr refresh
            ta5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta5, 'tStartRefresh')  # time at next scr refresh
            ta5.setAutoDraw(True)
        
        # *ta6* updates
        if ta6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta6.frameNStart = frameN  # exact frame index
            ta6.tStart = t  # local t and not account for scr refresh
            ta6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta6, 'tStartRefresh')  # time at next scr refresh
            ta6.setAutoDraw(True)
        
        # *ta7* updates
        if ta7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta7.frameNStart = frameN  # exact frame index
            ta7.tStart = t  # local t and not account for scr refresh
            ta7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta7, 'tStartRefresh')  # time at next scr refresh
            ta7.setAutoDraw(True)
        
        # *ta8* updates
        if ta8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta8.frameNStart = frameN  # exact frame index
            ta8.tStart = t  # local t and not account for scr refresh
            ta8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta8, 'tStartRefresh')  # time at next scr refresh
            ta8.setAutoDraw(True)
        
        # *ta9* updates
        if ta9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ta9.frameNStart = frameN  # exact frame index
            ta9.tStart = t  # local t and not account for scr refresh
            ta9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ta9, 'tStartRefresh')  # time at next scr refresh
            ta9.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9])
                        clickableList = [ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9]
                    except:
                        clickableList = [[ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9]]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in respuesta_imagen3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "respuesta_imagen3"-------
    for thisComponent in respuesta_imagen3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    respuestas.addData('image_tranquilo_activo.started', image_tranquilo_activo.tStartRefresh)
    respuestas.addData('image_tranquilo_activo.stopped', image_tranquilo_activo.tStopRefresh)
    respuestas.addData('ta1.started', ta1.tStartRefresh)
    respuestas.addData('ta1.stopped', ta1.tStopRefresh)
    respuestas.addData('ta2.started', ta2.tStartRefresh)
    respuestas.addData('ta2.stopped', ta2.tStopRefresh)
    respuestas.addData('ta3.started', ta3.tStartRefresh)
    respuestas.addData('ta3.stopped', ta3.tStopRefresh)
    respuestas.addData('ta4.started', ta4.tStartRefresh)
    respuestas.addData('ta4.stopped', ta4.tStopRefresh)
    respuestas.addData('ta5.started', ta5.tStartRefresh)
    respuestas.addData('ta5.stopped', ta5.tStopRefresh)
    respuestas.addData('ta6.started', ta6.tStartRefresh)
    respuestas.addData('ta6.stopped', ta6.tStopRefresh)
    respuestas.addData('ta7.started', ta7.tStartRefresh)
    respuestas.addData('ta7.stopped', ta7.tStopRefresh)
    respuestas.addData('ta8.started', ta8.tStartRefresh)
    respuestas.addData('ta8.stopped', ta8.tStopRefresh)
    respuestas.addData('ta9.started', ta9.tStartRefresh)
    respuestas.addData('ta9.stopped', ta9.tStopRefresh)
    # store data for respuestas (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9])
            clickableList = [ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9]
        except:
            clickableList = [[ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9]]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    respuestas.addData('mouse_3.x', x)
    respuestas.addData('mouse_3.y', y)
    respuestas.addData('mouse_3.leftButton', buttons[0])
    respuestas.addData('mouse_3.midButton', buttons[1])
    respuestas.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        respuestas.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    respuestas.addData('mouse_3.started', mouse_3.tStart)
    respuestas.addData('mouse_3.stopped', mouse_3.tStop)
    # the Routine "respuesta_imagen3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed veces_rep2 repeats of 'respuestas'


# ------Prepare to start Routine "fin"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
finComponents = [fin_text, key_resp_4]
for thisComponent in finComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fin"-------
while continueRoutine:
    # get current time
    t = finClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fin_text* updates
    if fin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fin_text.frameNStart = frameN  # exact frame index
        fin_text.tStart = t  # local t and not account for scr refresh
        fin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fin_text, 'tStartRefresh')  # time at next scr refresh
        fin_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin"-------
for thisComponent in finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fin_text.started', fin_text.tStartRefresh)
thisExp.addData('fin_text.stopped', fin_text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
