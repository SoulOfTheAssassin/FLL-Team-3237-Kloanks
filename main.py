from pybricks.pupdevices import Motor, Button
from pybricks.parameters import Port, Color, Icon
from pybricks.tools import wait, Matrix, StopWatch, hub_menu
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub

# Constants
DRIVEBASE_WHEEL_DIAMETER = 56
DRIVEBASE_AXLE_TRACK = 105 # confirm this value
LOW_VOLTAGE = 7000
HIGH_VOLTAGE = 8000

# Define the Robot
class Robot:
    def __init__(self):
        # DRIVE MOTORS: Left (A) Right (B) Big (E) Small (F)
        self.leftDrive = Motor(Port.A)
        self.rightDrive = Motor(Port.B)
        self.big = Motor(Port.E)
        self.small = Motor(Port.F)

        # Defines the drivebase
        self.driveBase = DriveBase(self.leftDrive, self.rightDrive, DRIVEBASE_WHEEL_DIAMETER, DRIVEBASE_AXLE_TRACK)
        self.driveBase.use_gyro(True)

        # Defines the hub
        self.hub = PrimeHub()

    def DisplayNumber(self, number:int):
        self.hub.display.off()
        self.hub.display.number(number)

    def StatusLight(self, color:Color):
        self.hub.light.off()
        self.hub.light.on(color)
    
    def BatteryDisplay(self):
        # display battery of hub
        v = 7900
        vPct = Rescale(v, LOW_VOLTAGE, HIGH_VOLTAGE)
        print(f"Battery %: {vPct}")
        if vPct < 70:
            print("Battery is below 70% Please charge!")
            self.StatusLight(Color.RED)
        else:
            self.StatusLight(Color.GREEN)

class Animations:
    running = [
        Matrix([
            [0, 0, 100, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 0, 0]
        ]), Matrix([
            [100, 0, 0, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 0, 0, 100]
        ]), Matrix([
            [100, 100, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 100, 100]
        ]), Matrix([
            [100, 100, 100, 0, 0],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [0, 0, 100, 100, 100]
        ]), Matrix([
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 100],
            [0, 0, 0, 0, 100],
            [0, 100, 100, 100, 100]
        ]), Matrix([
            [100, 100, 100, 100, 100],
            [100, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 100],
            [100, 100, 100, 100, 100]
        ]), Matrix([
            [100, 100, 100, 100, 100],
            [0, 0, 0, 0, 100],
            [0, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 100, 100, 100, 100]
        ]), Matrix([
            [0, 100, 100, 100, 100],
            [0, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 0],
            [100, 100, 100, 100, 0]
        ])
    ]

def run1(r:Robot):
    r.driveBase.turn(-90)
    r.driveBase.straight(100)
    # do 4 sqaure crab thing
    r.driveBase.straight(-20)
    r.driveBase.turn(90)
    r.driveBase.straight(100)
    r.driveBase.turn(-45)
    # do octopus push thing
    r.driveBase.straight(30)
    r.driveBase.straight(-30)
    r.driveBase.turn(90)
    r.driveBase.straight(100)
    # do leafy green thing

def run2(r:Robot):
    pass

def run3(r:Robot):
    pass

def run4(r:Robot):
    pass

def run5(r:Robot):
    pass

def run6(r:Robot):
    pass

def run7(r:Robot):
    pass

def Rescale(value, in_min, in_max):
    neg = value / abs(value) # will either be 1 or -1
    value = abs(value)
    if value < in_min: value = in_min
    if value > in_max: value = in_max
    retvalue = (value - in_min) * (100 / (in_max - in_min))
    if retvalue > 100: retvalue = 100
    if retvalue < 0: retvalue = 0
    return retvalue * neg

def RunMission(r:Robot, selected):
    # run current selection
    r.StatusLight(Color.YELLOW)
    r.hub.display.animate(Animations.running, 30)
    print(f"Running #{selected}...")
    start_time = StopWatch.time()
    eval(f'run{str(selected)}(r)')
    print(f"Done running #{selected}. Time: {StopWatch.time() - start_time}")
    r.StatusLight(Color.GREEN)

Robot.BatteryDisplay()

# run menu
while True:
    selected = hub_menu("1", "2", "3", "4", "5", "6", "7")
    RunMission(Robot(), selected)