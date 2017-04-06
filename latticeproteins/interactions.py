#!/usr/bin/python
# Begin interactions.py
"""A module containing interaction energies for lattice proteins.

Written by Jesse Bloom, 2004."""
#------------------------------------------------------------------------------
# 'miyazawa_jernigan' is a dictionary holding the contact energies from
# Miyazawa and Jernigan, "Estimation of effective interresidue contact
# energies from protein crystal structures: Quasi-chemical approximation",
# Macromolecules 18:534-552 (1985).  The values are from Table V of
# the paper, upper half and diagonal.
# The interaction energies between residues X and Y where X and Y are the
# one-letter codes for the residues are keyed by the string XY formed
# from the concatenation of X and Y.  For example, the energy of interaction
# between alanine and glycine is given by 'miyazawa_jernigan["AG"]'.
miyazawa_jernigan = {
'CC':-5.44, 'CM':-5.05, 'CF':-5.63, 'CI':-5.03, 'CL':-5.03, 'CV':-4.46, 'CW':-4.76, 'CY':-3.89, 'CA':-3.38, 'CG':-3.16, 'CT':-2.88, 'CS':-2.86, 'CQ':-2.73, 'CN':-2.59, 'CE':-2.08, 'CD':-2.66, 'CH':-3.63, 'CR':-2.70, 'CK':-1.54, 'CP':-2.92,
'MC':-5.05, 'MM':-6.06, 'MF':-6.68, 'MI':-6.33, 'ML':-6.01, 'MV':-5.52, 'MW':-6.37, 'MY':-4.92, 'MA':-3.99, 'MG':-3.75, 'MT':-3.73, 'MS':-3.55, 'MQ':-3.17, 'MN':-3.50, 'ME':-3.19, 'MD':-2.90, 'MH':-3.31, 'MR':-3.49, 'MK':-3.11, 'MP':-4.11,
'FC':-5.63, 'FM':-6.68, 'FF':-6.85, 'FI':-6.39, 'FL':-6.26, 'FV':-5.75, 'FW':-6.02, 'FY':-4.95, 'FA':-4.36, 'FG':-3.72, 'FT':-3.76, 'FS':-3.56, 'FQ':-3.30, 'FN':-3.55, 'FE':-3.51, 'FD':-3.31, 'FH':-4.61, 'FR':-3.54, 'FK':-2.83, 'FP':-3.73,
'IC':-5.03, 'IM':-6.33, 'IF':-6.39, 'II':-6.22, 'IL':-6.17, 'IV':-5.58, 'IW':-5.64, 'IY':-4.63, 'IA':-4.41, 'IG':-3.65, 'IT':-3.74, 'IS':-3.43, 'IQ':-3.22, 'IN':-2.99, 'IE':-3.23, 'ID':-2.91, 'IH':-3.76, 'IR':-3.33, 'IK':-2.70, 'IP':-3.47,
'LC':-5.03, 'LM':-6.01, 'LF':-6.26, 'LI':-6.17, 'LL':-5.79, 'LV':-5.38, 'LW':-5.50, 'LY':-4.26, 'LA':-3.96, 'LG':-3.43, 'LT':-3.43, 'LS':-3.16, 'LQ':-3.09, 'LN':-2.99, 'LE':-2.91, 'LD':-2.59, 'LH':-3.84, 'LR':-3.15, 'LK':-2.63, 'LP':-3.06,
'VC':-4.46, 'VM':-5.52, 'VF':-5.75, 'VI':-5.58, 'VL':-5.38, 'VV':-4.94, 'VW':-5.05, 'VY':-4.05, 'VA':-3.62, 'VG':-3.06, 'VT':-2.95, 'VS':-2.79, 'VQ':-2.67, 'VN':-2.36, 'VE':-2.56, 'VD':-2.25, 'VH':-3.38, 'VR':-2.78, 'VK':-1.95, 'VP':-2.96,
'WC':-4.76, 'WM':-6.37, 'WF':-6.02, 'WI':-5.64, 'WL':-5.50, 'WV':-5.05, 'WW':-5.42, 'WY':-4.44, 'WA':-3.93, 'WG':-3.37, 'WT':-3.31, 'WS':-2.95, 'WQ':-3.16, 'WN':-3.11, 'WE':-2.94, 'WD':-2.91, 'WH':-4.02, 'WR':-3.56, 'WK':-2.49, 'WP':-3.66,
'YC':-3.89, 'YM':-4.92, 'YF':-4.95, 'YI':-4.63, 'YL':-4.26, 'YV':-4.05, 'YW':-4.44, 'YY':-3.55, 'YA':-2.85, 'YG':-2.50, 'YT':-2.48, 'YS':-2.30, 'YQ':-2.53, 'YN':-2.47, 'YE':-2.42, 'YD':-2.25, 'YH':-3.33, 'YR':-2.75, 'YK':-2.01, 'YP':-2.80,
'AC':-3.38, 'AM':-3.99, 'AF':-4.36, 'AI':-4.41, 'AL':-3.96, 'AV':-3.62, 'AW':-3.93, 'AY':-2.85, 'AA':-2.51, 'AG':-2.15, 'AT':-2.15, 'AS':-1.89, 'AQ':-1.70, 'AN':-1.44, 'AE':-1.51, 'AD':-1.57, 'AH':-2.09, 'AR':-1.50, 'AK':-1.10, 'AP':-1.81,
'GC':-3.16, 'GM':-3.75, 'GF':-3.72, 'GI':-3.65, 'GL':-3.43, 'GV':-3.06, 'GW':-3.37, 'GY':-2.50, 'GA':-2.15, 'GG':-2.17, 'GT':-2.03, 'GS':-1.70, 'GQ':-1.54, 'GN':-1.56, 'GE':-1.22, 'GD':-1.62, 'GH':-1.94, 'GR':-1.68, 'GK':-0.84, 'GP':-1.72,
'TC':-2.88, 'TM':-3.73, 'TF':-3.76, 'TI':-3.74, 'TL':-3.43, 'TV':-2.95, 'TW':-3.31, 'TY':-2.48, 'TA':-2.15, 'TG':-2.03, 'TT':-1.72, 'TS':-1.59, 'TQ':-1.59, 'TN':-1.51, 'TE':-1.45, 'TD':-1.66, 'TH':-2.31, 'TR':-1.97, 'TK':-1.02, 'TP':-1.66,
'SC':-2.86, 'SM':-3.55, 'SF':-3.56, 'SI':-3.43, 'SL':-3.16, 'SV':-2.79, 'SW':-2.95, 'SY':-2.30, 'SA':-1.89, 'SG':-1.70, 'ST':-1.59, 'SS':-1.48, 'SQ':-1.37, 'SN':-1.31, 'SE':-1.48, 'SD':-1.46, 'SH':-1.94, 'SR':-1.22, 'SK':-0.83, 'SP':-1.35,
'QC':-2.73, 'QM':-3.17, 'QF':-3.30, 'QI':-3.22, 'QL':-3.09, 'QV':-2.67, 'QW':-3.16, 'QY':-2.53, 'QA':-1.70, 'QG':-1.54, 'QT':-1.59, 'QS':-1.37, 'QQ':-0.89, 'QN':-1.36, 'QE':-1.33, 'QD':-1.26, 'QH':-1.85, 'QR':-1.85, 'QK':-1.02, 'QP':-1.73,
'NC':-2.59, 'NM':-3.50, 'NF':-3.55, 'NI':-2.99, 'NL':-2.99, 'NV':-2.36, 'NW':-3.11, 'NY':-2.47, 'NA':-1.44, 'NG':-1.56, 'NT':-1.51, 'NS':-1.31, 'NQ':-1.36, 'NN':-1.59, 'NE':-1.43, 'ND':-1.33, 'NH':-2.01, 'NR':-1.41, 'NK':-0.91, 'NP':-1.43,
'EC':-2.08, 'EM':-3.19, 'EF':-3.51, 'EI':-3.23, 'EL':-2.91, 'EV':-2.56, 'EW':-2.94, 'EY':-2.42, 'EA':-1.51, 'EG':-1.22, 'ET':-1.45, 'ES':-1.48, 'EQ':-1.33, 'EN':-1.43, 'EE':-1.18, 'ED':-1.23, 'EH':-2.27, 'ER':-2.07, 'EK':-1.60, 'EP':-1.40,
'DC':-2.66, 'DM':-2.90, 'DF':-3.31, 'DI':-2.91, 'DL':-2.59, 'DV':-2.25, 'DW':-2.91, 'DY':-2.25, 'DA':-1.57, 'DG':-1.62, 'DT':-1.66, 'DS':-1.46, 'DQ':-1.26, 'DN':-1.33, 'DE':-1.23, 'DD':-0.96, 'DH':-2.14, 'DR':-1.98, 'DK':-1.32, 'DP':-1.19,
'HC':-3.63, 'HM':-3.31, 'HF':-4.61, 'HI':-3.76, 'HL':-3.84, 'HV':-3.38, 'HW':-4.02, 'HY':-3.33, 'HA':-2.09, 'HG':-1.94, 'HT':-2.31, 'HS':-1.94, 'HQ':-1.85, 'HN':-2.01, 'HE':-2.27, 'HD':-2.14, 'HH':-2.78, 'HR':-2.12, 'HK':-1.09, 'HP':-2.17,
'RC':-2.70, 'RM':-3.49, 'RF':-3.54, 'RI':-3.33, 'RL':-3.15, 'RV':-2.78, 'RW':-3.56, 'RY':-2.75, 'RA':-1.50, 'RG':-1.68, 'RT':-1.97, 'RS':-1.22, 'RQ':-1.85, 'RN':-1.41, 'RE':-2.07, 'RD':-1.98, 'RH':-2.12, 'RR':-1.39, 'RK':-0.06, 'RP':-1.85,
'KC':-1.54, 'KM':-3.11, 'KF':-2.83, 'KI':-2.70, 'KL':-2.63, 'KV':-1.95, 'KW':-2.49, 'KY':-2.01, 'KA':-1.10, 'KG':-0.84, 'KT':-1.02, 'KS':-0.83, 'KQ':-1.02, 'KN':-0.91, 'KE':-1.60, 'KD':-1.32, 'KH':-1.09, 'KR':-0.06, 'KK':0.13, 'KP':-0.67,
'PC':-2.92, 'PM':-4.11, 'PF':-3.73, 'PI':-3.47, 'PL':-3.06, 'PV':-2.96, 'PW':-3.66, 'PY':-2.80, 'PA':-1.81, 'PG':-1.72, 'PT':-1.66, 'PS':-1.35, 'PQ':-1.73, 'PN':-1.43, 'PE':-1.40, 'PD':-1.19, 'PH':-2.17, 'PR':-1.85, 'PK':-0.67, 'PP':-1.18}
#------------------------------------------------------------------------------
# miyazawa_jernigan_disulfide is like miyazawa_jernigan, except that the
# energy of a CC bond is increased and CX bonds (X != C) are slightly decreased
miyazawa_jernigan_disulfide = {}
for (aas, e) in miyazawa_jernigan.items():
    (r1, r2) = (aas[0], aas[1])
    if r1 == 'C' and r2 == 'C':
        miyazawa_jernigan_disulfide[aas] = e - 50.0
    elif r1 == 'C' or r2 == 'C':
        miyazawa_jernigan_disulfide[aas] = e + 2.5
    else:
        miyazawa_jernigan_disulfide[aas] = e
#------------------------------------------------------------------------------
# End interactions.py
