from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

@inject
def locator():
    pass

def generate_container():
    container = Container()
    container.wire(modules=[__name__])
    locator() 
    return container
