# Python Crop Simulation Environment (PCSE)

## Suitability Overview

Category | Note
-------- | ----
Setup    | Setting up PCSE is not difficult to setup, especially if you already have Jupyter Notebooks running.
Coverage | PCSE lacks some out of the box functionality of other models. For example, fertilization rates will require custom event listeners.
Documentation | PCSE comes with STELLAR technical documentation.
Flexibility | PCSE is a robust foundation for crop simulations built with customization in mind.

## Getting Started
Install PCSE using anaconda. [Here](http://pcse.readthedocs.io/en/master/installing.html) are the docs.

Fire up the conda environment you just setup:
```bash
activate py2_pcse
```
## Model details
PCSE is essentially an simulation manager for crop simulations — WOFOST and LINTUL3 (Light INTerception and UtiLisation). The default models allow you to listen to events within the model.

Custom simulation objects can then be used to modify existing portions of the simulation or for producing new outputs such as fertilization rates.

## Model Inputs
PCSE has 4 input requirements: Crop parameters, Site parameters, Agro-Management, Daily weather.

### Crop
Crop parameter files can be found in the WOFOST download — though it is important to note these files will be tailored to Europe.  

### Site parameters
Site parameters contain information about a site's soil characteristics.

### Daily Weather
Daily weather can be "manually" defined or captured from a NASA database.
