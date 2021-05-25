"""
The interactive_plots module contains the slider_plot function. slider_plot produces a plot of a data set  and an interactive overlay of a fit function whose fit parameters can be adjusted over a range with sliders. Any number of fit parameters can be specified, although the plot window has a limit as to how many sliders it can display nicely. Maybe 20-ish sliders.

When using jupyter notebook, invoke 
%matplotlib qt 
to use the interactive plot window, instead of inline plots.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def slider_plot(fitparams,function,plotparams,xData=None,yData=None,xErr=None,yErr=None):
    """
    Created by: Jim Hetrick
    Date: February 6, 2021
    Cite: This is a modification and extension of slider code from https://matplotlib.org/3.1.1/gallery/widgets/slider_demo.html

    Description:

        slider_plot produces a plot of a data set (xData,yData), and an interactive overlay of a fit function 'function' whose fit parameters can be adjusted over a range with sliders. Any number of fit parameters can be specified, although the plot window has a limit as to how many sliders it can display nicely. Maybe 20-ish sliders.

        When using jupyter notebook, invoke 
        %matplotlib qt 
        to use interactive plot window, instead of inline plots.

    Function Call:

        slider_plot(fitparams,function,plotparams,xData=None,yData=None,xErr=None,yErr=None)

        This is the function call to produce the interactive plot. The first three arguments are required.

    Arguments:

        fitparams = [['name1',min,max,start,delta],['name2',min,max,start,delta],etc.]

            A list of sub-lists. A sub-list must be given for each fit parameter. Each list consists of 5 items, a string name of the parameter, and 4 numbers that specify properties of the sliders that will be created: min-value, max-value, starting-value, and a delta-value which specifies how much the parameter changes with each step of the slider. One for each fit param.


        function = name 

            This is the name of the fitting function that has been defined in your code with a def command.


        plotparms = [['x',xmin,xmax],['y',ymin,ymax],[number of points]]

            A list of three sublists. The first two contain the min a max values of the horizontal and vertical scales for the plot.  It is recommended that the data be plotted beforehand to identify good max and min values. The third sub-list is a single number giving the number of points to use for producing the fit function. Choose number of points so the fit curve is smooth, but not so many as to slow down the interactive updates.

        xData = numpy array of x data to be fit.
        
            Supply None if there is no data; that is, if you are using interactive_plot to display just the fit function, not any data. The default value for xData is None. So things should work if you don't specify anything, and the variable xData is not a global variable being used for some other purpose. 

        yData = numpy array of y data to be fit. 
        
            Supply None if there is no data; that is, if you are using interactive_plot to display just the fit function, not any data. The default value for xData is None. So things should work if you don't specify anything, and the variable yData is not a global variable being used for some other purpose.

        xErr = numpy array of x-uncertainty in data. 
        
            None if none.

        yErr = numpy array of y-uncertainty in data. 
        
            None if none.
    """
    
    
    #Generates initparams, an array that holds the starting values for all fit parameters.
    #The starting values are the 4th item in the fitparams sublists.
    #The slider values will start at these values, which are not necessarily
    #the min value.
    initparams = np.array([])
    for param in fitparams:
        initparams = np.append(initparams,param[3])
        
    n = len(initparams) #counts the number of fit parameters.
    
    #Generate arrays of the x,y values for plotting the fit function. 
    x = np.linspace(plotparams[0][1],plotparams[0][2],plotparams[2][0])
    y = function(x,*initparams)

    #Set up the figure window.  
    fig, ax = plt.subplots(1, 1, figsize=(16, 6))
    #right=0.5 sizes the plot in the left half of the figure,
    #leaving the right half available for the sliders.
    plt.subplots_adjust(left=.05, right=0.5, bottom=.1, top=0.95)
    
    #Creates scatter plot of the data if data is passed. 
    #If xData=yData=None then nothing is plotted.
    ax.errorbar(xData,yData, yerr=yErr, xerr=xErr, linestyle='', marker='o', markersize=4, color='tab:blue',ecolor='red',capsize=2)
    
    #Creates a line plot of th fit function.
    plot, = ax.plot(x,y,'-',color='tab:orange')
    
    #Sets axes limits based on values passed in the plotparams array.
    ax.set_xlim(plotparams[0][1],plotparams[0][2])
    ax.set_ylim(plotparams[1][1],plotparams[1][2])

    ax = [] #initialize ax array
    axcolor = 'lightgoldenrodyellow' #background color of sliders.
    for i,param in enumerate(fitparams):
        #plt.axes positions and sizes the sliders using fractions of figure dimensions.
        #[x-start, y-start, delta-x, delta-y]
        #y-start steps its way down from the top of the figure, placing each
        #successive slider underneath the previous.
        ax.append(plt.axes([.55, .90-(i*.05), 0.35, .03], facecolor=axcolor))
    
    sa = [] #initialize the sa array
    for i,param in enumerate(fitparams):
        #This loops creates a slider for each fit parameter.
        #Size/Position info passed through ax[i]
        #Name, Min, Max, Start, Step values passed from info in the fitparams array.
        sa.append(Slider(ax[i], param[0], param[1], param[2], valinit=param[3],valstep=param[4]))

    def update(val):
        new = [] #initialize array
        for i,param in enumerate(fitparams):
            #Obtains updated values of fit parameters from the sliders.
            #And places values in the new array.
            new.append(sa[i].val)
        plot.set_ydata(function(x,*new)) #replot fit function with new values of params.
        fig.canvas.draw_idle()

    for i,param in enumerate(fitparams):
        #Polls the sliders to detect if anything has changes.
        #Update is called if changes are detected.
        sa[i].on_changed(update)
    
    plt.show()
    
    #returning reference to slider keeps plot from freezing.
    #See https://github.com/matplotlib/matplotlib/issues/3105
    return sa