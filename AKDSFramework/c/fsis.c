#include <Python.h>
#include <stdio.h>

static PyObject* inverse_sqrt(PyObject* self, PyObject* args){
    float number;

    // PyArgs ParseTuple and stuff.  
    if (!PyArg_ParseTuple(args, "f", &number)){
        return NULL;
    }

    if (number < 0){
        PyErr_SetString(PyExc_ValueError, "Can not compute a Negative number's square root.");
        return NULL;
    }

    if (number == 0){
        PyErr_SetString(PyExc_ZeroDivisionError, "Zero Cannot be in the denominator");
        return NULL;
    }

    const float threehalfs = 1.5F;

    float x2 = number * 0.5F;
    float y = number;

    // bit level crap
    long i = * ( long *) &y;
    i = 0x5f3759df - ( i >> 1 ); 
    y = * ( float * ) &i;

    y = y * ( threehalfs - ( x2 * y * y ) );


    return Py_BuildValue("f", y);
}

static char docs[] = "Calculate a 32 bit floating point number's root inverse, fast.";

static PyMethodDef methods[] = {
    {"inverse_sqrt", (PyCFunction)inverse_sqrt, METH_VARARGS, docs},
    {NULL, NULL, 0, NULL}       // sentinel or whatever
};

static struct PyModuleDef fastInverseSquare = {
    PyModuleDef_HEAD_INIT,
    "AKDSFramework.c.fsis",
    docs,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_fsis(void){
    return PyModule_Create(&fastInverseSquare);
}