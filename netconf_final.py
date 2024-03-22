from ncclient import manager
import xmltodict
studentID = "64070195"
loopback_ip = "172.30." + str(int(studentID[-3:]) // 1) + ".1"
loopback_subnet = "/24"
m = manager.connect(
    host="10.0.15.189",
    port= 22,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

def create():
    netconf_config = """<config>
  <interfaces>
    <interface>
      <name>Loopback{loopback_id}</name>
      <description>Loopback for Student {studentID}</description>
      <ip>
        <address>
          <primary>
            <address>{loopback_ip}</address>
            <mask>{loopback_subnet}</mask>
          </primary>
        </address>
      </ip>
    </interface>
  </interfaces>
</config>
    """.format(loopback_id=studentID, studentID=studentID, loopback_ip=loopback_ip, loopback_subnet=loopback_subnet)

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback" + studentID + "is created successfully"
        else:
            return "Cannot create: Interface loopback " + studentID
    except:
        print("Error!")


def delete():
    netconf_config = """<config>
  <interfaces>
    <interface operation="delete">
      <name>Loopback{loopback_id}</name>
    </interface>
  </interfaces>
</config>
""".format(loopback_id = studentID)

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback " + studentID + " is deleted successfully"
        else:
            return "Cannot delete: Interface loopback " + studentID
    except:
        print("Error!")
        return "Error deleting loopback interface"


def enable():
    netconf_config = """<config>
  <interfaces>
    <interface>
      <name>Loopback{loopback_id}</name>
      <shutdown/>
    </interface>
  </interfaces>
</config>
""".format(loopback_id=studentID)

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback " + studentID + " is enabled successfully"
        else:
            return "Cannot enable: Interface loopback " + studentID
    except:
        print("Error!")
        return "Error enabling loopback interface"


def disable():
    netconf_config = """<config>
  <interfaces>
    <interface>
      <name>Loopback{loopback_id}</name>
      <shutdown>
        <shutdown/>
      </shutdown>
    </interface>
  </interfaces>
</config>
""".format(loopback_id=studentID)

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback " + studentID + " is disable successfully"
        else:
            return "Cannot disable: Interface loopback " + studentID
    except:
        print("Error!")

def netconf_edit_config(netconf_config):
    m = manager.connect(host="<device_ip_address>",
                    port=830,
                    username="<username>",
                    password="<password>",
                    hostkey_verify=False)


# def status():
#     netconf_filter = """<!!!REPLACEME with YANG data!!!>"""

#     try:
#         # Use Netconf operational operation to get interfaces-state information
#         netconf_reply = m.<!!!REPLACEME with the proper Netconf operation!!!>(filter=<!!!REPLACEME with netconf_filter!!!>)
#         print(netconf_reply)
#         netconf_reply_dict = xmltodict.<!!!REPLACEME with the proper method!!!>(netconf_reply.xml)

#         # if there data return from netconf_reply_dict is not null, the operation-state of interface loopback is returned
#         if <!!!REPLACEME with the proper condition!!!>:
#             # extract admin_status and oper_status from netconf_reply_dict
#             admin_status = <!!!REPLACEME!!!>
#             oper_status = <!!!REPLACEME !!!>
#             if admin_status == 'up' and oper_status == 'up':
#                 return "<!!!REPLACEME with proper message!!!>"
#             elif admin_status == 'down' and oper_status == 'down':
#                 return "<!!!REPLACEME with proper message!!!>"
#         else: # no operation-state data
#             return "<!!!REPLACEME with proper message!!!>"
#     except:
#        print("Error!")
