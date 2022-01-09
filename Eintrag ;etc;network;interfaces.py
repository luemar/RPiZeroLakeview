#interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

#Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
auto wlan0

allow-hotplug wlan0

iface mywlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

iface mywlan1 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
