import pytest
from backend.data_fetcher import get_stock_data

def test_get_stock_data_valid_symbol():
    df = get_stock_data("2330.TW")
    assert not df.empty # 確認有抓到資料
    assert "Close" in df.columns # 必須有收盤價欄位
    assert len(df) > 0 # 確認資料筆數大於0

def test_get_stock_data_invalid_symbol():
    with pytest.raises(ValueError): # 測試錯誤情況
        get_stock_data("INVALIDSYMBOL123")