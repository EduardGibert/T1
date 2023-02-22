##Eduard Gibert Ramon 02/2023
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


##Exercici 1

##Cambiem la freqüència de la sinusoide a 4000Hz com ens diu l'enunciat:

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                              # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav



##Exercici 2

##Modifiquem el programa per fer servir la senyal del fitxer '.wav' com ens diu l'enunciat:
x_r, fm = sf.read('so_exemple1.wav')
fx = 4000

#Gràfic 5 periodes (fem servir el mateix codi que ens ha estat donat anteriorment)
Tx=1/fx                                 # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

#Gràfic FFT (fem servir el mateix codi que ens ha estat donat anteriorment amb alguns petits canvis)
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)         # Càlcul de la transformada de 5 períodes de la sinusoide (Canviem la x per x_r ja que volem que sigui amb el .wav)

k=np.arange(N)                        # Vector amb els valors 0≤k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformada, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

