# -*- coding: utf-8 -*-
#
# This file is part of the Rosenberg NMS
#
# Copyright (C) 2011-2014 Craig Small <csmall@enc.com.au>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>
#
#
""" Poller related database fields """
pollers = (
    ('no_poller', 'No Polling', 'no_poller', ''),
    ('input', 'SNMP Input Rate', 'snmp_counter',
        '1.3.6.1.2.1.31.1.1.1.6.${index}|1.3.6.1.2.1.2.2.1.10.${index}'),
    ('verify_interface_number', 'SNMP Verify Interface Number',
        'verify_interface_number', ''),
    ('cisco_snmp_ping_start', 'Cisco SNMP Ping Start', 'cisco_snmp_ping_start',
        ''),
    ('cisco_snmp_ping_wait', 'Cisco SNMP Ping Wait', 'cisco_snmp_ping_wait',
        ''),
    ('packetloss', 'Cisco SNMP Ping Get PL', 'cisco_snmp_ping_get_pl', ''),
    ('rtt', 'Cisco SNMP Ping Get RTT', 'cisco_snmp_ping_get_rtt', ''),
    ('cisco_snmp_ping_end', 'Cisco SNMP Ping End', 'cisco_snmp_ping_end', ''),
    ('output', 'SNMP Output Rate', 'snmp_counter',
        '1.3.6.1.2.1.31.1.1.1.10.${index}|1.3.6.1.2.1.2.2.1.16.${index}'),
    ('outputerrors', 'SNMP Output Errors', 'snmp_counter',
        '1.3.6.1.2.1.2.2.1.20.${index}'),
    ('inputerrors', 'SNMP Input Errors', 'snmp_counter',
        '1.3.6.1.2.1.2.2.1.14.${index}'),
    ('ifOper', 'SNMP Interface Operational Status', 'snmp_status',
        '1.3.6.1.2.1.2.2.1.8.${index}|'
        '1=up, 2=down, 3=testing, 4=unknown|down'),
    ('ifAdmin', 'SNMP Interface Administrative Status', 'snmp_status',
        '1.3.6.1.2.1.2.2.1.7.${index}|'
        '1=up, 2=down, 3=testing, 4=unknown|down'),
    ('cpu', 'Cisco CPU Utilization', 'snmp_counter',
        '1.3.6.1.4.1.9.9.109.1.1.1.1.5.1'),
    ('inpackets', 'SNMP Input Packets', 'snmp_counter',
        '1.3.6.1.2.1.31.1.1.1.7.${index}|1.3.6.1.2.1.2.2.1.11.${index}'),
    ('outpackets', 'SNMP Output Packets', 'snmp_counter',
        '1.3.6.1.2.1.31.1.1.1.11.${index}|1.3.6.1.2.1.2.2.1.17.${index}'),
    ('tcp_status,tcp_content,conn_delay', 'TCP Port Check & Delay',
        'tcp_status', ''),
    ('mem_used', 'Cisco Used Memory', 'snmp_counter',
        '1.3.6.1.4.1.9.9.48.1.1.1.5.1'),
    ('mem_free', 'Cisco Free Memory', 'snmp_counter',
        '1.3.6.1.4.1.9.9.48.1.1.1.6.1'),
    ('drops', 'SNMP Drops', 'snmp_counter',
        '1.3.6.1.2.1.2.2.1.19.${index}'),
    ('cpu', 'Cisco 2500 Series CPU Utilization', 'snmp_counter',
        '1.3.6.1.4.1.9.2.1.56.0'),
    ('bgpin', 'BGP Inbound Updates', 'snmp_counter',
        '1.3.6.1.2.1.15.3.1.10.${remote}'),
    ('bgpout', 'BGP Outbound Updates', 'snmp_counter',
        '1.3.6.1.2.1.15.3.1.11.${remote}'),
    ('bgpuptime', 'BGP Uptime', 'snmp_counter',
        '1.3.6.1.2.1.15.3.1.16.${remote}'),
    ('used_blocks', 'Storage Device Used Blocks', 'snmp_counter',
        '1.3.6.1.2.1.25.2.3.1.6.${index}'),
    ('total_blocks', 'Storage Device Total Blocks', 'snmp_counter',
        '1.3.6.1.2.1.25.2.3.1.5.${index}'),
    ('block_size', 'Storage Device Block Size', 'snmp_counter',
        '1.3.6.1.2.1.25.2.3.1.4.${index}'),
    ('bgp_peer_status', 'BGP Peer Status', 'snmp_status',
        '1.3.6.1.2.1.15.3.1.2.${remote}|6=up|down'),
    ('cpu_kernel_ticks', 'CPU Kernel Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.55.0'),
    ('cpu_idle_ticks', 'CPU Idle Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.53.0'),
    ('cpu_wait_ticks', 'CPU Wait Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.54.0'),
    ('cpu_system_ticks', 'CPU System Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.52.0'),
    ('mem_available', 'Real Memory Available', 'snmp_counter',
        '1.3.6.1.4.1.2021.4.6.0'),
    ('mem_total', 'Real Memory Total', 'snmp_counter',
        '1.3.6.1.4.1.2021.4.5.0'),
    ('swap_available', 'Swap Memory Available', 'snmp_counter',
        '1.3.6.1.4.1.2021.4.4.0'),
    ('swap_total', 'Swap Memory Total', 'snmp_counter',
        '1.3.6.1.4.1.2021.4.3.0'),
    ('load_average_15', 'Load Average 15 min', 'snmp_counter',
        '1.3.6.1.4.1.2021.10.1.3.3'),
    ('load_average_5', 'Load Average 5 min', 'snmp_counter',
        '1.3.6.1.4.1.2021.10.1.3.2'),
    ('load_average_1', 'Load Average 1 min', 'snmp_counter',
        '1.3.6.1.4.1.2021.10.1.3.1'),
    ('cpu_user_ticks', 'CPU User Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.50.0'),
    ('cpu_nice_ticks', 'CPU Nice Time', 'snmp_counter',
        '1.3.6.1.4.1.2021.11.51.0'),
    ('tcp_established', 'TCP MIB Established', 'snmp_tcp_established', ''),
    ('cpu', 'Host MIB Proc Average Util', 'snmp_walk_average',
        '1.3.6.1.2.1.25.3.3.1.2'),
    ('num_procs', 'Host MIB Number of Processes', 'snmp_counter',
        '1.3.6.1.2.1.25.1.6.0'),
    ('num_users', 'Host MIB Number of Users', 'snmp_counter',
        '1.3.6.1.2.1.25.1.5.0'),
    ('tcp_active', 'TCP MIB Active Opens', 'snmp_counter',
        '1.3.6.1.2.1.6.5.0'),
    ('tcp_passive', 'TCP MIB Passive Opens', 'snmp_counter',
        '1.3.6.1.2.1.6.6.0'),
    ('tcp_established', 'TCP MIB Established Connections', 'snmp_counter',
        '1.3.6.1.2.1.6.9.0'),
    ('app_status,current_instances,pids', 'Host MIB Process Verifier',
        'hostmib_apps', '${attribute}'),
    ('cisco_powersupply_status', 'Cisco Power Supply Status', 'snmp_status',
        '1.3.6.1.4.1.9.9.13.1.5.1.3.${index}|1=up|down'),
    ('cisco_temperature_status', 'Cisco Temperature Status', 'snmp_status',
        '1.3.6.1.4.1.9.9.13.1.3.1.6.${index}|1=up|down'),
    ('cisco_voltage_status', 'Cisco Voltage Status', 'snmp_status',
        '1.3.6.1.4.1.9.9.13.1.2.1.7.${index}|1=up|down'),
    ('temperature', 'Cisco Temperature', 'snmp_counter',
        '1.3.6.1.4.1.9.9.13.1.3.1.3.${index}'),
    ('forward_jitter', 'SA Agent Forward Jitter', 'cisco_saagent',
        '${index}|fwd_jitter'),
    ('backward_jitter', 'SA Agent Backward Jitter', 'cisco_saagent',
        '${index}|bwd_jitter'),
    ('rt_latency,forward_packetloss,backward_packetloss',
        'SA Agent Packetloss', 'cisco_saagent', '${index}|packetloss'),
    ('tcp_content_analisis', 'TCP Content Check', 'tcp_content', ''),
    ('rtt,packetloss', 'Reachability Ping', 'reach_ping', ''),
    ('status', 'Reachability Status', 'reach_status', ''),
    ('', 'TCP Port Status', 'buffer', 'tcp_status'),
    ('', 'Host MIB Status', 'buffer', 'app_status'),
    ('ntp_status', 'NTP Status', 'ntp_client', ''),
    ('used_memory', 'Host MIB Process Memory Usage', 'hostmib_perf', '2'),
    ('temperature', 'Compaq Temperature', 'snmp_counter',
        '1.3.6.1.4.1.232.6.2.6.8.1.4.${chassis}.${tempindex}'),
    ('temp_status', 'Compaq Temperature Status', 'snmp_status',
        '1.3.6.1.4.1.232.6.2.6.8.1.6.${chassis}.${tempindex}|2=up|down'),
    ('fan_status', 'Compaq Fan Condition', 'snmp_status',
        '1.3.6.1.4.1.232.6.2.6.7.1.9.${chassis}.${fanindex}|2=up|down'),
    ('compaq_disk', 'Compaq Drive Condition', 'snmp_status',
        '1.3.6.1.4.1.232.3.2.5.1.1.6.${controller}.${drvindex}|2=up|down'),
    ('tbr', 'IIS Total Bytes Received', 'snmp_counter',
        '1.3.6.1.4.1.311.1.7.3.1.4.0'),
    ('tcgir', 'IIS Total CGI Requests', 'snmp_counter',
        '1.3.6.1.4.1.311.1.7.3.1.35.0'),
    ('tfs', 'IIS Total Files Sent', 'snmp_counter',
        '1.3.6.1.4.1.311.1.7.3.1.5.0'),
    ('tg', 'IIS Total GETs', 'snmp_counter',
        '1.3.6.1.4.1.311.1.7.3.1.18.0'),
    ('tp', 'IIS Total Posts', 'snmp_counter', '1.3.6.1.4.1.311.1.7.3.1.19.0'),
    ('tac,tkb,cplo,up,bpr,bw,iw', 'Apache Status', 'apache', ''),
    ('capacity', 'APC Battery Capacity', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.2.2.1.0'),
    ('load', 'APC Output Load', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.4.2.3.0'),
    ('in_voltage', 'APC Input Voltage', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.3.2.1.0'),
    ('out_voltage', 'APC Output Voltage', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.4.2.1.0'),
    ('time_remaining', 'APC Time Remaining', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.2.2.3.0'),
    ('status', 'APC Battery Status', 'snmp_status',
        '1.3.6.1.4.1.318.1.1.1.2.1.1.0|'
        '2=battery normal, 3=battery low|battery unknown'),
    ('temperature', 'APC Temperature', 'snmp_counter',
        '1.3.6.1.4.1.318.1.1.1.2.2.2.0'),
    ('output_status', 'APC Output Status', 'snmp_status',
        '1.3.6.1.4.1.318.1.1.1.4.1.1.0|2=on line, 3=on battery'),
    ('admin_state', 'Alteon RServer Admin', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.5.2.1.10.${index}'),
    ('oper_state', 'Alteon RServer Oper', 'snmp_status',
        '1.3.6.1.4.1.1872.2.1.9.2.2.1.7.${index}|2=up|down'),
    ('current_sessions', 'Alteon RServer Current Sessions', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.5.1.2.${index}'),
    ('failures', 'Alteon RServer Failures', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.5.1.4.${index}'),
    ('octets', 'Alteon RServer Octets', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.5.1.7.${index}'),
    ('total_sessions', 'Alteon RServer Total Sessions', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.5.1.3.${index}'),
    ('admin_state', 'Alteon VServer Admin State', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.5.5.1.4.${index}'),
    ('current_sessions', 'Alteon VServer Current Sessions', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.7.1.2.${index}'),
    ('total_sessions', 'Alteon VServer Total Sessions', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.2.7.1.3.${index}'),
    ('octets', 'Alteon VServer Octets', 'snmp_counter',
        '.1.3.6.1.4.1.1872.2.1.8.2.7.1.6.${index}'),
    ('admin_state', 'Alteon RService Admin State', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.5.2.1.10.${real_server}'),
    ('oper_state', 'Alteon RService Oper State', 'snmp_status',
        '1.3.6.1.4.1.1872.2.1.9.2.4.1.6.${index}|2=up|down'),
    ('response_time', 'Alteon RService Response Time', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.9.2.4.1.7.${index}'),
    ('cpua_1sec', 'Alteon CPU A 1Sec', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.16.1.0'),
    ('cpua_4secs', 'Alteon CPU A 4Secs', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.16.3.0'),
    ('cpua_64secs', 'Alteon CPU A 64Secs', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.16.5.0'),
    ('cpub_1sec', 'Alteon CPU B 1Sec', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.1.16.2.0'),
    ('cpub_4secs', 'Alteon CPU B 4Secs', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.16.4.0'),
    ('cpub_64secs', 'Alteon CPU B 64Secs', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.16.6.0'),
    ('mem_total', 'Alteon Memory Total', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.12.6.0'),
    ('mem_used', 'Alteon Memory Used', 'snmp_counter',
        '1.3.6.1.4.1.1872.2.1.8.12.4.0'),
    ('sensor_value', 'Brocade Sensor Value', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.1.22.1.4.${index}'),
    ('oper_status', 'Brocade Sensor Oper', 'snmp_status',
        '1.3.6.1.4.1.1588.2.1.1.1.1.22.1.3.${index}|4=ok, 3=alert, 5=alert'),
    ('tx_words', 'Brocade FC Port TxWords', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.11.${index}'),
    ('rx_words', 'Brocade FC Port RxWords', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.12.${index}'),
    ('tx_frames', 'Brocade FC Port TxFrames', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.13.${index}'),
    ('rx_frames', 'Brocade FC Port RxFrames', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.14.${index}'),
    ('admin_state', 'Brocade FC Port Admin State', 'snmp_counter',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.5.${index}'),
    ('oper_status', 'Brocade FC Port Oper Status', 'snmp_status',
        '1.3.6.1.4.1.1588.2.1.1.1.6.2.1.4.${index}|1=up, 3=testing'),
    ('phy_state', 'Brocade FC Port Phy State', 'brocade_fcport_phystate',
        '${index}'),
    ('status', 'UPS Battery Status', 'snmp_status',
        '${ups_oid}.2.1.0|2=battery normal, 1=battery unknown, '
        '3=battery low, 3=battery depleted'),
    ('temperature', 'UPS Battery Temperature', 'snmp_counter',
        '${ups_oid}.2.7.0'),
    ('minutes_remaining', 'UPS Battery Minutes Remaining', 'snmp_counter',
        '${ups_oid}.2.3.0'),
    ('charge_remaining', 'UPS Battery Charge Remaining', 'snmp_counter',
        '${ups_oid}.2.4.0'),
    ('voltage', 'UPS Input Voltage', 'snmp_counter',
        '1.3.6.1.2.1.33.1.3.3.1.3.${index}'),
    ('current', 'UPS Input Current', 'snmp_counter',
        '1.3.6.1.2.1.33.1.3.3.1.4.${index}'),
    ('voltage', 'UPS Output Voltage', 'snmp_counter',
        '1.3.6.1.2.1.33.1.4.4.1.2.${index}'),
    ('current', 'UPS Output Current', 'snmp_counter',
        '1.3.6.1.2.1.33.1.4.4.1.3.${index}'),
    ('load', 'UPS Output Load', 'snmp_counter',
        '1.3.6.1.2.1.33.1.4.4.1.5.${index}'),
    ('voltage', 'Mitsu UPS Input Voltage', 'snmp_counter_mul',
        '1.3.6.1.4.1.13891.101.3.3.1.3.${index}|0.1'),
    ('current', 'Mitsu UPS Input Current', 'snmp_counter_mul',
        '1.3.6.1.4.1.13891.101.3.3.1.4.${index}|0.1'),
    ('power', 'Mitsu UPS Input Power', 'snmp_counter',
        '1.3.6.1.4.1.13891.101.3.3.1.5.${index}'),
    ('voltage', 'Mitsu UPS Output Voltage', 'snmp_counter_mul',
        '1.3.6.1.4.1.13891.101.4.4.1.2.${index}|0.1'),
    ('current', 'Mitsu UPS Output Current', 'snmp_counter_mul',
        '1.3.6.1.4.1.13891.101.4.4.1.3.${index}|0.1'),
    ('power', 'Mitsu UPS Output Power', 'snmp_counter',
        '1.3.6.1.4.1.13891.101.4.4.1.4.${index}'),
    ('load', 'Mitsu UPS Output Load', 'snmp_counter',
        '1.3.6.1.4.1.13891.101.4.4.1.5.${index}'),
    ('accepted_routes', 'BGP Accepted Routes', 'snmp_counter',
        '1.3.6.1.4.1.9.9.187.1.2.4.1.1.${remote}.1.1'),
    ('advertised_routes', 'BGP Advertised Routes', 'snmp_counter',
        '1.3.6.1.4.1.9.9.187.1.2.4.1.6.${remote}.1.1'),
    ('pix_connections', 'Pix Connections Poller', 'snmp_counter',
        '1.3.6.1.4.1.9.9.147.1.2.2.2.1.5.${index}'),
    ('other_in', 'Cisco NAT Other IP Inbound',
        'snmp_counter', '1.3.6.1.4.1.9.10.77.1.3.1.1.2.1'),
    ('icmp_in', 'Cisco NAT ICMP Inbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.2.2'),
    ('udp_in', 'Cisco NAT UDP Inbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.2.3'),
    ('tcp_in', 'Cisco NAT TCP Inbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.2.4'),
    ('other_out', 'Cisco NAT Other IP Outbound',
        'snmp_counter', '1.3.6.1.4.1.9.10.77.1.3.1.1.3.1'),
    ('icmp_out', 'Cisco NAT ICMP Outbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.3.2'),
    ('udp_out', 'Cisco NAT UDP Outbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.3.3'),
    ('tcp_out', 'Cisco NAT TCP Outbound', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.3.1.1.3.4'),
    ('active_binds', 'Cisco NAT Active Binds', 'snmp_counter',
        '1.3.6.1.4.1.9.10.77.1.2.1.0'),
    ('sensor_verify', 'Verify Sensor Index', 'verify_sensor_index', ''),
    ('value', 'Sensor Value', 'snmp_counter',
        '1.3.6.1.4.1.2021.13.16.${table_index}.1.3.${row_index}'),
    ('storage_verify', 'Verify Storage Index', 'verify_storage_index', ''),
    ('cpu400', 'OS 400 System Load', 'snmp_counter',
        '1.3.6.1.4.1.2.6.4.5.1.0'),
    ('dell_om_chassis', 'Dell OpenManage Chassis', 'snmp_status',
        '1.3.6.1.4.1.674.10892.1.200.10.1.2.1|'
        '1=other, 2=unknown, 3=ok, 4=noncritical, 5=critical, '
        '6=nonrecoverabl|unknown'),
    ('dell_om_temp', 'Dell OpenManage Ambient Temp', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.20.1.6.1.1'),
    ('fan1', 'Dell OpenManage Fan RPM #1', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.1'),
    ('fan2', 'Dell OpenManage Fan RPM #2', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.2'),
    ('fan3', 'Dell OpenManage Fan RPM #3', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.3'),
    ('fan4', 'Dell OpenManage Fan RPM #4', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.4'),
    ('fan5', 'Dell OpenManage Fan RPM #5', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.5'),
    ('fan6', 'Dell OpenManage Fan RPM #6', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.6'),
    ('fan7', 'Dell OpenManage Fan RPM #7', 'snmp_counter',
        '1.3.6.1.4.1.674.10892.1.700.12.1.6.1.7'),
    ('status', 'FC Oper Status', 'snmp_status',
        '1.3.6.1.2.1.75.1.2.2.1.2.${index}|1=up, 2=offline, 4=linkFailure'),
    ('rx_frames', 'FCPort RxFrames', 'snmp_counter',
        '1.3.6.1.2.1.75.1.4.3.1.1.${index}'),
    ('tx_frames', 'FCPort TxFrames', 'snmp_counter',
        '1.3.6.1.2.1.75.1.4.3.1.2.${index}'),
    ('associated', '802.11x Associated Clients', 'snmp_counter',
        '1.3.6.1.4.1.9.9.273.1.1.2.1.1.1'),
    ('power_status', 'Compaq Power Condition', 'snmp_status',
        '1.3.6.1.4.1.232.6.2.9.3.1.4.${chassis}.${bayindex}|2=up'),
    ('cur_disk_q', 'Inf-64 Disk CurrentDiskQueue', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.16.${index}'),
    ('avg_disk_q', 'Inf-64 Disk AvgDiskQueu', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.10.${index}'),
    ('avg_disk_rdq', 'Inf-64 Disk avg Read DiskQueue', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.11.${index}'),
    ('avg_disk_wrq', 'Inf-64 Disk avg Write DiskQueue', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.12.${index}'),
    ('inf_d_read_time', 'Inf-64 Disk Read Time', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.2.${index}'),
    ('inf_d_write_time', 'Inf-64 Disk Write Time', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.4.${index}'),
    ('rd_ops', 'Inf-64 Disk Read rate', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.19.${index}'),
    ('wr_ops', 'Inf-64 Disk Write rate', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.22.${index}'),
    ('inf_d_read_rate', 'Inf-64 Disk Read Bytes', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.18.${index}'),
    ('inf_d_write_rate', 'Inf-64 Disk Write Bytes', 'snmp_counter',
        '1.3.6.1.4.1.9600.1.2.44.1.21.${index}'),
)

backends = (
    (u'No Backend', '', ''),
    (u'Unknown Event', 'event_always', 'unknown'),
    (u'Alarm APC', 'event', 'apc_status'),
    (u'Alarm BGP Peer', 'event', 'bgp_status, ,180'),
    (u'Alarm Brocade FC Port', 'event', 'brocade_fcport'),
    (u'Alarm Environmental', 'event', 'environment'),
    (u'Alarm NTP', 'event', 'ntp, nothing'),
    (u'Set Admin Status', 'admin_status', 'down=2|up=1, 0'),
    (u'Alarm TCP Content', 'event', 'tcp_content'),
    (u'Alarm TCP Port', 'event', 'tcpudp_service'),
    (u'Alarm Verify Operational', 'event', 'interface_protocol, ,180'),
    (u'Alarm Reachability', 'event', 'reachability'),
    (u'Application Alarm', 'event', 'application'),
    (u'Alteon Admin Status', 'admin_status', 'down=0|up=2, 2'),
    (u'Alarm Alteon RServer', 'event', 'alteon_rserver'),
    (u'Alarm Alteon Service', 'event', 'alteon_service'),
    (u'Alarm Alteon VServer', 'event', 'alteon_vserver'),
    (u'Brocade FC Admin View', 'admin_status', 'down=2|up=1, 0'),
    (u'Change Interface Number', 'verify_index', ''),
    (u'Alarm OS/400', 'event', 'os400_error'),
    (u'Alarm Configuration', 'event_always', 'configuration'),
)

poller_sets = (
    (u'No Polling', u'No Interface Type', ()),
    (u'Cisco Interface', u'Physical Interfaces', (
        (u'SNMP Verify Interface Number', u'Change Interface Number'),
        (u'Cisco SNMP Ping Start', u''),
        (u'SNMP Interface Operational Status', u'Alarm Verify Operational'),
        (u'SNMP Interface Administrative Status', u'Set Admin Status'),
        (u'SNMP Input Rate', u''),
        (u'SNMP Input Packets', u''),
        (u'SNMP Output Rate', u''),
        (u'SNMP Output Packets', u''),
        (u'SNMP Output Errors', u''),
        (u'SNMP Input Errors', u''),
        (u'SNMP Drops', u''),
        #(u'Cisco SNMP Ping Wait', u''),
        #(u'Cisco SNMP Ping Get PL', u''),
        #(u'Cisco SNMP Ping Get RTT', u''),
        #(u'Cisco SNMP Ping End', u''),
    )),
    (u'Cisco Router', u'Cisco System Info', (
        (u'Cisco CPU Utilization', u''),
        (u'TCP MIB Established Connections', u''),
        (u'Cisco Used Memory', u''),
        (u'TCP MIB Active Opens', u''),
        (u'Cisco Free Memory', u''),
        (u'TCP MIB Passive Opens', u''),
        )),
    (u'TCP/IP Port', u'TCP Ports', (
        (u'TCP Port Check & Delay', u''),
        (u'TCP Port Status', u'Alarm TCP Port'),
        (u'TCP MIB Established', u''),
        (u'TCP Content Check', u'Alarm TCP Content')
        )),
    (u'BGP Neighbor', u'BGP Neighbors', (
        (u'BGP Peer Status', u'Alarm BGP Peer'),
        (u'BGP Inbound Updates', u''),
        (u'BGP Accepted Routes', u''),
        (u'BGP Advertised Routes', u''),
        (u'BGP Outbound Updates', u''),
        (u'BGP Uptime', u'')
        )),
    (u'Storage Device', u'Storage', (
        (u'Verify Storage Index', u'Change Interface Number'),
        (u'Storage Device Block Size', u''),
        (u'Storage Device Total Blocks', u''),
        (u'Storage Device Used Blocks', u'')
        )),
    (u'Linux/Unix Host', u'Linux/Unix System Info', (
        (u'CPU Nice Time', u''),
        (u'Host MIB Number of Processes', u''),
        (u'CPU User Time', u''),
        (u'Host MIB Number of Users', u''),
        (u'CPU Idle Time', u''),
        (u'TCP MIB Established Connections', u''),
        (u'CPU System Time', u''),
        (u'TCP MIB Active Opens', u''),
        (u'Load Average 1 min', u''),
        (u'TCP MIB Passive Opens', u''),
        (u'Load Average 5 min', u''),
        (u'Load Average 15 min', u'')
        )),
    (u'Solaris Host', u'Solaris System Info', (
        (u'CPU System Time', u''),
        (u'CPU Idle Time', u''),
        (u'CPU Kernel Time', u''),
        (u'CPU Wait Time', u''),
        (u'Load Average 1 min', u''),
        (u'Load Average 5 min', u''),
        (u'Load Average 15 min', u''),
        (u'Real Memory Available', u''),
        (u'Real Memory Total', u''),
        (u'Swap Memory Available', u''),
        (u'Swap Memory Total', u''),
        )),
    (u'Windows Host', u'Windows System Info', (
        (u'Host MIB Proc Average Util', u''),
        (u'Host MIB Number of Processes', u''),
        (u'Host MIB Number of Users', u''),
        (u'TCP MIB Active Opens', u''),
        (u'TCP MIB Established Connections', u''),
        (u'TCP MIB Passive Opens', u'')
        )),
    (u'HostMIB Application', u'Applications', (
        (u'Host MIB Process Verifier', u''),
        (u'Host MIB Status', u'Application Alarm'),
        (u'Host MIB Process Memory Usage', u'')
        )),
    (u'Cisco Power Supply', u'Cisco Power Supply', (
        (u'Cisco Power Supply Status', u'Alarm Environmental'),
        )),
    (u'Cisco Temperature', u'Cisco Temperature', (
        (u'Cisco Temperature Status', u'Alarm Environmental'),
        (u'Cisco Temperature', u'')
        )),
    (u'Cisco Voltage', u'Cisco Voltage', (
        (u'Cisco Voltage Status', u'Alarm Environmental'),
        )),
    (u'Cisco SA Agent', u'Cisco SA Agent', (
        (u'SA Agent Forward Jitter', u''),
        (u'SA Agent Backward Jitter', u''),
        (u'SA Agent Packetloss', u''),
        )),
    (u'Reachability', u'Reachable', (
        (u'Reachability Ping', u''),
        (u'Reachability Status', u'Alarm Reachability'),
        )),
    (u'NTP', u'NTP', (
        (u'NTP Status', u'Alarm NTP'),
        )),
    (u'Compaq Physical Drive', u'Compaq Physical Drives', (
        (u'Compaq Drive Condition', u'Alarm Environmental'),
        )),
    (u'Compaq Fan', u'Compaq Fans', (
        (u'Compaq Fan Condition', u'Alarm Environmental'),
        )),
    (u'Compaq Temperature', u'Compaq Temperature', (
        (u'Compaq Temperature Status', u'Alarm Environmental'),
        (u'Compaq Temperature', u'')
        )),
    (u'IIS Info', u'IIS Webserver Information', (
        (u'IIS Total Bytes Received', u''),
        (u'IIS Total CGI Requests', u''),
        (u'IIS Total Files Sent', u''),
        (u'IIS Total GETs', u''),
        (u'IIS Total Posts', u'')
        )),
    (u'Apache', u'Apache', (
        (u'Apache Status', u''),
        )),
    (u'APC', u'APC', (
        (u'APC Battery Status', u'Alarm Environmental'),
        (u'APC Output Status', u'Alarm APC'),
        (u'APC Battery Capacity', u''),
        (u'APC Output Load', u''),
        (u'APC Input Voltage', u''),
        (u'APC Output Voltage', u''),
        (u'APC Time Remaining', u''),
        (u'APC Temperature', u'')
    )),
    (u'Alteon Real Server', u'Alteon Real Server', (
        (u'Alteon RServer Admin', u'Alteon Admin Status'),
        (u'Alteon RServer Oper', u'Alarm Verify Operational'),
        (u'Alteon RServer Current Sessions', u''),
        (u'Alteon RServer Failures', u''),
        (u'Alteon RServer Octets', u''),
        (u'Alteon RServer Total Sessions', u'')
    )),
    (u'Alteon Virtual Server', u'Alteon Virtual Server', (
        (u'Alteon VServer Admin State', u'Set Admin Status'),
        (u'Alteon VServer Current Sessions', u''),
        (u'Alteon VServer Octets', u''),
        (u'Alteon VServer Total Sessions', u'')
    )),
    (u'Alteon Real Services', u'Alteon Real Services', (
        (u'Alteon RService Admin State', u'Set Admin Status'),
        (u'Alteon RService Oper State', u'Alarm Alteon Service'),
        (u'Alteon RService Response Time', u'')
    )),
    (u'Alteon System Info', u'Alteon System Info', (
        (u'Alteon CPU A 1Sec', u''),
        (u'Alteon CPU A 4Secs', u''),
        (u'Alteon CPU A 64Secs', u''),
        (u'Alteon CPU B 1Sec', u''),
        (u'Alteon CPU B 4Secs', u''),
        (u'Alteon CPU B 64Secs', u''),
        (u'TCP MIB Active Opens', u''),
        (u'TCP MIB Passive Opens', u''),
        (u'TCP MIB Established Connections', u''),
        (u'Alteon Memory Used', u''),
        (u'Alteon Memory Total', u'')
    )),
    (u'Brocade Sensors', u'Brocade Sensors', (
        (u'Brocade Sensor Oper', u'Alarm Verify Operational'),
        (u'Brocade Sensor Value', u''),
    )),
    (u'Brocade FC Ports', u'Brocade FC Ports', (
        (u'Brocade FC Port Admin State', u'Brocade FC Admin View'),
        (u'Brocade FC Port Oper Status', u'Alarm Verify Operational'),
        (u'Brocade FC Port Phy State', u'Alarm Brocade FC Port'),
        (u'Brocade FC Port TxWords', u''),
        (u'Brocade FC Port RxWords', u''),
        (u'Brocade FC Port TxFrames', u''),
        (u'Brocade FC Port RxFrames', u'')
    )),
    (u'UPS', u'UPS', (
        (u'UPS Battery Status', u'Alarm Environmental'),
        (u'UPS Battery Charge Remaining', u''),
        (u'UPS Battery Minutes Remaining', u''),
        (u'UPS Battery Temperature', u'')
    )),
    (u'UPS Input Line', u'UPS Input Line', (
        (u'UPS Input Voltage', u''),
        (u'UPS Input Current', u''),
    )),
    (u'UPS Output Line', u'UPS Output Line', (
        (u'UPS Output Voltage', u''),
        (u'UPS Output Current', u''),
        (u'UPS Output Load', u''),
    )),
    (u'Mitsubishi UPS Input Line', u'Mitsubishi UPS Input Line', (
        (u'Mitsu UPS Input Voltage', u''),
        (u'Mitsu UPS Input Current', u''),
        (u'Mitsu UPS Input Power', u''),
    )),
    (u'Mitsubishi UPS Output Line', u'Mitsubishi UPS Output Line', (
        (u'Mitsu UPS Output Voltage', u''),
        (u'Mitsu UPS Output Current', u''),
        (u'Mitsu UPS Output Load', u''),
        (u'Mitsu UPS Output Power', u'')
    )),
    (u'PIX Connection Stat', u'Cisco PIX', (
        (u'Pix Connections Poller', u''),
    )),
    (u'Cisco NAT', u'Cisco NAT', (
        (u'Cisco NAT Other IP Outbound', u''),
        (u'Cisco NAT Other IP Inbound', u''),
        (u'Cisco NAT ICMP Outbound', u''),
        (u'Cisco NAT ICMP Inbound', u''),
        (u'Cisco NAT UDP Outbound', u''),
        (u'Cisco NAT UDP Inbound', u''),
        (u'Cisco NAT TCP Outbound', u''),
        (u'Cisco NAT TCP Inbound', u''),
        (u'Cisco NAT Active Binds', u'')
    )),
    (u'Sensors', u'Sensors', (
        (u'Verify Sensor Index', u'Change Interface Number'),
        (u'Sensor Value', u''),
    )),
    (u'OS/400 Host', u'OS/400 System Info', (
        (u'OS 400 System Load', u''),
    )),
    (u'Dell Chassis', u'Dell Chassis', (
        (u'Dell OpenManage Chassis', u'Alarm Verify Operational'),
        (u'Dell OpenManage Chassis', u'Set Admin Status'),
        (u'Dell OpenManage Ambient Temp', u''),
        (u'Dell OpenManage Fan RPM #1', u''),
        (u'Dell OpenManage Fan RPM #2', u''),
        (u'Dell OpenManage Fan RPM #3', u''),
        (u'Dell OpenManage Fan RPM #4', u''),
        (u'Dell OpenManage Fan RPM #5', u''),
        (u'Dell OpenManage Fan RPM #6', u''),
        (u'Dell OpenManage Fan RPM #7', u''),
    )),
    (u'Compaq Power Supply', u'Compaq Power Supply', (
        (u'Compaq Power Condition', u'Alarm Environmental'),
    )),
    (u'Cisco 802.11X Device', u'Cisco 802.11X Device', (
        (u'802.11x Associated Clients', u''),
    )),
    (u'Fibre Channel Interface', u'Generic FC Ports', (
        (u'FC Oper Status', u'Alarm Environmental'),
        (u'FCPort RxFrames', u''),
        (u'FCPort TxFrames', u''),
    )),
    (u'SNMP Interface', u'Physical Interfaces', (
        (u'SNMP Verify Interface Number', u'Change Interface Number'),
        (u'SNMP Interface Operational Status', u'Alarm Verify Operational'),
        (u'SNMP Interface Administrative Status', u'Set Admin Status'),
        (u'SNMP Input Rate', u''),
        (u'SNMP Input Packets', u''),
        (u'SNMP Output Rate', u''),
        (u'SNMP Output Packets', u''),
        (u'SNMP Output Errors', u''),
        (u'SNMP Input Errors', u''),
        (u'SNMP Drops', u''),
    )),
)
