#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: pyhton list to print info about
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *ptr = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ptr->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
