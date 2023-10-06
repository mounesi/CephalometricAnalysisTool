# CephalometricAnalysisTool
The provided sample points in the script are arbitrary and for demonstration purposes. For accurate cephalometric analysis, use landmark coordinates from an actual cephalogram.



# Cephalometric Analysis Tool

This repository contains a Python tool for basic cephalometric analysis using landmark points. It provides functions to calculate critical angles such as SNA, SNB, and ANB and determines skeletal relationships based on these angles.

## Features:

1. Calculation of angles between given points using the dot product.
2. Determination of maxillary and mandibular positions (prognathism or retrognathism).
3. Classification of skeletal relationships as Class I, II, or III.

## Usage:

Define your landmark points as tuples with x and y coordinates:
```python
S = (x1, y1)
N = (x2, y2)
A = (x3, y3)
B = (x4, y4)
CS = (x5, y5)
CE = (x6, y6)
```


Run the provided script to calculate and print out the angles and classifications.

Output:
The script will provide the following outputs:

SNA, SNB, and ANB angles.
Maxillary and Mandibular position (Prognathism or Retrognathism).
Skeletal relationship (Class I, II, or III).
Additional angles such as CSA (Cranial to A-point) and CSB (Cranial to B-point).
Notes:
The provided sample points in the script are arbitrary and for demonstration purposes. For accurate cephalometric analysis, use landmark coordinates from an actual cephalogram.




