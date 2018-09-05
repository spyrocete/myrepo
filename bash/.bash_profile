curr=$(tail -1 ~/current.txt | head -1)
if [ "$curr" != $HOSTNAME ]; then
    hostname >> current.txt
fi
    
