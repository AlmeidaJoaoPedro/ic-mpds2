# Script to call a Python Script every 30 minutes.
# Remember to give permission to the script. 
#(chmod+x).
# Loop to correctly execute the function.
#!/bin/bash
while :
do

if [ $# -eq 0 ]
    then
        echo "Running file..."
fi

# Python 3.
   python3 img-2-arr-2-img-detection.py

# Calculation for the loop to be done every 30 minutes.
sleep $((3*60))
#sleep 2m 30s

done

# End