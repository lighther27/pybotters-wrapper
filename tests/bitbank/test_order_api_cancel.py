import pytest
import pytest_mock

import pybotters_wrapper as pbw


@pytest.fixture
def tester(cancel_order_tester):
    return cancel_order_tester(
        url="https://api.bitbank.cc/v1/user/spot/cancel_order",
        request_method="POST",
        factory_method=pbw.create_factory("bitbank").create_cancel_order_api,
        dummy_order_parameters={
            "symbol": "btc_jpy",
            "order_id": "0",
            "extra_params": {},
        },
        dummy_response={
            "success": 1,
            "data": {
                "order_id": 0,
                "pair": "string",
                "side": "string",
                "type": "string",
                "start_amount": "string",
                "remaining_amount": "string",
                "executed_amount": "string",
                "price": "string",
                "post_only": False,
                "average_price": "string",
                "ordered_at": 0,
                "expire_at": 0,
                "canceled_at": 0,
                "triggered_at": 0,
                "trigger_price": "string",
                "status": "string",
            },
        },
        expected_generate_endpoint="/user/spot/cancel_order",
        expected_translate_parameters={"pair": "btc_jpy", "order_id": "0"},
        expected_order_id="0",
    )


@pytest.mark.asyncio
@pytest.mark.skip
async def test_order(tester):
    resp = await tester.test_order()
    print(resp)


@pytest.mark.asyncio
async def test_generate_endpoint(tester):
    await tester.test_generate_endpoint()


@pytest.mark.asyncio
async def test_translate_parameters(tester):
    await tester.test_translate_parameters()


@pytest.mark.asyncio
async def test_combined(tester, mocker: pytest_mock.MockerFixture):
    await tester.test_combined(mocker)