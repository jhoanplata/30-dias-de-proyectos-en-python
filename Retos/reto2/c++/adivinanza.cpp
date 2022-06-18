#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{

    int numero, numero_usuario, intentos = 0;

    cout << "Adivina el numero del 1 al 100\n \n"
         << endl;

    srand(time(NULL));
    numero = rand() % 100 + 1;

    do
    {
        cout << "Ingrese un numero: ";
        cin >> numero_usuario;
        intentos++;

        if (numero_usuario < numero)
        {
            cout << "El numero es mayor\n";
        }
        else if (numero_usuario > numero)
        {
            cout << "El numero es menor\n";
        }
        else
        {
            cout << "Felicidades, adivinaste el numero en " << intentos << " intentos\n";
        }

    } while (numero_usuario != numero);

    return 0;
}

