from wheel.wheelfile import WheelFile
from wheel.cli import WheelError
def iswheel(file):
    try:
        r=WheelFile(file)
        return True
    except WheelError:
        return False
def pure_filename(old):
    try:
        return WheelFile(old).parsed_filename.group('namever')
    except:
        return old.split('-py')[0]
