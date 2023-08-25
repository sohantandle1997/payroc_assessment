import pytest

from etl_handlers.etl_handler import ETLHandler


@pytest.fixture(scope="class")
def etl_handler(request):
    handler = ETLHandler(
        longitude=2.35,
        latitude=48.86,
        forecast_days=2
    )

    return handler


@pytest.mark.usefixtures("etl_handler")
class TestETLHandler:
    # @pytest.mark.parametrize("test_input_params, expected_output", [
    #     ()
    # ])
    def test_upload_file_success(self, etl_handler):
        etl_handler.perform_etl()