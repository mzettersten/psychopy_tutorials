/************************** 
 * Animal_Words_2Afc Test *
 **************************/


// store info about the experiment session:
let expName = 'animal_words_2afc';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/dog.wav', 'path': 'stimuli/dog.wav'},
    {'name': 'psychopy_tutorial_trials.csv', 'path': 'psychopy_tutorial_trials.csv'},
    {'name': 'stimuli/dog.png', 'path': 'stimuli/dog.png'},
    {'name': 'stimuli/cat.png', 'path': 'stimuli/cat.png'},
    {'name': 'stimuli/cat.wav', 'path': 'stimuli/cat.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.1';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var startClock;
var star;
var right_rectangle;
var left_rectangle;
var right_image;
var left_image;
var mouse;
var trialClock;
var left_rectangle_trial;
var right_rectangle_trial;
var left_image_trial;
var right_image_trial;
var trial_mouse;
var trial_sound;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  star = new visual.ShapeStim ({
    win: psychoJS.window, name: 'star', 
    vertices: 'star7', size: [0.2, 0.2],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('yellow'),
    fillColor: new util.Color('yellow'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  right_rectangle = new visual.Rect ({
    win: psychoJS.window, name: 'right_rectangle', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0.5, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  left_rectangle = new visual.Rect ({
    win: psychoJS.window, name: 'left_rectangle', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [(- 0.5), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  right_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  left_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  left_rectangle_trial = new visual.Rect ({
    win: psychoJS.window, name: 'left_rectangle_trial', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [(- 0.5), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  right_rectangle_trial = new visual.Rect ({
    win: psychoJS.window, name: 'right_rectangle_trial', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0.0, pos: [0.5, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  left_image_trial = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_image_trial', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.5), 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  right_image_trial = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_image_trial', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.5, 0], size : [0.6, 0.6],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  trial_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  trial_mouse.mouseClock = new util.Clock();
  trial_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.5,
    });
  trial_sound.setVolume(1.0);
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'psychopy_tutorial_trials.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(startRoutineBegin(snapshot));
      trialsLoopScheduler.add(startRoutineEachFrame());
      trialsLoopScheduler.add(startRoutineEnd());
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var gotValidClick;
var startComponents;
function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'start'-------
    t = 0;
    startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    right_image.setImage(r_image);
    left_image.setImage(l_image);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse.mouseClock.reset();
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(star);
    startComponents.push(right_rectangle);
    startComponents.push(left_rectangle);
    startComponents.push(right_image);
    startComponents.push(left_image);
    startComponents.push(mouse);
    
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function startRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'start'-------
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *star* updates
    if (t >= 0.3 && star.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      star.tStart = t;  // (not accounting for frame time here)
      star.frameNStart = frameN;  // exact frame index
      
      star.setAutoDraw(true);
    }

    
    // *right_rectangle* updates
    if (t >= 0.3 && right_rectangle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_rectangle.tStart = t;  // (not accounting for frame time here)
      right_rectangle.frameNStart = frameN;  // exact frame index
      
      right_rectangle.setAutoDraw(true);
    }

    
    // *left_rectangle* updates
    if (t >= 0.3 && left_rectangle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_rectangle.tStart = t;  // (not accounting for frame time here)
      left_rectangle.frameNStart = frameN;  // exact frame index
      
      left_rectangle.setAutoDraw(true);
    }

    
    // *right_image* updates
    if (t >= 0.3 && right_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image.tStart = t;  // (not accounting for frame time here)
      right_image.frameNStart = frameN;  // exact frame index
      
      right_image.setAutoDraw(true);
    }

    
    // *left_image* updates
    if (t >= 0.3 && left_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image.tStart = t;  // (not accounting for frame time here)
      left_image.frameNStart = frameN;  // exact frame index
      
      left_image.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.3 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [star]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRoutineEnd() {
  return async function () {
    //------Ending Routine 'start'-------
    startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    left_image_trial.setImage(l_image);
    right_image_trial.setImage(r_image);
    // setup some python lists for storing info about the trial_mouse
    // current position of the mouse:
    trial_mouse.x = [];
    trial_mouse.y = [];
    trial_mouse.leftButton = [];
    trial_mouse.midButton = [];
    trial_mouse.rightButton = [];
    trial_mouse.time = [];
    trial_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    trial_sound = new sound.Sound({
    win: psychoJS.window,
    value: target_sound,
    secs: 1.5,
    });
    trial_sound.secs=1.5;
    trial_sound.setVolume(1.0);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(left_rectangle_trial);
    trialComponents.push(right_rectangle_trial);
    trialComponents.push(left_image_trial);
    trialComponents.push(right_image_trial);
    trialComponents.push(trial_mouse);
    trialComponents.push(trial_sound);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *left_rectangle_trial* updates
    if (t >= 0.0 && left_rectangle_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_rectangle_trial.tStart = t;  // (not accounting for frame time here)
      left_rectangle_trial.frameNStart = frameN;  // exact frame index
      
      left_rectangle_trial.setAutoDraw(true);
    }

    
    // *right_rectangle_trial* updates
    if (t >= 0.0 && right_rectangle_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_rectangle_trial.tStart = t;  // (not accounting for frame time here)
      right_rectangle_trial.frameNStart = frameN;  // exact frame index
      
      right_rectangle_trial.setAutoDraw(true);
    }

    
    // *left_image_trial* updates
    if (t >= 0.0 && left_image_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_image_trial.tStart = t;  // (not accounting for frame time here)
      left_image_trial.frameNStart = frameN;  // exact frame index
      
      left_image_trial.setAutoDraw(true);
    }

    
    // *right_image_trial* updates
    if (t >= 0.0 && right_image_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_image_trial.tStart = t;  // (not accounting for frame time here)
      right_image_trial.frameNStart = frameN;  // exact frame index
      
      right_image_trial.setAutoDraw(true);
    }

    // *trial_mouse* updates
    if (t >= 0.0 && trial_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_mouse.tStart = t;  // (not accounting for frame time here)
      trial_mouse.frameNStart = frameN;  // exact frame index
      
      trial_mouse.status = PsychoJS.Status.STARTED;
      trial_mouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (trial_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = trial_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = trial_mouse.getPos();
          trial_mouse.x.push(_mouseXYs[0]);
          trial_mouse.y.push(_mouseXYs[1]);
          trial_mouse.leftButton.push(_mouseButtons[0]);
          trial_mouse.midButton.push(_mouseButtons[1]);
          trial_mouse.rightButton.push(_mouseButtons[2]);
          trial_mouse.time.push(trial_mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [left_image_trial,right_image_trial,left_rectangle_trial,right_rectangle_trial]) {
            if (obj.contains(trial_mouse)) {
              gotValidClick = true;
              trial_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // start/stop trial_sound
    if (t >= 0.0 && trial_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_sound.tStart = t;  // (not accounting for frame time here)
      trial_sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ trial_sound.play(); });  // screen flip
      trial_sound.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (1.5 > 0.5) {
        trial_sound.stop();  // stop the sound (if longer than duration)
      }
      trial_sound.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('trial_mouse.x', trial_mouse.x);
    psychoJS.experiment.addData('trial_mouse.y', trial_mouse.y);
    psychoJS.experiment.addData('trial_mouse.leftButton', trial_mouse.leftButton);
    psychoJS.experiment.addData('trial_mouse.midButton', trial_mouse.midButton);
    psychoJS.experiment.addData('trial_mouse.rightButton', trial_mouse.rightButton);
    psychoJS.experiment.addData('trial_mouse.time', trial_mouse.time);
    psychoJS.experiment.addData('trial_mouse.clicked_name', trial_mouse.clicked_name);
    
    trial_sound.stop();  // ensure sound has stopped at end of routine
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
