import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import json

# define DSS path
dataset = "IEEETestCases"

# define path
DIR = os.getcwd()

# ness files
ness_files = [
"ness_5.json",
"ness_6.json",
"ness_7.json",
"ness_8.json",
"ness_9.json",
"ness_10.json",
]

########
# 123
########
NetworkModel = "123Bus"           # "SecondaryTestCircuit_modified", "13Bus", "123Bus"

# initialize
err_123_l2 = []
err_123_l1 = []
err_123_linf = []
err_123_fro = []

for ness_123_file in ness_files:
    # read ness file
    ness_path = os.path.join(NetworkModel, ness_123_file)
    f = open(ness_path)
    ness = json.load(f)

    # preallocate
    p_nm = []
    ptdf_p_nm = []
    for br in ness["branch"]:
        cols = [br["uid"].split(".")[1] + "." + str(ph) for ph in br["phases"]]
        p_nm.append(pd.DataFrame.from_dict(br["p_nm"]))
        p_nm[-1].columns = cols
        ptdf_p_nm.append(pd.DataFrame.from_dict(br["ptdf_p_nm"]))
        ptdf_p_nm[-1].columns = cols

    # concatenate
    p_nm = pd.concat(p_nm, axis=1)
    ptdf_p_nm = pd.concat(ptdf_p_nm, axis=1)

    # calculate error
    err_123_l2.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=2))
    err_123_l1.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=1))
    err_123_linf.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=np.inf))
    err_123_fro.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord='fro'))


########
# 13
########
NetworkModel = "13Bus"           # "SecondaryTestCircuit_modified", "13Bus", "123Bus"

# initialize
err_13_l2 = []
err_13_l1 = []
err_13_linf = []
err_13_fro = []

for ness_13_file in ness_files:
    # read ness file
    ness_path = os.path.join(NetworkModel, ness_13_file)
    f = open(ness_path)
    ness = json.load(f)

    # preallocate
    p_nm = []
    ptdf_p_nm = []
    for br in ness["branch"]:
        cols = [br["uid"].split(".")[1] + "." + str(ph) for ph in br["phases"]]
        p_nm.append(pd.DataFrame.from_dict(br["p_nm"]))
        p_nm[-1].columns = cols
        ptdf_p_nm.append(pd.DataFrame.from_dict(br["ptdf_p_nm"]))
        ptdf_p_nm[-1].columns = cols

    # concatenate
    p_nm = pd.concat(p_nm, axis=1)
    ptdf_p_nm = pd.concat(ptdf_p_nm, axis=1)

    # calculate error
    err_13_l2.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=2))
    err_13_l1.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=1))
    err_13_linf.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=np.inf))
    err_13_fro.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord='fro'))
        

        
########
# 3
########
NetworkModel = "case3"           # "SecondaryTestCircuit_modified", "3Bus", "123Bus"

# initialize
err_3_l2 = []
err_3_l1 = []
err_3_linf = []
err_3_fro = []

for ness_3_file in ness_files:
    # read ness file
    ness_path = os.path.join(NetworkModel, ness_3_file)
    f = open(ness_path)
    ness = json.load(f)

    # preallocate
    p_nm = []
    ptdf_p_nm = []
    for br in ness["branch"]:
        cols = [br["uid"].split(".")[1] + "." + str(ph) for ph in br["phases"]]
        p_nm.append(pd.DataFrame.from_dict(br["p_nm"]))
        p_nm[-1].columns = cols
        ptdf_p_nm.append(pd.DataFrame.from_dict(br["ptdf_p_nm"]))
        ptdf_p_nm[-1].columns = cols

    # concatenate
    p_nm = pd.concat(p_nm, axis=1)
    ptdf_p_nm = pd.concat(ptdf_p_nm, axis=1)

    # calculate error
    err_3_l2.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=2))
    err_3_l1.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=1))
    err_3_linf.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord=np.inf))
    err_3_fro.append(np.linalg.norm(p_nm.values - ptdf_p_nm.values, ord='fro'))
        

# iteration
x = [val / 10.0 for val in range(5, 11, 1)] 

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, np.array(err_123_l2), 'tab:blue', marker='d')
axs[0, 0].plot(x, np.array(err_13_l2), 'tab:orange', marker='*')
axs[0, 0].plot(x, np.array(err_3_l2), 'tab:green', marker='o')
axs[0, 0].set_title('L2 norm')
axs[0, 1].plot(x, np.array(err_123_l1), 'tab:blue', marker='d')
axs[0, 1].plot(x, np.array(err_13_l1), 'tab:orange', marker='*')
axs[0, 1].plot(x, np.array(err_3_l1), 'tab:green', marker='o')
axs[0, 1].set_title('L1 norm')
axs[1, 0].plot(x, np.array(err_123_linf), 'tab:blue', marker='d')
axs[1, 0].plot(x, np.array(err_13_linf), 'tab:orange', marker='*')
axs[1, 0].plot(x, np.array(err_3_linf), 'tab:green', marker='o')
axs[1, 0].set_title('Linf norm')
axs[1, 1].plot(x, np.array(err_123_fro), 'tab:blue', marker='d')
axs[1, 1].plot(x, np.array(err_13_fro), 'tab:orange', marker='*')
axs[1, 1].plot(x, np.array(err_3_fro), 'tab:green', marker='o')
axs[1, 1].set_title('Frobenius norm')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.yaxis.grid(color='gray', linestyle='dashed')

plt.setp(axs[0,0].get_xticklabels(), visible=False)
plt.setp(axs[0,1].get_xticklabels(), visible=False)
axs[1,0].set(xlabel='ANSI') 
axs[1,1].set(xlabel='ANSI') 
axs[0,0].set(ylabel='Total Error[kW]') 
axs[1,0].set(ylabel='Total Error[kW]') 
fig.tight_layout()
plt.show()