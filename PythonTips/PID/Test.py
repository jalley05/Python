
import PID
import time
import matplotlib.pyplot as plt
import numpy as np
#from scipy.interpolate import spline
#from scipy.interpolate import BSpline, make_interp_spline #  Switched to BSpline

def test_pid(P = 0.2,  I = 0.0, D= 0.0, L=20):
    pid = PID.PID(P, I, D)

    pid.SetPoint=0.0 # 0 is the target rate error

    END = L
    feedback = 0

    np.random.seed(5)

    feedback_list   = []
    setpoint_list   = []
    p_list = []
    i_list = []
    d_list = []
    err_list = []

    for i in range(1, END):
        pid.update(feedback)
        output = pid.output
        if pid.SetPoint > 0:
            feedback += (output - (1/i))
        if i>9:
            pid.SetPoint = 50

        #feedback += output + np.random.uniform(-1.0, 1.0)

        #if i == END//2:
        #    feedback += 20.0

        time.sleep(0.01)

        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        p_list.append(pid.PTerm)
        i_list.append(pid.ITerm * pid.Ki)
        d_list.append(pid.DTerm * pid.Kd)
        err_list.append(pid.error)

    #plt.plot(feedback)
    plt.plot(setpoint_list, linestyle='--')
    plt.plot(feedback_list, label="Output")
    #plt.plot(p_list, label="P")
    #plt.plot(i_list, label="I")
    #plt.plot(d_list, label="D")
    #plt.plot(err_list, label="Err", linestyle=':')
    plt.legend(loc="upper left")
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    #plt.ylim((-20, 20))

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_pid(0.8, 3, 0.001, L=100)
#    test_pid(0.8, L=50)