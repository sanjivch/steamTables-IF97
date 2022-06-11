# -*coding: utf-8 -*-
"""
Created on Mon Apr  9 20:42:57 2018
Steam Tables based on IAPWS-IF97


@author: Sanjiv Chemudupati
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import streamlit as st


#==============================================================================
# Reference constants
#==============================================================================

R = 0.461526    #kJ/kg K
Tc = 647.096    #K
pc = 22.064     #MPa
rhoc = 322.0    #kg/m3

#==============================================================================
# REGION I
# 273.15 K <= T <= 623.15 K
# p_s (T) <= p <= 100 MPa 
# BASIC EQUATION
#==============================================================================

def prop(p,T):
    
    I1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32])
    J1 = np.array([-2, -1, 0, 1, 2, 3, 4, 5, -9, -7, -1, 0, 1, 3, -3, 0, 1, 3, 17, -4, 0, 6, -5, -2, 10, -8, -11, -6, -29, -31, -38, -39, -40, -41])
    n1 = np.array([0.14632971213167, -0.84548187169114, -3.756360367204, 3.3855169168385, -0.95791963387872, 0.15772038513228, -0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, -6.0706301565874E-04, -0.018990068218419, -0.032529748770505, -0.021841717175414, -5.283835796993E-05, -4.7184321073267E-04, -3.0001780793026E-04, 4.7661393906987E-05, -4.4141845330846E-06, -7.2694996297594E-16, -3.1679644845054E-05, -2.8270797985312E-06, -8.5205128120103E-10, -2.2425281908E-06, -6.5171222895601E-07, -1.4341729937924E-13, -4.0516996860117E-07, -1.2734301741641E-09, -1.7424871230634E-10, -6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, -1.1947622640071E-23, 1.8228094581404E-24, -9.3537087292458E-26])
    
    pi = p / 16.53
    tau = 1386. / T
    
    gamma = np.sum(n1*(7.1-pi)**I1 *(tau-1.222)**J1)
    
    gamma_pi = np.sum(-n1*I1*(7.1-pi)**(I1-1) *(tau-1.222)**J1)
    
    gamma_pipi = np.sum(-n1*I1*(I1-1)*(7.1-pi)**(I1-2) *(tau-1.222)**J1)
    
    gamma_tau = np.sum(n1*(7.1-pi)**I1 *J1*(tau-1.222)**(J1-1))
    
    gamma_tautau = np.sum(n1*(7.1-pi)**I1 *J1*(J1-1)*(tau-1.222)**(J1-2))
    
    gamma_pitau = np.sum(-n1*I1*(7.1-pi)**(I1-1) *J1*(tau-1.222)**(J1-1))
    
    
    
    #Specific Volume (m3/kg)
    v_pT = gamma_pi*pi*R*T*0.001/p
    
    #Specific Enthalpy (kJ/kg)
    h_pT = tau*gamma_tau*R*T
    
    #Specific Entropy
    s_pT = R*(tau*gamma_tau - gamma)    
    
    #Specific Heat capactiy at constant pressure, Cp 
    Cp_pT = -tau**2 *gamma_tautau*R
    
    #Specific Heat capacity at constant volume, Cv
    Cv_pT = Cp_pT-R
    
    #Specific Internal Energy
    u_pT = (tau*gamma_tau - pi*gamma_pi)*R*T
    
    #Speed of sound Precision is causing an issue here divide by zero error
    #w_pT = math.sqrt(1000.0*R*T*gamma_pi**2/((((gamma_pi tau*gamma_pitau)**2)/(tau**2 *gamma_tautau)) gamma_pipi))
    #w_pT = (1000 * R * T * gamma_pi ** 2 / ((gamma_pi tau * gamma_pitau) ** 2 / (tau ** 2 * gamma_tautau) gamma_pipi)) ** 0.5
    
    
    #print(gamma, gamma_pi, gamma_tau
    return v_pT, h_pT, s_pT, Cp_pT, Cv_pT, u_pT#, w_pT
    



#==============================================================================
# REGION I
# 273.15 K <= T <= 623.15 K
# p_s (T) <= p <= 100 MPa 
# BACKWARD EQUATION Temperature as function of pressure, enthalpy
#==============================================================================

def T(p,h):
    
    I1 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6])
    J1 = np.array([0, 1, 2, 6, 22, 32, 0, 1, 2, 3, 4, 10, 32, 10, 32, 10, 32, 32, 32, 32])
    n1 = np.array([-238.72489924521, 404.21188637945, 113.49746881718, -5.8457616048039, -1.528548241314E-04, -1.0866707695377E-06, -13.391744872602, 43.211039183559, -54.010067170506, 30.535892203916, -6.5964749423638, 9.3965400878363E-03, 1.157364750534E-07, -2.5858641282073E-05, -4.0644363084799E-09, 6.6456186191635E-08, 8.0670734103027E-11, -9.3477771213947E-13, 5.8265442020601E-15, -1.5020185953503E-17])
    
    eta = h / 2500.0
    pi = p/1.0
    
    
    
    theta = np.sum(n1*pi**I1 * (eta+1)**J1)
    print(theta)
    
#T(3.0,500.0)
#T(80.0, 500.0)
#T(80.0, 1500.0)

#==============================================================================
# REGION I
# 273.15 K <= T <= 623.15 K
# p_s (T) <= p <= 100 MPa 
# BACKWARD EQUATION Temperature as function of pressure, entropy
#==============================================================================
def T1(p,s):
    

    I1 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4])
    J1 = np.array([0, 1, 2, 3, 11, 31, 0, 1, 2, 3, 12, 31, 0, 1, 2, 9, 31, 10, 32, 32])
    n1 = np.array([174.78268058307, 34.806930892873, 6.5292584978455, 0.33039981775489, -1.9281382923196E-07, -2.4909197244573E-23, -0.26107636489332, 0.22592965981586, -0.064256463395226, 7.8876289270526E-03, 3.5672110607366E-10, 1.7332496994895E-24, 5.6608900654837E-04, -3.2635483139717E-04, 4.4778286690632E-05, -5.1322156908507E-10, -4.2522657042207E-26, 2.6400441360689E-13, 7.8124600459723E-29, -3.0732199903668E-31])
        
    pi = p/1.0
    sigma = s/1.0    
    
    theta = np.sum(n1*pi**I1 * (sigma+2)**J1)
    print(theta)
    
#T1(3.0,0.5)
#T1(80.0,0.5)
#T1(80.0,3.0)


#==============================================================================
# REGION I
# 273.15 K <= T <= 623.15 K
# p_s (T) <= p <= 100 MPa 
# BACKWARD EQUATION Pressure as function of enthalpy, entropy
#==============================================================================

def p_hs(h,s):
    
    I1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5])
    J1 = np.array([0, 1, 2, 4, 5, 6, 8, 14, 0, 1, 4, 6, 0, 1, 10, 4, 1, 4, 0])
    n1 = np.array([-0.691997014660582, -18.361254878756, -9.28332409297335, 65.9639569909906, -16.2060388912024, 450.620017338667, 854.68067822417, 6075.23214001162, 32.6487682621856, -26.9408844582931, -319.9478483343, -928.35430704332, 30.3634537455249, -65.0540422444146, -4309.9131651613, -747.512324096068, 730.000345529245, 1142.84032569021, -436.407041874559])
    
    eta = h / 3400.0
    sigma = s / 7.6
    
    pi = np.sum(n1*(eta+0.05)**I1 *(sigma+0.05)**J1) * 100.0
    print(pi)
    
#p_hs(0.001,0.0)
#p_hs(90.0,0.0)
#p_hs(1500.0,3.4)


#==============================================================================
# REGION II
# 273.15 K <= T <= 623.15 K
# p_s (T) <= p <= 100 MPa 
# 
#=============================================================================


def prop2(p,T):

    J0 = np.array([0, 1, -5, -4, -3, -2, -1, 2, 3])
    n0 = np.array([-9.6927686500217, 10.086655968018, -0.005608791128302, 0.071452738081455, -0.40710498223928, 1.4240819171444, -4.383951131945, -0.28408632460772, 0.021268463753307])
    Ir = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24])
    Jr = np.array([0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58])
    nr = np.array([-1.7731742473213E-03, -0.017834862292358, -0.045996013696365, -0.057581259083432, -0.05032527872793, -3.3032641670203E-05, -1.8948987516315E-04, -3.9392777243355E-03, -0.043797295650573, -2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, -3.227767723857E-05, -1.5033924542148E-03, -0.040668253562649, -7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, -1.6714766451061E-11, -2.1171472321355E-03, -23.895741934104, -5.905956432427E-18, -1.2621808899101E-06, -0.038946842435739, 1.1256211360459E-11, -8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, -1.0234747095929E-13, -1.0018179379511E-09, -8.0882908646985E-11, 0.10693031879409, -0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, -4.2002467698208E-06, -5.9056029685639E-26, 3.7826947613457E-06, -1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, -9.436970724121E-07])

    tau = 540.0 / T
    pi = p/ 1.0
    
    gamma0 = math.log(pi) + np.sum(n0*tau**J0) 
    gammar = np.sum(nr*pi**Ir * (tau-0.5)**Jr)
    gamma = gamma0+gammar
    
    gamma0_pi = 1.0/pi
    gammar_pi = np.sum(nr*Ir*pi**(Ir-1) * (tau-0.5)**Jr)
    gamma_pi = gamma0_pi + gammar_pi
    
    gamma0_pipi =  -1.0/pi**2
    gammar_pipi = np.sum(nr*Ir*(Ir-1)*pi**(Ir-2) * (tau-0.5)**Jr)
    gamma_pipi = gamma0_pipi + gammar_pipi
    
    
    gamma0_tau = np.sum(n0*J0*tau**(J0-1))
    gammar_tau = np.sum(nr*pi**Ir * Jr*(tau-0.5)**(Jr-1))
    gamma_tau = gamma0_tau + gammar_tau
    
    gamma0_tautau = np.sum(n0*J0*(J0-1)*tau**(J0-2))
    gammar_tautau = np.sum(nr*pi**Ir * Jr*(Jr-1)*(tau-0.5)**(Jr-2))
    gamma_tautau = gamma0_tautau + gammar_tautau
    
    #Specific Volume m3/kg
    v_pT = R*T*pi*gamma_pi*0.001/p 
    print(v_pT)
    
    #Specific enthalpy
    h_pT = R*T*tau*gamma_tau
    print(h_pT)
    
    #Specific entropy
    s_pT =R*(tau*gamma_tau-gamma)
    print(s_pT)
    
    #Specific internal energy
    u_pT = R*T*(tau*gamma_tau -pi*gamma_pi)
    print(u_pT)
    
    #Specific Heat at constant pressure
    Cp_pT = -R*tau*tau*gamma_tautau
    print(Cp_pT)
    
    #TODO Speed of sound
    
    
prop2(0.0035,300.0)
prop2(0.0035,700.0)
prop2(30.0,700.0)


#==============================================================================
# REGION II Metastable vapor region 
# Replace the below gamma functions in the metastable vapor region
#==============================================================================

def prop2_metavap(p,T):
    I1 = np.array([1,1,1,1,2,2,2,3,3,4,4,5,5])
    J1 = np.array([0,2,5,11,1,7,16,4,16,7,10,9,10])
    n1 = np.array([-0.73362260186506E-02,-0.88223831943146E-01, -0.72334555213245E-01, -0.40813178534455E-02, 0.20097803380207E-02,-0.53045921898642E-01,-0.76190409086970E-02,-0.63498037657313E-02,-0.86043093028588E-01,0.75321581522770E-02,-0.79238375446139E-02,-0.22888160778447E-01,-0.264565014828E-02])
    
    
    pi = p/1.0
    tau = 540.0/T
    
    gamma = np.sum(n1*pi**I1 * (tau-0.5)**J1)
    gamma_pi = np.sum(n1*I1*pi**(I1-1) * (tau-0.5)**J1)
    gamma_pipi = np.sum(n1*I1*(I1-10)*pi**(I1-2) * (tau-0.5)**J1)
    gamma_tau = np.sum(n1*pi**I1 * J1*(tau-0.5)**(J1-1))
    gamma_tautau = np.sum(n1*pi**I1 * J1*(J1-1)*(tau-0.5)**(J1-2))
    gamma_pitau = np.sum(n1*I1*pi**(I1-1) * J1*(tau-0.5)**(J1-1))
    
#==============================================================================
# Region II - Subregions
#    
# Backward equations - T(p,h) and T(p,s)   
#==============================================================================
    
def T2_ph(p,h):   
    
    eta = h/2000.0
    pi = p/1.0    
    
    #Case 1
    #'''Subregion A
    #'Table 20, Eq 22, page 22'''
    Ja = np.array([0, 1, 2, 3, 7, 20, 0, 1, 2, 3, 7, 9, 11, 18, 44, 0, 2, 7, 36, 38, 40, 42, 44, 24, 44, 12, 32, 44, 32, 36, 42, 34, 44, 28])
    Ia = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7])
    na = np.array([1089.8952318288, 849.51654495535, -107.81748091826, 33.153654801263, -7.4232016790248, 11.765048724356, 1.844574935579, -4.1792700549624, 6.2478196935812, -17.344563108114, -200.58176862096, 271.96065473796, -455.11318285818, 3091.9688604755, 252266.40357872, -6.1707422868339E-03, -0.31078046629583, 11.670873077107, 128127984.04046, -985549096.23276, 2822454697.3002, -3594897141.0703, 1722734991.3197, -13551.334240775, 12848734.66465, 1.3865724283226, 235988.32556514, -13105236.545054, 7399.9835474766, -551966.9703006, 3715408.5996233, 19127.72923966, -415351.64835634, -62.459855192507])
    
    #Case 2
    #'Subregion B
    #'Table 21, Eq 23, page 23
    Jb = np.array([0, 1, 2, 12, 18, 24, 28, 40, 0, 2, 6, 12, 18, 24, 28, 40, 2, 8, 18, 40, 1, 2, 12, 24, 2, 12, 18, 24, 28, 40, 18, 24, 40, 28, 2, 28, 1, 40])
    Ib = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 9, 9])
    nb = np.array([1489.5041079516, 743.07798314034, -97.708318797837, 2.4742464705674, -0.63281320016026, 1.1385952129658, -0.47811863648625, 8.5208123431544E-03, 0.93747147377932, 3.3593118604916, 3.3809355601454, 0.16844539671904, 0.73875745236695, -0.47128737436186, 0.15020273139707, -0.002176411421975, -0.021810755324761, -0.10829784403677, -0.046333324635812, 7.1280351959551E-05, 1.1032831789999E-04, 1.8955248387902E-04, 3.0891541160537E-03, 1.3555504554949E-03, 2.8640237477456E-07, -1.0779857357512E-05, -7.6462712454814E-05, 1.4052392818316E-05, -3.1083814331434E-05, -1.0302738212103E-06, 2.821728163504E-07, 1.2704902271945E-06, 7.3803353468292E-08, -1.1030139238909E-08, -8.1456365207833E-14, -2.5180545682962E-11, -1.7565233969407E-18, 8.6934156344163E-15])
 
    #Case Else
    #'Subregion C
    #'Table 22, Eq 24, page 24
    Jc = np.array([0, 4, 0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 4, 8, 4, 0, 1, 4, 10, 12, 16, 20, 22])
    Ic = np.array([-7, -7, -6, -6, -5, -5, -2, -2, -1, -1, 0, 0, 1, 1, 2, 6, 6, 6, 6, 6, 6, 6, 6])
    nc = np.array([-3236839855524.2, 7326335090218.1, 358250899454.47, -583401318515.9, -10783068217.47, 20825544563.171, 610747.83564516, 859777.2253558, -25745.72360417, 31081.088422714, 1208.2315865936, 482.19755109255, 3.7966001272486, -10.842984880077, -0.04536417267666, 1.4559115658698E-13, 1.126159740723E-12, -1.7804982240686E-11, 1.2324579690832E-07, -1.1606921130984E-06, 2.7846367088554E-05, -5.9270038474176E-04, 1.2918582991878E-03])
    
    
    if p < 4:
         Ta_ph = np.sum(na*pi**Ia * (eta-2.1)**Ja)
         print(Ta_ph)
    elif p < (905.84278514723 - 0.67955786399241 * h + 1.2809002730136E-04 * h*h):
        Tb_ph = np.sum(nb*(pi-2)**Ib * (eta-2.6)**Jb)
        print(Tb_ph)
    else:
        Tc_ph = np.sum(nc*(pi+25)**Ic * (eta-1.8)**Jc)
        print(Tc_ph)
        
        
T2_ph(40.0,2700.0)
T2_ph(60.0,2700.0)
T2_ph(60.0,3200.0)

def T2_ps(p,s):
       
       
    #Case 1
    #'Subregion A
    #'Table 25, Eq 25, page 26
    Ia = np.array([-1.5, -1.5, -1.5, -1.5, -1.5, -1.5, -1.25, -1.25, -1.25, -1, -1, -1, -1, -1, -1, -0.75, -0.75, -0.5, -0.5, -0.5, -0.5, -0.25, -0.25, -0.25, -0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 1, 1.25, 1.25, 1.5, 1.5])
    Ja = np.array([-24, -23, -19, -13, -11, -10, -19, -15, -6, -26, -21, -17, -16, -9, -8, -15, -14, -26, -13, -9, -7, -27, -25, -11, -6, 1, 4, 8, 11, 0, 1, 5, 6, 10, 14, 16, 0, 4, 9, 17, 7, 18, 3, 15, 5, 18])
    na = np.array([-392359.83861984, 515265.7382727, 40482.443161048, -321.93790923902, 96.961424218694, -22.867846371773, -449429.14124357, -5011.8336020166, 0.35684463560015, 44235.33584819, -13673.388811708, 421632.60207864, 22516.925837475, 474.42144865646, -149.31130797647, -197811.26320452, -23554.39947076, -19070.616302076, 55375.669883164, 3829.3691437363, -603.91860580567, 1936.3102620331, 4266.064369861, -5978.0638872718, -704.01463926862, 338.36784107553, 20.862786635187, 0.033834172656196, -4.3124428414893E-05, 166.53791356412, -139.86292055898, -0.78849547999872, 0.072132411753872, -5.9754839398283E-03, -1.2141358953904E-05, 2.3227096733871E-07, -10.538463566194, 2.0718925496502, -0.072193155260427, 2.074988708112E-07, -0.018340657911379, 2.9036272348696E-07, 0.21037527893619, 2.5681239729999E-04, -0.012799002933781, -8.2198102652018E-06])
    
    
   
    #Case 2
    #'Subregion B
    #'Table 26, Eq 26, page 27
    Ib = np.array([-6, -6, -5, -5, -4, -4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5])
    Jb = np.array([0, 11, 0, 11, 0, 1, 11, 0, 1, 11, 12, 0, 1, 6, 10, 0, 1, 5, 8, 9, 0, 1, 2, 4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 0, 1, 5, 0, 1, 3, 0, 1, 0, 1, 2])
    nb = np.array([316876.65083497, 20.864175881858, -398593.99803599, -21.816058518877, 223697.85194242, -2784.1703445817, 9.920743607148, -75197.512299157, 2970.8605951158, -3.4406878548526, 0.38815564249115, 17511.29508575, -1423.7112854449, 1.0943803364167, 0.89971619308495, -3375.9740098958, 471.62885818355, -1.9188241993679, 0.41078580492196, -0.33465378172097, 1387.0034777505, -406.63326195838, 41.72734715961, 2.1932549434532, -1.0320050009077, 0.35882943516703, 5.2511453726066E-03, 12.838916450705, -2.8642437219381, 0.56912683664855, -0.099962954584931, -3.2632037778459E-03, 2.3320922576723E-04, -0.1533480985745, 0.029072288239902, 3.7534702741167E-04, 1.7296691702411E-03, -3.8556050844504E-04, -3.5017712292608E-05, -1.4566393631492E-05, 5.6420857267269E-06, 4.1286150074605E-08, -2.0684671118824E-08, 1.6409393674725E-09])
    
    
    #Case Else
    #'Subregion C
    #'Table 27, Eq 27, page 28
    Ic = np.array([-2, -2, -1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7])
    Jc = np.array([0, 1, 0, 0, 1, 2, 3, 0, 1, 3, 4, 0, 1, 2, 0, 1, 5, 0, 1, 4, 0, 1, 2, 0, 1, 0, 1, 3, 4, 5])
    nc = np.array([909.68501005365, 2404.566708842, -591.6232638713, 541.45404128074, -270.98308411192, 979.76525097926, -469.66772959435, 14.399274604723, -19.104204230429, 5.3299167111971, -21.252975375934, -0.3114733441376, 0.60334840894623, -0.042764839702509, 5.8185597255259E-03, -0.014597008284753, 5.6631175631027E-03, -7.6155864584577E-05, 2.2440342919332E-04, -1.2561095013413E-05, 6.3323132660934E-07, -2.0541989675375E-06, 3.6405370390082E-08, -2.9759897789215E-09, 1.0136618529763E-08, 5.9925719692351E-12, -2.0677870105164E-11, -2.0874278181886E-11, 1.0162166825089E-10, -1.6429828281347E-10])
   
    
    pi = p/1.0

    if p < 4:
        sigma = s / 2.0
        Ta_ps = np.sum(na*pi**Ia * (sigma-2)**Ja)
        print(Ta_ps)
    elif s < 5.85:
        sigma = s / 2.9251
        Tc_ps = np.sum(nc*pi**Ic * (2-sigma)**Jc)
        print(Tc_ps)       
    else:
        sigma = s / 0.7853
        Tb_ps = np.sum(nb*pi**Ib * (10-sigma)**Jb)
        print(Tb_ps)
        
T2_ps(20.0,5.75)
T2_ps(80.0,5.25)
T2_ps(80.0,5.75)
        
   
#==============================================================================
# REGION II 
# Backward equations - p_hs 
#==============================================================================

def p2_hs(h,s):
      
    #Case 1
    #'Subregion A
    #'Table 6, Eq 3, page 8
    Ia = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 6, 7])
    Ja = np.array([1, 3, 6, 16, 20, 22, 0, 1, 2, 3, 5, 6, 10, 16, 20, 22, 3, 16, 20, 0, 2, 3, 6, 16, 16, 3, 16, 3, 1])
    na = np.array([-1.82575361923032E-02, -0.125229548799536, 0.592290437320145, 6.04769706185122, 238.624965444474, -298.639090222922, 0.051225081304075, -0.437266515606486, 0.413336902999504, -5.16468254574773, -5.57014838445711, 12.8555037824478, 11.414410895329, -119.504225652714, -2847.7798596156, 4317.57846408006, 1.1289404080265, 1974.09186206319, 1516.12444706087, 1.41324451421235E-02, 0.585501282219601, -2.97258075863012, 5.94567314847319, -6236.56565798905, 9659.86235133332, 6.81500934948134, -6332.07286824489, -5.5891922446576, 4.00645798472063E-02])
    
    
    #Case 2
    #'Subregion B
    #'Table 7, Eq 4, page 9
    Ib = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 12, 14])
    Jb = np.array([0, 1, 2, 4, 8, 0, 1, 2, 3, 5, 12, 1, 6, 18, 0, 1, 7, 12, 1, 16, 1, 12, 1, 8, 18, 1, 16, 1, 3, 14, 18, 10, 16])
    nb = np.array([8.01496989929495E-02, -0.543862807146111, 0.337455597421283, 8.9055545115745, 313.840736431485, 0.797367065977789, -1.2161697355624, 8.72803386937477, -16.9769781757602, -186.552827328416, 95115.9274344237, -18.9168510120494, -4334.0703719484, 543212633.012715, 0.144793408386013, 128.024559637516, -67230.9534071268, 33697238.0095287, -586.63419676272, -22140322476.9889, 1716.06668708389, -570817595.806302, -3121.09693178482, -2078413.8463301, 3056059461577.86, 3221.57004314333, 326810259797.295, -1441.04158934487, 410.694867802691, 109077066873.024, -24796465425889.3, 1888019068.65134, -123651009018773.0])
    
    #Case Else
    #'Subregion C
    #'Table 8, Eq 5, page 10
    Ic = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 10, 12, 16])
    Jc = np.array([0, 1, 2, 3, 4, 8, 0, 2, 5, 8, 14, 2, 3, 7, 10, 18, 0, 5, 8, 16, 18, 18, 1, 4, 6, 14, 8, 18, 7, 7, 10])
    nc = np.array([0.112225607199012, -3.39005953606712, -32.0503911730094, -197.5973051049, -407.693861553446, 13294.3775222331, 1.70846839774007, 37.3694198142245, 3581.44365815434, 423014.446424664, -751071025.760063, 52.3446127607898, -228.351290812417, -960652.417056937, -80705929.2526074, 1626980172256.69, 0.772465073604171, 46392.9973837746, -13731788.5134128, 1704703926305.12, -25110462818730.8, 31774883083552.0, 53.8685623675312, -55308.9094625169, -1028615.22421405, 2042494187562.34, 273918446.626977, -2.63963146312685E+15, -1078908541.08088, -29649262098.0124, -1.11754907323424E+15])
    
    
    
    
     
    if h < (-3498.98083432139 + 2575.60716905876 * s - 421.073558227969 * s**2 + 27.6349063799944 * s**3):
        eta = h / 4200.0
        sigma = s / 12.0
        p2a_hs = 4*np.sum(na*(eta-0.5)**Ia * (sigma-1.2)**Ja)**4
        print(p2a_hs)
    elif s < 5.85:
        eta = h / 3500.0
        sigma = s / 5.9
        p2c_hs = 100*np.sum(nc*(eta-0.7)**Ic * (sigma-1.1)**Jc)**4
        print(p2c_hs)
    else:
        eta = h / 4100.0
        sigma = s / 7.9
        p2b_hs = 100*np.sum(nb*(eta-0.6)**Ib * (sigma-1.01)**Jb)**4
        print(p2b_hs)
        

p2_hs(2800.0,5.10)
p2_hs(2800.0,5.8)
p2_hs(3400.0,5.8)
    
#==============================================================================
# REGION III
#==============================================================================

st.set_page_config(layout='wide')

st.title('Steam Tables - IAPWS IF-97')

st.sidebar.write('This web application calculates steam and water properties like Enthalpy, Entropy, Density, Saturation Temperature and Pressure, Degree Superheat for specified Pressure and Temperature.')
st.sidebar.selectbox('Units', ['SI', "MKS"])

st.subheader("Properties")
temperature_property = st.checkbox("Temperature")
pressure_property = st.checkbox("Pressure")

temperature = st.number_input('Temperature')
pressure = st.number_input('Pressure')

st.subheader("Results")
result = prop(pressure, temperature)
st.write(result)
# #Specific Volume (m3/kg)
#     v_pT = gamma_pi*pi*R*T*0.001/p
    
#     #Specific Enthalpy (kJ/kg)
#     h_pT = tau*gamma_tau*R*T
    
#     #Specific Entropy
#     s_pT = R*(tau*gamma_tau - gamma)    
    
#     #Specific Heat capactiy at constant pressure, Cp 
#     Cp_pT = -tau**2 *gamma_tautau*R
    
#     #Specific Heat capacity at constant volume, Cv
#     Cv_pT = Cp_pT-R
    
#     #Specific Internal Energy
#     u_pT = (tau*gamma_tau - pi*gamma_pi)*R*T
#prop(3.0,300.0)
#prop(80.0,300.0)
#prop(3.0,500.0)