/*
* main.c (C)
* 
* Purpose: Simple program to run with GDB.
* 
* Site: https://www.geofisicando.com
* 
* Version 1.0
* 
* Programmer: Rodolfo A C Neves (Dirack) 19/08/2021
* 
* Email: rodolfo_profissional@hotmail.com
* 
* License: GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.txt>.
*/

#include <stdio.h>

float soma(float f1, float f2){
	return f1+f2;
}

float sub(float f1, float f2){
	return f1-f2;
}

int main(void){

	float f1;
	float f2;
	float f3,f4;

	f1 = 1.0;
	f2 = 2.0;

	f3 = soma(f1,f2);
	f4 = sub(f1,f2);

	printf("Sum %f+%f é %f\n",f1,f2,f3);

	printf("Difference %f-%f é %f\n",f1,f2,f4);

}
