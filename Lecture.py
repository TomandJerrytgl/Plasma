"""
n_0=n_e=n_i: density of electrons and ions

lambda_D: Debye length
lamda_D=sqrt(epsilon0*k_B*T_e/n_0*e^2)
n_D=4/3*pi*n_0*lambda_D^3: number of particles in a Debye sphere
g=1/n_D: plasma parameter
#g>>1 strongly coupled plasma
#g<<1 weakly coupled plasma

plasma frequency: omega_p=sqrt(n_0*e^2/epsilon0*m_e)

Collision

e^2/4*pi*epslon0*b_0=m_e*v_e^2
lambda: mean free path
sigma: cross section area
n_n: density of neutral particles
collision frequency: nu=sigma*n_n*v_average
v_average: mean velocity of electrons
b: impact parameter
effection cross section: sigma=pi*b_0^2
nu:frequency of collision
nu_large_angle: nu_large_angle=sigma*n_n*v_average=n_i*z^4*e^4/16*pi*epsilon0^2*m_e^2*v_e^3
nu propotion to T_e^-3/2

Ionization fraction

Quantum mechanics, energy eigenstate
photoionization and recombination
photon+natom_neutral<->natom_ionized+electron
electron ionization
electron+atom_neutral->natom_ionized+2electron
fusion change exchange
atom_neutral_high_energy+proton->proton_high_energy+atom_neutral_low_energy
shoot high energy neutral atom into tokamak, low energy neutral atom will escape and high energy proton will be confined in tokamak, this is called neutral beam injection
Coronal Equilibrim
ionize by eletron ionization and recombine by photonionization recombination
local equilibrim: boltsmann distribution
assume proton not move, only electron move
p_i->p_i+1 + e: ionization
Kai_i:binding energy of i-th ionization state
delta_E=Kai_i+1/2*m_e*v_e^2
P_i+1*P_e/P_i=exp(-delta_E/k_B*T)
g_i: number of bound electron quantum state
L_i:translational quantum state
P_i=n_i*volume/(g_i*L_i)
P_e:Fractional occupancy of free electron
k=m_e*v_e/hbar
delta_L_e=2*volume/(2*pi)^3*4*pi*k^2*dk
delta_K_e=4*pi*v^2*dv*(m_e/(2*pi*k_B*T))^1.5*n_e*volume*exp(-m_e*v^2/2*k_B*T)
P_e=delta_K_e/delta_L_e=n_e/2*h^3/m_e^3*(m_e/(2*pi*k_B*T))^1.5*exp(-m_e*v^2/2*k_B*T)
Saha equation: 
n_e*n_i+1/n_i=g_i+1/g_i*2*m_e^3/h^3*(2*pi*T*k_B/m_e)^1.5*exp(-Kai_i/k_B*T)

Single particle motion
circle motion
gyrofrequency: omega_c=abs(q*B/m)
gyroradius: rho=v_perp/omega_c
magnetic moment: mu=pi*rho^2*I=m*v_perp^2/(2*B)
"""

