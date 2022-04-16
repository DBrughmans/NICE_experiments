datasets_pmlb = [
 'GAMETES_Epistasis_2_Way_20atts_0.1H_EDM_1_1',
 'GAMETES_Epistasis_2_Way_20atts_0.4H_EDM_1_1',
 'GAMETES_Heterogeneity_20atts_1600_Het_0.4_0.2_50_EDM_2_001',
 'GAMETES_Heterogeneity_20atts_1600_Het_0.4_0.2_75_EDM_2_001',
 'Hill_Valley_without_noise',
 'adult',
 'agaricus_lepiota',
 'australian',
 'breast_w',
 'buggyCrx',
 'chess',
 'churn',
 'clean2',
 'coil2000',
 'credit_a',
 'credit_g',
 'crx',
 'diabetes',
 'dis',
 'german',
 'hypothyroid',
 'kr_vs_kp',
 'magic',
 'mofn_3_7_10',
 'monk1',
 'monk2',
 'monk3',
 'mushroom',
 'parity5+5',
 'phoneme',
 'pima',
 'profb',
 'ring',
 'spambase',
 'threeOf9',
 'tic_tac_toe',
 'tokyo1',
 'twonorm',
 'wdbc',
 'xd6'
]


PARAMETERS_GRID ={
    'RF':{'n_estimators': [50,100, 250, 500, 1000],
          'max_depth': [1,2,5,10, 25, None]
          },
    'ANN':{'hidden_layer_sizes':[]}
}

AE_GRID = {'learning_rate_init': [0.05,0.01,0.005,0.001,0.0005,0.0001,0.00005,0.00001]}

cvnt001 = {
    2: 2.576,
    3: 2.913,
    4: 3.113,
    5: 3.255,
    6: 3.364,
    7: 3.452,
    8: 3.526,
    9: 3.590,
    10: 3.646,
    11: 3.696,
    12: 3.741,
    13: 3.781,
    14: 3.818,
    15: 3.853,
    16: 3.884,
    17: 3.914,
    18: 3.941,
    19: 3.967,
    20: 3.992,
    21: 4.015,
    22: 4.037,
    23: 4.057,
    24: 4.077,
    25: 4.096,
    26: 4.114,
    27: 4.132,
    28: 4.148,
    29: 4.164,
    30: 4.179,
    31: 4.194,
    32: 4.208,
    33: 4.222,
    34: 4.236,
    35: 4.249,
    36: 4.261,
    37: 4.273,
    38: 4.285,
    39: 4.296,
    40: 4.307,
    41: 4.318,
    42: 4.329,
    43: 4.339,
    44: 4.349,
    45: 4.359,
    46: 4.368,
    47: 4.378,
    48: 4.387,
    49: 4.395,
    50: 4.404,
}
cvnt005 = {
    2: 1.960,
    3: 2.344,
    4: 2.569,
    5: 2.728,
    6: 2.850,
    7: 2.948,
    8: 3.031,
    9: 3.102,
    10: 3.164,
    11: 3.219,
    12: 3.268,
    13: 3.313,
    14: 3.354,
    15: 3.391,
    16: 3.426,
    17: 3.458,
    18: 3.489,
    19: 3.517,
    20: 3.544,
    21: 3.569,
    22: 3.593,
    23: 3.616,
    24: 3.637,
    25: 3.658,
    26: 3.678,
    27: 3.696,
    28: 3.714,
    29: 3.732,
    30: 3.749,
    31: 3.765,
    32: 3.780,
    33: 3.795,
    34: 3.810,
    35: 3.824,
    36: 3.837,
    37: 3.850,
    38: 3.863,
    39: 3.876,
    40: 3.888,
    41: 3.899,
    42: 3.911,
    43: 3.922,
    44: 3.933,
    45: 3.943,
    46: 3.954,
    47: 3.964,
    48: 3.973,
    49: 3.983,
    50: 3.992,
}
cvnt010 = {
    2: 1.645,
    3: 2.052,
    4: 2.291,
    5: 2.460,
    6: 2.589,
    7: 2.693,
    8: 2.780,
    9: 2.855,
    10: 2.920,
    11: 2.978,
    12: 3.030,
    13: 3.077,
    14: 3.120,
    15: 3.159,
    16: 3.196,
    17: 3.230,
    18: 3.261,
    19: 3.291,
    20: 3.319,
    21: 3.346,
    22: 3.371,
    23: 3.394,
    24: 3.417,
    25: 3.439,
    26: 3.459,
    27: 3.479,
    28: 3.498,
    29: 3.516,
    30: 3.533,
    31: 3.550,
    32: 3.567,
    33: 3.582,
    34: 3.597,
    35: 3.612,
    36: 3.626,
    37: 3.640,
    38: 3.653,
    39: 3.666,
    40: 3.679,
    41: 3.691,
    42: 3.703,
    43: 3.714,
    44: 3.726,
    45: 3.737,
    46: 3.747,
    47: 3.758,
    48: 3.768,
    49: 3.778,
    50: 3.788,
}