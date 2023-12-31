import optparse
import subprocess

def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address.")
  parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
  (options, arguments) = parser.parse_args()
  if not options.interface:
    parser.error("[-] Please specify an interface, use --help for more info.")
  elif not options.new_mac:
    parser.error("[-] Please specify a new mac, use --help for more info.")
  else:
    return options

def change_mac(interface, new_mac):
  print("Changing the mac address of " +interface+ "to " +new_mac)
  subprocess.call("ifconfig", shell=True)
  subprocess.call("ifconfig", interface, " down")
  subprocess.call("ifconfig", interface, "hw", "ether", new_mac)
  subprocess.call("ifconfig", interface, "up")

options = get_arguments()
change_mac(options.interface, options.new_mac)
