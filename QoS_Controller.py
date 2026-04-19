from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):

    log.info("Switch connected. Installing QoS rules...")

    msg = of.ofp_flow_mod()
    msg.priority = 100
    msg.match.dl_type = 0x0800
    msg.match.nw_proto = 1
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

    msg2 = of.ofp_flow_mod()
    msg2.priority = 10
    msg2.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg2)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("QoS Controller Started")