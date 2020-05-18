#include <Python.h>
#include <stdio.h>
#define PY_REP(x) (((PyObject *)(x))->ob_type)
#define DATATYPE PY_REP(((PyListObject *)(p))->ob_item[i])->tp_name
#define MAX_SIZE 15
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void trim_zeros(char *x);
void print_python_float(PyObject *p);

/**
 *print_python_list - function to print about list
 *@p: pointer to refer to a list of python
 *Return: Nothing
 */
void print_python_list(PyObject *p)
{
	int i = 0, tamano = 0;

	printf("[*] Python list info\n");
	fflush(stdout);
	if (PyList_Check(p))
	{
		tamano = (int)(((PyVarObject *)(p))->ob_size);

		printf("[*] Size of the Python List = %d\n", tamano);
		fflush(stdout);
		printf("[*] Allocated = %d\n", (int)(((PyListObject *)(p))->allocated));
		fflush(stdout);
		for (i = 0; i < tamano; i++)
		{
			printf("Element %d: %s\n", i, DATATYPE);
			fflush(stdout);
			if (PyBytes_Check((((PyListObject *)(p))->ob_item[i])))
				print_python_bytes((((PyListObject *)(p))->ob_item[i]));
			else if (PyFloat_Check((((PyListObject *)(p))->ob_item[i])))
				print_python_float((((PyListObject *)(p))->ob_item[i]));
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
	}
}
/**
 *print_python_bytes - function to print about list
 *@p: pointer to refer to a byte object of python
 *Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{

		printf("\n");

	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
	}
}
/**
 *trim_zeros - this will cut a string with the zero delimiter
 *@x: string to cut for float logic
 *Return: Nothing
 */
void trim_zeros(char *x)
{
	int i, length, flag_passed = 0;

	length = strlen(x) - 1;
	for (i = 0; i < length; i++)
	{
		if (x[i] == '.' && x[i + 1] == '0')
		{
			i = i + 2;
			x[i] = 0;
			break;
		}
		else if (x[i] == '.')
			flag_passed = 1;
		if (flag_passed == 1 && x[i] == '0')
		{
			x[i] = 0;
			break;
		}
	}
	for (; i < length; i++)
		x[i + 1] = 0;
}
/**
 *print_python_float - function to print about float objects
 *@p: pointer to refer to a list of python
 *Return: Nothing
 */
void print_python_float(PyObject *p)
{
	char float_number[MAX_SIZE];

	printf("[.] float object info\n");
	fflush(stdout);
	if (PyFloat_Check(p))
	{
		sprintf(float_number, "%0.15f", ((PyFloatObject *)(p))->ob_fval);
		trim_zeros(float_number);
		printf("  value: %s\n", float_number);
		fflush(stdout);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
	}
}
