from pynput.keyboard import Listener, Key
 
store = set()
 
def handleKeyPress( key ):
    store.add( key )
 
    print( 'Press: {}'.format( store ) )
 
def handleKeyRelease( key ):
    print( 'Released: {}'.format( key ) )
 
    if key in store:
        store.remove( key )
        
    # 종료
    if key == Key.esc:
        return False
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()
