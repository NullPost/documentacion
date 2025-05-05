import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

# Número de simulaciones
N = 100

# Númetro de pasos por simulación
n = 10000

# Arreglos temporales a rellenar con datos
index = np.arange(0,n)
superMsd = np.empty((1,n))
print(superMsd)


for run in range(N):
    # Movimiento browniano (suma de números aleatorios)
    x = np.cumsum(np.random.normal(loc=0, scale=1,size=n))
    y = np.cumsum(np.random.normal(loc=0, scale=1,size=n))

    # Desplazamiento cuadrado
    msd = []
    for i in range(len(x)):
        msd.append(x[i]**2 + y[i]**2)
    msd = np.array(msd)
    superMsd = np.vstack((superMsd,msd))
    
    

    
    #print(index)
    #print(msd)
    if run == 0:
        #interpolación de lineas entre puntos para ver trayectoria con colores
        k = 10
        x2 = np.interp(np.arange(n * k), np.arange(n) * k, x)
        y2 = np.interp(np.arange(n * k), np.arange(n) * k, y)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))


        scatter = ax1.scatter(x2, y2, c=range(n * k), linewidths=0,
                marker='o', s=3, cmap=plt.cm.jet,)
        ax1.axis('equal')
        #ax.set_axis_off()
        ax1.set_title("Ejemplo de una trayectoria")


        ax1.vlines(0,ymin=min(y),ymax=max(y),colors="black")
        ax1.hlines(0,xmin=min(x),xmax=max(x),colors="black")
    # Grafica de desviaciones cuadráticas
    ax2.scatter(index,msd,c=range(n),cmap=plt.cm.jet,s=1,alpha=0.01)

cbar = fig.colorbar(scatter, ax=ax2)
cbar.ax.set_ylabel("número de pasos", rotation=-90, va="bottom")

# Cálculo del promedio de desviaciones cuadráticas entre simulaciones
totalAvg = []
totalStd = []

# Cálculo de <Dr^2> entre simulaciones con desviación estandar para el i-esimo paso
for i in range(n):
    totalAvg.append(np.mean(superMsd[:,i][1:]))
    totalStd.append(np.std(superMsd[:,i][1:]))


totalAvg = np.array(totalAvg)
totalStd = np.array(totalStd)

ax2.plot(index, totalAvg, color="black", label=r"$\langle \Delta r ^{2} \rangle$")
ax2.plot(index, totalAvg+totalStd, color="red", label=r"$\langle \Delta r ^{2} \rangle \pm \sigma $" )
ax2.plot(index, totalAvg-totalStd, color="red")
ax2.set_title(f"Simulación de {N} trayectorias con desviación cuadrática media entre ellas y desviación estándar")
ax2.legend()

plt.tight_layout()
plt.savefig("/home/nullpost/Scripts/college stuf/brownan.png",bbox_inches=0,pad_inches=0,dpi=120)
