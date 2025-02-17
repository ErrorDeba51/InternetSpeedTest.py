
import speedtest
import geocoder
import time

try:  # Get current location
    g = geocoder.ip('me')

    city = g.city if g.city else "city not recognize"
    country = g.country if g.country else "country not recognize"

    st = speedtest.Speedtest()

    st.get_best_server()

    isp = st.results.client['isp']
    time.sleep(5)
    #PRINT LOCATION & NETWORK PROVIDER
    print(f"\nLocation: {city}, {country}")
    print(f"network provider: {isp}")
     #DOWNLOAD SPPED 
    print("\nTesting Network Speed....")
    down_speed = st.download()
    down_speed_mbps = round(down_speed / 1_000_000, 2)
    print("\nDOWNLOAD SPEED TEST RESULT: ")
    time.sleep(5)
    print(f"Download speed: {down_speed_mbps} Mbps ")
    # UPLOAD SPEED
    print("\nUPLOAD SPEED RESULT....")
    up_speed = st.upload()
    up_speed_mbps = round(up_speed / 1_000_000, 2)
    print(f"Upload speed: {up_speed_mbps} Mbps")

    ping = st.results.ping
    # PING
    print(f"\nPing: {ping} ms")
    print("\nEnjoy your internet speed!")
    # ERROR HANDLING
except speedtest.ConfigRetrievalError as e:
    print(f"Speedtest configuration error: {e}","TRY AGAIN")
except OSError as e:
    print(f"An OS-related error occurred: {e}","TRY AGAIN")
except ValueError as e:
    print(f"Invalid value: {e}","TRY AGAIN")
