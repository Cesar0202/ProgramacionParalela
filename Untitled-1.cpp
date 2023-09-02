#include <iostream>
#include <chrono>
#include <omp.h>
using namespace std;

const int tamMatriz = 1000;

void inicializarMatriz(int matriz[][tamMatriz]) {
    for (int i = 0; i < tamMatriz; ++i) {
        for (int j = 0; j < tamMatriz; ++j) {
            matriz[i][j] = rand() % 100;
        }
    }
}

void multiplicarSecuencial(const int matrizA[][tamMatriz], const int matrizB[][tamMatriz], int resultado[][tamMatriz]) {
    for (int i = 0; i < tamMatriz; ++i) {
        for (int j = 0; j < tamMatriz; ++j) {
            int suma = 0;
            for (int k = 0; k < tamMatriz; ++k) {
                suma += matrizA[i][k] * matrizB[k][j];
            }
            resultado[i][j] = suma;
        }
    }
}

void multiplicarParalelo(const int matrizA[][tamMatriz], const int matrizB[][tamMatriz], int resultado[][tamMatriz]) {
    #pragma omp parallel for
    for (int i = 0; i < tamMatriz; ++i) {
        for (int j = 0; j < tamMatriz; ++j) {
            int suma = 0;
            for (int k = 0; k < tamMatriz; ++k) {
                suma += matrizA[i][k] * matrizB[k][j];
            }
            resultado[i][j] = suma;
        }
    }
}

int main() {
    // Inicialización de las matrices
    int matrizA[tamMatriz][tamMatriz];
    int matrizB[tamMatriz][tamMatriz];
    int resultadoSecuencial[tamMatriz][tamMatriz];
    int resultadoParalelo[tamMatriz][tamMatriz];
    srand(time(NULL));
    inicializarMatriz(matrizA);
    inicializarMatriz(matrizB);

    // Multiplicación secuencial
    auto tiempoInicio = chrono::high_resolution_clock::now();
    multiplicarSecuencial(matrizA, matrizB, resultadoSecuencial);
    auto tiempoFin = chrono::high_resolution_clock::now();
    auto duracionSecuencial = chrono::duration_cast<chrono::milliseconds>(tiempoFin - tiempoInicio);

    // Multiplicación en paralelo
    tiempoInicio = chrono::high_resolution_clock::now();
    multiplicarParalelo(matrizA, matrizB, resultadoParalelo);
    tiempoFin = chrono::high_resolution_clock::now();
    auto duracionParalelo = chrono::duration_cast<chrono::milliseconds>(tiempoFin - tiempoInicio);

    cout << "Tiempo secuencial: " << duracionSecuencial.count() << " ms\n";
    cout << "Tiempo en paralelo: " << duracionParalelo.count() << " ms\n";
    return 0;
}
