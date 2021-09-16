import matplotlib.pyplot as plt
import ruptures as rpt
import argparse
import numpy as np
import pandas as pd
import sys
import os

parser = argparse.ArgumentParser(description='RupturesApp')
parser.add_argument('--src', required=True, help='Path for source dataset')
# parser.add_argument('--out', required=True, help='Path for storing output images')

args = parser.parse_args()


iexec_out = os.environ['IEXEC_OUT']
print(args.src)
signal = pd.read_csv(args.src)


algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

rpt.display(signal, [], result)
plt.savefig('{}/results_change_point_detect_{}.pdf'.format(iexec_out, args.src.split('/')[-1]))
