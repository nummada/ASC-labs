#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
 
void simpleMultiply(int n, double** a, double** b, double** c)
{
	int i, j, k;
	for (i = 0 ; i < n ; i++){
		double *orig_pa = &a[i][0];
		for (j = 0 ; j < n ; j++){
			double *pa = orig_pa;
			register double sum = 0.0;
			for (k = 0 ; k < n ; k++){
				sum += *pa * b[k][j];
				pa++;
			}
			c[i][j] = sum;
		}
	}
}


int main(void)
{
    int n;
    double** A;
    double** B;
    double** C;
    int numreps = 10;
    int i = 0 , j = 0;
    struct timeval tv1, tv2;
    struct timezone tz;
    double elapsed;
    // TODO: set matrix dimension n
    n = 500;
    // allocate memory for the matrices
 
    ///////////////////// Matrix A //////////////////////////
	A = calloc(n, sizeof(double*));
	for (int i = 0 ; i < n ; i++) {
		A[i] = calloc(n, sizeof(double));
	}
 
    ///////////////////// Matrix B ////////////////////////// 
	B = calloc(n, sizeof(double*));
	for (int i = 0 ; i < n ; i++) {
		B[i] = calloc(n, sizeof(double));
	}
    ///////////////////// Matrix C //////////////////////////
	C = calloc(n, sizeof(double*));
	for (int i = 0 ; i < n ; i++) {
		C[i] = calloc(n, sizeof(double));
	}
    // Initialize matrices A & B
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            A[i][j] = 1;
            B[i][j] = 2;
        }
    }

    //multiply matrices
 
    printf("Multiply matrices %d times...\n", numreps);
    for (i=0; i<numreps; i++)
    {
        gettimeofday(&tv1, &tz);
        simpleMultiply(n,A,B,C);
        gettimeofday(&tv2, &tz);
        elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
    }
    printf("Time = %lf \n",elapsed);
 
    //deallocate memory for matrices A, B & C
	for (int i = 0 ; i < n ; i++) {
		free(A[i]);
	}
	free(A);
	for (int i = 0 ; i < n ; i++) {
		free(B[i]);
	}
	free(B);
	for (int i = 0 ; i < n ; i++) {
		free(C[i]);
	}
	free(C);
 
    return 0;
}