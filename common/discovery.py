from common import const
import grpc


def get_service_stub(service_name, service_stub):

    def gunfunc(channel):
        return service_stub(channel)
    stub = Stub(service_name, gunfunc)
    if stub.stub:
        return stub
    if stub.refresh():
        return stub


class Stub:
    def __init__(self, service_name, genfunc):
        self.service_name = service_name
        self.gunfunc = genfunc
        self.stub = None
        self.chan = None
        self.addr = None

    def refresh(self):
        chan, addr = get_service_channel(self.service_name)
        self.stub = self.gunfunc(chan)
        self.chan = chan
        self.addr = addr
        return True

    def call_rpc(self, func_name, request):
        func = getattr(self.stub, func_name)
        return func(request)


def get_service_channel(service):
    service_addr = _get_addr(service)
    chan = grpc.insecure_channel(service_addr)
    return chan, service_addr


def _get_addr(service):
    addr = const.SERVICES[service]
    return addr
