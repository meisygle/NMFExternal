## NMFExternal: Transferring knowledge across aquatic species via clustering techniques to unravel patterns of pesticide toxicity
```
### Using the code

```
1. Prepare the test matrix according to the format of file S2.xlsx
2. run the following script
>>>python NMF.py
3. The predicted values are provided in the form of reciprocals. Note: the very small predicted values much smaller than the pesticide's smallest value is suggested to be treated as zero, indicating that the values cannot be determined. 
4. The final predicted toxicities are the reciprocals of the non-zero values.

```
### License
MIT License
