##Eduard Gibert Ramon 02/2023
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


# Exercici 1
import sounddevice as sd      
from numpy.fft import fft  

T= 2.5                               
fm=8000                              
fx=4000                              
A=4                                  
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('so_exemple1.wav', x, fm)   
Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(111)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show()                                

import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                # Reproducció d'àudio
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show() 


##Exercici 2

x_r, fm = sf.read('so_exemple1.wav')       # Llegim el fitxer
T = (1/fm)*len(x_r)
Tm=1/fm 
L = int(fm * T) 
t=Tm*np.arange(L)

fx=4000
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
plt.figure(2)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.
sd.play(x_r, fm)  

N=5000                       
X=fft(x_r[0 : Ls], N)         
k=np.arange(N)                        
plt.figure(1)                        
plt.subplot(211)                     
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))   
plt.xlabel('Index k')               
plt.ylabel('$\phi_x[k]$')             
plt.show()    

##Exercici 3

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple3.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
Tx=1/fx                                   
Ls=int(fm*Tx*5)                           

plt.figure(0)                             
plt.plot(t[0:Ls], x[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('5 períodes')  
plt.show()   
sd.play(x,fm)         


N=5000 
X=fft(x[0:L],N) 
k=np.arange(N)  
X2 = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N         #Calcul de la fk, pels valors de l'eix d'abscisses
plt.figure(1)
plt.subplot(211)   
plt.plot(fk,X2[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')              
plt.show() 

##Exercici 4

T= 0.025   #donem un periode de 25ms com ens diu l'enunciat                              
data, fm =sf.read('luzbel44.wav')     #fm es la frenquencia de mostreig  
L = int(fm * T)     #el numero de mostres que te el fitxer d'audio                 
Tm=1/fm                            
t=Tm*np.arange(L)                   

plt.figure(41)                          
plt.plot(t[0:L],data[0:L])              
plt.xlabel('t en segons')               
plt.title('Exercici 4')  
plt.show()      

N=5000                        
X=fft(data[0 : L], N)    
k=np.arange(N)                                         
plt.figure(42)                         
X3 = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)   
plt.plot(fk,X3[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                   
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')          
plt.show() 
