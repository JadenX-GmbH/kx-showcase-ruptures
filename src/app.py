import matplotlib.pyplot as plt
import ruptures as rpt
import numpy as np
import pandas as pd
import sys
import os

iexec_out = os.environ['IEXEC_OUT']
signal = pd.read_csv(sys.argv[1])

algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

rpt.display(signal, [], result)
plt.savefig('{}/results_change_point_detect_{}.pdf'.format(iexec_out, sys.argv[1].split('/')[-1]))
