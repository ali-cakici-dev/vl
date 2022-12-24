def cancel(proto, payload):
    """ Send Control message to cancel last executed command if it was running """

    return proto.send(proto.MOD_ALL, None, proto.TYPE_CTRL)

cmds = [cancel]
