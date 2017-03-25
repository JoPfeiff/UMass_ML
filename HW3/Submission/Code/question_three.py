import numpy as np
import matplotlib.pyplot as plt


def plot_line_graph():
    arrays = np.array([[401.6489758491516, 210.33531498908997, 144.43129706382751, 112.32910704612732, 133.5269730091095, 129.54033708572388, 138.04477715492249, 141.1620671749115]])
    labels = ['time']
    title_img =  'Comparing Cores with Time'
    #label = label_dict[title_img]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ticks = range(1,9)
    for i in range(len(arrays)):
        array = arrays[i]
        index = range(len(array))
        values = array
        ax.plot(ticks, values)#, colors[i])
        #ax.set_xlabel(tuning_parameter)
        ax.set_ylabel('Seconds')
        ax.set_xlabel('Cores')
    plt.title(title_img)
    #plt.legend(labels, loc = 'lower right')

    plt.savefig(title_img+".pdf")

plot_line_graph()