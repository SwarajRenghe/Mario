import signal
import sys
import tty
import termios


class inputFunctionClass:
    """
            Create a function that reads input from standard I/O 
            without needing to press an enter / escape char
    """

    def __call__(self):
        """
                Is called when the instance of this class is called, as opposed to when the class itself is called
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


class noInputRecievedException (Exception):
    """
            Defines a custom exception, which is calle when 
            input is None
    """
    pass


def noInputRecievedHandler(signalNumber, frameObject):
    """
            Called when timeout is reached; raises the user defined
            error noInputRecievedException
    """
    raise noInputRecievedException


def getInput(inputFunction, timeout=0.1):
    """
            Waits for input within timeout seconds, else
            proceeds with an input = None
            inputFunction is an object of inputFunctionClass, 
            it is the prefered input mode
    """
    signal.signal(signal.SIGALRM, noInputRecievedHandler)
    # Assigns the function alarmHandler when signal.SIGALRM is raised (which happens when signal.setitimer runs)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    # Sends an alarm after timeout seconds (we're not using singal.alarm because that only takes integers)

    try:
        enteredKey = inputFunction()
        signal.alarm(0)
        return enteredKey
    except:
        return None
