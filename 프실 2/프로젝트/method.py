from tkinter import *
import numpy as np
from matplotlib import pyplot as pl
from matplotlib import animation
from scipy.fftpack import fft,ifft
def bring(V0,a,r):
    class Schrodinger(object):
   
        def __init__(self, x, psi_x0, V_x,
                     k0 = None, hbar=1, m=1, t0=0.0):
       
            # Validation of array inputs
            self.x, psi_x0, self.V_x = map(np.asarray, (x, psi_x0, V_x))
            N = self.x.size
            assert self.x.shape == (N,)
            assert psi_x0.shape == (N,)
            assert self.V_x.shape == (N,)

            # Set internal parameters
            self.hbar = hbar
            self.m = m
            self.t = t0
            self.dt_ = None
            self.N = len(x)
            self.dx = self.x[1] - self.x[0]
            self.dk = 2 * np.pi / (self.N * self.dx)
    
            # set momentum scale
            if k0 == None:
                self.k0 = -0.5 * self.N * self.dk
            else:
                self.k0 = k0
            self.k = self.k0 + self.dk * np.arange(self.N)
    
            self.psi_x = psi_x0
            self.compute_k_from_x()
    
            # variables which hold steps in evolution of the
            self.x_evolve_half = None
            self.x_evolve = None
            self.k_evolve = None
    
            # attributes used for dynamic plotting
            self.psi_x_line = None
            self.psi_k_line = None
            self.V_x_line = None

        def _set_psi_x(self, psi_x):
            self.psi_mod_x = (psi_x * np.exp(-1j * self.k[0] * self.x)* self.dx / np.sqrt(2 * np.pi))

        def _get_psi_x(self):
            return (self.psi_mod_x * np.exp(1j * self.k[0] * self.x)* np.sqrt(2 * np.pi) / self.dx)

        def _set_psi_k(self, psi_k):
            self.psi_mod_k = psi_k * np.exp(1j * self.x[0]
                                            * self.dk * np.arange(self.N))

        def _get_psi_k(self):
            return self.psi_mod_k * np.exp(-1j * self.x[0] * 
                                            self.dk * np.arange(self.N))
    
        def _get_dt(self):
            return self.dt_

        def _set_dt(self, dt):
            if dt != self.dt_:
                self.dt_ = dt
                self.x_evolve_half = np.exp(-0.5 * 1j * self.V_x
                                             / self.hbar * dt )
                self.x_evolve = self.x_evolve_half * self.x_evolve_half
                self.k_evolve = np.exp(-0.5 * 1j * self.hbar /
                                        self.m * (self.k * self.k) * dt)
    
        psi_x = property(_get_psi_x, _set_psi_x)
        psi_k = property(_get_psi_k, _set_psi_k)
        dt = property(_get_dt, _set_dt)

        def compute_k_from_x(self):
            self.psi_mod_k = fft(self.psi_mod_x)

        def compute_x_from_k(self):
            self.psi_mod_x = ifft(self.psi_mod_k)

        def time_step(self, dt, Nsteps = 1):
   
            self.dt = dt

            if Nsteps > 0:
                self.psi_mod_x *= self.x_evolve_half

            for i in range(Nsteps - 1):
                self.compute_k_from_x()
                self.psi_mod_k *= self.k_evolve
                self.compute_x_from_k()
                self.psi_mod_x *= self.x_evolve

            self.compute_k_from_x()
            self.psi_mod_k *= self.k_evolve

            self.compute_x_from_k()
            self.psi_mod_x *= self.x_evolve_half

            self.compute_k_from_x()

            self.t += dt * Nsteps


        def gauss_x(x, a, x0, k0):
   
            return ((a * np.sqrt(np.pi)) ** (-0.5)
                * np.exp(-0.5 * ((x - x0) * 1. / a) ** 2 + 1j * x * k0))

        def gauss_k(k,a,x0,k0):
   
   
            return ((a / np.sqrt(np.pi))**0.5
                * np.exp(-0.5 * (a * (k - k0)) ** 2 - 1j * (k - k0) * x0))




        def theta(x):
            x = np.asarray(x)
            y = np.zeros(x.shape)
            y[x > 0] = 1.0
            y[x < -50] = -1.0
    
            return y

        def square_barrier(x, width, height):
            return height * (theta(x) - theta(x - width))




        dt = 0.01
        N_steps = 50
        t_max = 120
        frames = int(t_max / float(N_steps * dt))


        hbar = 1.0   # planck's constant
        m = 1.9      # particle mass


        N = 2 ** 11
        dx = 0.1
        x = dx * (np.arange(N) - 0.5 * N)


        L = hbar / np.sqrt(2 * m * V0)

        x0 = -60 * L
        V_x = square_barrier(x, a, V0)
        V_x[x < -98] = 1E6
        V_x[x > 98] = 1E6


        p0 = np.sqrt(2 * m * r * V0)
        dp2 = p0 * p0 * 1./80
        d = hbar / np.sqrt(2 * dp2)

        k0 = p0 / hbar
        v0 = p0 / m
        psi_x0 = gauss_x(x, d, x0, k0)


        S = Schrodinger(x=x,
                    psi_x0=psi_x0,
                    V_x=V_x,
                    hbar=hbar,
                    m=m,
                    k0=-28)


        fig = pl.figure()


        xlim = (-100, 100)
        klim = (-5, 5)


        ymin = 0
        ymax = V0
        ax1 = fig.add_subplot(211, xlim=xlim,
                          ylim=(ymin - 0.2 * (ymax - ymin),
                                ymax + 0.2 * (ymax - ymin)))
        psi_x_line, = ax1.plot([], [], c='r', label=r'$|\psi(x)|$')
        V_x_line, = ax1.plot([], [], c='k', label=r'$V(x)$')
        center_line = ax1.axvline(0, c='k', ls=':',
                              label = r"$x_0 + v_0t$")
    
        title = ax1.set_title("")
        ax1.legend(prop=dict(size=12))
        ax1.set_xlabel('$x$')
        ax1.set_ylabel(r'$|\psi(x)|$')


        ymin = abs(S.psi_k).min()
        ymax = abs(S.psi_k).max()
        ax2 = fig.add_subplot(212, xlim=klim,ylim=(ymin - 0.2 * (ymax - ymin),ymax + 0.2 * (ymax - ymin)))
        psi_k_line, = ax2.plot([], [], c='r', label=r'$|\psi(k)|$')

        p0_line1 = ax2.axvline(-p0 / hbar, c='k', ls=':', label=r'$\pm p_0$')
        p0_line2 = ax2.axvline(p0 / hbar, c='k', ls=':')
        mV_line = ax2.axvline(np.sqrt(2 * V0) / hbar, c='k', ls='--',
                          label=r'$\sqrt{2mV_0}$')
        ax2.legend(prop=dict(size=12))
        ax2.set_xlabel('$k$')
        ax2.set_ylabel(r'$|\psi(k)|$')

        V_x_line.set_data(S.x, S.V_x)


        def init():
            psi_x_line.set_data([], [])
            V_x_line.set_data([], [])
            center_line.set_data([], [])

            psi_k_line.set_data([], [])
            title.set_text("")
            return (psi_x_line, V_x_line, center_line, psi_k_line, title)

        def animate(i):
            S.time_step(dt, N_steps)
            psi_x_line.set_data(S.x, 4 * abs(S.psi_x))
            V_x_line.set_data(S.x, S.V_x)
            center_line.set_data(2 * [x0 + S.t * p0 / m], [0, 1])

            psi_k_line.set_data(S.k, abs(S.psi_k))
            title.set_text("t = %.2f" % S.t)
            return (psi_x_line, V_x_line, center_line, psi_k_line, title)


        anim = animation.FuncAnimation(fig, animate, init_func=init,frames=frames, interval=30, blit=True)
