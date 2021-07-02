import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

read = pd.read_csv('data.csv')

def readscore():
    data = read['reading score'].tolist()
    #print(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)

    print('The mean , median and mode of reading score is {} , {} and {} respectively'.format(mean,median,mode))
    print('The standard deviation for reading score is',stdev)

    f_stdev_start , f_stdev_end = mean-stdev , mean+stdev
    s_stdev_start , s_stdev_end = mean- (2*stdev) , mean+ (2*stdev)
    t_stdev_start , t_stdev_end = mean- (3*stdev) , mean+ (3*stdev)

    within_f_std = [result for result in data if result >f_stdev_start and result<f_stdev_end]
    within_s_std = [result for result in data if result >s_stdev_start and result<s_stdev_end]
    within_t_std = [result for result in data if result >t_stdev_start and result<t_stdev_end]

    print('{}% lies between first standard deviation'.format(len(within_f_std)*100/len(data)),'for reading score')
    print('{}% lies between second standard deviation'.format(len(within_s_std)*100/len(data)),'for reading score')
    print('{}% lies between Third standard deviation'.format(len(within_t_std)*100/len(data)),'for reading score')

    fig = ff.create_distplot([data],['Reading Score'],show_hist=False)
    fig.add_trace(go.Scatter(x= [f_stdev_start,f_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 1 start', mode = 'lines'))
    
    fig.add_trace(go.Scatter(x= [s_stdev_start,s_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 2 start', mode = 'lines'))

    fig.add_trace(go.Scatter(x= [t_stdev_start,t_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 3 start ', mode = 'lines'))
   
    fig.show()

def write():
    data = read['writing score'].tolist()
    #print(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)

    print('The mean , median and mode of writing score is {} , {} and {} respectively'.format(mean,median,mode))
    print('The standard deviation for writing score is',stdev)

    f_stdev_start , f_stdev_end = mean-stdev , mean+stdev
    s_stdev_start , s_stdev_end = mean- (2*stdev) , mean+ (2*stdev)
    t_stdev_start , t_stdev_end = mean- (3*stdev) , mean+ (3*stdev)

    within_f_std = [result for result in data if result >f_stdev_start and result<f_stdev_end]
    within_s_std = [result for result in data if result >s_stdev_start and result<s_stdev_end]
    within_t_std = [result for result in data if result >t_stdev_start and result<t_stdev_end]

    print('{}% lies between first standard deviation'.format(len(within_f_std)*100/len(data)),'for writing score')
    print('{}% lies between second standard deviation'.format(len(within_s_std)*100/len(data)),'for writing score')
    print('{}% lies between Third standard deviation'.format(len(within_t_std)*100/len(data)),'for writing score')

    fig = ff.create_distplot([data],['Writing Score'],show_hist=False)
    fig.add_trace(go.Scatter(x= [f_stdev_start,f_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 1 start', mode = 'lines'))
    
    fig.add_trace(go.Scatter(x= [s_stdev_start,s_stdev_start], y = [0,0.17] , name = 'Standard Deviation 2 start', mode = 'lines'))

    fig.add_trace(go.Scatter(x= [t_stdev_start,t_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 3 start ', mode = 'lines'))
    
   
    fig.show()

def math():
    data = read['math score'].tolist()
    #print(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    stdev = statistics.stdev(data)

    print('The mean , median and mode of math score is {} , {} and {} respectively'.format(mean,median,mode))
    print('The standard deviation for math score is',stdev)

    f_stdev_start , f_stdev_end = mean-stdev , mean+stdev
    s_stdev_start , s_stdev_end = mean- (2*stdev) , mean+ (2*stdev)
    t_stdev_start , t_stdev_end = mean- (3*stdev) , mean+ (3*stdev)

    within_f_std = [result for result in data if result >f_stdev_start and result<f_stdev_end]
    within_s_std = [result for result in data if result >s_stdev_start and result<s_stdev_end]
    within_t_std = [result for result in data if result >t_stdev_start and result<t_stdev_end]

    print('{}% lies between first standard deviation'.format(len(within_f_std)*100/len(data)),'for math score')
    print('{}% lies between second standard deviation'.format(len(within_s_std)*100/len(data)),'for math score')
    print('{}% lies between Third standard deviation'.format(len(within_t_std)*100/len(data)),'for math score')

    fig = ff.create_distplot([data],['Math Score'],show_hist=False)
    fig.add_trace(go.Scatter(x= [f_stdev_start,f_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 1 start', mode = 'lines'))
    
    fig.add_trace(go.Scatter(x= [s_stdev_start,s_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 2 start', mode = 'lines'))

    fig.add_trace(go.Scatter(x= [t_stdev_start,t_stdev_start] , y = [0,0.17] , name = 'Standard Deviation 3 start ', mode = 'lines'))
   
    fig.show()
readscore()    

write()
math()