from netmiko import ConnectHandler # module used for making ssh connection
from datetime import datetime      # module used for timestamp details

start_time = datetime.now()  # indicates when the script started

# dictionary contains device parameters to login
Internet = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.0.100",
    "username" : "madhu",
    "password" : "cisco",
    "secret" : "cisco",
}

net_connect = ConnectHandler(**Internet)  # uses the device parameters to ssh into device

net_connect.enable() # enters into enable mode

output = net_connect.send_command("show ip int brief")  #enters user mode allows show comamnds
print (output)    #prints output of show command

for loopback in range(10,11,10): #creates loopback interface of 10
    config_commands = ["interface loopback " + str(loopback) , "description loopback_" + str(loopback),
                        "ip address 1.1.1.1 255.255.255.255"]
    output = net_connect.send_config_set(config_commands) #enters global config mode to change config
    print (output)

net_connect.save_config()  #saves running config to startup config

end_time = datetime.now()  # indicates when script processing done
total_time = end_time - start_time # indicates how much acutally script took to execute

print (total_time)

net_connect.disconnect()  # close the ssh session






