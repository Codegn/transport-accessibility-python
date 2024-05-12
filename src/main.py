from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from src.application.accessibility_calculator.accessibility_calculator import AccessibilityCalculator
from src.domain.accessibility.repository.accessibility_repository import AccessibilityRepository
from src.domain.accessibility.use_cases.get_accessibility_by_zone import GetAccessibilityByZone
from src.domain.impedance_matrices.repository.impedance_matrices_repository import ImpedanceMatricesRepository
from src.domain.impedance_matrices.use_cases.get_impedance_matrix_from_source import GetImpedanceMatrixFromSource
from src.domain.oportunities.repository.oportunities_repository import OportunitiesRepository
from src.domain.oportunities.use_cases.get_from_source import GetOportunitiesFromSource
from src.infrastructure.components.accessibility_procesor import AccessibilityProcessor
from src.infrastructure.components.impedance_matrix_reader import ImpedanceMatrixReader
from src.infrastructure.components.oportunities_reader import OportunitiesReader
from src.infrastructure.repository.accessibility_repository_impl import AccessibilityRepositoryImpl
from src.infrastructure.repository.impedance_matrix_repository_impl import ImpedanceMatricesRepositoryImpl
from src.infrastructure.repository.oportunities_repository_impl import OportunitiesRepositoryImpl


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    oportunities_reader = providers.Singleton(OportunitiesReader)
    oportunities_repository = providers.Singleton(OportunitiesRepositoryImpl, oportunities_reader=oportunities_reader)
    get_oportunities_from_source = providers.Singleton(
        GetOportunitiesFromSource, oportunities_repository=oportunities_repository
    )

    impedance_matrix_reader = providers.Singleton(ImpedanceMatrixReader)
    impedance_matrices_repository = providers.Singleton(
        ImpedanceMatricesRepositoryImpl, impedance_matrix_reader=impedance_matrix_reader
    )
    get_impedance_matrix_from_source = providers.Singleton(
        GetImpedanceMatrixFromSource, impedance_matrices_repository=impedance_matrices_repository
    )

    accessibility_processor = providers.Singleton(AccessibilityProcessor)
    accessibility_repository = providers.Singleton(
        AccessibilityRepositoryImpl, accessibility_processor=accessibility_processor
    )
    get_accessibility_by_zone = providers.Singleton(
        GetAccessibilityByZone, accessibility_repository=accessibility_repository
    )

    accessibility_calculator = providers.Singleton(
        AccessibilityCalculator,
        get_accessibility_by_zone,
        get_impedance_matrix_from_source,
        get_oportunities_from_source,
    )


@inject
def locator(
    oportunities_reader: OportunitiesReader = Provide[Container.oportunities_reader],
    oportunities_repository: OportunitiesRepository = Provide[Container.oportunities_repository],
    get_oportunities_from_source: GetOportunitiesFromSource = Provide[Container.get_oportunities_from_source],
    impedance_matrix_reader: ImpedanceMatrixReader = Provide[Container.impedance_matrix_reader],
    impedance_matrix_repository: ImpedanceMatricesRepository = Provide[Container.impedance_matrices_repository],
    get_impedance_matrix_from_source: GetImpedanceMatrixFromSource = Provide[Container.get_impedance_matrix_from_source],
    accessibility_processor: AccessibilityProcessor = Provide[Container.accessibility_processor],
    accessibility_repository: AccessibilityRepository = Provide[Container.accessibility_repository],
    get_accessibility_by_zone: GetAccessibilityByZone = Provide[Container.get_accessibility_by_zone],
    accessibility_calculator: AccessibilityCalculator = Provide[Container.accessibility_calculator],
):
    pass


def generate_container():
    container = Container()
    container.wire(modules=[__name__])
    locator()
    return container
