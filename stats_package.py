import math


def std_err_mean(values):
    # input array of values
    # return mean, std deviation, and std error of mean
    dev = []
    mean = sum(values)/len(values)
    for x in range(len(values)):
        a = values[x]
        dev.append((a-mean)**2)
    std_dev = math.sqrt((1/((len(values))-1))*sum(dev))
    std_err_mean = std_dev/(math.sqrt(len(values)))
    return [mean, std_dev, std_err_mean]



def std_dev(values):
    mean = sum(values)/len(values)
    sum_square = 0
    for x in range(len(values)):
        sum_square += (values[x]-mean)**2
    # return standard dev
    return math.sqrt(sum_square/len(values))

def variance(values):
    # input array of values
    # output sum of squares, variance
    mean = sum(values)/len(values)
    sum_squares = 0
    for x in range(len(values)):
        sum_squares += (values[x] - mean) ** 2
    var = sum_squares/(len(values)-1)
    return('mean = ' + str(mean) + ', sum squares = ' + str(sum_squares) + ', variance = ' + str(var))

def med(values):
    # add quartiles later
    val_in_ord = sorted(values)
    min = val_in_ord[0]
    max = val_in_ord[-1]
    rng = max - min
    med_pos = (len(values)/2) - 0.5
    quarters = len(values) / 4
    if med_pos.is_integer() == False:
        med_pos_up = int(med_pos + .5)
        med_pos_low = int(med_pos - .5)
        median = (val_in_ord[med_pos_up] + val_in_ord[med_pos_low]) / 2
    else:
        median = val_in_ord[int(med_pos)]
    return median

def precision(values,expected_value):
    dist_for_value = []
    for x in range(len(values)):
        dist_for_value.append(math.sqrt((values[x]-expected_value)**2))
    return (sum(dist_for_value))/len(values)

def z_score(values,mean,std_dev,n):
    # input a list of values, may need more to be solved at once
    # input mean and standard deviation
    z_scr_list = []
    for x in range(len(values)):
        z_scr_list.append((values[x]-mean)/(std_dev/math.sqrt(n)))
    return z_scr_list

def t_test(vals_1,vals_2):
    diff_list = []
    for x in range(len(vals_1)):
        diff_list.append(vals_1[x]-vals_2[x])
    mean_stuff = std_err_mean(diff_list)
    t_score = mean_stuff[0]/(mean_stuff[1]/math.sqrt(len(diff_list)))
    return t_score

def confidence_interval(PE,std_dev,n,pair_unpair,confidence):
    if pair_unpair.upper() == 'PAIR':
        MOE = confidence * (std_dev/math.sqrt(n))
    elif pair_unpair.upper() == 'UNPAIR':
        sum_stuff = 0
        for x in range(len(std_dev)):
            sum_stuff += (std_dev**2)/n
        MOE = math.sqrt(sum_stuff)

def miller_units(A420,A600,t,v):
    # imput time in minutes and volume in mL
    miller_unit = (A420*1000)/(A600*t*v)
    return miller_unit
    
def sample_size(crit_val,std_dev,MOE):
    samp_size = ((crit_val*std_dev)/MOE)**2
    return samp_size




