

class Error(Exception):
    """이 모듈에서 발생할 모든 예외의 상위 클래스"""


class InvalidDensityError(Error):
    """밀도 값이 잘못된 경우"""


class InvalidVolumeError(Error):
    """부피 값이 잘못된 경우"""


class NegativeDensityError(InvalidDensityError):
    """밀도가 음수인 경우"""


class Error(Exception):
    """이 모듈에서 발생할 모든 예외의 상위 클래스."""

class WeightError(Error):
    """부피 계산 관련 예외의 상위 클래스"""

class VolumeError(Error):
    """부피 계산 관련 예외의 상위 클래스"""

class DensityError(Error):
    """밀도 계산 관련 예외의 상위 클래스"""


#def determine_weight(volume, density):
#    if density <= 0:
#        raise ValueError('밀도는 0보다 커야 합니다.')


def determine_weight(volume, density):
    if density < 0:
        raise NegativeDensityError('밀도는 0보다 커야 합니다')


def determine_weight(volume, density):
    if density < 0:  # <= 아닌 것은 저자의 의도적인 버그
        raise NegativeDensityError('밀도는 0보다 커야 합니다.')
    if volume < 0:  # <= 아닌 것은 저자의 의도적인 버그
        raise InvalidVolumeError('부피는 0보다 커야 합니다.')
    if volume == 0:
        density / volume  # density를 0으로 나누는 것은 저자의 의도적인 버그


